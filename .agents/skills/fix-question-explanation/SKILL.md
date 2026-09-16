---
name: fix-question-explanation
description: >-
  Quy trình chuẩn từng bước để kiểm tra, tra cứu, kiểm chứng và chỉnh sửa lời giải thích (explanation)
  hoặc đáp án đúng trong bộ 600 câu hỏi sát hạch GPLX (On_THI_B). Sử dụng skill này khi người dùng
  yêu cầu sửa giải thích bị sai, kiểm tra tính chính xác của câu hỏi/đáp án sa hình, biển báo, luật,
  hoặc cập nhật nội dung giải thích trong scripts/explanations/ và src/data/questions.json.
---

# Quy trình chuẩn sửa đổi và chuẩn hóa giải thích câu hỏi sát hạch GPLX

Tài liệu này cung cấp cẩm nang hành động (runbook) toàn diện cho agent khi cần sửa đổi, bổ sung hoặc khắc phục sai lệch trong nội dung giải thích (`explanation`) và đáp án của bộ 600 câu hỏi ôn thi giấy phép lái xe.

---

## 1. Bước 1: Xác định câu hỏi và Tệp nguồn (File Mapping)

Khi nhận được yêu cầu sửa một hoặc nhiều câu hỏi (ví dụ: Câu `QID`):

### 1.1. Tra cứu nhanh bằng lệnh
Chạy script tra cứu tích hợp sẵn để xem ngay toàn bộ thông tin câu hỏi, file nguồn cần sửa, hình ảnh đi kèm và giải thích hiện tại:

```bash
python3 scripts/lookup_question.py <QID>
# Hoặc tra cứu một khoảng câu:
python3 scripts/lookup_question.py <start_qid> <end_qid>
```

### 1.2. Bảng phân bổ 11 phần (Part Mapping)
Nếu cần xác định thủ công, đối chiếu dải câu hỏi với tệp nguồn tương ứng:

| Dải câu hỏi (ID) | Tên chương | Tệp nguồn cần chỉnh sửa | Tên biến Dictionary |
| :--- | :--- | :--- | :--- |
| **1 - 60** | Chương 1: Quy định chung & Quy tắc giao thông | `scripts/explanations/part1.py` | `PART1_EXPLANATIONS` |
| **61 - 120** | Chương 1: Quy tắc giao thông (tiếp) | `scripts/explanations/part2.py` | `PART2_EXPLANATIONS` |
| **121 - 180** | Chương 1: Tốc độ, nồng độ cồn, khoảng cách | `scripts/explanations/part3.py` | `PART3_EXPLANATIONS` |
| **181 - 205** | Chương 2: Nghiệp vụ vận tải | `scripts/explanations/part4.py` | `PART4_EXPLANATIONS` |
| **206 - 263** | Chương 3: Văn hóa & Đạo đức người lái xe | `scripts/explanations/part5.py` | `PART5_EXPLANATIONS` |
| **264 - 300** | Chương 4: Kỹ thuật lái xe | `scripts/explanations/part6.py` | `PART6_EXPLANATIONS` |
| **301 - 360** | Chương 4: Cấu tạo & Sửa chữa thông thường | `scripts/explanations/part7.py` | `PART7_EXPLANATIONS` |
| **361 - 420** | Chương 5: Biển báo hiệu đường bộ (Phần 1) | `scripts/explanations/part8.py` | `PART8_EXPLANATIONS` |
| **421 - 485** | Chương 5: Biển báo hiệu đường bộ (Phần 2) | `scripts/explanations/part9.py` | `PART9_EXPLANATIONS` |
| **486 - 540** | Chương 6: Giải thế sa hình (Phần 1) | `scripts/explanations/part10.py` | `PART10_EXPLANATIONS` |
| **541 - 600** | Chương 6: Giải thế sa hình & Tình huống (Phần 2) | `scripts/explanations/part11.py` | `PART11_EXPLANATIONS` |

---

## 2. Bước 2: Kiểm tra trực quan hình ảnh (Đối với câu có ảnh)

Nếu câu hỏi có trường `image` (chẳng hạn `images/cau_XXX.png`):
**BẮT BUỘC** phải xem trực tiếp file ảnh bằng công cụ `view_file` tại đường dẫn `public/images/cau_XXX.png`.

### Các chi tiết then chốt cần soi kỹ trên ảnh:
1. **Biển báo giao thông**:
   - Biển tròn viền đỏ (Biển cấm): Mã hiệu biển (P.102 cấm đi ngược chiều, P.103a cấm ô tô, P.105 cấm mô tô, P.106a cấm xe tải, P.108 cấm máy kéo, P.120 cấm kéo rơ moóc, P.123 cấm rẽ, P.126 cấm vượt, P.130 cấm dừng đỗ, P.132 nhường đường qua đường hẹp...).
   - Biển nguy hiểm (tam giác vàng viền đỏ): W.207 giao nhau với đường không ưu tiên, W.208 giao nhau với đường ưu tiên (tam giác ngược), W.219 dốc nguy hiểm...
   - Biển hiệu lệnh (tròn xanh): R.122 STOP (dừng lại), R.301 hướng đi phải theo, R.303 nơi giao nhau chạy theo vòng xuyến...
   - Biển phụ: Hình xe tải, mũi tên phụ rẽ, hướng đường ưu tiên nét đậm (S.506), phạm vi tác dụng trước/sau (S.508)...
