# scripts/explanations/part2.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 61 đến Câu 120
Chương 1: Quy định chung và quy tắc giao thông đường bộ
"""

PART2_EXPLANATIONS = {
    61: "Khi dừng, đỗ xe trên đường phố hẹp, người lái xe phải đỗ cách xe ô tô đang đỗ ngược chiều tối thiểu 20 mét để bảo đảm có đủ khoảng trống cho các phương tiện khác lưu thông qua lại an toàn, tránh gây ùn tắc giao thông.",
    
    62: "🚨 [CÂU ĐIỂM LIỆT] Nghiêm cấm dừng đỗ song song với xe khác đang đỗ, đỗ ở đoạn đường cong, gần đầu dốc khuất tầm nhìn hoặc bên trái đường một chiều vì sẽ bịt kín làn đường và tiềm ẩn nguy cơ tai nạn đặc biệt nghiêm trọng.",
    
    63: "🚨 [CÂU ĐIỂM LIỆT] Xe mô tô, xe gắn máy KHÔNG ĐƯỢC PHÉP kéo hoặc đẩy các phương tiện khác, vật khác khi tham gia giao thông. Hành vi này làm mất khả năng giữ thăng bằng và mất lái hoàn toàn.",
    
    64: "🚨 [CÂU ĐIỂM LIỆT] Cấm người điều khiển mô tô buông cả hai tay; cấm đứng, nằm trên xe lái xe; cấm dùng chân chống hoặc vật khác quẹt xuống đường tạo tia lửa điện khi xe đang chạy.",
    
    65: "🚨 [CÂU ĐIỂM LIỆT] Người điều khiển mô tô hai bánh, ba bánh, xe gắn máy không được buông cả 2 tay, không được kéo đẩy xe khác, không được quệt chân chống xuống đường khi đang chạy.",
    
    66: "Người được chở trên xe mô tô, xe gắn máy không được mang vác vật cồng kềnh, không được bám, kéo hoặc đẩy các phương tiện khác vì dễ gây mất thăng bằng ngã đổ xe.",
    
    67: "Người được chở trên xe mô tô, xe gắn máy tuyệt đối KHÔNG ĐƯỢC PHÉP bám, kéo hoặc đẩy các phương tiện khác dưới bất kỳ hình thức nào.",
    
    68: "Người lái xe và người ngồi trên xe mô tô hai bánh, ba bánh, xe gắn máy bắt buộc phải đội mũ bảo hiểm đạt chuẩn chất lượng quốc gia và cài quai đúng quy cách để bảo vệ phần đầu khi có va chạm.",
    
    69: "Xe mô tô 2 bánh, xe gắn máy chỉ được chở tối đa 2 người trong 4 trường hợp đặc biệt: 1. Chở người bệnh đi cấp cứu; 2. Áp giải người vi phạm pháp luật; 3. Trẻ em dưới 12 tuổi; 4. Người già yếu hoặc người khuyết tật.",
    
    70: "🚨 [CÂU ĐIỂM LIỆT] Người lái xe mô tô bị nghiêm cấm: đi xe dàn hàng ngang; buông 2 tay; kéo đẩy xe khác; chở người đứng trên xe, giá đèo hàng hoặc ngồi trên tay lái; nằm trên xe lái xe; quẹt chân chống xuống đường.",
    
    71: "🚨 [CÂU ĐIỂM LIỆT] Nghiêm cấm lái xe mô tô dàn hàng ngang, đi vào vỉa hè dành cho người đi bộ, sử dụng ô (dù), sử dụng thiết bị âm thanh như tai nghe nhạc (chỉ trừ thiết bị trợ thính y tế).",
    
    72: "🚨 [CÂU ĐIỂM LIỆT] Người điều khiển xe mô tô không được thực hiện hành vi: đi xe dàn hàng ngang và đi xe vào phần đường dành cho người đi bộ.",
    
    73: "Người ngồi trên xe mô tô, xe gắn máy khi trời mưa KHÔNG ĐƯỢC PHÉP sử dụng ô (dù) vì sức gió cản của ô sẽ làm lật đổ xe, gây nguy hiểm cho bản thân và người xung quanh.",
    
    74: "🚨 [CÂU ĐIỂM LIỆT] Người ngồi trên mô tô KHÔNG ĐƯỢC PHÉP kéo theo người đang đi xe đạp vì rất dễ làm xe đạp mất lái, ngã cuốn vào gầm xe khác.",
    
    75: "🚨 [CÂU ĐIỂM LIỆT] Pháp luật quy định xử phạt vi phạm hành chính đối với CẢ NGƯỜI ĐIỀU KHIỂN VÀ NGƯỜI ĐƯỢC CHỞ trên xe mô tô, xe gắn máy nếu người được chở không đội mũ bảo hiểm hoặc cài quai không đúng quy cách.",
    
    76: "Người lái mô tô an toàn phải: Đội mũ bảo hiểm đạt chuẩn, cài quai đúng quy cách; tuyệt đối không dùng ô, điện thoại di động hay tai nghe nhạc khi đang lái xe.",
    
    77: "Quy tắc an toàn khi qua phà: Xe cơ giới, xe máy chuyên dùng phải xuống phà trước để ổn định trọng tâm phà; xe thô sơ và người đi bộ xuống sau cùng.",
    
    78: "Trên đường có nhiều làn cùng chiều: Xe phải đi trong MỘT LÀN ĐƯỜNG và chỉ được chuyển làn ở nơi cho phép; mỗi lần chuyển làn CHỈ ĐƯỢC CHUYỂN SANG MỘT LÀN LIỀN KỀ; phải bật tín hiệu báo trước và quan sát an toàn.",
    
    79: "Trên đường một chiều có phân làn: Xe thô sơ phải đi trên làn bên PHẢI TRONG CÙNG; xe cơ giới, xe máy chuyên dùng đi trên các làn đường bên TRÁI.",
    
    80: "Từ 22 giờ hôm trước đến 05 giờ sáng hôm sau trong đô thị và khu đông dân cư, người lái xe muốn xin vượt CHỈ ĐƯỢC BÁO HIỆU BẰNG ĐÈN (nháy pha/cos), cấm bấm còi làm ảnh hưởng giấc ngủ của người dân.",
    
    81: "Khi có xe sau xin vượt, nếu đủ an toàn, người lái xe phía trước phải giảm tốc độ, bật xi-nhan rẽ phải báo hiệu đồng ý và đi sát lề phải cho đến khi xe sau vượt qua hoàn toàn.",
    
    82: "Khi xe sau xin vượt nhưng thấy phía trước KHÔNG ĐỦ ĐIỀU KIỆN AN TOÀN (có chướng ngại vật, xe ngược chiều...), người lái xe phải BẬT TÍN HIỆU RẼ TRÁI để báo cho xe sau biết là CHƯA ĐƯỢC VƯỢT.",
    
    83: "Khi chuyển hướng (rẽ), người lái xe phải quan sát kỹ, nhường đường cho người đi bộ, xe thô sơ và các xe đi ngược chiều, chỉ chuyển hướng khi hoàn toàn không gây trở ngại cho người khác.",
    
    84: "🚨 [CÂU ĐIỂM LIỆT] Quy trình chuyển hướng: Phải quan sát an toàn, giảm tốc độ, bật xi-nhan báo rẽ liên tục, chuyển dần sang làn đường gần nhất với hướng rẽ, bảo đảm an toàn tuyệt đối mới được thực hiện chuyển hướng.",
    
    85: "Khi lùi xe, người lái xe phải quan sát kỹ hai bên gương và phía sau xe, bật đèn lùi/tín hiệu cảnh báo lùi và chỉ lùi khi chắc chắn không có chướng ngại vật hoặc phương tiện phía sau.",
    
    86: "Ở nơi có tầm nhìn bị che khuất (như góc cua hẹp, ngã ba khuất...), người lái xe KHÔNG ĐƯỢC LÙI XE vì không thể quan sát được dòng phương tiện tiếp cận phía sau.",
    
    87: "🚨 [CÂU ĐIỂM LIỆT] Khi tránh xe đi ngược chiều trên đường hai chiều hẹp, người lái xe phải GIẢM TỐC ĐỘ và cho xe đi sát về bên PHẢI theo chiều đi của mình. Tuyệt đối không được lấn làn hay tăng tốc.",
    
    88: "Quy tắc nhường đường khi tránh xe ngược chiều: 1. Xe gần chỗ tránh hơn phải vào vị trí tránh nhường đường; 2. Xe xuống dốc phải nhường đường cho xe đang lên dốc; 3. Xe có chướng ngại vật phía trước phải nhường cho xe không có vật cản.",
    
    89: "Khi hai xe gặp nhau trên dốc hẹp, xe ĐANG XUỐNG DỐC phải dừng lại nhường đường cho xe ĐANG LÊN DỐC (vì xe lên dốc cần đà và khó khởi hành lại hơn).",
    
    90: "Khi lái xe trên đường cong có tầm nhìn bị hạn chế (khuất cua), người lái xe bắt buộc phải QUAN SÁT VÀ GIẢM TỐC ĐỘ, đi đúng làn đường của mình. Nghiêm cấm lấn làn hoặc vượt xe tại góc cua.",
    
    91: "🚨 [CÂU ĐIỂM LIỆT] Tại nơi giao nhau, xe đi từ đường nhánh, đường không ưu tiên bắt buộc phải NHƯỜNG ĐƯỜNG cho xe đi trên đường chính, đường ưu tiên TỪ BẤT KỲ HƯỚNG NÀO TỚI.",
    
    92: "🚨 [CÂU ĐIỂM LIỆT] Mẹo nhớ quy tắc vòng xuyến: 'CÓ vòng xuyến nhường BÊN TRÁI; KHÔNG vòng xuyến nhường BÊN PHẢI'. Tại nơi giao nhau có báo hiệu vòng xuyến, phải nhường đường cho xe đến từ bên trái.",
    
    93: "🚨 [CÂU ĐIỂM LIỆT] Mẹo nhớ quy tắc giao nhau: 'KHÔNG vòng xuyến nhường BÊN PHẢI'. Tại ngã tư không có biển báo vòng xuyến, người lái xe bắt buộc phải nhường đường cho xe đi đến từ bên phải.",
    
    94: "🚨 [CÂU ĐIỂM LIỆT] Người lái xe phải giảm tốc độ, đi sát lề phải hoặc dừng lại nhường đường cho các xe ưu tiên đang phát tín hiệu: xe chữa cháy, quân sự, công an, kiểm sát làm nhiệm vụ, đoàn xe có CSGT dẫn đường, xe cứu thương, xe hộ đê, cứu hộ khẩn cấp và đoàn xe tang.",
    
    95: "Xe ưu tiên khi đi làm nhiệm vụ khẩn cấp (có tín hiệu còi, đèn ưu tiên): không bị hạn chế tốc độ, được phép vượt đèn đỏ, được đi vào đường ngược chiều và được đi ngược chiều trên làn khẩn cấp của cao tốc.",
    
    96: "🚨 [CÂU ĐIỂM LIỆT] Khi nghe thấy tín hiệu còi, đèn ưu tiên, mọi phương tiện tham gia giao thông phải lập tức GIẢM TỐC ĐỘ, đi sát lề đường bên PHẢI hoặc dừng lại để nhường đường, tuyệt đối không cản trở xe ưu tiên.",
    
    97: "Nếu xe Cảnh sát giao thông chạy phía trước KHÔNG PHÁT TÍN HIỆU ƯU TIÊN (không bật còi, đèn nhấp nháy làm nhiệm vụ), người lái xe ĐƯỢC PHÉP VƯỢT khi bảo đảm an toàn và tuân thủ tốc độ quy định.",
    
    98: "Khi xe cứu thương đang phát tín hiệu còi, đèn ưu tiên làm nhiệm vụ cấp cứu, người lái xe TUYỆT ĐỐI KHÔNG ĐƯỢC VƯỢT trong bất kỳ hoàn cảnh nào.",
    
    99: "Tại đường ngang không có rào chắn, chuông đèn: Người lái xe phải dừng lại bên phải đường trước vạch dừng, quan sát kỹ hai phía đường ray, khi chắc chắn không có tàu hỏa tới mới được lái xe qua.",
    
    100: "Tại nơi giao nhau với đường sắt, khi có chuông kêu, đèn đỏ nhấp nháy hoặc cần chắn đang hạ xuống, người tham gia giao thông phải DỪNG LẠI VỀ BÊN PHẢI đường của mình, phía trước vạch dừng xe.",
    
    101: "🚨 [CÂU ĐIỂM LIỆT] Khi xe bị chết máy, tai nạn nằm trên đường ray mà không thể di chuyển ra ngoài phạm vi an toàn, người lái xe và mọi người có mặt phải NGAY LẬP TỨC báo hiệu để dừng tàu (chạy về hai phía tối thiểu 500m phát tín hiệu) và thực hiện các biện pháp an toàn khẩn cấp.",
    
    102: "Phải dừng lại bên phải trước vạch dừng khi: có hiệu lệnh nhân viên gác chắn, đèn đỏ nhấp nháy/chuông kêu, hoặc rào chắn đường sắt đang dịch chuyển/đã đóng kín.",
    
    103: "Quy tắc lái xe trong hầm đường bộ: Bắt buộc bật đèn chiếu gần (cốt); xe thô sơ phải có đèn hoặc vật phát sáng; CẤM dừng, đỗ, quay đầu hoặc lùi xe trong hầm. Nếu gặp sự cố phải đưa vào vị trí dừng khẩn cấp và đặt cảnh báo an toàn.",
    
    104: "Khi kéo xe ô tô bị hỏng mà hệ thống phanh (hãm) của xe được kéo không còn hiệu lực, bắt buộc phải sử dụng THANH NỐI CỨNG để xe trước có thể hãm hộ xe sau, cấm dùng dây cáp mềm vì xe sau sẽ đâm vào xe trước khi phanh.",
    
    105: "Xe kéo rơ moóc, ô tô đầu kéo phải kéo rơ moóc phù hợp thiết kế và tải trọng cho phép; chốt kết nối phải chắc chắn, có xích an toàn theo quy định.",
    
    106: "Quy tắc kéo xe: Xe được kéo phải có người ngồi lái và hệ thống lái hoạt động bình thường; nếu mất phanh phải nối bằng thanh nối cứng; phía trước xe kéo và sau xe được kéo phải gắn biển báo hiệu và bật đèn vàng cảnh báo.",
    
    107: "🚨 [CÂU ĐIỂM LIỆT] Người lái xe phải quan sát, giảm tốc độ hoặc dừng lại khi: gặp biển báo nguy hiểm/chướng ngại vật, chuyển hướng, cầu cống hẹp, ngầm, đường dốc, có vật nuôi trên đường, hoặc tại trạm xe buýt đang có hành khách lên xuống.",
    
    108: "Trên đường có một làn xe cơ giới mỗi chiều, không được vượt xe khi: có chướng ngại vật phía trước, hoặc xe chạy phía trước đã có tín hiệu chuẩn bị vượt xe khác.",
    
    109: "Được phép vượt bên phải trong 3 trường hợp: 1. Khi xe phía trước có tín hiệu rẽ trái hoặc đang rẽ trái; 2. Khi xe điện đang chạy giữa đường; 3. Khi xe chuyên dùng đang thi công trên đường không thể vượt bên trái.",
    
    110: "Khi có xe sau xin vượt, nếu đủ điều kiện an toàn, người lái xe phải giảm tốc độ, bật đèn xi-nhan rẽ phải báo hiệu đồng ý và đi sát mép đường bên phải cho đến khi xe sau vượt qua.",
    
    111: "Các phương tiện KHÔNG ĐƯỢC đi vào đường cao tốc: Người đi bộ, xe thô sơ, xe mô tô, xe gắn máy, xe 4 bánh chở người/hàng có gắn động cơ, và xe máy chuyên dùng có tốc độ thiết kế NHỎ HƠN tốc độ tối thiểu của đường cao tốc.",
    
    112: "Theo Luật Trật tự, ATGT đường bộ mới: Xe ưu tiên đi làm nhiệm vụ khẩn cấp nếu đi ngược chiều trên đường cao tốc thì CHỈ ĐƯỢC ĐI NGƯỢC CHIỀU TRÊN LÀN DỪNG XE KHẨN CẤP để bảo đảm an toàn cho các làn xe đang chạy tốc độ cao.",
    
    113: "Trên đường cao tốc, nghiêm cấm người lái xe: Dừng đỗ xe trên làn đường xe chạy (trừ xe hỏng bất khả kháng), lùi xe, hoặc quay đầu xe.",
    
    114: "Khi gặp sự cố trên cao tốc: Phải bật đèn khẩn cấp, cố gắng đưa xe vào làn dừng khẩn cấp; nếu xe không lăn bánh được, phải bật đèn cảnh báo nguy hiểm và ĐẶT BIỂN/ĐÈN CẢNH BÁO PHÍA SAU XE TỐI THIỂU 150 MÉT, đồng thời gọi điện cứu hộ.",
    
    115: "🚨 [CÂU ĐIỂM LIỆT] Khi lái xe trên đường cao tốc mà lỡ đi quá lối rẽ, tuyệt đối KHÔNG ĐƯỢC lùi xe hay quay đầu chạy ngược chiều (nguy cơ va chạm liên hoàn thảm khốc), mà bắt buộc phải TIẾP TỤC ĐI THẲNG đến nút giao/lối ra tiếp theo.",
    
    116: "Khi xảy ra ùn tắc trên đường cao tốc, người lái xe TUYỆT ĐỐI KHÔNG ĐƯỢC chạy vào làn dừng khẩn cấp để vượt lên, vì làn này dành riêng cho các phương tiện cứu nạn, cứu thương, công an tiếp cận hiện trường.",
    
    117: "Quy tắc nhập làn cao tốc: Bật xi-nhan xin vào, quan sát nhường đường cho xe đang chạy trên cao tốc; nếu có làn tăng tốc thì phải tăng tốc độ tương đương dòng xe trước khi chuyển làn an toàn.",
    
    118: "Theo Luật mới: Người đủ 18 tuổi trở lên được cấp GPLX hạng C1 (lái xe ô tô tải có khối lượng từ trên 3.500 kg đến 7.500 kg; kéo rơ moóc đến 750 kg).",
    
    119: "🚨 [CÂU ĐIỂM LIỆT] Độ tuổi cấp GPLX: Người đủ 18 tuổi trở lên được cấp GPLX hạng A1 (mô tô đến 125 cm3) và hạng B (ô tô chở người đến 8 chỗ, ô tô tải đến 3.500 kg). Người từ 16 đến dưới 18 tuổi chỉ được lái xe gắn máy dưới 50 cm3.",
    
    120: "Độ tuổi lái xe khách lớn: Người đủ 27 tuổi trở lên mới được cấp GPLX hạng D (lái xe chở người trên 29 chỗ, xe khách giường nằm)."
}

