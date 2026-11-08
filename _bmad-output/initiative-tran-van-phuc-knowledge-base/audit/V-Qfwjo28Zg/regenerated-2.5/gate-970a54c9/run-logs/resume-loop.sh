#!/bin/bash
# Resume the single authorized gate run (owner-approved) until the quota resets; max 24 attempts, 30 min apart.
cd /home/openclaw/orca/workspaces/tranvanphuc-knowledge/lane-b-audit
for n in $(seq 2 25); do
  sleep 1800
  echo "attempt $n $(date -u +%FT%TZ)" >> /tmp/gate2-2.5-Ehsi/resume-loop.log
  ./review-summaries --provider codex --model gpt-6.1-sol --videos-dir /tmp/gate2-2.5-Ehsi/videos --limit 1 --no-commit > /tmp/gate2-2.5-Ehsi/run-resume$n.log 2>&1 < /dev/null
  if [ -f /tmp/gate2-2.5-Ehsi/videos/2026-10-10-V-Qfwjo28Zg/review.md ]; then echo "DONE $(date -u +%FT%TZ)" >> /tmp/gate2-2.5-Ehsi/resume-loop.log; exit 0; fi
  grep -q 'usage limit' /tmp/gate2-2.5-Ehsi/run-resume$n.log || { echo "STOPPED non-quota $(date -u +%FT%TZ)" >> /tmp/gate2-2.5-Ehsi/resume-loop.log; exit 1; }
done
echo GAVEUP >> /tmp/gate2-2.5-Ehsi/resume-loop.log
