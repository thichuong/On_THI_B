# Bộ Kiểm Thử Tự Động (Test Suite) - Ứng Dụng Ôn Thi GPLX 600 Câu

Thư mục này chứa toàn bộ các bài kiểm thử tự động (Unit Tests) để xác minh độ chính xác của các tính năng cốt lõi trong hệ thống.
Bộ test sử dụng **Node.js Native Test Runner** (`node:test` và `node:assert`), không cần cài đặt thêm thư viện nặng bên ngoài, chạy cực nhanh và ổn định.

---

## 🚀 Cách Chạy Kiểm Thử

Để chạy toàn bộ test suite, sử dụng lệnh:

```bash
npm test
```

Hoặc chạy trực tiếp bằng Node.js:

```bash
node --test tests/**/*.test.js
```

Để chạy riêng lẻ từng file test:

```bash
# Chỉ test bộ tạo đề thi và chu kỳ câu hỏi
node --test tests/examEngine.test.js

# Chỉ test dịch vụ lưu trữ câu sai, chu kỳ và bookmark
node --test tests/storageService.test.js
```

---

## 📋 Cấu Trúc Các Bài Test (Test Cases)

### 1. `tests/examEngine.test.js` (8 Test Cases)
- **Standard Exam Generation**: Kiểm tra đề thi chuẩn tạo đủ đúng 50 câu, có 1-2 câu điểm liệt, không trùng lặp câu nào trong cùng 1 đề.
- **Quick Exam Generation**: Kiểm tra đề thi nhanh tạo đủ đúng 20 câu, có tối thiểu 1 câu điểm liệt, không trùng lặp.
- **Unseen Questions Cycle for Standard Exam**: Mô phỏng 13 đề thi chuẩn liên tiếp ($12 \times 50 = 600$ câu):
  - Xác nhận đề 1 đến đề 12 lấy 100% câu chưa làm, không trùng lặp bất kỳ câu nào giữa các đề.
  - Xác nhận đề 13 phát hiện hết câu ($0 < 50$), tự động kích hoạt cờ `isCycleReset: true` và gọi callback `onCycleReset` để bắt đầu chu kỳ mới.
- **Unseen Questions Cycle for Quick Exam**: Mô phỏng 31 đề thi nhanh liên tiếp ($30 \times 20 = 600$ câu):
  - Xác nhận 30 đề đầu không trùng lặp câu nào.
  - Xác nhận đề 31 tự động reset chu kỳ.
- **Wrong Redo Mode (0 câu sai)**: Kiểm tra khi danh sách câu sai rỗng $\rightarrow$ trả về đề 0 câu.
- **Wrong Redo Mode (< 20 câu sai, ví dụ 7 câu)**: Kiểm tra đề thi trả về đúng 7 câu sai tương ứng.
- **Wrong Redo Mode (> 20 câu sai, ví dụ 35 câu)**: Kiểm tra đề thi giới hạn tối đa đúng 20 câu từ danh sách sai.
- **Grading Logic (`gradeExam`)**: Kiểm tra thuật toán chấm điểm đúng/sai, đếm câu chưa làm, phát hiện câu điểm liệt và kết luận ĐẠT / KHÔNG ĐẠT.

### 2. `tests/storageService.test.js` (5 Test Cases)
- **Record and retrieve wrong questions**: Kiểm tra ghi nhận câu sai và đếm số lần sai.
- **Remove wrong question (`removeWrongQuestion`)**: Kiểm tra việc xóa triệt để một câu hỏi khỏi danh sách câu sai khi người dùng làm đúng ở chế độ làm lại câu sai.
- **Record correct question (`recordCorrectQuestion`)**: Kiểm tra giảm số lần sai và tự động xóa khi số lần sai $\le 0$.
- **Exam Cycle tracking and status**: Kiểm tra tính toán `seenCount`, `remainingCount` và hàm `resetExamCycle`.
- **Bookmarks toggle**: Kiểm tra đánh dấu và bỏ đánh dấu câu hỏi.

---

## ➕ Cách Thêm Test Case Mới Trong Tương Lai

1. Mở file test tương ứng hoặc tạo mới file `tests/<tên_tính_năng>.test.js`.
2. Import module `test` và `assert`:
   ```javascript
   import test from 'node:test';
   import assert from 'node:assert/strict';
   ```
3. Khai báo test case:
   ```javascript
   test('Tên tính năng cần kiểm thử', () => {
     // Chuẩn bị dữ liệu & gọi hàm
     const result = ...;
     // Kiểm tra kết quả kỳ vọng
     assert.equal(result, expectedValue);
   });
   ```
4. Chạy `npm test` để xác nhận bài test vượt qua.

