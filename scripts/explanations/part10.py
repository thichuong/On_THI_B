# scripts/explanations/part10.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 486 đến Câu 540
Chương 6: Giải thế sa hình và kỹ năng xử lý tình huống giao thông (Phần 1)
"""

PART10_EXPLANATIONS = {
    486: "Xét theo đèn tín hiệu và mũi tên chỉ hướng làn đường:\n"
         "- Xe khách ở làn rẽ trái có đèn đỏ cấm đi, nhưng mũi tên lại chỉ đi thẳng -> Sai phạm (vượt đèn đỏ và sai làn).\n"
         "- Xe tải ở làn đi thẳng có đèn đỏ, nhưng mũi tên lại rẽ trái -> Sai phạm (vượt đèn đỏ và sai làn).\n"
         "- Xe con ở làn ngoài cùng bên phải có đèn xanh rẽ phải, xe rẽ phải đúng hướng -> Đúng quy tắc.\n"
         "- Phía đối diện: Xe mô tô ở làn rẽ trái gặp đèn đỏ nhưng mũi tên rẽ trái vượt qua -> Sai phạm.\n"
         "Do đó chỉ có duy nhất XE CON chấp hành đúng quy tắc giao thông.",

    487: "Phân tích theo biển báo và hướng đi:\n"
         "1. Xe tải và xe mô tô nằm trên trục đường có cắm biển W.207 'Giao nhau với đường không ưu tiên' (đang ở trên đường ưu tiên). Giữa hai xe, xe tải đi thẳng được đi trước (thứ 1), xe mô tô rẽ trái đi sau (thứ 2).\n"
         "2. Xe khách và xe con nằm trên đường nhánh có cắm biển W.208 'Giao nhau với đường ưu tiên' (đường không ưu tiên). Giữa hai xe, xe khách đi thẳng đi trước (thứ 3), xe con rẽ trái đi cuối cùng (thứ 4).\n"
         "Thứ tự đúng: Xe tải -> Xe mô tô -> Xe khách -> Xe con.",

    488: "Áp dụng thứ tự ưu tiên sa hình:\n"
         "1. Xe ưu tiên: Xe công an đi làm nhiệm vụ khẩn cấp được quyền đi đầu tiên (bước 'Nhì ưu').\n"
         "2. Biển báo: Xe con nằm trên trục đường có cắm biển W.207 'Giao nhau với đường không ưu tiên' (đường ưu tiên) và đi thẳng nên được đi thứ 2.\n"
         "3. Xe tải và xe khách đều gặp biển W.208 'Giao nhau với đường ưu tiên' (đường nhánh). Xe tải đi thẳng đi thứ 3, xe khách rẽ trái đi cuối cùng (thứ 4).\n"
         "Thứ tự đúng: Xe công an -> Xe con -> Xe tải -> Xe khách.",

    489: "Áp dụng quy tắc sa hình:\n"
         "1. Xe ưu tiên: Xe công an đi làm nhiệm vụ khẩn cấp được quyền đi trước tiên.\n"
         "2. Hướng đường ưu tiên: Trước mặt xe công an có biển hình thoi I.401 'Bắt đầu đường ưu tiên' kèm biển phụ S.506b thể hiện hướng đường ưu tiên rẽ trái sang phía xe tải. Do đó xe tải nằm trên đường ưu tiên nên được đi thứ 2.\n"
         "3. Xe khách và xe con ở đường không ưu tiên (gặp biển tam giác ngược W.208): Xe khách đi thẳng đi thứ 3, xe con rẽ trái đi sau cùng.\n"
         "Thứ tự đúng: Xe công an -> Xe tải -> Xe khách -> Xe con.",

    490: "Ngã tư đồng cấp (không có biển báo, không có xe ưu tiên):\n"
         "Áp dụng quy tắc 'Bên phải không vướng':\n"
         "- Hướng bên phải của xe mô tô hoàn toàn trống (không có xe) nên xe mô tô được quyền đi đầu tiên.\n"
         "- Sau khi mô tô đã đi qua, hướng bên phải của xe con trở nên trống nên xe con đi thứ 2.\n"
         "- Cuối cùng bên phải xe tải trống nên xe tải rẽ trái đi sau cùng.\n"
         "Thứ tự đúng: Xe mô tô -> Xe con -> Xe tải.",

    491: "Quy tắc nhường đường tại nơi giao nhau chạy theo vòng xuyến:\n"
         "- Tại ngã tư có cắm biển hiệu lệnh R.303 'Nơi giao nhau chạy theo vòng xuyến'.\n"
         "- Luật Giao thông đường bộ quy định: Khi có biển báo hiệu đi theo vòng xuyến, người lái xe phải nhường đường cho phương tiện đi từ bên trái tới.\n"
         "- Xe tải đã vào bên trong vòng xuyến (đang lưu thông từ bên trái của xe con). Xe con chuẩn bị nhập vào vòng xuyến bắt buộc PHẢI NHƯỜNG ĐƯỜNG cho xe tải.",

    492: "Xét biển báo hiệu đường bộ:\n"
         "- Phía trước xe mô tô có cắm biển hiệu lệnh R.122 'STOP' (Dừng lại). Khi gặp biển STOP, tất cả các phương tiện đều bắt buộc phải dừng lại và chỉ được tiếp tục đi khi thấy an toàn, nhường đường cho các xe trên đường cắt ngang.\n"
         "- Xe con không gặp biển cấm/dừng lại nên XE CON ĐƯỢC QUYỀN ĐI TRƯỚC.",

    493: "Áp dụng quy tắc vàng sa hình 'Nhất chớm - Nhì ưu':\n"
         "1. 'Nhất chớm': Xe con (A) đã vượt qua vạch dừng của người đi bộ, chớm vào trong tâm giao lộ trước khi xe cứu thương tới. Theo luật, xe đã vào trong giao lộ được quyền thoát khỏi giao lộ trước tiên.\n"
         "2. 'Nhì ưu': Tiếp theo là xe cứu thương (xe ưu tiên theo luật định) đi thứ 2.\n"
         "3. Cuối cùng là xe con (B) đi sau cùng.\n"
         "Thứ tự đúng: Xe con (A) -> Xe cứu thương -> Xe con (B).",

    494: "Thứ tự các loại xe ưu tiên theo Luật Giao thông đường bộ:\n"
         "Quy tắc ghi nhớ: 'HỎA - SỰ - CÔNG - THƯƠNG' (Xe chữa cháy > Xe quân sự > Xe công an > Xe cứu thương).\n"
         "- Xe chữa cháy đi làm nhiệm vụ có quyền ưu tiên cao hơn xe cứu thương đang làm nhiệm vụ.\n"
         "- Do đó xe chữa cháy đi đầu tiên, tiếp theo là xe cứu thương, xe con đi cuối cùng.\n"
         "Thứ tự đúng: Xe chữa cháy -> Xe cứu thương -> Xe con.",

    495: "Quyền ưu tiên của các phương tiện tham gia giao thông:\n"
         "Xe cứu thương đang phát tín hiệu đi làm nhiệm vụ cấp cứu là xe ưu tiên theo quy định của Luật Giao thông đường bộ. Các phương tiện giao thông thông thường (xe mô tô) phải chủ động giảm tốc độ, nhường đường cho xe ưu tiên đi trước.",

    496: "Phân tích quyền ưu tiên theo biển báo và hướng đi tại nơi giao nhau:\n"
         "1. Xét quyền ưu tiên theo biển báo:\n"
         "- Trục đường của xe con có cắm biển W.207 'Giao nhau với đường không ưu tiên' (biển tam giác đỉnh hướng lên trên), biểu thị xe con đang đi trên ĐƯỜNG ƯU TIÊN -> Xe con được quyền đi trước.\n"
         "- Trục đường của xe tải và xe khách có cắm biển W.208 'Giao nhau với đường ưu tiên' (biển tam giác ngược đỉnh chúc xuống), biểu thị cả hai xe đều đang ở trên ĐƯỜNG KHÔNG ƯU TIÊN.\n"
         "2. Xét hướng di chuyển và xung đột dòng xe:\n"
         "- Xe tải rẽ phải ôm cua vào làn bên phải, hoàn toàn không giao cắt hay vướng hướng đi của xe con, do đó trên thực tế xe con và xe tải có thể di chuyển cùng lúc.\n"
         "- Xe khách rẽ trái cắt ngang giao lộ, vừa phải nhường đường cho xe trên đường ưu tiên (xe con), vừa phải nhường cho xe rẽ phải (xe tải).\n"
         "Do đó XE KHÁCH là xe phải nhường đường đi cuối cùng qua nơi giao nhau.",

    497: "Phân tích biển báo và quy tắc nhường đường tại nơi giao nhau:\n"
         "- Về biển báo: Cả xe con và xe tải đều gặp biển tam giác ngược W.208 'Giao nhau với đường ưu tiên' kèm biển phụ S.506b thể hiện hướng đường ưu tiên. Do đó, cả hai xe đều đang ở trên đường nhánh không ưu tiên (cùng cấp).\n"
         "- Về hướng đi: Theo hướng mũi tên, cả xe tải và xe con đều đi thẳng qua nơi giao nhau.\n"
         "- Quy tắc nhường đường (Bên phải trống): Tại nơi giao nhau cùng cấp, xe nào có phía bên phải không vướng thì được quyền đi trước (nhường đường cho xe đến từ bên phải). Xe tải có phía bên phải trống nên được quyền đi trước; xe con có xe tải ở phía bên phải tới nên phải nhường đường.\n"
         "Do đó XE CON PHẢI NHƯỜNG ĐƯỜNG là đúng quy tắc giao thông.",

    498: "Thứ tự xe ưu tiên theo Luật Giao thông đường bộ:\n"
         "Quy tắc ưu tiên: 'HỎA - SỰ - CÔNG - THƯƠNG'.\n"
         "Xe chữa cháy đi làm nhiệm vụ chữa cháy có mức độ khẩn cấp và quyền ưu tiên cao hơn xe công an đi làm nhiệm vụ khẩn cấp. Do đó XE CHỮA CHÁY ĐƯỢC QUYỀN ĐI TRƯỚC.",

    499: "Quan sát tín hiệu đèn giao thông:\n"
         "- Làn đường của xe con và xe khách có tín hiệu ĐÈN XANH nên được phép đi (xe con rẽ phải, xe khách đi thẳng).\n"
         "- Làn đường của xe mô tô có tín hiệu ĐÈN ĐỎ nên bắt buộc phải dừng lại trước vạch dừng.\n"
         "Do đó: Xe con và xe khách được phép đi.",

    500: "Theo tín hiệu đèn, xe nào ở làn có đèn màu xanh thì được phép đi:\n"
         "- Xe con và xe tải: Ở các làn có đèn tín hiệu màu xanh -> Được phép đi.\n"
         "- Xe khách và xe mô tô: Ở các làn có đèn tín hiệu màu đỏ -> Phải dừng lại.\n"
         "Do đó: Xe con và xe tải đi là đúng quy tắc giao thông.",

    501: "Thứ tự ưu tiên giữa các xe ưu tiên theo Luật:\n"
         "Quy tắc ưu tiên: 'Hỏa - Sự - Công - Thương'.\n"
         "Xe quân sự đi làm nhiệm vụ khẩn cấp có quyền ưu tiên cao hơn xe công an đi làm nhiệm vụ khẩn cấp. Do đó XE QUÂN SỰ ĐƯỢC QUYỀN ĐI TRƯỚC.",

    502: "Quan sát hệ thống đèn tín hiệu giao thông:\n"
         "- Đèn tín hiệu chính hình tròn đang bật ĐÈN ĐỎ, cấm các phương tiện đi thẳng (hướng 3) hoặc rẽ trái (hướng 4), rẽ nhánh (hướng 2).\n"
         "- Bên cạnh đèn chính có gắn một ĐÈN PHỤ HÌNH MŨI TÊN MÀU XANH chỉ sang phải (hướng 1).\n"
         "Do đó xe tải chỉ được phép đi theo HƯỚNG 1 (rẽ phải theo đèn phụ màu xanh).",

    503: "Xét vi phạm về đèn tín hiệu và chỉ dẫn hướng đi trên làn đường:\n"
         "- Xe khách: Ở làn rẽ trái nhưng mũi tên lại đi thẳng -> Vi phạm hướng đi của làn đường.\n"
         "- Xe tải: Ở làn đi thẳng gặp đèn đỏ nhưng mũi tên lại vượt đèn đỏ rẽ trái -> Vi phạm hiệu lệnh đèn tín hiệu và sai làn.\n"
         "- Xe con: Ở làn rẽ phải có đèn xanh rẽ phải đúng -> Chấp hành đúng.\n"
         "- Xe mô tô: Ở làn rẽ phải gặp đèn xanh rẽ phải nhưng mũi tên lại rẽ trái sang làn đối diện -> Vi phạm hướng đi của làn đường.\n"
         "Vậy những xe vi phạm quy tắc giao thông gồm: Xe khách, xe tải, xe mô tô.",

    504: "Tại nơi đường giao nhau cùng cấp không có biển báo và không có xe ưu tiên, áp dụng quy tắc ưu tiên theo thứ tự: Bên phải trống -> Rẽ phải -> Đi thẳng -> Rẽ trái -> Quay đầu:\n"
         "- Xe mô tô: Bên phải trống (không có xe) và rẽ phải -> Đi đầu tiên (thứ 1).\n"
         "- Sau khi xe mô tô đi, bên phải xe tải trống -> Xe tải đi thẳng (thứ 2).\n"
         "- Sau khi xe tải đi, bên phải xe khách trống -> Xe khách rẽ trái (thứ 3).\n"
         "- Xe con quay đầu đi sau cùng (thứ 4).\n"
         "Thứ tự đúng: Xe mô tô -> Xe tải -> Xe khách -> Xe con.",

    505: "Phân tích biển báo cấm và biển phụ:\n"
         "- Biển chính là biển P.130 'Cấm dừng xe và đỗ xe'.\n"
         "- Bên dưới có gắn biển phụ S.505a vẽ hình xe ô tô tải. Biển phụ này quy định hiệu lực của biển cấm dừng đỗ CHỈ ÁP DỤNG RIÊNG ĐỐI VỚI XE TẢI.\n"
         "- Xe con và xe mô tô không thuộc đối tượng áp dụng của biển phụ nên được phép đỗ bình thường.\n"
         "Do đó chỉ có duy nhất XE TẢI ĐỖ VI PHẠM.",

    506: "Phân tích biển báo ưu tiên tại nơi giao nhau:\n"
         "- Trước mặt xe con (B) có cắm biển W.207 'Giao nhau với đường không ưu tiên' (đỉnh tam giác hướng lên trên), báo hiệu xe con (B) đang lưu thông trên đường ưu tiên.\n"
         "- Trước mặt xe con (A) và xe tải đều cắm biển W.208 'Giao nhau với đường ưu tiên' (tam giác ngược đỉnh chúc xuống), báo hiệu đang ở đường không ưu tiên.\n"
         "Do đó xe con (B) nằm trên đường ưu tiên ĐƯỢC QUYỀN ĐI TRƯỚC.",

    507: "Phân biệt giữa xe gắn máy và xe mô tô theo Quy chuẩn báo hiệu đường bộ:\n"
         "- Biển 2 là biển P.105 'Cấm xe mô tô'. Biển này CHỈ CẤM XE MÔ TÔ (dung tích xi lanh từ 50 cm3 trở lên), KHÔNG CẤM XE GẮN MÁY (dưới 50 cm3).\n"
         "- Biển 3 là biển P.103a 'Cấm xe ô tô', không có tác dụng cấm xe 2 bánh.\n"
         "- Do người điều khiển đang lái XE GẮN MÁY (dung tích dưới 50 cm3), phương tiện này không bị cấm bởi bất kỳ biển báo nào trong hình.\n"
         "Do đó xe gắn máy được phép đi CẢ BA HƯỚNG.",

    508: "Phân tích biển báo cấm và phạm vi tác dụng:\n"
         "- Biển P.130 'Cấm dừng xe và đỗ xe' có đặt kèm biển phụ S.508b vẽ mũi tên hai đầu (chỉ cả hướng lên và hướng xuống).\n"
         "- Biển phụ này biểu thị biển cấm có hiệu lực ở CẢ PHÍA TRƯỚC VÀ PHÍA SAU vị trí cắm biển.\n"
         "- Xe tải đỗ ở phía trước biển, xe mô tô đỗ ở phía sau biển; cả hai xe đều nằm trong phạm vi hiệu lực cấm.\n"
         "Do đó CẢ HAI XE ĐỀU ĐỖ VI PHẠM.",

    509: "Phân tích hành vi đỗ xe vi phạm theo Luật Giao thông đường bộ:\n"
         "- Xe tải: Đỗ ngược chiều lưu thông của làn đường bên trái -> Vi phạm nghiêm trọng quy định dừng, đỗ xe.\n"
         "- Xe con và xe mô tô: Đỗ đè lên phần đường kẻ vạch dành cho người đi bộ qua đường (vạch ngựa vằn) -> Vi phạm quy định dừng, đỗ xe tại nơi đường giao nhau và vạch đi bộ.\n"
         "Do đó CẢ BA XE ĐỀU ĐỖ VI PHẠM.",

    510: "Quy định về việc kéo xe theo Luật Giao thông đường bộ:\n"
         "- Đoạn đường có cắm biển P.120 'Cấm xe ô tô kéo rơ-moóc hoặc kéo phương tiện khác'.\n"
         "- Ngoài ra, Luật cũng quy định xe ô tô khi tham gia giao thông không được phép kéo theo xe mô tô, xe gắn máy không đảm bảo an toàn kỹ thuật.\n"
         "Do đó việc xe tải kéo xe mô tô ba bánh như hình là KHÔNG ĐÚNG quy tắc giao thông.",

    511: "Xét biển báo hiệu tại vòng xuyến:\n"
         "- Xe ô tô con đang di chuyển quanh đảo vòng xuyến có 5 hướng đi ra.\n"
         "- Quan sát tại lối vào hướng 1 có cắm biển báo cấm P.103a 'Cấm xe ô tô' (biển tròn viền đỏ vẽ hình ô tô con ở giữa).\n"
         "- Các hướng 2, 3, 4, 5 không có biển cấm đối với ô tô.\n"
         "Do đó CHỈ HƯỚNG 1 LÀ XE KHÔNG ĐƯỢC PHÉP ĐI.",

    512: "Phân tích biển báo cấm rẽ tại ngã ba/ngã tư:\n"
         "- Phía trước ngã tư có đặt biển P.123a 'Cấm rẽ trái' (biển tròn viền đỏ có mũi tên rẽ trái bị gạch chéo đỏ).\n"
         "- Hướng 3 chính là hướng rẽ trái nên xe ô tô không được phép đi vào hướng 3.\n"
         "- Theo Quy chuẩn 41:2019, biển cấm rẽ trái không cấm quay đầu xe, do đó hướng 2 (quay đầu), hướng 1 (rẽ phải), hướng 4 (đi thẳng) đều được đi.\n"
         "Do đó hướng xe không được phép đi là HƯỚNG 3.",

    513: "Phân tích biển báo cấm vượt và vạch kẻ đường:\n"
         "- Biển báo trên đường là biển P.126 'Cấm xe ô tô tải vượt' (vẽ ô tô tải màu đỏ vượt ô tô con màu đen). Biển này CHỈ CẤM RIÊNG XE TẢI VƯỢT, hoàn toàn KHÔNG CẤM xe con hay xe khách vượt.\n"
         "- Vạch tim đường là vạch nét đứt màu vàng, cho phép các phương tiện đè vạch để vượt khi phía trước an toàn.\n"
         "Do đó CẢ HAI XE (xe con và xe khách) ĐỀU VƯỢT ĐÚNG quy tắc giao thông.",

    514: "Xét hiệu lệnh của biển báo giao thông:\n"
         "- Trước ngã tư đặt biển hiệu lệnh R.301e 'Các hướng đi phải theo' (hình tròn nền xanh vẽ hai mũi tên: đi thẳng và rẽ trái).\n"
         "- Biển này bắt buộc người lái xe chỉ được đi thẳng (hướng 2) hoặc rẽ trái (hướng 3), không được rẽ phải sang hướng 1.\n"
         "Do đó những hướng xe được phép đi là HƯỚNG 2 VÀ HƯỚNG 3.",

    515: "Quy định về việc kéo rơ-moóc và phương tiện khác:\n"
         "- Trong hình, xe ô tô tải đang kéo một rơ-moóc thùng hàng, đồng thời rơ-moóc này lại tiếp tục kéo thêm một xe ô tô đầu kéo khác phía sau.\n"
         "- Luật Giao thông đường bộ quy định nghiêm cấm: Ô tô không được kéo theo một xe khác khi xe này đang kéo một phương tiện khác; không được kéo nhiều xe/rơ-moóc cùng lúc trái quy định.\n"
         "Do đó xe kéo nhau như hình là VI PHẠM quy tắc giao thông.",

    516: "Phân tích biển báo qua cầu hẹp/đoạn đường hẹp:\n"
         "- Phía trước xe khách có đặt biển P.132 'Nhường đường cho xe cơ giới đi ngược chiều qua đường hẹp' (biển tròn viền đỏ, mũi tên màu đỏ chỉ chiều xe khách).\n"
         "- Phía đối diện xe tải có đặt biển chỉ dẫn I.406 'Được ưu tiên qua đường hẹp' (biển vuông màu xanh, mũi tên màu trắng chỉ chiều xe tải).\n"
         "Do đó xe khách gặp biển P.132 bắt buộc PHẢI NHƯỜNG ĐƯỜNG cho xe tải đi qua cầu trước.",

    517: "Quy tắc hướng đi ưu tiên tại nơi đường giao nhau có đèn tín hiệu:\n"
         "- Cả xe con và xe mô tô đều đang gặp ĐÈN XANH nên đều được phép di chuyển vào giao lộ.\n"
         "- Xe mô tô RẼ PHẢI; xe ô tô con RẼ TRÁI.\n"
         "- Áp dụng quy tắc hướng rẽ ưu tiên ('Phải > Thẳng > Trái'): Xe rẽ phải luôn được quyền đi trước xe rẽ trái.\n"
         "Do đó XE MÔ TÔ ĐƯỢC QUYỀN ĐI TRƯỚC.",

    518: "Quy định an toàn khi điều khiển xe đầu kéo sơ mi rơ-moóc:\n"
         "- Hình ảnh thể hiện một tổ hợp xe đầu kéo kéo sơ mi rơ-moóc (xe container) nhưng phía đuôi sơ mi rơ-moóc lại gắn nối kéo thêm một chiếc xe tải thùng phía sau.\n"
         "- Luật Giao thông đường bộ quy định: Xe đầu kéo kéo sơ mi rơ-moóc tuyệt đối không được phép kéo thêm xe khác hoặc kéo thêm rơ-moóc khác.\n"
         "Do đó trường hợp này là KHÔNG ĐÚNG quy định.",

    519: "Phân tích biển hiệu lệnh kết hợp biển phụ và biển cấm:\n"
         "- Biển tròn xanh bên phải là biển hiệu lệnh R.301e (chỉ được rẽ phải) có gắn kèm biển phụ S.505a vẽ hình xe tải. Hiệu lệnh này CHỈ ÁP DỤNG ĐỐI VỚI XE TẢI, xe ô tô con không bị ràng buộc.\n"
         "- Hướng 2 có cắm biển P.103a 'Cấm xe ô tô' (cấm xe con đi thẳng vào hướng 2).\n"
         "- Hướng 1 (rẽ phải), hướng 3 (rẽ trái), hướng 4 (quay đầu) không có biển cấm xe con.\n"
         "Do đó xe ô tô con ĐƯỢC PHÉP ĐI HƯỚNG 1, 3 VÀ 4.",

    520: "Tại nơi đường giao nhau cùng cấp không có biển báo và không có xe ưu tiên, áp dụng quy tắc ưu tiên theo thứ tự: Bên phải trống -> Rẽ phải -> Đi thẳng -> Rẽ trái -> Quay đầu:\n"
         "- Xe mô tô và xe đạp: Bên phải trống (không có xe) và cùng rẽ phải -> Đi đầu tiên (thứ 1).\n"
         "- Sau khi xe mô tô và xe đạp đi, bên phải xe con (A) trống -> Xe con (A) đi thẳng (thứ 2).\n"
         "- Sau khi xe con (A) đi, bên phải xe con (B) trống -> Xe con (B) rẽ trái đi sau cùng (thứ 3).\n"
         "Thứ tự đúng: Xe mô tô + xe đạp -> Xe con (A) -> Xe con (B).",

    521: "Xét biển hiệu lệnh và biển phụ chỉ hướng:\n"
         "- Bên phải có đặt biển hiệu lệnh R.301 'Hướng đi phải theo' (chỉ rẽ phải) kèm biển phụ S.505a hình ô tô tải bên dưới. Nghĩa là hiệu lệnh bắt buộc rẽ phải chỉ áp dụng riêng cho xe tải.\n"
         "- Ngoài ra, hướng 2 có cắm biển P.106a cấm xe tải đi thẳng.\n"
         "Do đó xe tải CHỈ ĐƯỢC PHÉP ĐI THEO HƯỚNG 1 (rẽ phải).",

    522: "Phân tích biển báo cấm theo hướng mũi tên:\n"
         "- Trước ngã ba có cắm biển P.106a 'Cấm ô tô tải' kết hợp biển phụ S.504 chỉ mũi tên rẽ phải (hướng 1), nghĩa là cấm xe tải rẽ phải vào hướng 1.\n"
         "- Hướng 2 (đi thẳng) và hướng 3 (rẽ trái) hoàn toàn không có biển cấm đối với xe tải.\n"
         "Do đó xe tải ĐƯỢC PHÉP ĐI HƯỚNG 2 VÀ HƯỚNG 3.",

    523: "Phân tích biển báo cấm tại đầu dải phân cách:\n"
         "- Tại đầu dải phân cách giữa có cắm biển P.103a 'Cấm xe ô tô' (hình tròn viền đỏ vẽ ô tô con). Biển này cấm tất cả các loại xe ô tô (kể cả xe tải, xe khách theo nguyên tắc 'cấm nhỏ cấm luôn lớn') đi vào phần đường phía sau biển (hướng 2, 3, 4).\n"
         "- Hướng 1 (rẽ phải trước biển) và hướng 5 (quay đầu xe trước biển) không nằm trong phạm vi cấm của biển.\n"
         "Do đó xe ô tô tải ĐƯỢC PHÉP ĐI HƯỚNG 1 VÀ HƯỚNG 5.",

    524: "Phân tích biển báo cấm xe tải tại ngã tư:\n"
         "- Tại lối vào hướng 2 có cắm biển P.106a 'Cấm xe ô tô tải' (vẽ hình xe tải trong vòng tròn viền đỏ), do đó xe tải bị cấm đi thẳng vào hướng 2.\n"
         "- Các hướng 1 (rẽ phải), hướng 3 (rẽ trái), hướng 4 (quay đầu) không có biển cấm xe tải.\n"
         "Do đó xe ô tô tải được đi các hướng TRỪ HƯỚNG 2.",

    525: "Phân tích biển báo đường ưu tiên và hướng ưu tiên:\n"
         "- Phía trước xe mô tô có cắm biển hình thoi I.401 'Bắt đầu đường ưu tiên' kèm biển phụ S.506b chỉ hướng đường ưu tiên rẽ trái (nét đậm sang nhánh bên kia).\n"
         "- Phía trước xe con có cắm biển tam giác ngược W.208 'Giao nhau với đường ưu tiên' (đang trên đường không ưu tiên).\n"
         "Do đó xe mô tô nằm trên đường ưu tiên ĐƯỢC QUYỀN ĐI TRƯỚC xe con.",

    526: "Xét hiệu lực của biển báo hiệu lệnh:\n"
         "- Phía trước ngã tư có cắm biển hiệu lệnh R.301a 'Các phương tiện chỉ được đi thẳng'.\n"
         "- Xe ô tô con không chấp hành hiệu lệnh đi thẳng mà lại thực hiện quay đầu xe tại ngã tư.\n"
         "Do đó xe ô tô con VI PHẠM quy tắc giao thông.",

    527: "Phân tích vạch kẻ đường và hành vi các xe:\n"
         "- Vạch tim đường phân chia hai chiều xe chạy là VẠCH ĐƠN NÉT LIỀN MÀU VÀNG (vạch 1.2), cấm phương tiện đè vạch hoặc lấn làn.\n"
         "- Xe ô tô con thực hiện quay đầu xe đè qua vạch liền màu vàng -> Vi phạm quy tắc giao thông.\n"
         "- Xe mô tô đánh lái tránh chướng ngại vật công trường có cọc tiêu rào chắn trên đường -> Phù hợp tình huống thực tế.\n"
         "Do đó chỉ có XE CON VI PHẠM quy tắc giao thông.",

    528: "Hiệu lệnh của người điều khiển giao thông (Cảnh sát giao thông):\n"
         "- Luật Giao thông đường bộ quy định: Khi người điều khiển giao thông giơ tay thẳng đứng, tất cả người tham gia giao thông ở mọi hướng đều phải dừng lại trước ngã tư.\n"
         "- Ngoại lệ: Những phương tiện đã chớm ở trong khu vực ngã tư thì được phép tiếp tục di chuyển để giải phóng giao lộ (như xe tải màu xanh trong hình).\n"
         "Đáp án đúng: Tất cả các xe phải dừng lại trước ngã tư, trừ những xe đã ở trong ngã tư được phép tiếp tục đi.",

    529: "Hiệu lệnh CSGT giang hai tay sang ngang:\n"
         "- Luật Giao thông đường bộ quy định: Khi người điều khiển giao thông giang hai tay hoặc một tay sang ngang thì người tham gia giao thông ở phía trước và phía sau phải dừng lại; người tham gia giao thông ở phía bên phải và bên trái được đi tất cả các hướng.\n"
         "- Trong hình: Xe mô tô và xe tải nằm ở phía bên tay phải và bên tay trái của CSGT nên ĐƯỢC PHÉP ĐI; xe con ở phía trước mặt CSGT phải dừng lại.\n"
         "Đáp án đúng: Xe mô tô, xe tải.",

    530: "Quy định về các trường hợp được phép vượt xe về bên phải:\n"
         "- Luật Giao thông đường bộ quy định: Phương tiện được phép vượt về bên phải khi 'Xe phía trước có tín hiệu rẽ trái hoặc đang rẽ trái'.\n"
         "- Trong hình: Xe tải phía trước đang bật tín hiệu rẽ trái và đã mở lái sang làn rẽ trái, chừa lại khoảng trống bên phải. Xe con đi thẳng vượt qua bên phải xe tải là ĐÚNG quy tắc giao thông.",

    531: "Phân tích vạch kẻ đường kép phân chia hai chiều xe chạy:\n"
         "- Vạch tim đường là VẠCH KÉP MÀU VÀNG (vạch 1.4) gồm một vạch nét liền và một vạch nét đứt chạy song song:\n"
         "  + Phía xe con: Vạch tim đường là VẠCH NÉT ĐỨT, cho phép xe con đè vạch lấn sang làn đối diện để vượt xe tải khi an toàn -> Xe con vượt ĐÚNG.\n"
         "  + Phía xe tải (container): Vạch tim đường là VẠCH NÉT LIỀN, tuyệt đối cấm đè vạch hoặc lấn làn -> Xe tải lấn làn vượt xe khách là SAI.\n"
         "Do đó chỉ có duy nhất XE CON VƯỢT ĐÚNG.",

    532: "Phân tích biển báo cấm và quyền của xe ưu tiên:\n"
         "- Xe tải: Phía trước có cắm biển P.123a 'Cấm rẽ trái' (cấm quay đầu xe/rẽ trái), nhưng xe tải lại quay đầu xe -> Xe tải VI PHẠM.\n"
         "- Xe chữa cháy: Đang đi làm nhiệm vụ khẩn cấp có tín hiệu còi, đèn ưu tiên, được quyền đi vào đường có biển P.102 'Cấm đi ngược chiều' theo Luật Giao thông đường bộ.\n"
         "Do đó xe vi phạm quy tắc giao thông là XE TẢI.",

    533: "Phân tích biển báo và quy tắc nhường đường tại nơi giao nhau:\n"
         "- Biển báo: Nơi giao nhau có cắm biển W.205 'Giao nhau giữa các đường cùng cấp' (tam giác viền đỏ nền vàng hình chữ T), do đó các tuyến đường có quyền ưu tiên ngang nhau.\n"
         "- Quy tắc hướng đi ưu tiên: Xe rẽ phải -> Xe đi thẳng -> Xe rẽ trái:\n"
         "  + Xe tải rẽ phải: Hướng rẽ phải được ưu tiên đi đầu tiên (không xung đột cắt ngang luồng xe khác).\n"
         "  + Xe khách và Xe con cùng lưu thông đối diện nhau trên cùng một con đường: Xe con rẽ trái (chuyển hướng) bắt buộc phải nhường đường cho xe khách đi thẳng. Do đó xe khách đi thứ 2.\n"
         "  + Xe con rẽ trái: Nhường cho xe khách đi thẳng xong mới được rẽ, nên đi sau cùng (thứ 3).\n"
         "Thứ tự đúng: Xe tải -> Xe khách -> Xe con.",

    534: "Phân tích biển báo và quy tắc hướng đi ưu tiên (Rẽ phải -> Đi thẳng -> Rẽ trái):\n"
         "- Biển báo: Nơi giao nhau có cắm biển W.205 'Giao nhau giữa các đường cùng cấp', do đó các tuyến đường có quyền ưu tiên ngang nhau.\n"
         "- Xét hướng đi của các xe:\n"
         "  + Cả xe khách và xe tải đều rẽ phải: Hướng rẽ phải được ưu tiên đi trước. Quỹ đạo rẽ phải của hai xe không giao cắt xung đột nhau nên xe khách và xe tải được ĐI ĐỒNG THỜI (thứ 1).\n"
         "  + Xe con rẽ trái: Thuộc hướng ưu tiên sau cùng nên phải nhường đường và đi sau cùng (thứ 2).\n"
         "Thứ tự đúng: Xe khách và xe tải, xe con.",

    535: "Phân tích biển cấm tại các hướng đi của xe tải:\n"
         "- Ngay tại lối vào hướng 4 (hướng đi thẳng) có cắm biển P.102 'Cấm đi ngược chiều' (biển tròn đỏ có vạch ngang màu trắng), do đó xe tải bị cấm đi vào hướng 4.\n"
         "- Các hướng còn lại: Hướng 1 (rẽ phải), Hướng 2 (rẽ trái), Hướng 3 (quay đầu xe) không có biển cấm đối với xe tải.\n"
         "Do đó xe tải được phép đi các hướng TRỪ HƯỚNG 4.",

    536: "Áp dụng thứ tự ưu tiên sa hình:\n"
         "1. 'Nhì ưu': Xe công an đi làm nhiệm vụ khẩn cấp được quyền đi đầu tiên.\n"
         "2. 'Tam đường': Xe con nằm trên đường có cắm biển W.207 'Giao nhau với đường không ưu tiên' (đang trên đường ưu tiên) và đi thẳng nên được đi thứ 2.\n"
         "3. 'Tứ hướng': Xe tải và xe khách cùng ở đường không ưu tiên (gặp biển tam giác ngược W.208), xe tải đi thẳng đi thứ 3, xe khách rẽ trái đi cuối cùng.\n"
         "Thứ tự đúng: Xe công an -> Xe con -> Xe tải -> Xe khách.",

    537: "Phân tích biển báo cấm theo từng hướng đi:\n"
         "- Trước ngã tư có cắm biển P.123a 'Cấm rẽ trái' (biển tròn viền đỏ mũi tên rẽ trái gạch chéo), do đó xe tải bị CẤM RẼ VÀO HƯỚNG 2. Biển cấm rẽ trái không cấm quay đầu xe nên hướng 3 vẫn được đi.\n"
         "- Hướng 4 (đi thẳng) có cắm biển P.108 'Cấm máy kéo'. Theo nguyên tắc 'Cấm xe lớn không cấm xe nhỏ', biển cấm máy kéo không cấm ô tô tải nên xe tải vẫn được đi vào hướng 4.\n"
         "- Hướng 1 (rẽ phải) không có biển cấm.\n"
         "Do đó xe tải được phép đi các HƯỚNG 1, 3 VÀ 4.",

    538: "Quan sát đèn tín hiệu và hướng mũi tên của từng phương tiện:\n"
         "- Xe khách: Ở làn rẽ trái có đèn đỏ cấm rẽ trái -> Đang dừng lại trước vạch dừng -> Đúng.\n"
         "- Xe tải: Ở làn đi thẳng có đèn xanh đi thẳng -> Đi thẳng -> Đúng.\n"
         "- Xe con: Ở làn rẽ phải có đèn xanh rẽ phải -> Rẽ phải -> Đúng.\n"
         "- Phía đối diện: Xe tải rẽ trái theo đèn xanh rẽ trái; xe con và mô tô dừng đèn đỏ -> Tất cả đều đúng.\n"
         "Do đó: TẤT CẢ CÁC LOẠI XE TRÊN đều chấp hành đúng quy tắc giao thông.",

    539: "Phân tích biển báo đối với xe mô tô:\n"
         "- Hướng 1 (rẽ phải): Không có biển cấm -> Được đi.\n"
         "- Hướng 2 (đi thẳng): Có cắm biển P.105 'Cấm xe mô tô' -> Cấm mô tô đi vào.\n"
         "- Hướng 3 (rẽ trái): Có cắm biển P.103a 'Cấm xe ô tô'. Biển cấm ô tô không có hiệu lực cấm xe mô tô hai bánh -> Mô tô được phép đi.\n"
         "Do đó xe mô tô được phép đi HƯỚNG 1 VÀ HƯỚNG 3.",

    540: "Áp dụng thứ tự ưu tiên xe ưu tiên và đường cùng cấp:\n"
         "1. Trong hình có hai xe ưu tiên: Xe quân sự và Xe công an. Theo Luật Giao thông: 'Hỏa - Sự - Công - Thương', xe quân sự có quyền ưu tiên cao hơn xe công an, do đó xe quân sự đi trước (thứ 1), tiếp theo là xe công an (thứ 2).\n"
         "2. Xe con và xe mô tô: Cả hai xe đều đi thẳng (không xung đột hướng đi) nên cùng đi một lúc (thứ 3).\n"
         "Thứ tự đúng: Xe quân sự -> Xe công an -> Xe con + xe mô tô."
}
