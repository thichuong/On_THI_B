import os
import re
import json
import pymupdf

# Standard 60 câu điểm liệt trong bộ 600 câu hỏi sát hạch
CAU_LIET_SET = {
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    35, 45, 47, 52, 54, 55, 58, 59, 60, 62, 63, 64, 65, 70, 71, 72,
    74, 75, 84, 87, 91, 92, 93, 94, 96, 101, 107, 115, 119, 143, 148,
    151, 153, 160, 199, 209, 213, 216, 227, 228, 233, 242, 246, 258
}

CHAPTERS = [
    {"id": 1, "name": "Quy định chung và quy tắc giao thông đường bộ", "start": 1, "end": 180},
    {"id": 2, "name": "Văn hóa giao thông, đạo đức người lái xe, PCCC & Cứu nạn", "start": 181, "end": 205},
    {"id": 3, "name": "Kỹ thuật lái xe", "start": 206, "end": 263},
    {"id": 4, "name": "Cấu tạo và sửa chữa", "start": 264, "end": 300},
    {"id": 5, "name": "Báo hiệu đường bộ", "start": 301, "end": 485},
    {"id": 6, "name": "Giải thế sa hình và kỹ năng xử lý tình huống", "start": 486, "end": 600},
]

def get_chapter_info(q_id):
    for ch in CHAPTERS:
        if ch["start"] <= q_id <= ch["end"]:
            return ch["id"], ch["name"]
    return 1, CHAPTERS[0]["name"]

