"""Hermetic launcher tests: no downloads, Gemini requests or real git writes."""
import hashlib
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

LAUNCHER = Path(__file__).resolve().parents[1] / 'weekly-sync'


class LocalWeeklyLauncherTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        self.root.mkdir()
        self.home = Path(self.tmp.name) / 'home'
        self.home.mkdir()
        self.evidence = Path(self.tmp.name) / 'evidence'
        self.evidence.mkdir()
        self.commands = []
        self.fail_prepare = False
        self.fail_process = None
        self.branch = 'feature'
        self.dirty = ''
        self.staged = ''
        self.module = runpy.run_path(str(LAUNCHER), run_name='launcher_test')
        self.main = self.module['main']
        self.main.__globals__['ROOT'] = self.root
        self.cache = self.home / '.cache' / 'tranvanphuc-weekly' / hashlib.sha256(str(self.root).encode()).hexdigest()[:12]
        self.detector = types.ModuleType('detect_new_videos')
        self.detector.DEFAULT_CHANNEL_ID = 'channel'
        self.detector.get_channel_video_ids = lambda _: ['new', 'known', 'other']
        self.detector.get_known_video_ids = lambda _: {'known'}

    def state(self, summarized=False):
        return {'version': 1, 'selected': 'new', 'pending': ['other'],
                'items': [{'dir': 'videos/new', 'kind': 'fetched',
                           'video_id': 'new', 'summary_candidate': summarized}],
                'notices': [], 'failures': [], 'fatal': []}

    def prepare_resume(self, summarized=False):
        (self.evidence / 'report.json').write_text(json.dumps(self.state(summarized)))
        (self.evidence / 'before.sha').write_text('a' * 40 + '\n')
        if summarized:
            directory = self.root / 'videos/new'
            directory.mkdir(parents=True)
            (directory / 'summary.md').write_text('already generated')

    def output(self, command, **kwargs):
        if command[:3] == ['gh', 'variable', 'get']:
            return 'gemini-test\n'
        words = command[1:]
        if words == ['branch', '--show-current']:
            return self.branch
        if words == ['diff', '--cached', '--name-only']:
            return self.staged
        if words[:2] == ['diff', '--name-only']:
            return self.dirty
        if words[:1] == ['ls-files']:
            return ''
        if words == ['rev-parse', 'HEAD']:
            return 'a' * 40
        raise AssertionError(command)

    def execute(self, command, **kwargs):
        self.commands.append((command, kwargs.get('env', dict(os.environ))))
        if 'scripts/weekly_sync.py' in command:
            phase = command[2]
            if phase == self.fail_process:
                return subprocess.CompletedProcess(command, 1)
            report = Path(command[command.index('--report') + 1])
            if phase == 'prepare':
                state = self.state()
                if self.fail_prepare:
                    state['failures'] = ['fetch blocked']
            else:
                state = json.loads(report.read_text())
                if phase == 'summarize':
                    state['items'][0]['summary_candidate'] = True
                    directory = self.root / state['items'][0]['dir']
                    directory.mkdir(parents=True, exist_ok=True)
                    (directory / 'summary.md').write_text('generated summary')
                elif phase == 'finalize':
                    state['report'] = {'status': 'clean', 'published': [], 'pushed': True}
            report.write_text(json.dumps(state))
        return subprocess.CompletedProcess(command, 0)

    def invoke(self, resume=False, answers=('y', 'y'), resume_env=False):
        argv = ['weekly-sync', '--resume', str(self.evidence)] if resume else ['weekly-sync']
        env = {'PATH': '/bin', 'GEMINI_API_KEY': 'inherited-secret'}
        if resume_env:
            env['WEEKLY_RUN'] = str(self.evidence)
        # Restore sys.path after the launcher's detector import as well.
        with patch.dict(os.environ, env, clear=True), \
             patch.object(sys, 'argv', argv), patch.object(sys, 'prefix', str(self.cache)), \
             patch.object(sys, 'path', list(sys.path)), patch('os.chdir'), \
             patch('pathlib.Path.home', return_value=self.home), \
             patch('subprocess.check_output', side_effect=self.output), \
             patch('subprocess.run', side_effect=self.execute), \
             patch('builtins.input', side_effect=answers), \
             patch('getpass.getpass', return_value='prompted-secret'), \
             patch.dict(sys.modules, {'detect_new_videos': self.detector}):
            self.main()

    def phases(self):
        return [cmd[2] for cmd, _ in self.commands if 'scripts/weekly_sync.py' in cmd]

    def test_fresh_runs_all_phases_and_scopes_key(self):
        self.invoke()
        self.assertEqual(self.phases(), ['prepare', 'summarize', 'finalize'])
        for cmd, env in self.commands:
            if 'summarize' in cmd:
                self.assertEqual(env['GEMINI_API_KEY'], 'prompted-secret')
            else:
                self.assertNotIn('GEMINI_API_KEY', env)
        self.assertIn(['git', 'pull', '--ff-only', 'origin', 'feature'], [c for c, _ in self.commands])

    def test_resume_does_not_prepare_or_pull(self):
        self.prepare_resume()
        self.invoke(resume=True, answers=('y',))
        self.assertEqual(self.phases(), ['summarize', 'finalize'])
        self.assertFalse(any(c[0] == 'git' for c, _ in self.commands))

    def test_resume_does_not_repeat_successful_summary(self):
        self.prepare_resume(summarized=True)
        self.invoke(resume=True, answers=('y',))
        self.assertEqual(self.phases(), ['finalize'])

    def test_recorded_prepare_failure_stops_even_with_exit_zero(self):
        self.fail_prepare = True
        with self.assertRaisesRegex(RuntimeError, 'recorded a failure'):
            self.invoke()
        self.assertEqual(self.phases(), ['prepare'])

    def test_summarize_nonzero_does_not_finalize(self):
        self.prepare_resume()
        self.fail_process = 'summarize'
        with self.assertRaisesRegex(RuntimeError, 'summarize exit 1'):
            self.invoke(resume=True)
        self.assertEqual(self.phases(), ['summarize'])

    def test_declining_finalize_then_resuming_is_safe(self):
        self.prepare_resume()
        with self.assertRaisesRegex(RuntimeError, 'Stopped by owner'):
            self.invoke(resume=True, answers=('n',))
        self.assertEqual(self.phases(), ['summarize'])
        self.commands.clear()
        self.invoke(resume=True, answers=('y',))
        self.assertEqual(self.phases(), ['finalize'])

    def test_unrelated_dirty_work_is_rejected(self):
        self.dirty = 'README.md\n'
        with self.assertRaisesRegex(RuntimeError, 'Unrelated dirty work'):
            self.invoke()
        self.assertEqual(self.commands, [])

    def test_staged_work_is_rejected(self):
        self.staged = 'videos/new/metadata.json\n'
        with self.assertRaisesRegex(RuntimeError, 'Staged work'):
            self.invoke()
        self.assertEqual(self.commands, [])

    def test_main_branch_is_rejected(self):
        self.branch = 'main'
        with self.assertRaisesRegex(RuntimeError, 'feature branch'):
            self.invoke()
        self.assertEqual(self.commands, [])

    def test_missing_resume_cannot_fetch(self):
        with self.assertRaisesRegex(RuntimeError, 'no report.json'):
            self.invoke(resume=True)
        self.assertEqual(self.commands, [])

    def test_missing_environment_resume_cannot_fetch(self):
        with self.assertRaisesRegex(RuntimeError, 'no report.json'):
            self.invoke(resume_env=True)
        self.assertEqual(self.commands, [])

    def test_environment_resume_skips_prepare(self):
        self.prepare_resume(summarized=True)
        self.invoke(resume_env=True, answers=('y',))
        self.assertEqual(self.phases(), ['finalize'])

    def test_invalid_resume_states_cannot_start_fresh(self):
        for state in ({}, None, [], {'version': 999}):
            for environment in (False, True):
                with self.subTest(state=state, environment=environment):
                    (self.evidence / 'report.json').write_text(json.dumps(state))
                    with self.assertRaisesRegex(RuntimeError, 'Invalid resume report'):
                        self.invoke(resume=not environment, resume_env=environment)
                    self.assertEqual(self.commands, [])

    def test_missing_recorded_summary_stops_without_regeneration(self):
        self.prepare_resume(summarized=True)
        (self.root / 'videos/new/summary.md').unlink()
        with self.assertRaisesRegex(RuntimeError, 'successful summary is missing'):
            self.invoke(resume=True)
        self.assertEqual(self.phases(), [])


if __name__ == '__main__':
    unittest.main()
