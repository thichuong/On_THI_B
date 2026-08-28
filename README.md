# 🚗 Ứng Dụng Ôn Thi Sát Hạch GPLX 600 Câu (2025)

Ứng dụng web hiện đại, trực quan và tối ưu giúp học viên ôn luyện toàn diện bộ **600 câu hỏi sát hạch lý thuyết lái xe ô tô / mô tô** theo chuẩn tài liệu của Cục Cảnh sát giao thông & Luật Trật tự, An toàn giao thông đường bộ.

---

## 🌟 Tính Năng Nổi Bật

- 📝 **Thi Thử Sát Hạch Chuẩn (50 câu / 33 phút)**:
  - Tự động sinh đề ngẫu nhiên chuẩn tỉ lệ 6 chương và bắt buộc có 1-2 câu điểm liệt.
  - Bấm giờ đếm ngược thời gian thực (33 phút / 1980 giây).
  - Chấm điểm tự động chuẩn xác: Đạt từ 45/50 điểm trở lên và không sai câu điểm liệt.
  - Chế độ xem lại chi tiết từng câu kèm lời giải thích và đáp án chuẩn.

- ⚡ **Chế Độ Thi Nhanh (20 câu / 10 phút)**:
  - Dành cho việc luyện phản xạ nhanh chóng mà không tốn nhiều thời gian.
  - Tự động chọn 20 câu ngẫu nhiên cân đối các chương và **luôn có ít nhất 1 câu điểm liệt**.
  - Bấm giờ đếm ngược 10 phút (600 giây), điểm đạt chuẩn 18/20 và không sai câu điểm liệt.

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
├── wrangler.jsonc             # Cấu hình deploy Cloudflare Workers
└── README.md
```

---

## 💻 Danh Sách Lệnh & Hướng Dẫn Sử Dụng

### 1. Bảng tóm tắt các lệnh nhanh (Command Cheat Sheet)

| Lệnh | Mô tả tác vụ |
| :--- | :--- |
| `npm install` | Cài đặt các thư viện phụ thuộc của dự án |
| `npm run dev` | Khởi chạy máy chủ phát triển (Dev server) tại `http://localhost:5173` |
| `npm run build` | Đóng gói tối ưu ứng dụng cho Production ra thư mục `dist/` |
| `npm run preview` | Xem thử kết quả bản đóng gói `dist/` trên máy local |
| `npm run deploy` | Tự động **Build + Deploy** lên **Cloudflare Workers** |
| `npm run deploy:pages` | Tự động **Build + Deploy** lên **Cloudflare Pages** |
| `npx wrangler login` | Đăng nhập tài khoản Cloudflare trên Terminal qua trình duyệt |
| `python3 extract_questions.py` | Trích xuất lại toàn bộ câu hỏi & cắt ảnh từ file PDF gốc |

---

### 2. Phát triển tại môi trường cục bộ (Local Development)

```bash
# Cài đặt thư viện (chỉ cần chạy lần đầu hoặc khi đổi máy)
npm install

# Bật dev server có hỗ trợ Hot Module Replacement (HMR)
npm run dev
```

---

### 3. Đóng gói & Kiểm tra bản Production

```bash
# Build mã nguồn thành file tĩnh tối ưu trong thư mục dist/
npm run build

# Chạy server local để kiểm tra xem bản build dist/ hoạt động trơn tru không
npm run preview
```

---

### 4. 🚀 Hướng Dẫn Deploy Lên Cloudflare

Ứng dụng được thiết lập sẵn sàng để triển khai trực tiếp lên mạng lưới toàn cầu (Edge Network) của Cloudflare:

#### Deploy lên Cloudflare Workers
```bash
# Bước 1: Đăng nhập tài khoản Cloudflare (chỉ cần làm 1 lần trên máy)
npx wrangler login

# Bước 2: Build và đẩy lên Cloudflare Workers
npm run deploy
```
*Sau khi hoàn tất, bạn sẽ nhận được đường dẫn truy cập trực tiếp (VD: `https://on-thi-gplx-600.<subdomain>.workers.dev`).*

---

### 5. 🐍 Trích xuất & Làm mới Dữ liệu từ PDF (Tùy chọn)

Nếu bạn có tài liệu PDF mới hoặc muốn tạo lại file câu hỏi và hình ảnh:

```bash
# Cài đặt thư viện Python xử lý PDF
pip install pymupdf

# Chạy script bóc tách câu hỏi, đáp án gạch chân và trích xuất hình ảnh minh họa
python3 extract_questions.py
```

---

## 📄 Bản Quyền & Giấy Phép

Nội dung câu hỏi và hình ảnh sát hạch thuộc bản quyền tài liệu của Cục Cảnh sát giao thông & Bộ Giao thông vận tải. Ứng dụng được xây dựng phục vụ mục đích học tập và ôn thi sát hạch giấy phép lái xe.

