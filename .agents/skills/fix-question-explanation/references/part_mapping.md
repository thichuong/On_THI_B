# Bảng phân bổ 600 câu hỏi và file nguồn (Part Mapping)

Hệ thống giải thích cho 600 câu hỏi thi sát hạch lái xe được module hóa thành 11 tệp Python trong thư mục `scripts/explanations/`.

| Part | Dải câu hỏi (ID) | Tên chương | Tệp nguồn | Tên biến Python | Số câu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Part 1** | 1 - 60 | Chương 1: Khái niệm & Quy tắc giao thông đường bộ | `scripts/explanations/part1.py` | `PART1_EXPLANATIONS` | 60 |
| **Part 2** | 61 - 120 | Chương 1: Quy tắc giao thông đường bộ (tiếp theo) | `scripts/explanations/part2.py` | `PART2_EXPLANATIONS` | 60 |
| **Part 3** | 121 - 180 | Chương 1: Tốc độ, nồng độ cồn, khoảng cách an toàn | `scripts/explanations/part3.py` | `PART3_EXPLANATIONS` | 60 |
| **Part 4** | 181 - 205 | Chương 2: Nghiệp vụ vận tải | `scripts/explanations/part4.py` | `PART4_EXPLANATIONS` | 25 |
| **Part 5** | 206 - 263 | Chương 3: Văn hóa giao thông & Đạo đức người lái xe | `scripts/explanations/part5.py` | `PART5_EXPLANATIONS` | 58 |
| **Part 6** | 264 - 300 | Chương 4: Kỹ thuật lái xe | `scripts/explanations/part6.py` | `PART6_EXPLANATIONS` | 37 |
| **Part 7** | 301 - 360 | Chương 4: Cấu tạo & Sửa chữa thông thường | `scripts/explanations/part7.py` | `PART7_EXPLANATIONS` | 60 |
| **Part 8** | 361 - 420 | Chương 5: Hệ thống biển báo hiệu đường bộ (Phần 1) | `scripts/explanations/part8.py` | `PART8_EXPLANATIONS` | 60 |
| **Part 9** | 421 - 485 | Chương 5: Hệ thống biển báo hiệu đường bộ (Phần 2) | `scripts/explanations/part9.py` | `PART9_EXPLANATIONS` | 65 |
| **Part 10** | 486 - 540 | Chương 6: Giải thế sa hình & Tình huống (Phần 1) | `scripts/explanations/part10.py` | `PART10_EXPLANATIONS` | 55 |
| **Part 11** | 541 - 600 | Chương 6: Giải thế sa hình & Kỹ năng xử lý (Phần 2) | `scripts/explanations/part11.py` | `PART11_EXPLANATIONS` | 60 |

---

## Các tệp liên quan trực tiếp
- `src/data/questions.json`: Tệp dữ liệu JSON tập trung chứa 600 câu hỏi, đáp án, ảnh và trường `explanation`.
- `scripts/apply_explanations.py`: Script tổng hợp dữ liệu từ cả 11 parts và cập nhật vào `src/data/questions.json`.
- `scripts/validate_explanations.py`: Script kiểm định chất lượng, độ dài (>= 25 ký tự) và cảnh báo câu điểm liệt.
- `scripts/lookup_question.py`: Script tra cứu nhanh thông tin câu hỏi và file nguồn.

