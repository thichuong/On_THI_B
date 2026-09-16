# scripts/apply_explanations.py
# -*- coding: utf-8 -*-
"""
Script kiểm tra tính toàn vẹn và cập nhật giải thích cho toàn bộ 600 câu hỏi vào src/data/questions.json
"""
import sys
import json
from pathlib import Path

# Add scripts directory to sys.path
sys.path.insert(0, str(Path(__file__).parent))

from explanations.part1 import PART1_EXPLANATIONS
from explanations.part2 import PART2_EXPLANATIONS
from explanations.part3 import PART3_EXPLANATIONS
from explanations.part4 import PART4_EXPLANATIONS
from explanations.part5 import PART5_EXPLANATIONS
from explanations.part6 import PART6_EXPLANATIONS
from explanations.part7 import PART7_EXPLANATIONS
from explanations.part8 import PART8_EXPLANATIONS
from explanations.part9 import PART9_EXPLANATIONS
from explanations.part10 import PART10_EXPLANATIONS
from explanations.part11 import PART11_EXPLANATIONS

def main():
    merged = {}
    parts = [
        ("Part 1 (Q1-60)", PART1_EXPLANATIONS, 1, 60),
        ("Part 2 (Q61-120)", PART2_EXPLANATIONS, 61, 120),
        ("Part 3 (Q121-180)", PART3_EXPLANATIONS, 121, 180),
        ("Part 4 (Q181-205)", PART4_EXPLANATIONS, 181, 205),
        ("Part 5 (Q206-263)", PART5_EXPLANATIONS, 206, 263),
        ("Part 6 (Q264-300)", PART6_EXPLANATIONS, 264, 300),
        ("Part 7 (Q301-360)", PART7_EXPLANATIONS, 301, 360),
        ("Part 8 (Q361-420)", PART8_EXPLANATIONS, 361, 420),
        ("Part 9 (Q421-485)", PART9_EXPLANATIONS, 421, 485),
        ("Part 10 (Q486-540)", PART10_EXPLANATIONS, 486, 540),
        ("Part 11 (Q541-600)", PART11_EXPLANATIONS, 541, 600),
    ]

    print("=== KIỂM TRA CÁC PHẦN GIẢI THÍCH ===")
    for name, data, start, end in parts:
        expected_count = end - start + 1
        actual_count = len(data)
        missing = [i for i in range(start, end + 1) if i not in data]
        if missing:
            print(f"❌ {name}: Thiếu các câu {missing}")
            sys.exit(1)
        if actual_count != expected_count:
            print(f"❌ {name}: Số lượng không khớp! Kì vọng {expected_count}, có {actual_count}")
            sys.exit(1)
        print(f"✅ {name}: Đầy đủ {actual_count}/{expected_count} câu (từ {start} đến {end})")
        merged.update(data)

    print(f"\nTổng số câu đã tổng hợp: {len(merged)} câu")
    expected_all = set(range(1, 601))
    if set(merged.keys()) != expected_all:
        missing_all = sorted(list(expected_all - set(merged.keys())))
        print(f"❌ Thiếu các câu trong toàn bộ tập dữ liệu: {missing_all}")
        sys.exit(1)

    # Đọc src/data/questions.json
    questions_file = Path("src/data/questions.json")
    with open(questions_file, "r", encoding="utf-8") as f:
        questions = json.load(f)

    if len(questions) != 600:
        print(f"❌ Số câu trong questions.json là {len(questions)}, không phải 600!")
        sys.exit(1)

    updated_count = 0
    critical_with_alert = 0

    for q in questions:
        qid = q["id"]
        exp = merged[qid].strip()
        q["explanation"] = exp
        updated_count += 1
        if q.get("is_critical") and "CÂU ĐIỂM LIỆT" in exp:
            critical_with_alert += 1

    # Ghi lại file src/data/questions.json
    with open(questions_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 Đã cập nhật thành công {updated_count}/600 câu vào {questions_file}!")
    print(f"🚨 Số câu điểm liệt có cảnh báo: {critical_with_alert}/60 câu")

if __name__ == "__main__":
    main()

