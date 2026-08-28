# 🚗 Ứng Dụng Ôn Thi Sát Hạch GPLX 600 Câu (2025)

Ứng dụng web hiện đại, trực quan và tối ưu giúp học viên ôn luyện toàn diện bộ **600 câu hỏi sát hạch lý thuyết lái xe ô tô / mô tô** theo chuẩn tài liệu của Cục Cảnh sát giao thông & Luật Trật tự, An toàn giao thông đường bộ.

---

## 🌟 Tính Năng Nổi Bật

- 📝 **Thi Thử Sát Hạch Chuẩn (30 câu / 20 phút)**:
  - Tự động sinh đề ngẫu nhiên theo đúng cấu trúc tỉ lệ các chương và bắt buộc có câu điểm liệt.
  - Bấm giờ làm bài đếm ngược thời gian thực.
  - Chấm điểm tự động, phân loại kết quả **ĐẠT / KHÔNG ĐẠT**, cảnh báo nếu làm sai câu điểm liệt.
  - Chế độ xem lại chi tiết từng câu kèm đáp án đúng/sai.

- ⚠️ **Luyện 60 Câu Điểm Liệt**:
  - Bộ 60 câu hỏi cốt lõi bắt buộc phải trả lời đúng trong kỳ thi sát hạch.
  - Chế độ phản hồi kết quả ngay lập tức để ghi nhớ sâu.

- 📚 **Học & Ôn Luyện Theo Chương**:
  - **Chương 1**: Quy định chung và quy tắc giao thông đường bộ *(Câu 1 - 180)*
  - **Chương 2**: Văn hóa giao thông, đạo đức người lái xe, PCCC & Cứu nạn *(Câu 181 - 205)*
  - **Chương 3**: Kỹ thuật lái xe *(Câu 206 - 263)*
  - **Chương 4**: Cấu tạo và sửa chữa *(Câu 264 - 300)*
  - **Chương 5**: Hệ thống báo hiệu đường bộ *(Câu 301 - 485)*
  - **Chương 6**: Giải thế sa hình và kỹ năng xử lý tình huống *(Câu 486 - 600)*

- 🔍 **Tra Cứu Nhanh & Bộ Lọc Nâng Cao**:
  - Tìm kiếm tức thì theo từ khóa nội dung hoặc số thứ tự câu hỏi.
  - Lọc nhanh các câu điểm liệt hoặc **318 câu hỏi có hình ảnh minh họa**.
  - Tích hợp **Lightbox Zoom** phóng to hình ảnh sa hình, biển báo chi tiết, rõ nét.

- ❌ **Ôn Tập Câu Hay Làm Sai & ⭐ Lưu Câu Hỏi (Bookmarks)**:
  - Tự động ghi nhớ các câu hỏi người dùng trả lời sai để luyện tập lại.
  - Đánh dấu lưu các câu hỏi quan trọng cần xem lại bất cứ lúc nào.
  - Dữ liệu lưu trữ bền vững qua `localStorage`.

- 🌓 **Giao Diện Hiện Đại & Chế Độ Sáng/Tối (Dark/Light Theme)**:
  - Phong cách thiết kế hiện đại, tinh tế, mượt mà trên cả máy tính và điện thoại.

---

## 🛠️ Công Nghệ Sử Dụng

- **Frontend Core**: HTML5, Vanilla JavaScript (ES Modules), CSS3 (Modern Glassmorphism & Custom Properties).
- **Bundler / Dev Server**: [Vite](https://vitejs.dev/) v8.
- **Xử lý Dữ liệu & Hình ảnh**: Python 3 kết hợp `PyMuPDF` (`pymupdf`) để tự động trích xuất nội dung, đáp án gạch chân và hình ảnh biển báo/sa hình chất lượng cao từ tài liệu PDF gốc.

---

## 📁 Cấu Trúc Thư Mục

```text
On_THI_B/
├── 600-cau-hoi-sat-hach.pdf   # Tài liệu gốc 600 câu hỏi
├── extract_questions.py       # Script Python trích xuất câu hỏi và cắt ảnh
├── index.html                 # Giao diện chính của ứng dụng
├── package.json               # Cấu hình project & dependencies
├── public/                    # Tài nguyên tĩnh
│   ├── data/questions.json    # Dữ liệu 600 câu hỏi dạng JSON
│   └── images/                # 318 hình ảnh minh họa (sa hình, biển báo)
├── src/                       # Mã nguồn ứng dụng
│   ├── data/questions.json    # JSON câu hỏi nạp vào app
│   ├── exam_engine.js         # Logic tạo đề thi, tính điểm, cấu trúc chương
│   ├── main.js                # Logic điều khiển giao diện & các chế độ thi
│   ├── storage.js             # Quản lý lưu trữ localStorage
│   └── styles/
│       └── main.css           # Toàn bộ CSS hệ thống giao diện
└── README.md
```

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Ứng Dụng

### 1. Yêu cầu môi trường
- **Node.js**: Phiên bản 18 trở lên
- **Python**: Phiên bản 3.8+ (chỉ cần khi muốn trích xuất lại dữ liệu từ PDF)

### 2. Khởi chạy ứng dụng Web

```bash
# 1. Cài đặt các gói phụ thuộc
npm install

# 2. Khởi chạy máy chủ phát triển
npm run dev

# 3. Đóng gói cho môi trường Production
npm run build

# 4. Xem thử bản build Production
npm run preview
```

### 3. Trích xuất lại dữ liệu từ PDF (Tùy chọn)

Nếu bạn cập nhật tài liệu PDF hoặc muốn tái tạo bộ dữ liệu JSON và hình ảnh:

```bash
# Cài đặt thư viện PyMuPDF
pip install pymupdf

# Chạy script trích xuất
python3 extract_questions.py
```

---

## 📄 Bản Quyền & Giấy Phép

Nội dung câu hỏi và hình ảnh sát hạch thuộc bản quyền tài liệu của Cục Cảnh sát giao thông & Bộ Giao thông vận tải. Ứng dụng được xây dựng phục vụ mục đích học tập và ôn thi sát hạch giấy phép lái xe.
