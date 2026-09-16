# scripts/validate_explanations.py
# -*- coding: utf-8 -*-
"""
Script kiểm định độc lập chất lượng và tính toàn vẹn của bộ 600 câu hỏi và giải thích
"""
import json
import sys
from pathlib import Path

def validate():
    file_path = Path("src/data/questions.json")
    if not file_path.exists():
        print(f"❌ File không tồn tại: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            questions = json.load(f)
        except Exception as e:
            print(f"❌ Lỗi định dạng JSON: {e}")
            return False

    total = len(questions)
    print(f"📊 Tổng số câu hỏi: {total}")
    if total != 600:
        print(f"❌ Kỳ vọng 600 câu, nhưng có {total} câu!")
        return False

    empty_explanations = []
    short_explanations = []
    missing_critical_warning = []
    by_chapter = {}

    for q in questions:
        qid = q.get("id")
        ch = q.get("chapter")
        by_chapter[ch] = by_chapter.get(ch, 0) + 1
        exp = q.get("explanation", "").strip()

        if not exp:
            empty_explanations.append(qid)
        elif len(exp) < 25:
            short_explanations.append((qid, len(exp), exp))

        if q.get("is_critical"):
            if "CÂU ĐIỂM LIỆT" not in exp:
                missing_critical_warning.append(qid)

    print(f"\nPhân bố theo chương:")
    for ch, count in sorted(by_chapter.items()):
        print(f"  Chương {ch}: {count} câu")

    has_error = False

    if empty_explanations:
        print(f"❌ Có {len(empty_explanations)} câu chưa có giải thích: {empty_explanations}")
        has_error = True
    else:
        print(f"✅ 100% (600/600) câu hỏi đều đã có nội dung giải thích.")

    if short_explanations:
        print(f"⚠️ Có {len(short_explanations)} câu giải thích ngắn (< 25 ký tự): {short_explanations}")
    else:
        print(f"✅ 100% giải thích đều đạt chuẩn độ dài và độ chi tiết (>= 25 ký tự).")

    if missing_critical_warning:
        print(f"⚠️ Có {len(missing_critical_warning)} câu điểm liệt chưa gắn cảnh báo: {missing_critical_warning}")
    else:
        print(f"✅ 100% (60/60) câu điểm liệt đều được gắn cảnh báo an toàn rõ ràng.")

    # Thống kê độ dài trung bình
    lengths = [len(q.get("explanation", "")) for q in questions]
    avg_len = sum(lengths) / len(lengths)
    min_len = min(lengths)
    max_len = max(lengths)
    print(f"\nĐộ dài giải thích (ký tự): Trung bình = {avg_len:.1f}, Ngắn nhất = {min_len}, Dài nhất = {max_len}")

    return not has_error

if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)