2. **Vạch kẻ đường**:
   - Vạch nét đứt (được đè vạch/vượt xe khi an toàn).
   - Vạch đơn nét liền (cấm đè vạch, cấm vượt).
   - Vạch kép 1.4 (một liền một đứt: bên đứt được đè, bên liền cấm đè).
   - Vạch người đi bộ qua đường (cấm quay đầu xe, cấm dừng đỗ).
   - Vạch kênh hóa dòng xe (xương cá: cấm đi đè lên).
3. **Đèn tín hiệu & Vạch chỉ hướng**:
   - Đèn chính (xanh/đỏ/vàng) vs đèn phụ hình mũi tên.
   - Mũi tên chỉ hướng sơn trên mặt đường của từng làn xe.
4. **Hiệu lệnh CSGT**:
   - Tay giơ thẳng đứng: Tất cả các hướng dừng lại (trừ xe đã ở trong ngã tư).
   - Hai tay dang ngang: Phía trước và sau dừng lại; bên phải và trái được đi các hướng.

---

## 3. Bước 3: Tra cứu và kiểm chứng câu trả lời đúng

### 3.1. Phương pháp tìm kiếm internet
Sử dụng công cụ `search_web` với các mẫu câu truy vấn chính xác:
- `"bộ 600 câu hỏi" "câu <QID>" "đáp án"`
- `"câu <QID>" "<từ khóa nổi bật của câu hỏi>"`
- `"sa hình câu <QID>" "giải thích"`

### 3.2. Căn cứ pháp lý & Quy tắc giao thông chuẩn mực
- **Quy chuẩn QCVN 41:2019/BGTVT**: Ý nghĩa biển báo, vạch sơn tín hiệu đường bộ.
- **Luật Trật tự, an toàn giao thông đường bộ**: Quy tắc quyền ưu tiên, nhường đường, vượt xe, dừng đỗ xe.
- **5 Bước vàng giải Sa hình**:
  1. *Bước 1 ("Nhất chớm")*: Xe đã vượt qua vạch dừng/vào giao lộ được đi trước.
  2. *Bước 2 ("Nhì ưu")*: Thứ tự: Hỏa (Chữa cháy) > Sự (Quân sự) > Công (Công an) > Thương (Cứu thương).
  3. *Bước 3 ("Tam đường")*: Đường ưu tiên (W.207, I.401) đi trước; đường nhánh không ưu tiên (W.208, STOP) đi sau.
  4. *Bước 4 ("Tứ phải")*: Đồng cấp không biển: Bên phải không vướng đi trước. Vòng xuyến có biển R.303 nhường bên trái; không biển nhường bên phải.
  5. *Bước 5 ("Ngũ hướng")*: Hướng rẽ ưu tiên: **Rẽ phải** > **Đi thẳng** > **Rẽ trái** > **Quay đầu**.

---

## 4. Bước 4: Soạn thảo lời giải thích chuẩn mực

### Tiêu chuẩn cấu trúc giải thích:
1. **Đối với câu điểm liệt (`is_critical: true`)**:
   - BẮT BUỘC bắt đầu bằng tiền tố: `🚨 [CÂU ĐIỂM LIỆT]`
   - Nêu rõ nguy cơ mất an toàn nghiêm trọng dẫn đến tai nạn thảm khốc hoặc quy định nghiêm cấm của pháp luật.
2. **Đối với câu hỏi thường**:
   - Nêu tình huống thực tế trong ảnh/câu hỏi (biển báo gì, vạch gì, phương tiện nào).
   - Phân tích nguyên tắc luật pháp / quy tắc ưu tiên áp dụng.
   - Kết luận rõ ràng phương án đúng (khớp với nội dung phương án trong `options`).

---

## 5. Bước 5: Chỉnh sửa mã nguồn và đồng bộ dữ liệu

### 5.1. Sửa tệp nguồn `scripts/explanations/partX.py`
Dùng công cụ `replace_file_content` để cập nhật giá trị của câu hỏi trong `PARTX_EXPLANATIONS`:

```python
    <QID>: "Nội dung giải thích mới chuẩn xác...",
```

### 5.2. Chạy đồng bộ vào `src/data/questions.json`
Chạy script tự động kiểm tra và đồng bộ dữ liệu:

```bash
python3 scripts/apply_explanations.py
```
*Script sẽ kiểm tra đủ 600 câu và cập nhật trường `explanation` vào `src/data/questions.json`.*

### 5.3. Chạy kiểm định độc lập
Chạy script kiểm định:

```bash
python3 scripts/validate_explanations.py
```
*Đảm bảo 100% câu hỏi đều đạt chuẩn độ dài (>= 25 ký tự) và đủ 60 câu điểm liệt.*

### 5.4. Chạy bộ unit tests của dự án
Đảm bảo hệ thống vận hành trơn tru và không bị lỗi hồi quy:

```bash
npm test
```

---

## 6. Danh sách kiểm tra hoàn thành (Checklist)

- [ ] Đã chạy `python3 scripts/lookup_question.py <QID>` để xác định đúng file part và nội dung hiện tại.
- [ ] Đã mở và kiểm tra trực tiếp ảnh `public/images/cau_<QID>.png` (nếu có ảnh).
- [ ] Đã tra cứu internet/luật giao thông để đảm bảo đáp án chính xác 100%.
- [ ] Đã gắn tiền tố `🚨 [CÂU ĐIỂM LIỆT]` nếu là câu điểm liệt.
- [ ] Đã cập nhật dictionary trong `scripts/explanations/partX.py`.
- [ ] Đã chạy `python3 scripts/apply_explanations.py` thành công.
- [ ] Đã chạy `python3 scripts/validate_explanations.py` đạt 100% tiêu chí.
- [ ] Đã chạy `npm test` pass 13/13 tests.

