#!/usr/bin/env python3
"""Rebuild ticket 2.6 from the immutable, hash-checked 2.5 summary."""
from pathlib import Path
import hashlib
import re

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'regenerated-2.5' / 'summary.md'
EXPECTED = '970a54c9e30fceb11fb27b3011a905f035b8adec38082272672a32a71c80974d'
source = BASE.read_text(encoding='utf-8')
assert hashlib.sha256(BASE.read_bytes()).hexdigest() == EXPECTED
brief = (HERE / 'decision-brief.md').read_text(encoding='utf-8')
rows = {}
group = None
for block in re.split(r'^(?=### Group |#### c\d+)', brief, flags=re.M):
    m = re.match(r'### Group (\w+)', block)
    if m:
        group = m.group(1)
    m = re.match(r'#### (c\d+) — ', block)
    if m:
        rows[m.group(1)] = (group, block)

# Explicitly checked drafted recommendations, including the owner's c384 clarification.
custom = {
'c047': lambda s: s.replace(' (superoxide dismutase)', ''),
'c155': 'Bác sĩ nói trong mười bình luận của khán giả có tràn ngập những vấn đề kiến thức đều liên quan tới chủ đề hôm nay, đó chính là gốc tự do.',
'c225': '',
'c216': 'Bác sĩ nói nếu chị Ngân mang điều đó đến trưởng khoa để thuyết phục thì trưởng khoa sẽ không đồng ý; ông giải thích rằng nghiên cứu dinh dưỡng để có bằng chứng thực chứng rất khó khi không thể dừng mọi thứ khác của bệnh nhân để chỉ bổ sung một thứ.',
'c368': 'Phần nhận xét nói điều đáng bận tâm của bác không nằm ở con số feritin hay TSAT mà nằm ở chỗ làm sao để vỗ về ngọn lửa viêm mạn tính.',
'c370': lambda s: s.replace('Bác sĩ nói rằng', 'Phần nhận xét nói', 1),
'c384': 'Phần nhận xét liên hệ sự cô đơn sau cái chết của người bạn đời, việc hút thuốc lá và hàng chục năm làm nghề thợ mộc với tổn hại lồng ngực.',
'c387': lambda s: s.replace('Theo bác sĩ', 'Phần nhận xét nói', 1),
'c388': lambda s: s.replace('Bác sĩ nói', 'Phần nhận xét nói', 1),
'c391': lambda s: s.replace('Theo bác sĩ', 'Phần nhận xét nói', 1),
'c318': 'Ure máu là 7,4 (đơn vị phiên âm ghi là "m/l"), sát ngưỡng trên của khoảng tham chiếu từ 2,5 đến 7,5.',
'c331': 'Vitamin D là 31,76 (đơn vị phiên âm ghi là "n/ml").',
'c087': 'Bác sĩ mô tả ba bước khi gốc tự do tấn công cơ thể: bước một là đội "cảm tử", bước hai là đội "đặc nhiệm", bước ba là phát tín hiệu "Rn F2" về ADN để sản xuất thêm đội đặc nhiệm.',
'c154': 'Người xem hỏi bác sĩ phân tích việc bổ sung duy trì vitamin D liều 50.000 đơn vị, tần suất một tháng một viên, có an toàn và hợp lý về mặt y khoa hay không.',
'c184': 'Bác sĩ nói phải phân tích kiến thức dưới nhiều góc độ, như y khoa, toán học, vật lý học (ví dụ với một bài thơ).',
'c245': 'Ông nói phải phòng ngay từ khi đừng để tình trạng ấy xảy ra, và muốn vậy thì phải bổ sung vi chất cho đầy đủ.',
'c375': 'Phần nhận xét nêu các lý do khiến chỉ số B12 tăng không đáng lo: B12 tan trong nước và phần dư được thận đào thải; chỉ số tăng trong xét nghiệm thường do dương tính giả hoặc nhiễu kỹ thuật; tổn thương gan mạn tính làm giải phóng B12 dự trữ vào máu.',
'c478': '',
}
omissions = {
'O5': ('01:31:32', 'Khán giả tự kể Nguyễn Điểm sau khi bổ sung vi chất thấy đau đầu và đau cổ vai gáy gần như khỏi hẳn, các triệu chứng dạ dày, tê chân tay và đầy hơi cũng khỏi, và sức khỏe đại gia đình cải thiện.'),
'O7': ('02:19:04', 'Bác sĩ nói một cơn gió nhẹ, đánh răng hay một nụ cười có thể khởi phát cơn đau dây thần kinh số 5.'),
'O8': ('02:16:47', 'Bác sĩ mô tả nang dưới nhện là chỗ tăng tích dịch tại khe rãnh cuộn não.'),
'O10': ('03:28:54', 'Phần nhận xét nói một phần lá phổi của người thợ mộc đã vĩnh viễn ngừng trao đổi khí.'),
'O11': ('03:28:54', 'Phần nhận xét nói gió mùa đông bắc hoặc vi khuẩn xâm nhập có thể khiến phế quản co thắt dữ dội và đẩy bác vào đợt cấp viêm phổi tắc nghẽn mạn tính.'),
'O14': ('04:33:26', 'Bác sĩ nói việc cướp E và lấy H+ nhằm tạo thành H2O hiền hòa.'),
'O15': ('04:44:28', 'Bác sĩ nói có những bạn trẻ được dán nhãn trầm cảm, tăng động giảm chú ý, tự kỷ hoặc học dốt thấy mọi thứ tốt lên sau khi bổ sung vi chất.'),
'O16': ('05:17:28', 'Bác sĩ nói đừng tránh betacaroten như các chị đang bình luận.'),
}

def build():
    text = source
    changes = []
    for claim, (group, block) in rows.items():
        if group not in {'A', 'B', 'C', 'F', 'G1'} and claim not in {'c318', 'c331'}:
            continue
        old = re.search(r'^- Summary now: (.*)$', block, re.M).group(1)
        if claim in custom:
            new = custom[claim]
            if callable(new):
                new = new(old)
        else:
            m = re.search(r'^- \*\*Recommend: FIX\*\* \(proposal from proposed-corrections\.md \(not yet owner-reviewed\)\): (.*)$', block, re.M)
            assert m, claim
            new = m.group(1)
        assert text.count(old) == 1, claim
        text = text.replace(old, new, 1)
        changes.append((claim, old, new))
    assert len(changes) == 52
    for claim, (heading, sentence) in omissions.items():
        m = re.search(r'^## \[' + heading + r'\].*$', text, re.M)
        assert m, claim
        end = re.search(r'^## \[', text[m.end():], re.M)
        pos = m.end() + end.start() if end else len(text)
        # Append to the heading's content, without touching pre-existing prose.
        text = text[:pos].rstrip() + '\n\n' + sentence + '\n\n' + text[pos:]
        changes.append((claim, '', sentence))
    assert text.count('thiếu máu thiếu sắt') >= 1
    text = text.replace('**Topics:** gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu thiếu sắt, lối sống lành mạnh', '**Topics:** gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu, thiếu sắt, lối sống lành mạnh', 1)
    return text, changes

if __name__ == '__main__':
    result, _ = build()
    (HERE / 'summary.md').write_text(result, encoding='utf-8')
    print(hashlib.sha256(result.encode()).hexdigest())
