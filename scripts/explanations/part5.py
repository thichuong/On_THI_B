# scripts/explanations/part5.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 206 đến Câu 263
Chương 3: Kỹ thuật lái xe
"""

PART5_EXPLANATIONS = {
    206: "Khi xe tay ga xuống dốc dài: Giữ tay ga ở mức độ phù hợp để duy trì độ bám côn, kết hợp nhịp nhàng cả phanh trước và phanh sau. Tuyệt đối không tắt máy thả trôi vì sẽ mất hoàn toàn lực hãm động cơ và mất trợ lực lái.",
    
    207: "Khởi hành xe ô tô số tự động (AT): Bắt buộc phải ĐẠP HẾT HÀNH TRÌNH BÀN ĐẠP PHANH CHÂN, sau đó mới gạt cần số sang D hoặc R, hạ phanh tay, quan sát kỹ rồi từ từ nhấc chân phanh cho xe lăn bánh để tránh xe chồm lên đột ngột.",
    
    208: "Thao tác nhả phanh tay cơ khí: Dùng tay phải bóp khóa hãm (nút bấm ở đầu cần phanh) và đẩy cần phanh về phía trước hết hành trình. Nếu bị kẹt cứng, hơi kéo nhẹ cần phanh ra sau đồng thời bóp khóa hãm rồi hạ xuống.",
    
    209: "🚨 [CÂU ĐIỂM LIỆT] Khởi hành ô tô số sàn (MT) trên đường bằng: Đạp côn hết hành trình -> vào số 1 -> hạ hết phanh tay -> tăng ga nhẹ -> nhả côn từ từ đến 1/2 hành trình cho xe bắt côn bắt đầu chuyển động, sau đó tiếp tục nhả đều côn và đệm thêm ga.",
    
    210: "Kỹ thuật quay đầu xe an toàn: Quay đầu với tốc độ chậm; bật xi-nhan báo trước; nếu quay đầu ở nơi nguy hiểm (vực sâu, sườn dốc hẹp) thì nguyên tắc vàng là 'TIẾN ĐẦU VỀ PHÍA NGUY HIỂM, LÙI ĐUÔI VỀ PHÍA AN TOÀN' để người lái luôn quan sát trực diện được mép nguy hiểm.",
    
    211: "Tư thế ngồi lái xe chuẩn: Chỉnh ghế ngồi thoải mái để chân đạp hết tầm phanh, lưng thẳng tựa sát đệm ghế. Hai tay cầm vô lăng ở vị trí chuẩn '9 giờ 15 phút' hoặc '10 giờ 10 phút' (tay trái 9-10h, tay phải 2-4h).",
    
    212: "Lái xe lên dốc cao: Chủ động về số thấp từ chân dốc để xe đủ mô-men xoắn leo dốc; gần lên đến đỉnh dốc phải đi chậm, bám sát bên phải và bấm còi/nháy đèn báo hiệu cho xe ngược chiều ở góc khuất đỉnh dốc.",
    
    213: "🚨 [CÂU ĐIỂM LIỆT] Kỹ thuật đổ đèo, xuống dốc dài: Bắt buộc phải VỀ SỐ THẤP để sử dụng lực ghì hãm của động cơ (phanh động cơ), kết hợp rà phanh chân ngắt quãng. Tuyệt đối KHÔNG ĐƯỢC về số 0 (N) hay tắt máy vì sẽ làm phanh chân bị quá nhiệt dẫn đến cháy phanh, mất phanh hoàn toàn.",
    
    214: "Muốn dừng xe khi đang xuống dốc: Bật xi-nhan phải, tấp sát lề phải; đạp phanh sớm và sâu hơn đường bằng; về số 1; khi xe dừng hẳn thì về N, kéo phanh tay và có thể chèn bánh xe nếu dốc cao.",
    
    215: "Kỹ thuật vào cua (đường vòng): Giảm tốc độ TRƯỚC KHI VÀO CUA, về số thấp phù hợp, giữ đều ga trong cua và quay vô lăng theo bán kính vòng cua. Tránh phanh gấp hoặc đạp mạnh ga giữa khúc cua vì dễ làm xe văng đuôi trượt bánh.",
    
    216: "🚨 [CÂU ĐIỂM LIỆT] Thao tác rẽ phải an toàn: Bật xi-nhan phải trước một khoảng cách an toàn, giảm tốc độ, quan sát kỹ gương chiếu hậu và điểm mù bên phải, sau đó từ từ ôm cua rẽ phải sát mép đường bên phải.",
    
    217: "Thao tác rẽ trái an toàn: Bật xi-nhan trái từ xa, giảm tốc độ, quan sát các phương tiện ngược chiều và phía sau, chuyển dần sang làn sát tim đường rồi từ từ rẽ trái khi an toàn.",
    
    218: "Vượt qua rãnh lớn cắt ngang đường: Vào số 1, cho 2 bánh trước từ từ tụt xuống rãnh, tăng nhẹ ga cho bánh trước bò lên rãnh; tiếp tục để 2 bánh sau từ từ xuống rãnh rồi tăng đều ga cho xe vượt qua rãnh êm ái.",
    
    219: "Lái xe qua đường sắt: Nếu chuông reo/rào hạ thì dừng trước vạch an toàn, kéo phanh tay nếu dốc. Nếu không có tàu thì về số thấp, giữ đều ga, KHÔNG ĐƯỢC CHUYỂN SỐ giữa đường ray để tránh bị kẹt số hoặc chết máy trên đường ray.",
    
    220: "Lái xe tải tự đổ (xe ben): Đi đường xấu phải đi chậm để tránh lệch thùng ben; khi đổ hàng phải chọn nền đất cứng phẳng, kéo hết phanh đỗ rồi mới nâng ben; đổ xong phải hạ hết thùng ben trước khi lăn bánh.",
    
    221: "Thao tác tăng số (xe số sàn): Tuyệt đối KHÔNG NHÌN XUỐNG BUỒNG LÁI (mắt luôn nhìn đường); tăng số theo thứ tự từ thấp đến cao (1 -> 2 -> 3 -> 4...) phối hợp tay chân nhịp nhàng.",
    
    222: "Thao tác giảm số: Mắt luôn nhìn bao quát đường phía trước, không nhìn xuống cần số; giảm số theo thứ tự từ cao về thấp, vù ga đồng tốc phù hợp để xe không bị giật khựng.",
    
    223: "Để giảm tốc độ an toàn khi xuống dốc dài: Người lái xe phải VỀ SỐ THẤP thích hợp, nhả bàn đạp ga và kết hợp phanh chân có mức độ để kiểm soát tốc độ xe.",
    
    224: "Lái xe qua đường ngập nước: Quan sát mực nước (không ngập quá tâm bánh xe/cổ hút gió), VỀ SỐ THẤP (số 1 hoặc số L), GIỮ ĐỀU GA ở mức vừa phải để nước không tràn vào ống xả, không dừng xe hoặc chuyển số giữa vùng ngập.",
    
    225: "Gặp xe ngược chiều ban đêm: Bắt buộc CHUYỂN TỪ PHA SANG CỐT (đèn chiếu gần); mắt nhìn chếch sang lề đường bên phải xe mình để tránh bị ánh sáng đèn đối diện gây lóa mù mắt tạm thời.",
    
    226: "Lái xe trên đường trơn ướt, bùn lầy: Giữ thẳng lái theo vệt bánh xe trước, đi số thấp, giữ đều ga; TUYỆT ĐỐI KHÔNG ĐÁNH LÁI NGOẶT VÀ KHÔNG PHANH GẤP vì xe sẽ bị bó cứng bánh mất lái trượt xoay vòng.",
    
    227: "🚨 [CÂU ĐIỂM LIỆT] Biểu tượng chữ (P) hoặc dấu chấm than (!) màu đỏ trong vòng tròn: Báo hiệu hệ thống PHANH ĐỖ (phanh tay) đang hoạt động hoặc hệ thống phanh gặp sự cố thiếu dầu phanh.",
    
    228: "🚨 [CÂU ĐIỂM LIỆT] Biểu tượng bình dầu có giọt dầu nhỏ màu đỏ: Cảnh báo ÁP SUẤT DẦU BÔI TRƠN Ở MỨC THẤP hoặc thiếu dầu nhớt động cơ. Phải lập tức tấp xe vào lề tắt máy kiểm tra, nếu cố chạy sẽ bị bó kẹt lột dên phá hỏng động cơ.",
    
    229: "Biểu tượng hình chiếc ô tô mở toang cửa: Cảnh báo CỬA XE ĐÓNG CHƯA CHẶT hoặc có cửa xe chưa đóng, gây nguy cơ rơi hành khách ra ngoài khi xe chạy.",
    
    230: "Biểu tượng người ngồi thắt dây chéo màu đỏ: Báo hiệu người lái xe hoặc hành khách ngồi hàng ghế trước CHƯA CÀI DÂY ĐAI AN TOÀN.",
    
    231: "Biểu tượng cây bơm xăng màu vàng: Báo hiệu xe SẮP HẾT NHIÊN LIỆU, người lái cần chủ động tìm trạm cấp nhiên liệu gần nhất.",
    
    232: "Xăng sinh học (như E5, E10) và khí sinh học (CNG, LPG) khi đốt cháy sinh ra ít khí độc hại (CO, HC, muội than) hơn rất nhiều so với xăng khoáng và dầu diesel thông thường, giúp bảo vệ môi trường.",
    
    233: "🚨 [CÂU ĐIỂM LIỆT] Biện pháp tiết kiệm nhiên liệu tối ưu: Thường xuyên bảo dưỡng xe định kỳ; kiểm tra áp suất lốp đúng chuẩn (lốp non gây hao 5-10% xăng); lái xe đều ga, giữ khoảng cách và tốc độ ổn định.",
    
    234: "Mở cửa xe an toàn: Quan sát kỹ gương chiếu hậu và ngoái đầu nhìn phía sau; mở hé cửa 10-15 cm để người phía sau thấy; khi thấy thật an toàn mới mở rộng cửa vừa đủ để bước xuống xe.",
    
    235: "Qua đường sắt không rào chắn: Dừng xe cách đường ray tối thiểu 5m, quan sát 2 phía; nếu không có tàu thì về số thấp, giữ đều ga vượt dứt khoát qua đường sắt.",
    
    236: "Quy tắc an toàn qua đường sắt không người gác: Dừng lại trước vạch dừng, hạ cửa kính, tắt thiết bị âm thanh để lắng nghe tiếng còi tàu và quan sát 2 phía đường ray. Hành động này là hoàn toàn CHÍNH XÁC.",
    
    237: "Lái xe số tự động trên đường trơn, lầy lội: Chủ động gạt cần số về các cấp số thấp (L, D1, D2 hoặc chế độ M/S gán số 1, 2) kết hợp phanh chân để tăng lực kéo và ghì xe an toàn.",
    
    238: "Khi động cơ đang nổ máy mà muốn chỉnh ghế ngồi: Cần số bắt buộc phải để ở vị trí N (số mo) hoặc P (đỗ) và kéo phanh tay, tránh trường hợp chân vô tình đạp trúng chân ga làm xe vọt đi gây tai nạn.",
    
    239: "Nguyên tắc sống còn khi lái xe số tự động: 'CHỈ SỬ DỤNG CHÂN PHẢI' để luân phiên điều khiển bàn đạp ga và bàn đạp phanh; chân trái luôn đặt cố định trên bàn để chân bên trái, cấm dùng chân trái đạp phanh.",
    
    240: "Lái xe trong sương mù hoặc mưa to: Giảm tốc độ, giữ khoảng cách gấp đôi bình thường với xe trước, bật đèn sương mù và đèn chiếu gần (đèn cốt). Tuyệt đối không bật đèn pha vì ánh sáng pha sẽ phản xạ vào hạt sương gây lóa mắt.",
    
    241: "Bị đèn pha xe ngược chiều làm chói mắt: Giảm tốc độ, giữ chặt tay lái, hướng ánh nhìn chếch xuống lề đường bên phải xe mình để lấy vạch mép đường làm căn cứ định hướng.",
    
    242: "🚨 [CÂU ĐIỂM LIỆT] Kỹ năng phanh xe mô tô hiệu quả nhất: Giảm hết tay ga, sử dụng ĐỒNG THỜI CẢ PHANH TRƯỚC VÀ PHANH SAU với lực phanh nhấp nhả nhịp nhàng để xe không bị trượt lết bánh hoặc lộn đầu.",
    
    243: "Lái xe qua đoạn đường gồ ghề nhiều ổ gà: Giảm tốc độ, về số thấp, giữ đều chân ga để giảm chấn và bảo vệ hệ thống treo gầm xe.",
    
    244: "Gặp mưa to sương mù dày đặc che khuất hoàn toàn tầm nhìn: Bật đèn chiếu gần và đèn khẩn cấp, tìm vị trí an toàn ngoài lề đường dừng xe lại chờ thời tiết cải thiện.",
    
    245: "Lái xe dưới trời mưa: Giảm tốc độ, không phanh gấp, không ngoặt vô lăng đột ngột vì mặt đường mưa rất trơn trượt (hiện tượng trượt nước Hydroplaning); bật gạt mưa và đèn chiếu gần.",
    
    246: "🚨 [CÂU ĐIỂM LIỆT] Lùi xe an toàn: Bật xi-nhan/đèn cảnh báo, quan sát bao quát gương chiếu hậu 2 bên và phía sau xe, lùi xe với tốc độ thật chậm để làm chủ tình huống.",
    
    247: "Lái xe trong khu dân cư đông đúc: Luôn làm chủ tốc độ an toàn, nhường đường cho người đi bộ, giữ cự ly an toàn với xe trước và chỉ chuyển làn ở nơi có vạch đứt cho phép.",
    
    248: "Nhập làn cao tốc: Bật xi-nhan xin vào làn, cho xe chạy trên làn tăng tốc để đạt vận tốc tương đương với dòng xe đang chạy trên cao tốc, quan sát gương chiếu hậu thấy an toàn mới chuyển làn nhập vào đường chính.",
    
    249: "Ra khỏi cao tốc: Quan sát biển báo lối ra từ xa, bật xi-nhan phải, chuyển dần vào làn giảm tốc độ, rà phanh giảm dần tốc độ theo biển chỉ dẫn trước khi rẽ ra khỏi cao tốc.",
    
    250: "Làn dừng xe khẩn cấp trên cao tốc CHỈ ĐƯỢC DÙNG khi: xe gặp sự cố kỹ thuật hỏng hóc, tai nạn hoặc trường hợp bất khả kháng về y tế. Cấm dừng đỗ để đi vệ sinh, nghỉ ngơi, chụp ảnh.",
    
    251: "Vượt xe container/xe kéo rơ moóc: Tránh rơi vào điểm mù lớn của xe tải rơ moóc; bật xi-nhan và nháy đèn xin vượt; chỉ vượt khi có đủ khoảng trống an toàn; vượt dứt khoát không chạy song song quá lâu.",
    
    252: "Xuống dốc dài xe số tự động: Nhả chân ga, gạt cần số về số thấp (vị trí L, D1, D2 hoặc chế độ tay M-) để tận dụng lực hãm của động cơ, phối hợp rà phanh chân ngắt quãng.",
    
    253: "Từ đường nhánh ra đường chính: Bắt buộc phải quan sát kỹ, giảm tốc độ và NHƯỜNG ĐƯỜNG cho mọi phương tiện đang lưu thông trên đường chính từ bất kỳ hướng nào tới.",
    
    254: "Muốn dùng điện thoại khi lái xe: Người lái xe phải giảm tốc độ, tìm nơi dừng xe/đỗ xe hợp pháp và an toàn theo quy định, dừng hẳn xe lại rồi mới sử dụng điện thoại.",
    
    255: "Thói quen nguy hiểm chết người khi lái xe tay ga: CHỈ BÓP PHANH TRƯỚC (tay phanh bên phải). Do phanh đĩa trước ăn rất gắt, khi chỉ bóp phanh trước bánh trước sẽ bị khóa cứng gây trượt đổ xe hoặc lộn nhào qua đầu xe.",
    
    256: "Mở cửa xe an toàn: Quan sát gương chiếu hậu và ngoái đầu nhìn sau; mở hé cửa thăm dò; khi chắc chắn an toàn mới mở rộng cửa vừa đủ để xuống xe.",
    
    257: "Quay đầu xe mô tô: Bật xi-nhan trước khi quay, giảm tốc độ, chỉ quay đầu tại nơi quy định, quan sát toàn diện và nhường đường cho xe từ bên phải và xe đi thẳng đối diện.",
    
    258: "🚨 [CÂU ĐIỂM LIỆT] Tay ga trên xe mô tô hai bánh có 2 tác dụng chính: 1. Để điều khiển xe chạy tiến về phía trước; 2. Để điều tiết lượng hòa khí vào động cơ, qua đó kiểm soát công suất và tốc độ xe. (Xe mô tô không có số lùi).",
    
    259: "Tác dụng của gương chiếu hậu mô tô: Dùng để quan sát an toàn phía sau ở cả bên trái và bên phải trước khi chuyển hướng hoặc chuyển làn.",
    
    260: "Nguyên tắc điều khiển tay ga xe mô tô an toàn: 'TĂNG GA TỪ TỪ - GIẢM GA THẬT NHANH' để kiểm soát tốc độ êm ái và xử lý phanh khẩn cấp kịp thời khi gặp chướng ngại vật.",
    
    261: "Đi xe mô tô trên đường hẹp mấp mô, trơn trượt: Đi chậm, nhìn xa 5-10m phía trước để chọn lối đi, không bóp cứng phanh trước, giữ trọng tâm cơ thể cân bằng thẳng hàng với thân xe.",
    
    262: "Lái xe ô tô điện đổ đèo, xuống dốc dài: Nhả bàn đạp ga để hệ thống phanh tái sinh (Regenerative Braking) hoạt động ghì xe lại và nạp lại điện cho pin, kết hợp rà phanh chân khi cần thiết.",
    
    263: "Lái xe điện qua vùng ngập nước: Xác định mức độ ngập an toàn của xe, đi đều chân ga tốc độ chậm không tạo sóng nước tràn vào cổ hút gió làm mát pin, giữ khoảng cách với người đi bộ."
}

