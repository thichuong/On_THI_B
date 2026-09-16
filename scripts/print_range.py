import json
import sys

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else start + 9

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for q in qs:
    if start <= q['id'] <= end:
        crit = " [CÂU ĐIỂM LIỆT]" if q.get('is_critical') else ""
        print(f"================ Câu {q['id']}{crit} ================")
        print(f"Câu hỏi: {q['question']}")
        if q.get('image'):
            print(f"Hình ảnh: {q['image']}")
        for i, opt in enumerate(q['options'], 1):
            mark = " <= [ĐÚNG]" if i == q['correct_option'] else ""
            print(f"  {i}. {opt}{mark}")
        print()
