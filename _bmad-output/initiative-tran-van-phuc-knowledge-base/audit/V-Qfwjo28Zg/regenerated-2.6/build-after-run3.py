#!/usr/bin/env python3
"""Apply owner-approved run-3 decisions to the preserved, hash-bound run-3 input."""
from pathlib import Path
import hashlib
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / 'gate-run3/work/V-Qfwjo28Zg/summary.md'
EXPECTED = '602cea058a35a087b04428f1f0e915f666ccd0c3ffae8a5aad0e6623b95d0979'
REPLACEMENTS = {
'c110': ('Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào thể hiện "ma dê" (bản ghi âm ghi như vậy) giúp làm giảm đường huyết.', 'Điều dưỡng kể chủ nhiệm khoa nói không có cơ chế nào thể hiện “ma dê” (bản ghi âm ghi như vậy) giúp làm giảm đường huyết.'),
'c156': ('Bác sĩ nói trong mười bình luận của khán giả có tràn ngập những vấn đề kiến thức đều liên quan tới chủ đề hôm nay, đó chính là gốc tự do.', 'Bác sĩ nói cả mười bình luận đều rất liên quan tới chủ đề phát sóng hôm nay là glutathion.'),
'c287': ('Bác sĩ hướng dẫn trong vài tiếng đồng hồ, và sau đó chị bổ sung vi chất theo từng bước, nâng dần liều.', 'Bác sĩ nói đã hướng dẫn trong bốn đến năm tiếng; sau đó, để bổ sung vi chất, ông trải qua từng bước một, “nâng cao nâng cao dần”.'),
'c413': ('Bác sĩ nói một thân thể đã chịu 73 năm bão táp cần ít nhất nửa năm đến một năm được chăm sóc đúng cách.', 'Phần nhận xét nói một thân thể đã mất 73 năm gánh chịu dông bão cần ít nhất nửa năm đến một năm được tưới tắm trong tình yêu thương, luyện thở đúng đắn và nguồn dinh dưỡng tế bào chuẩn mực.'),
}
ADDITIONS = {
'O2': ('01:21:37', 'Khán giả tự kể từ năm 2012 cơ hàm khó điều khiển, hay đơ cứng và khiến họ nói không tròn vành rõ chữ.'),
'O3': ('01:18:51', 'Khán giả tự kể vẫn mong khỏi nốt viêm xoang và hen phế quản.'),
'O4': ('01:29:22', 'Khán giả tự kể sau khi cai đường, đi bấm huyệt và uống thuốc nam thì cơ thể đã được 30%.'),
'O6': ('01:40:58', 'Bác sĩ khuyến khích lan tỏa kiến thức và hành vi tốt từ bạn bè tới trường học và xã hội, và tổ chức seminar về ăn uống, dinh dưỡng.'),
}

def build():
    raw = BASE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED, 'run-3 input hash mismatch'
    text = raw.decode('utf-8')
    for claim, (old, new) in REPLACEMENTS.items():
        assert text.count(old) == 1, claim
        text = text.replace(old, new, 1)
    for claim, (heading, sentence) in ADDITIONS.items():
        m = re.search(r'^## \[' + heading + r'\].*$', text, re.M)
        assert m, claim
        nxt = re.search(r'^## \[', text[m.end():], re.M)
        pos = m.end() + nxt.start() if nxt else len(text)
        text = text[:pos].rstrip() + '\n\n' + sentence + '\n\n' + text[pos:]
    return text

if __name__ == '__main__':
    result = build()
    (HERE / 'summary.md').write_text(result, encoding='utf-8')
    print(hashlib.sha256(result.encode()).hexdigest())