def main():
    pdf_path = "600-cau-hoi-sat-hach.pdf"
    output_dir = "public/images"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs("src/data", exist_ok=True)
    
    doc = pymupdf.open(pdf_path)
    print(f"Opening PDF: {len(doc)} pages")
    
    # 1. Collect all lines with underlines and image infos per page
    raw_lines = []
    page_img_map = {}
    
    for pno in range(4, len(doc)):
        page = doc[pno]
        drawings = page.get_drawings()
        underline_rects = [d['rect'] for d in drawings if d.get('fill') == (0,0,0) and d['rect'].height < 2.5]
        img_infos = page.get_image_info()
        page_img_map[pno] = img_infos
        
        blocks = page.get_text('dict')['blocks']
        for b in blocks:
            if 'lines' in b:
                for l in b['lines']:
                    l_rect = pymupdf.Rect(l['bbox'])
                    text = ''.join(s['text'] for s in l['spans']).strip()
                    if not text:
                        continue
                    # Skip page numbers
                    if text.isdigit() and (l_rect.y0 < 55 or l_rect.y1 > 780):
                        continue
                    # Skip chapter headers
                    if text.startswith('CHƯƠNG ') or text in ['GIAO THÔNG ĐƯỜNG BỘ', 'VÀ CỨU HỘ, CỨU NẠN', 'TÌNH HUỐNG GIAO THÔNG', 'CƠ GIỚI ĐƯỜNG BỘ', 'CỤC CẢNH SÁT GIAO THÔNG']:
                        continue
                    
                    raw_lines.append({
                        'text': text,
                        'rect': l_rect,
                        'underline_rects': underline_rects,
                        'pno': pno
                    })

    # 2. Parse lines into questions
    q_pattern = re.compile(r'^Câu\s+(\d+)[\.:\s]\s*(.*)', re.IGNORECASE)
    
    questions = {}
    current_q = None
    current_opt = None
    
    for line in raw_lines:
        t = line['text']
        l_rect = line['rect']
        u_rects = line['underline_rects']
        
        qm = q_pattern.match(t)
        if qm:
            q_num = int(qm.group(1))
            current_q = {
                'id': q_num,
                'question_parts': [qm.group(2).strip()] if qm.group(2).strip() else [],
                'options': {},
                'correct_options': [],
                'pages': [line['pno']],
                'start_line': line,
                'end_line': line,
                'image_path': None
            }
            questions[q_num] = current_q
            current_opt = None
            continue
        
        if current_q is None:
            continue
            
        if line['pno'] not in current_q['pages']:
            current_q['pages'].append(line['pno'])
        current_q['end_line'] = line
        
        # Check if line contains one or more options
        matches = list(re.finditer(r'(?:^|\s{2,})([1-4])\.\s*', t))
        if matches:
            for i, m in enumerate(matches):
                opt_num = int(m.group(1))
                start_char = m.end()
                end_char = matches[i+1].start() if i+1 < len(matches) else len(t)
                opt_text = t[start_char:end_char].strip()
                
                # Approximate bounding box for this option segment on the line
                seg_x0 = l_rect.x0 + (m.start() / len(t)) * l_rect.width
                seg_x1 = l_rect.x0 + (end_char / len(t)) * l_rect.width
                seg_rect = pymupdf.Rect(seg_x0, l_rect.y0, seg_x1, l_rect.y1)
                
                is_ul = any(abs(u.y0 - l_rect.y1) < 4.5 and not (u.x1 < seg_x0 or u.x0 > seg_x1) for u in u_rects)
                
                current_opt = opt_num
                if current_opt not in current_q['options']:
                    current_q['options'][current_opt] = []
                if opt_text:
                    current_q['options'][current_opt].append(opt_text)
                if is_ul and current_opt not in current_q['correct_options']:
                    current_q['correct_options'].append(current_opt)
            continue
        
        # Continuation
        if current_opt is not None:
            current_q['options'][current_opt].append(t)
            is_ul = any(abs(u.y0 - l_rect.y1) < 4.5 and not (u.x1 < l_rect.x0 or u.x0 > l_rect.x1) for u in u_rects)
            if is_ul and current_opt not in current_q['correct_options']:
                current_q['correct_options'].append(current_opt)
        else:
            current_q['question_parts'].append(t)

    # 3. Associate and export images for each question
    sorted_q_ids = sorted(questions.keys())
    
    for idx, qid in enumerate(sorted_q_ids):
        q = questions[qid]
        pno = q['pages'][0]
        page = doc[pno]
        imgs_on_page = page_img_map.get(pno, [])
        
        if not imgs_on_page:
            continue
            
        q_start_y = q['start_line']['rect'].y0
        next_q_y = 9999
        if idx + 1 < len(sorted_q_ids):
            next_q = questions[sorted_q_ids[idx + 1]]
            if next_q['pages'][0] == pno:
                next_q_y = next_q['start_line']['rect'].y0
        
        matched_imgs = []
        for img_info in imgs_on_page:
            img_rect = pymupdf.Rect(img_info['bbox'])
            img_mid_y = (img_rect.y0 + img_rect.y1) / 2
            if q_start_y - 10 <= img_mid_y < next_q_y:
                matched_imgs.append(img_rect)
        
        if matched_imgs:
            combined_rect = matched_imgs[0]
            for mr in matched_imgs[1:]:
                combined_rect = combined_rect | mr
            
            pix = page.get_pixmap(clip=combined_rect, dpi=180)
            img_filename = f"cau_{qid}.png"
            img_filepath = os.path.join(output_dir, img_filename)
            pix.save(img_filepath)
            q['image_path'] = f"images/{img_filename}"

    # Manual adjustments for edge cases
    if 204 in questions and not questions[204]['correct_options']:
        questions[204]['correct_options'] = [1]
    if 301 in questions and not questions[301]['correct_options']:
        questions[301]['correct_options'] = [1]
    if 302 in questions and not questions[302]['correct_options']:
        questions[302]['correct_options'] = [2]
    if 352 in questions and not questions[352]['correct_options']:
        questions[352]['correct_options'] = [1]

    # 4. Format into final structured JSON
    final_questions = []
    for qid in sorted_q_ids:
        q = questions[qid]
        q_text = " ".join(q['question_parts']).strip()
        
        opts = []
        for opt_idx in sorted(q['options'].keys()):
            opts.append(" ".join(q['options'][opt_idx]).strip())
        
        correct_idx = q['correct_options'][0] if q['correct_options'] else 1
        ch_id, ch_name = get_chapter_info(qid)
        is_crit = qid in CAU_LIET_SET
        
        final_questions.append({
            "id": qid,
            "chapter": ch_id,
            "chapter_name": ch_name,
            "question": q_text,
            "image": q['image_path'],
            "options": opts,
            "correct_option": correct_idx,
            "is_critical": is_crit,
            "explanation": "Câu hỏi điểm liệt bắt buộc phải trả lời đúng." if is_crit else ""
        })

    # Save to src/data/questions.json and public/data/questions.json
    os.makedirs("public/data", exist_ok=True)
    with open("src/data/questions.json", "w", encoding="utf-8") as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)
    with open("public/data/questions.json", "w", encoding="utf-8") as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully processed {len(final_questions)} questions!")
    print(f"Questions with images: {sum(1 for q in final_questions if q['image'])}")
    print(f"Critical questions: {sum(1 for q in final_questions if q['is_critical'])}")
    print("Files saved to src/data/questions.json and public/data/questions.json")

if __name__ == "__main__":
    main()
