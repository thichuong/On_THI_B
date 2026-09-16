#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Công cụ tra cứu nhanh thông tin câu hỏi, file nguồn partX.py và lời giải thích hiện tại
Cách dùng:
    python3 lookup_question.py <qid>
    python3 lookup_question.py <start_qid> <end_qid>
Ví dụ:
    python3 lookup_question.py 487
    python3 lookup_question.py 486 490
"""
import sys
import json
from pathlib import Path

# Mapping 600 câu hỏi vào các part
PART_RANGES = [
    (1, 60, "scripts/explanations/part1.py", "PART1_EXPLANATIONS"),
    (61, 120, "scripts/explanations/part2.py", "PART2_EXPLANATIONS"),
    (121, 180, "scripts/explanations/part3.py", "PART3_EXPLANATIONS"),
    (181, 205, "scripts/explanations/part4.py", "PART4_EXPLANATIONS"),
    (206, 263, "scripts/explanations/part5.py", "PART5_EXPLANATIONS"),
    (264, 300, "scripts/explanations/part6.py", "PART6_EXPLANATIONS"),
    (301, 360, "scripts/explanations/part7.py", "PART7_EXPLANATIONS"),
    (361, 420, "scripts/explanations/part8.py", "PART8_EXPLANATIONS"),
    (421, 485, "scripts/explanations/part9.py", "PART9_EXPLANATIONS"),
    (486, 540, "scripts/explanations/part10.py", "PART10_EXPLANATIONS"),
    (541, 600, "scripts/explanations/part11.py", "PART11_EXPLANATIONS"),
]

def get_source_file(qid: int):
    for start, end, filepath, varname in PART_RANGES:
        if start <= qid <= end:
            return filepath, varname
    return None, None

def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python3 lookup_question.py <qid> [end_qid]")
        sys.exit(1)

    start_qid = int(sys.argv[1])
    end_qid = int(sys.argv[2]) if len(sys.argv) > 2 else start_qid

    # Tìm file questions.json
    root_dir = Path(__file__).resolve().parents[3] # Nếu nằm trong .agents/skills/fix-question-explanation/scripts/
    json_path = root_dir / "src" / "data" / "questions.json"
    if not json_path.exists():
        # Thử tìm từ cwd
        json_path = Path("src/data/questions.json")
    
    if not json_path.exists():
        print(f"❌ Không tìm thấy file {json_path}")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    q_map = {q["id"]: q for q in questions}

    for qid in range(start_qid, end_qid + 1):
        if qid not in q_map:
            print(f"⚠️ Không tìm thấy câu {qid} trong cơ sở dữ liệu!")
            continue

        q = q_map[qid]
        src_file, var_name = get_source_file(qid)
        crit_label = " 🚨 [CÂU ĐIỂM LIỆT]" if q.get("is_critical") else ""

        print("=" * 60)
        print(f"📌 CÂU HỎI {qid}{crit_label} (Chương {q.get('chapter')}: {q.get('chapter_name')})")
        print(f"📁 File nguồn cần sửa: {src_file} (Biến: {var_name})")
        
        img = q.get("image")
        if img:
            local_img = f"public/{img}"
            exists = " (Tồn tại)" if Path(local_img).exists() else " (Không tìm thấy!)"
            print(f"🖼️ Ảnh sa hình/biển báo: {local_img}{exists}")

        print(f"\n❓ Câu hỏi: {q['question']}")
        print("\n📋 Các phương án:")
        for idx, opt in enumerate(q["options"], 1):
            mark = " ✅ [ĐÁP ÁN ĐÚNG]" if idx == q["correct_option"] else ""
            print(f"   {idx}. {opt}{mark}")

        exp = q.get("explanation", "").strip()
        print(f"\n💡 Lời giải thích hiện tại:")
        if exp:
            print(f"   {exp}")
        else:
            print("   (Chưa có giải thích)")
        print("=" * 60 + "\n")

if __name__ == "__main__":
    main()

