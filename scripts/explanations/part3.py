# scripts/explanations/part3.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 121 đến Câu 180
Chương 1: Quy định chung và quy tắc giao thông đường bộ
"""

PART3_EXPLANATIONS = {
    121: "Theo Luật Trật tự, an toàn giao thông đường bộ 2024: Độ tuổi tối đa của người lái xe ô tô chở người trên 29 chỗ, xe khách giường nằm là đủ 57 tuổi đối với nam và đủ 55 tuổi đối với nữ.",
    
    122: "Độ tuổi lái xe ô tô chở người từ trên 16 chỗ đến 29 chỗ (hạng D2) là đủ 24 tuổi trở lên.",
    
    123: "Người đủ từ 16 tuổi đến dưới 18 tuổi CHỈ ĐƯỢC PHÉP điều khiển xe gắn máy (có dung tích xi-lanh dưới 50 cm3 hoặc xe máy điện có công suất động cơ điện không quá 4 kW). Chưa được cấp bằng lái ô tô hoặc mô tô.",
    
    124: "Người có GPLX hạng A1 KHÔNG ĐƯỢC PHÉP điều khiển xe mô tô ba bánh (xe ba bánh dành riêng cho thương binh, người khuyết tật yêu cầu giấy phép lái xe chuyên biệt).",
    
    125: "Theo Luật mới áp dụng từ 01/01/2025: Giấy phép lái xe hạng A1 cấp cho người lái xe mô tô hai bánh có dung tích xi-lanh ĐẾN 125 cm3 hoặc công suất động cơ điện đến 11 kW.",
    
    126: "Giấy phép lái xe hạng A cấp cho người điều khiển xe mô tô hai bánh có dung tích xi-lanh TRÊN 125 cm3 (hoặc xe điện trên 11 kW) và được phép điều khiển toàn bộ các loại xe quy định cho hạng A1.",
    
    127: "Hạng B (theo luật mới): Được lái ô tô chở người đến 8 chỗ (không kể ghế lái), ô tô tải và ô tô chuyên dùng có khối lượng toàn bộ theo thiết kế đến 3.500 kg; kéo rơ moóc đến 750 kg.",
    
    128: "Hạng C1: Được cấp cho người lái xe ô tô tải và ô tô chuyên dùng có khối lượng toàn bộ từ TRÊN 3.500 kg ĐẾN 7.500 kg; kéo rơ moóc đến 750 kg.",
    
    129: "Hạng C: Được lái ô tô tải và ô tô chuyên dùng có khối lượng toàn bộ TRÊN 7.500 kg và toàn bộ các loại xe quy định cho hạng C1; kéo rơ moóc đến 750 kg.",
    
    130: "Hạng D1: Được lái ô tô chở người từ TRÊN 8 CHỖ ĐẾN 16 CHỖ (không kể ghế lái); kéo rơ moóc đến 750 kg.",
    
    131: "Hạng D2: Được lái ô tô chở người từ TRÊN 16 CHỖ ĐẾN 29 CHỖ (kể cả xe buýt); và toàn bộ xe quy định cho hạng D1; kéo rơ moóc đến 750 kg.",
    
    132: "Hạng D: Được lái xe chở khách TRÊN 29 CHỖ, xe giường nằm và toàn bộ các loại xe quy định cho các hạng B, C1, C, D1, D2.",
    
    133: "Hạng BE: Cấp cho người đã có GPLX hạng B để kéo thêm rơ moóc có khối lượng toàn bộ TRÊN 750 kg.",
    
    134: "Hạng CE: Cấp cho người đã có GPLX hạng C để kéo thêm rơ moóc có khối lượng toàn bộ TRÊN 750 kg, hoặc lái xe ô tô đầu kéo kéo sơ mi rơ moóc.",
    
    135: "Hạng DE: Cấp cho người đã có GPLX hạng D để kéo thêm rơ moóc có khối lượng toàn bộ TRÊN 750 kg, hoặc điều khiển ô tô chở khách nối toa.",
    
    136: "Người tập lái ô tô khi tham gia giao thông bắt buộc phải thực hành trên xe tập lái có gắn biển 'TẬP LÁI', chạy trên các tuyến đường được phê duyệt tập lái và có giáo viên dạy lái ngồi bên cạnh bảo trợ tay lái.",
    
    137: "Người lái xe khi tham gia giao thông phải đủ độ tuổi, có đủ sức khỏe và sở hữu Giấy phép lái xe hợp lệ (đang còn điểm và còn hạn sử dụng) phù hợp với loại xe đang điều khiển.",
    
    138: "Khi lái xe, người lái phải mang theo: Đăng ký xe (hoặc bản sao kèm biên bản ngân hàng thế chấp), GPLX, Chứng nhận đăng kiểm và Bảo hiểm TNDS bắt buộc. Trường hợp các giấy tờ đã tích hợp trên VNeID thì việc xuất trình qua VNeID có giá trị tương đương.",
    
    139: "GPLX bị thu hồi khi: Không đủ điều kiện sức khỏe theo kết luận y tế; GPLX được cấp sai quy định; hoặc quá thời hạn tạm giữ/hết thời hiệu xử phạt mà người vi phạm không đến nhận không có lý do chính đáng.",
    
    140: "Quy định trừ điểm bằng lái: Người có GPLX chưa bị trừ hết 12 điểm sẽ được TỰ ĐỘNG PHỤC HỒI ĐỦ 12 ĐIỂM nếu trong thời hạn 12 tháng kể từ ngày bị trừ điểm gần nhất không bị trừ thêm điểm nào.",
    
    141: "Nếu bị trừ hết 12 điểm: Sau thời hạn ÍT NHẤT 06 THÁNG kể từ ngày bị trừ hết điểm, người lái xe phải tham gia kiểm tra lại kiến thức pháp luật về TTATGT đường bộ, khi đạt yêu cầu mới được phục hồi đủ 12 điểm.",
    
    142: "Chủ xe đứng tên trên Giấy chứng nhận đăng ký xe khi mua bán, chuyển nhượng mà chưa làm thủ tục thu hồi đăng ký, biển số thì vẫn phải TIẾP TỤC CHỊU MỌI TRÁCH NHIỆM pháp lý của chủ xe.",
    
    143: "🚨 [CÂU ĐIỂM LIỆT] Xe bắt buộc phải lắp thiết bị giám sát hành trình (hộp đen): Toàn bộ xe ô tô kinh doanh vận tải (chở khách từ 8 chỗ trở lên, xe đầu kéo, xe tải chở hàng...) và xe cứu thương để kiểm soát lộ trình và an toàn giao thông.",
    
    144: "Xe máy chuyên dùng, xe gắn máy (kể cả xe máy điện) khi tham gia giao thông trên đường bộ chỉ được chạy với tốc độ tối đa cho phép là 40 km/h.",
    
    145: "Trong khu đông dân cư trên đường đôi (hoặc đường một chiều có từ 2 làn xe cơ giới trở lên): Tốc độ tối đa của ô tô con, xe mô tô, ô tô chở người đến 28 chỗ là 60 km/h.",
    
    146: "Trong khu đông dân cư trên đường hai chiều (hoặc đường một chiều có 1 làn xe cơ giới): Tốc độ tối đa của ô tô con, xe mô tô, ô tô chở người đến 28 chỗ là 50 km/h.",
    
    147: "Trong khu đông dân cư trên đường 2 chiều (hoặc 1 chiều 1 làn xe cơ giới): Ô tô tải, xe khách trên 28 chỗ được chạy tốc độ tối đa là 50 km/h (riêng xe gắn máy luôn chỉ được chạy tối đa 40 km/h).",
    
    148: "🚨 [CÂU ĐIỂM LIỆT] Trong khu đông dân cư trên đường đôi (hoặc 1 chiều có từ 2 làn cơ giới): Ô tô tải, ô tô khách trên 28 chỗ được chạy tốc độ tối đa là 60 km/h.",
    
    149: "Ngoài khu đông dân cư trên đường đôi có dải phân cách giữa: Tốc độ tối đa 90 km/h áp dụng cho xe ô tô chở người đến 28 chỗ (trừ buýt) và ô tô tải có trọng tải đến 3,5 tấn.",
    
    150: "Ngoài khu đông dân cư trên đường đôi có dải phân cách giữa: Tốc độ tối đa 80 km/h áp dụng cho xe ô tô chở người trên 28 chỗ và ô tô tải có trọng tải trên 3,5 tấn.",
    
    151: "🚨 [CÂU ĐIỂM LIỆT] Ngoài khu đông dân cư trên đường đôi có dải phân cách giữa: Tốc độ tối đa 70 km/h áp dụng cho xe buýt, xe đầu kéo kéo sơ mi rơ moóc, xe mô tô và ô tô chuyên dùng.",
    
    152: "Ngoài khu đông dân cư trên đường đôi có dải phân cách giữa: Tốc độ tối đa 60 km/h áp dụng cho các loại xe kéo rơ moóc, kéo xe khác, ô tô trộn vữa, ô tô xi téc.",
    
    153: "🚨 [CÂU ĐIỂM LIỆT] Ngoài khu đông dân cư trên đường hai chiều (không có dải phân cách giữa): Tốc độ tối đa 80 km/h áp dụng cho xe ô tô chở người đến 28 chỗ và ô tô tải trọng tải đến 3,5 tấn.",
    
    154: "Ngoài khu đông dân cư trên đường hai chiều: Tốc độ tối đa 70 km/h áp dụng cho ô tô chở người trên 28 chỗ và ô tô tải có trọng tải trên 3,5 tấn.",
    
    155: "Ngoài khu đông dân cư trên đường hai chiều: Tốc độ tối đa 60 km/h áp dụng cho xe buýt, xe đầu kéo kéo sơ mi rơ moóc, ô tô chuyên dùng và xe mô tô.",
    
    156: "Ngoài khu đông dân cư trên đường hai chiều: Tốc độ tối đa 50 km/h áp dụng cho ô tô kéo rơ moóc, kéo xe khác, ô tô trộn bê tông, ô tô xi téc.",
    
    157: "Xe chở hàng bốn bánh có gắn động cơ tham gia giao thông trong phạm vi và thời gian cho phép được chạy với tốc độ tối đa cho phép là 50 km/h.",
    
    158: "Khoảng cách an toàn tối thiểu: Khi xe chạy với tốc độ từ trên 80 km/h đến 100 km/h trên đường khô ráo, khoảng cách an toàn tối thiểu với xe liền trước là 70 mét.",
    
    159: "Khoảng cách an toàn tối thiểu: Khi xe chạy với tốc độ từ trên 100 km/h đến 120 km/h trên đường khô ráo, khoảng cách an toàn tối thiểu với xe liền trước là 100 mét.",
    
    160: "🚨 [CÂU ĐIỂM LIỆT] Khoảng cách an toàn tối thiểu: Khi xe chạy với tốc độ từ trên 60 km/h đến 80 km/h trên đường khô ráo, khoảng cách an toàn tối thiểu với xe liền trước là 55 mét.",
    
    161: "Khoảng cách an toàn tối thiểu: Khi xe chạy với tốc độ 60 km/h trên đường khô ráo, khoảng cách an toàn tối thiểu với xe liền trước là 35 mét.",
    
    162: "Khi điều khiển xe chạy với tốc độ dưới 60 km/h, người lái xe phải chủ động giữ khoảng cách an toàn phù hợp với mật độ giao thông và diễn biến thực tế trên đường.",
    
    163: "Khi gặp biển báo nguy hiểm và cảnh báo, người lái xe bắt buộc phải giảm tốc độ dưới mức tối đa cho phép, chú ý quan sát để sẵn sàng xử lý các tình huống bất ngờ.",
    
    164: "Xe đưa đón trẻ em mầm non, học sinh được ưu tiên tổ chức phân luồng, điều tiết giao thông và bố trí điểm dừng, đỗ thuận tiện, an toàn tại khu vực cổng trường học và các điểm đón trả.",
    
    165: "Người lái xe phải giảm tốc độ hoặc dừng lại nhường đường: tại vạch cho người đi bộ qua đường; nơi đường sắt giao nhau; đường đèo dốc hiểm trở; khu vực gần trường học, bệnh viện, chợ đông người.",
    
    166: "Tại những đoạn đường không có biển báo hạn chế tốc độ hoặc khoảng cách an toàn, người lái xe vẫn bắt buộc phải chấp hành các quy định chung của luật về giới hạn tốc độ và khoảng cách an toàn tối thiểu.",
    
    167: "Khi gặp xe buýt đang dừng đón trả khách, người điều khiển xe phía sau phải quan sát cẩn thận, giảm tốc độ và chú ý người đi bộ có thể bất ngờ bước ra từ đầu xe buýt.",
    
    168: "Quy định vận tải khách: Bắt buộc đón trả khách đúng nơi quy định; hướng dẫn khách dùng trang thiết bị an toàn (thắt dây an toàn); cấm chở người trên nóc hoặc để khách đu bám bên ngoài.",
    
    169: "Trong hoạt động vận tải đường bộ, nghiêm cấm vận chuyển hàng hóa cấm lưu hành, vận chuyển động vật hoang dã trái phép hoặc chở hóa chất nguy hiểm không tuân thủ quy định an toàn.",
    
    170: "Trong vận tải hành khách, nghiêm cấm các hành vi: Đe dọa, xúc phạm, chèn ép, tranh giành hành khách; sang nhượng/chuyển tải hành khách giữa đường nhằm trốn tránh bị xử phạt quá tải.",
    
    171: "Quy định an toàn lao động: Thời gian lái xe LIÊN TỤC của người lái xe ô tô kinh doanh vận tải KHÔNG ĐƯỢC QUÁ 4 GIỜ để phòng ngừa ngủ gật và mất tập trung.",
    
    172: "Tổng thời gian làm việc của người lái xe ô tô kinh doanh vận tải trong một ngày KHÔNG ĐƯỢC QUÁ 10 GIỜ nhằm bảo đảm sức khỏe và khả năng phản xạ an toàn.",
    
    173: "Trước khi xuất bến, lái xe và nhân viên phục vụ phải kiểm tra kỹ các điều kiện an toàn kỹ thuật của xe, đồng thời hướng dẫn hành khách thắt dây an toàn và cách thoát hiểm khẩn cấp.",
    
    174: "Xe chở học sinh mầm non, tiểu học bắt buộc phải có thiết bị ghi hình và thiết bị cảnh báo/chống bỏ quên trẻ em trên xe; có niên hạn không quá 20 năm; có dây đai an toàn phù hợp lứa tuổi.",
    
    175: "Vận chuyển động vật sống phải có đầy đủ giấy tờ kiểm dịch, xe có kết cấu chuồng/thùng chuyên dùng bảo đảm an toàn và không gây ô nhiễm môi trường trên đường.",
    
    176: "Vận chuyển hàng hóa nguy hiểm (chất độc, chất dễ cháy nổ...) bắt buộc phải có Giấy phép vận chuyển do cơ quan có thẩm quyền cấp và phải bố trí người áp tải chuyên trách khi cần thiết.",
    
    177: "Xe ô tô tay lái nghịch (bên phải) của người nước ngoài vào Việt Nam du lịch phải chấp hành nghiêm luật pháp Việt Nam, chạy đúng lộ trình cấp phép và phải có xe hướng dẫn/hỗ trợ đi cùng đoàn.",
    
    178: "Vận chuyển hành khách, hàng hóa bằng mô tô, xe gắn máy phải bảo đảm an toàn kỹ thuật của phương tiện, mang đủ giấy tờ, xếp hàng không vượt quá chiều rộng/chiều cao quy định.",
    
    179: "Vận chuyển hàng siêu trường, siêu trọng phải chạy đúng tốc độ ghi trong Giấy phép lưu hành, gắn cờ/đèn báo kích thước hàng và phải bố trí xe dẫn đường hỗ trợ khi cần thiết.",
    
    180: "Xe cứu hộ giao thông đường bộ phải có dấu hiệu nhận diện đặc trưng, gắn thiết bị giám sát hành trình, camera hành trình và tuân thủ đúng tải trọng kéo/chở cho phép."
}

