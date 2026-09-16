# scripts/explanations/part1.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 1 đến Câu 60
Chương 1: Quy định chung và quy tắc giao thông đường bộ
"""

PART1_EXPLANATIONS = {
    1: "Theo Luật Trật tự, an toàn giao thông đường bộ, 'Phần đường xe chạy' là phần của đường bộ được sử dụng cho phương tiện giao thông đường bộ đi lại. Phần lề đường chỉ dùng để dừng, đỗ xe hoặc cho người đi bộ khi cần thiết, không phải phần đường xe chạy.",
    
    2: "'Làn đường' là một phần của phần đường xe chạy được chia theo chiều dọc của đường, có đủ chiều rộng cho xe chạy an toàn. Điểm mấu chốt bắt buộc phải có là 'có đủ chiều rộng cho xe chạy an toàn'.",
    
    3: "'Khổ giới hạn của đường bộ' là khoảng trống có kích thước giới hạn về cả CHIỀU RỘNG và CHIỀU CAO của đường bộ để các phương tiện (bao gồm cả hàng hoá xếp trên xe) lưu thông qua an toàn theo quy chuẩn kỹ thuật.",
    
    4: "'Dải phân cách' là bộ phận của đường để phân chia phần đường xe chạy thành hai chiều riêng biệt hoặc để phân chia phần đường dành cho xe cơ giới và xe thô sơ hoặc các loại xe khác nhau trên cùng một chiều đường.",
    
    5: "Theo quy chuẩn báo hiệu đường bộ, 'Vạch kẻ đường' là một dạng báo hiệu để chỉ sự phân chia làn đường, vị trí hoặc hướng đi, vị trí dừng lại của phương tiện tham gia giao thông.",
    
    6: "'Người điều khiển phương tiện tham gia giao thông đường bộ' bao gồm người điều khiển xe cơ giới, người điều khiển xe thô sơ và người điều khiển xe máy chuyên dùng.",
    
    7: "'Người lái xe' được định nghĩa trong luật là người trực tiếp điều khiển xe cơ giới (như xe ô tô, xe mô tô, xe máy...).",
    
    8: "Xe cơ giới gồm: xe ô tô, rơ moóc được kéo bởi ô tô, sơ mi rơ moóc kéo bởi ô tô đầu kéo, xe chở người/hàng bốn bánh có gắn động cơ, xe mô tô, xe gắn máy và các xe tương tự. Chú ý: xe đạp, xe đạp điện, xe lăn và xe máy chuyên dùng không thuộc nhóm xe cơ giới.",
    
    9: "Xe thô sơ bao gồm: xe đạp (kể cả xe đạp máy, xe đạp điện), xe xích lô, xe lăn dùng cho người khuyết tật, xe do súc vật kéo và các loại xe tương tự.",
    
    10: "Phương tiện giao thông đường bộ gồm 2 nhóm chính: Phương tiện giao thông cơ giới đường bộ và Phương tiện giao thông thô sơ đường bộ, xe máy chuyên dùng cùng các loại xe tương tự.",
    
    11: "'Người tham gia giao thông đường bộ' là khái niệm rộng nhất, bao gồm người điều khiển, người sử dụng phương tiện; người dẫn dắt súc vật; người đi bộ trên đường bộ.",
    
    12: "'Người điều khiển phương tiện giao thông' gồm cả người lái xe cơ giới, xe thô sơ, xe máy chuyên dùng và người dẫn dắt súc vật khi tham gia giao thông.",
    
    13: "'Người điều khiển giao thông đường bộ' là Cảnh sát giao thông (CSGT) và người được giao nhiệm vụ hướng dẫn giao thông tại nơi thi công, nơi ùn tắc, bến phà, tại cầu đường bộ đi chung với đường sắt.",
    
    14: "'Dừng xe' là trạng thái đứng yên TẠM THỜI của phương tiện trong một khoảng thời gian cần thiết đủ để cho người lên, xuống xe, xếp dỡ hàng hóa hoặc thực hiện công việc khác (người lái xe không được rời vị trí lái).",
    
    15: "'Đỗ xe' là trạng thái đứng yên KHÔNG GIỚI HẠN THỜI GIAN của phương tiện giao thông đường bộ (người lái xe có thể rời khỏi phương tiện sau khi đã thực hiện các biện pháp an toàn).",
    
    16: "'Đường cao tốc' là cấp kỹ thuật đường bộ đặc biệt: chỉ dành cho một số loại xe cơ giới/chuyên dùng đạt chuẩn tốc độ; có dải phân cách giữa phân chia 2 chiều; hoàn toàn không giao cắt cùng mức; chỉ ra/vào tại các điểm quy định và có trang thiết bị bảo đảm giao thông an toàn liên tục.",
    
    17: "🚨 [CÂU ĐIỂM LIỆT] Theo Luật mới, thiết bị an toàn cho trẻ em được định nghĩa là thiết bị bảo đảm an toàn cho trẻ ở tư thế NGỒI hoặc NẰM trên xe ô tô, thiết kế để hạn chế sự di chuyển của cơ thể trẻ, giảm nguy cơ chấn thương khi va chạm hoặc phanh gấp. Trẻ em tuyệt đối không được ở tư thế đứng trên xe.",
    
    18: "🚨 [CÂU ĐIỂM LIỆT] Theo chức năng phục vụ, đường bộ được phân loại đầy đủ gồm: đường chính, đường nhánh, đường gom, đường bên, đường dành cho giao thông công cộng, đường nội bộ, đường dành riêng cho người đi bộ, xe đạp và các đường khác.",
    
    19: "🚨 [CÂU ĐIỂM LIỆT] Hành vi rải vật sắc nhọn (đinh, chông), đổ dầu nhớt hoặc các chất gây trơn trượt trên đường bộ là hành vi phá hoại đặc biệt nguy hiểm, trực tiếp đe dọa tính mạng người tham gia giao thông nên bị nghiêm cấm triệt để và có thể bị truy cứu trách nhiệm hình sự.",
    
    20: "🚨 [CÂU ĐIỂM LIỆT] Nghiêm cấm đưa phương tiện không có chứng nhận đăng kiểm an toàn kỹ thuật & bảo vệ môi trường, hoặc xe đã hết niên hạn sử dụng tham gia giao thông vì nguy cơ hỏng hóc kỹ thuật (mất phanh, gãy trục...) gây tai nạn thảm khốc.",
    
    21: "🚨 [CÂU ĐIỂM LIỆT] Hoạt động tổ chức đua xe chỉ được phép thực hiện khi có sự chấp thuận và cấp phép chính thức từ cơ quan nhà nước có thẩm quyền trên các cung đường, trường đua được bảo vệ an toàn.",
    
    22: "🚨 [CÂU ĐIỂM LIỆT] Đua xe trái phép là hành vi gây nguy hiểm đặc biệt cho xã hội; tùy theo tính chất và mức độ vi phạm sẽ bị xử phạt vi phạm hành chính nặng hoặc bị truy cứu trách nhiệm hình sự (khởi tố tù giam).",
    
    23: "🚨 [CÂU ĐIỂM LIỆT] Sử dụng ma túy khi điều khiển phương tiện làm tê liệt hệ thần kinh, mất hoàn toàn nhận thức và phản xạ lái xe. Người vi phạm sẽ bị phạt tiền ở khung kịch khung và bị tước quyền sử dụng Giấy phép lái xe.",
    
    24: "🚨 [CÂU ĐIỂM LIỆT] Luật quy định cấm tuyệt đối hành vi điều khiển phương tiện tham gia giao thông đường bộ mà trong máu hoặc hơi thở có nồng độ cồn ('Đã uống rượu bia - Không lái xe'). Không có mức dung sai nồng độ cồn tối thiểu.",
    
    25: "🚨 [CÂU ĐIỂM LIỆT] Người lái ô tô vi phạm nồng độ cồn sẽ bị áp dụng đồng thời cả hai hình thức: Bị phạt tiền nặng và bị tước giấy phép lái xe theo Nghị định xử phạt của Chính phủ.",
    
    26: "🚨 [CÂU ĐIỂM LIỆT] Theo Luật Phòng chống tác hại của rượu, bia, cấm tuyệt đối NGƯỜI ĐIỀU KHIỂN phương tiện giao thông (gồm cả ô tô, mô tô, xe gắn máy, xe đạp) sử dụng rượu bia khi tham gia giao thông. Người ngồi sau xe hoặc hành khách không trực tiếp điều khiển thì không thuộc nhóm bị cấm này.",
    
    27: "🚨 [CÂU ĐIỂM LIỆT] Chủ phương tiện tuyệt đối không được giao xe cho người chưa đủ tuổi, người không có GPLX, hoặc người có GPLX nhưng đã bị trừ hết 12 điểm. Nếu giao xe mà người đó gây tai nạn nghiêm trọng, chủ xe có thể bị xử lý hình sự về tội 'Giao cho người không đủ điều kiện điều khiển phương tiện'.",
    
    28: "🚨 [CÂU ĐIỂM LIỆT] Nghiêm cấm mọi hành vi lạng lách, đánh võng, rú ga liên tục cũng như hành vi xúc phạm, đe dọa, cản trở hoặc chống người thi hành công vụ kiểm soát trật tự an toàn giao thông.",
    
    29: "🚨 [CÂU ĐIỂM LIỆT] Nghiêm cấm cải tạo xe trái phép, cố ý can thiệp tua đồng hồ công-tơ-mét (quãng đường đã chạy) hoặc tẩy xóa, đục sửa, đóng lại số khung, số động cơ trái quy định của pháp luật.",
    
    30: "🚨 [CÂU ĐIỂM LIỆT] Bị nghiêm cấm: tự ý lắp đặt còi/đèn ưu tiên, đèn led pha siêu sáng gây mất an toàn giao thông; cản trở giao thông hoặc ném gạch đá, vật lạ vào phương tiện đang lưu thông trên đường.",
    
    31: "🚨 [CÂU ĐIỂM LIỆT] Biển số xe do cơ quan công an có thẩm quyền cấp và quản lý. Mọi hành vi tự ý sản xuất, mua bán, sử dụng biển số giả hoặc sửa đổi chữ số đều là hành vi vi phạm pháp luật và bị nghiêm cấm.",
    
    32: "🚨 [CÂU ĐIỂM LIỆT] Khi điều khiển phương tiện, hành vi lạng lách, đánh võng, rú ga bóp còi liên tục gây hoảng loạn cho người đi đường, nguy cơ cao dẫn đến tai nạn nên bị pháp luật nghiêm cấm.",
    
    33: "Hệ thống báo hiệu đường bộ Việt Nam gồm 5 nhóm chính: 1. Biển báo cấm; 2. Biển báo nguy hiểm và cảnh báo; 3. Biển hiệu lệnh; 4. Biển chỉ dẫn; 5. Biển phụ, biển viết bằng chữ.",
    
    34: "Khi đến nơi có vạch kẻ đường cho người đi bộ qua đường hoặc khi thấy người đi bộ, người khuyết tật dùng xe lăn đang qua đường, người lái xe phải quan sát, giảm tốc độ hoặc dừng lại để nhường đường an toàn.",
    
    35: "🚨 [CÂU ĐIỂM LIỆT] Người lái xe mô tô, ô tô bắt buộc phải quan sát, giảm tốc độ hoặc dừng lại nhường đường khi: gặp người đi bộ qua đường; gặp xe buýt đang dừng đón trả khách; hoặc tại nơi giao nhau không có báo hiệu đi theo vòng xuyến.",
    
    36: "Hiệu lệnh CSGT giang hai tay hoặc một tay sang ngang: Người tham gia giao thông ở phía trước và phía sau người chỉ huy phải DỪNG LẠI; người tham gia giao thông ở phía bên phải và bên trái được ĐI TẤT CẢ CÁC HƯỚNG.",
    
    37: "Hiệu lệnh CSGT giơ tay thẳng đứng: Người tham gia giao thông ở TẤT CẢ CÁC HƯỚNG đều phải dừng lại (trừ các xe đã ở trong khu vực giao nhau thì được tiếp tục đi).",
    
    38: "Thứ tự ưu tiên hiệu lực của báo hiệu giao thông: 1. Hiệu lệnh của người điều khiển giao thông (CSGT) là cao nhất; 2. Tín hiệu đèn; 3. Biển báo hiệu; 4. Vạch kẻ đường. Do đó phải chấp hành hiệu lệnh của CSGT trước.",
    
    39: "Khi tại một khu vực đồng thời có biển báo cố định và biển báo tạm thời (như khu vực công trường, sửa chữa đường) mà ý nghĩa khác nhau, người tham gia giao thông phải chấp hành theo hiệu lệnh của BIỂN BÁO HIỆU TẠM THỜI.",
    
    40: "Khi gặp tín hiệu đèn vàng: Người lái xe phải dừng lại trước vạch dừng. Trường hợp đã đi quá vạch dừng hoặc đã quá gần vạch dừng mà dừng lại sẽ gây nguy hiểm thì được phép tiếp tục đi tiếp.",
    
    41: "Người lái xe khi tham gia giao thông trên đường bộ phải chấp hành nghiêm túc quy định về tốc độ, luôn làm chủ tốc độ và TUYỆT ĐỐI KHÔNG ĐƯỢC VƯỢT QUÁ tốc độ tối đa cho phép trên tuyến đường đó.",
    
    42: "Luật Trật tự, ATGT đường bộ quy định: Khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 mét trên xe ô tô con, KHÔNG ĐƯỢC cho trẻ ngồi cùng hàng ghế với người lái xe (trừ loại xe chỉ có một hàng ghế); đồng thời phải sử dụng thiết bị an toàn phù hợp.",
    
    43: "Quy tắc cơ bản khi tham gia giao thông: Phương tiện di chuyển với tốc độ THẤP HƠN phải đi về phía bên PHẢI theo chiều đi của mình để không cản trở các xe di chuyển nhanh hơn.",
    
    44: "Trên đường một chiều có nhiều làn phân cách bằng vạch kẻ, làn đường bên trái ngoài cùng thường dành cho xe cơ giới di chuyển nhanh; các phương tiện thô sơ và xe di chuyển chậm phải đi trên các làn phía bên phải.",
    
    45: "🚨 [CÂU ĐIỂM LIỆT] Khi xe sau xin vượt, nếu đủ điều kiện an toàn, người lái xe phía trước phải giảm tốc độ, bật đèn xi-nhan rẽ phải và đi sát về lề bên phải để nhường đường. Tuyệt đối không được tăng tốc hay gây cản trở xe sau vượt.",
    
    46: "Khái niệm 'Vượt xe': Là tình huống giao thông trên đường mà mỗi chiều đường chỉ có một làn xe cơ giới, xe phía sau muốn đi lên trước phải mượn phần đường hoặc làn đường bên trái của xe trước để vượt qua.",
    
    47: "🚨 [CÂU ĐIỂM LIỆT] Cầu hẹp một làn xe và khúc cua khuất tầm nhìn là những vị trí tiềm ẩn nguy cơ đối đầu trực diện với xe ngược chiều vô cùng nguy hiểm. Pháp luật NGHIÊM CẤM vượt xe trong mọi trường hợp tại các vị trí này.",
    
    48: "Khi muốn vượt xe, người lái xe mô tô phải có tín hiệu báo hiệu nhấp nháy bằng đèn chiếu sáng phía trước hoặc bằng còi. Tuyệt đối không rú ga, nẹt pô hay bấm còi dồn dập gây hoảng loạn.",
    
    49: "Trong khu đông dân cư và khu vực bệnh viện, chỉ được phép sử dụng còi trong khung giờ ban ngày từ 05 giờ sáng đến 22 giờ đêm nhằm bảo đảm sự yên tĩnh và nghỉ ngơi của người dân.",
    
    50: "Tín hiệu còi chỉ được dùng để báo hiệu khi có nguy cơ mất an toàn hoặc báo hiệu xin vượt xe. Từ 22h đêm đến 5h sáng hôm sau trong đô thị, phải dùng đèn pha/cos nhấp nháy thay cho còi.",
    
    51: "Khi lưu thông trong khu đông dân cư có đèn đường vào ban đêm, người lái xe CHỈ ĐƯỢC BẬT ĐÈN CHIẾU GẦN (đèn cốt). Cấm bật đèn chiếu xa (đèn pha) vì sẽ làm lóa mắt các phương tiện đi ngược chiều và phía trước.",
    
    52: "🚨 [CÂU ĐIỂM LIỆT] Dùng tay cầm và sử dụng điện thoại, thiết bị điện tử khi đang lái xe làm phân tâm thị giác, giảm 80% khả năng phản xạ xử lý tình huống khẩn cấp, là nguyên nhân hàng đầu gây tai nạn nên bị nghiêm cấm triệt để.",
    
    53: "Không được vượt xe khác khi: đi trên cầu hẹp một làn xe, nơi đường giao nhau, đường bộ giao cắt đường sắt, khi tầm nhìn bị che khuất, hoặc khi có xe ưu tiên đang phát tín hiệu làm nhiệm vụ.",
    
    54: "🚨 [CÂU ĐIỂM LIỆT] Nghiêm cấm quay đầu xe tại các vị trí: phần đường người đi bộ, trên cầu, đầu cầu, gầm cầu vượt, ngầm, đường sắt giao nhau, đường dốc, đường hẹp, đường cong khuất tầm nhìn, trong hầm và trên đường cao tốc.",
    
    55: "🚨 [CÂU ĐIỂM LIỆT] Người lái xe không được phép quay đầu xe ở phần đường người đi bộ qua đường, trên cầu, đầu cầu, trên đường cao tốc, nơi giao cắt với đường sắt, đoạn đường cong hay đường dốc vì nguy cơ xung đột luồng xe cực lớn.",
    
    56: "Trước khi chuyển hướng, người lái xe phải thực hiện đầy đủ: 1. Quan sát an toàn gương chiếu hậu; 2. Giảm tốc độ và bật xi-nhan báo rẽ; 3. Chuyển dần sang làn đường thích hợp khi bảo đảm không gây trở ngại.",
    
    57: "Quy tắc an toàn khi chuyển làn: Người lái xe phải bật đèn tín hiệu báo rẽ (xi-nhan) TRƯỚC KHI thay đổi làn đường một khoảng cách an toàn để các xe phía sau kịp thời nhận biết và chủ động nhường đường.",
    
    58: "🚨 [CÂU ĐIỂM LIỆT] Cấm lùi xe ở: đường một chiều, khu vực cấm dừng đỗ, phần đường người đi bộ, nơi giao nhau, nơi giao cắt đường sắt, nơi khuất tầm nhìn, trong hầm đường bộ và đặc biệt trên đường cao tốc.",
    
    59: "🚨 [CÂU ĐIỂM LIỆT] Cấm dừng xe, đỗ xe trên miệng cống thoát nước, miệng hầm đường dây điện thoại, điện cao thế, trụ nước cứu hỏa và trong phạm vi hành lang an toàn đường sắt để phục vụ thoát nạn và cứu hỏa.",
    
    60: "🚨 [CÂU ĐIỂM LIỆT] Khi dừng xe, đỗ xe trên đường phố sát lề đường/vỉa hè bên phải, khoảng cách từ bánh xe gần nhất đến mép lề đường, hè phố không được vượt quá 0,25 mét để bảo đảm không chiếm dụng lòng đường và cản trở lưu thông."
}

