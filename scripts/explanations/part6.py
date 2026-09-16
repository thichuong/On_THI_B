# scripts/explanations/part6.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 264 đến Câu 300
Chương 4: Cấu tạo và sửa chữa
"""

PART6_EXPLANATIONS = {
    264: "Kiểm tra mức dầu bôi trơn: Đỗ xe nơi bằng phẳng, tắt máy; rút que thăm dầu ra, dùng giẻ sạch lau khô que, cắm hết cỡ que vào lại các-te rồi rút ra xem vệt dầu. Mức dầu chuẩn phải nằm giữa hai vạch Min (tối thiểu) và Max (tối đa).",
    
    265: "Tiêu chuẩn an toàn kỹ thuật ô tô: Đầy đủ kính an toàn không rạn nứt; phanh và lái hoạt động chuẩn xác; vô lăng bên trái; đủ hệ thống đèn (chiếu sáng, xi-nhan, đèn phanh, soi biển số); ống xả có giảm thanh và giảm khói.",
    
    266: "Bộ phận giảm thanh (ống pô): BẮT BUỘC phải có và hoạt động tốt trên cả mô tô và ô tô nhằm giảm thiểu ô nhiễm tiếng ồn ra môi trường xung quanh.",
    
    267: "Hệ thống đèn bắt buộc: Đèn chiếu sáng xa/gần, đèn soi biển số, đèn phanh (báo hãm), và đèn xi-nhan báo rẽ. Dàn đèn nóc xe tự chế lắp thêm bị nghiêm cấm vì gây chói mắt nguy hiểm.",
    
    268: "Kính chắn gió ô tô bắt buộc phải là loại KÍNH AN TOÀN nhiều lớp (Laminated Glass): khi vỡ không tạo mảnh nhọn sắc gây sát thương, hình ảnh quan sát qua kính phải thật, không bị biến dạng méo mó.",
    
    269: "Quy chuẩn bánh xe, lốp xe: Bánh lắp chắc chắn đúng quy cách; lốp đủ số lượng, đủ áp suất tiêu chuẩn, không nứt rách/phồng rộp; lốp trên cùng một trục phải cùng kích cỡ, cùng kiểu hoa lốp.",
    
    270: "Hệ thống lái ô tô: Bảo đảm xe chuyển hướng chính xác, nhẹ nhàng, ổn định ở mọi vận tốc; các cơ cấu lái không va chạm vào gầm; lực đánh lái sang trái và sang phải phải đều nhau.",
    
    271: "Mục đích bảo dưỡng ô tô thường xuyên: Giúp xe luôn vận hành ổn định, giảm hao mòn cơ khí, kéo dài tuổi thọ phương tiện và kịp thời phát hiện nguy cơ hư hỏng để khắc phục sớm.",
    
    272: "Động cơ diesel hoạt động theo nguyên lý nén nổ (không dùng bugi đánh lửa). Vì vậy nguyên nhân động cơ diesel không nổ là: Hết nhiên liệu, tắc lọc dầu, tắc lọc gió, hoặc nhiên liệu bị lẫn bọt khí (e gió)/tạp chất. (Các đáp án có chữ 'không có tia lửa điện' là sai vì máy dầu không có bugi đánh lửa).",
    
    273: "Quy chuẩn ống xả ô tô: Không đặt ở vị trí gần ống dẫn nhiên liệu gây nguy cơ cháy nổ; miệng thoát khí thải không được hướng về phía trước hoặc hướng chếch sang bên phải phía người đi bộ trên vỉa hè.",
    
    274: "Dây đai an toàn: Phải đủ số lượng cho các vị trí ghế; dây không rách đứt; chốt cài trơn tru không tự bung; cơ cấu hãm quán tính phải khóa chặt dây lại ngay lập tức khi giật dây đột ngột.",
    
    275: "Định nghĩa động cơ 4 kỳ: Là loại động cơ nhiệt mà để hoàn thành một chu trình công tác (Hút - Nén - Nổ - Xả), pít-tông phải thực hiện 4 HÀNH TRÌNH (tương ứng trục khuỷu quay 2 vòng), trong đó chỉ có 1 kỳ sinh công (kỳ nổ).",
    
    276: "Công dụng hệ thống bôi trơn: Cung cấp dầu nhớt sạch dưới áp suất đến các bề mặt ma sát chuyển động để: giảm ma sát, giảm mài mòn, làm mát chi tiết, làm kín buồng đốt, làm sạch muội than và chống gỉ sét kim loại.",
    
    277: "Niên hạn sử dụng của xe ô tô tải chở hàng: Không quá 25 NĂM (tính bắt đầu từ năm sản xuất).",
    
    278: "Niên hạn sử dụng của xe ô tô chở người trên 8 chỗ ngồi (xe khách kinh doanh vận tải): Không quá 20 NĂM (tính bắt đầu từ năm sản xuất).",
    
    279: "Công dụng của động cơ xe ô tô: Biến đổi NHIỆT NĂNG (từ việc đốt cháy hòa khí nhiên liệu trong xi-lanh) thành CƠ NĂNG làm quay trục khuỷu, truyền lực đến các bánh xe chủ động giúp xe chuyển động.",
    
    280: "Công dụng hệ thống truyền lực (drivetrain): Dùng để truyền mô-men quay từ trục khuỷu động cơ qua ly hợp, hộp số, trục các-đăng và bộ vi sai tới các bánh xe chủ động của ô tô.",
    
    281: "Công dụng ly hợp (bộ côn): Dùng để truyền hoặc ngắt truyền động mô-men xoắn từ động cơ đến hộp số một cách êm dịu khi người lái khởi hành hoặc chuyển đổi cấp số.",
    
    282: "Công dụng hộp số: Truyền và thay đổi mô-men quay/tốc độ từ động cơ đến bánh xe chủ động; ngắt truyền động lâu dài (về số 0/mo); và cho phép ô tô chuyển động lùi (số R).",
    
    283: "Công dụng hệ thống lái: Dùng để THAY ĐỔI HƯỚNG CHUYỂN ĐỘNG hoặc giữ cho xe chuyển động ổn định theo một hướng xác định theo sự điều khiển của người lái.",
    
    284: "Công dụng hệ thống phanh (thắng): Dùng để giảm tốc độ, dừng hẳn chuyển động của xe ô tô và GIỮ CHO XE ĐỨNG YÊN trên đường bằng cũng như trên đường dốc (phanh tay/phanh đỗ).",
    
    285: "Đèn phanh (đèn hậu màu đỏ): Có 2 tác dụng: 1. Cảnh báo xe sau biết xe đang giảm tốc/phanh để chủ động giữ cự ly tránh đâm va; 2. Định vị nhận diện kích thước xe trong đêm tối hoặc thời tiết xấu.",
    
    286: "Biểu tượng nhiệt kế ngâm trong sóng nước: Báo hiệu NHIỆT ĐỘ NƯỚC LÀM MÁT ĐỘNG CƠ QUÁ CAO (quá nhiệt). Cần tấp xe vào lề an toàn, để máy nổ không tải cho nguội bớt trước khi kiểm tra két nước.",
    
    287: "Biểu tượng khối động cơ (Check Engine) màu vàng: Cảnh báo HỆ THỐNG ĐỘNG CƠ HOẶC CẢM BIẾN KHÍ THẢI ĐANG BỊ LỖI, cần đưa xe đến xưởng kiểm tra bằng máy quét lỗi chuyên dụng.",
    
    288: "Biểu tượng mặt cắt lốp xe có dấu chấm than (!) ở giữa: Cảnh báo ÁP SUẤT LỐP KHÔNG ĐỦ (lốp bị non hơi hoặc thủng lốp), người lái cần kiểm tra và bơm bổ sung áp suất theo tiêu chuẩn.",
    
    289: "Biểu tượng vòng tròn chữ ABS ở giữa: Báo hiệu HỆ THỐNG PHANH CHỐNG BÓ CỨNG (ABS) GẶP SỰ CỐ BỊ LỖI. Lúc này xe vẫn có phanh cơ khí thông thường nhưng tính năng chống trượt bánh khi phanh gấp không hoạt động.",
    
    290: "Khởi động xe ô tô số tự động có nút bấm Start/Stop: BẮT BUỘC PHẢI ĐẠP HẾT HÀNH TRÌNH BÀN ĐẠP PHANH CHÂN thì nút khởi động mới cho phép đề nổ máy (cơ chế an toàn chống vọt xe ngoài ý muốn).",
    
    291: "Công dụng bình ắc quy: Dùng để TÍCH TRỮ ĐIỆN NĂNG (dạng hóa năng) và cung cấp nguồn điện cho củ đề khởi động xe, đèn, còi và các thiết bị điện tử khi động cơ chưa hoạt động.",
    
    292: "Công dụng máy phát điện (Alternator): Khi động cơ đã nổ máy, máy phát biến cơ năng thành điện năng để CUNG CẤP CHO TOÀN BỘ PHỤ TẢI ĐIỆN trên xe hoạt động và đồng thời nạp điện bổ sung vào ắc quy.",
    
    293: "Tác dụng của dây đai an toàn (Seatbelt): Giữ chặt cơ thể người lái và hành khách dính vào lưng ghế, ngăn không cho cơ thể bị quăng quật hoặc văng ra khỏi kính chắn gió khi xe phanh gấp hoặc va chạm mạnh.",
    
    294: "Tác dụng của túi khí (Airbag): Bung ra trong vài phần nghìn giây khi có va chạm mạnh để GIẢM KHẢ NĂNG VA ĐẬP của vùng đầu, ngực với vô lăng/taplo, đồng thời hấp thụ phân tán lực va đập tác động lên cơ thể.",
    
    295: "Biểu tượng vô lăng lái kèm dấu chấm than (!): Cảnh báo HỆ THỐNG TRỢ LỰC LÁI GẶP SỰ CỐ KỸ THUẬT (lái sẽ bị nặng hoặc mất trợ lực điện/dầu).",
    
    296: "Hình ảnh con đội/kích chữ A (kích cơ khí hoặc kích thủy lực): Thiết bị chuyên dùng để KÍCH (NÂNG) XE Ô TÔ lên khỏi mặt đất khi cần thay bánh xe dự phòng.",
    
    297: "Hình ảnh chiếc búa nhọn màu đỏ: Búa thoát hiểm chuyên dùng để PHÁ VỠ CỬA KÍNH Ô TÔ trong các tình huống khẩn cấp (tai nạn, xe chìm xuống nước, cháy nổ kẹt cửa).",
    
    298: "Hình ảnh bình chữa cháy mini dạng bột/CO2 xách tay: Dùng để DẬP TẮT CÁC ĐÁM CHÁY HỎA HOẠN ban đầu phát sinh trên xe cơ giới.",
    
    299: "Nút bấm tam giác kép màu đỏ: Nút bật ĐÈN CẢNH BÁO NGUY HIỂM / KHẨN CẤP (Hazard Light). Bấm nút này 4 đèn xi-nhan sẽ nhấp nháy đồng thời để cảnh báo xe gặp sự cố trên đường.",
    
    300: "Biểu tượng chữ ECO màu xanh lá cây: Báo hiệu CHẾ ĐỘ LÁI TIẾT KIỆM NHIÊN LIỆU (Eco Mode) đang được kích hoạt nhằm tối ưu hóa phản ứng chân ga và bước số."
}

