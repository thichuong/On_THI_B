# scripts/explanations/part11.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 541 đến Câu 600
Chương 6: Giải thế sa hình và kỹ năng xử lý tình huống giao thông (Phần 2)
"""

PART11_EXPLANATIONS = {
    541: "Quy tắc nhường đường khi tránh nhau trên đường dốc hẹp:\n"
         "- Phía trước bên phải xe B có cắm biển báo W.220 'Dốc lên nguy hiểm' (vạch dốc hướng lên khi nhìn từ trái sang phải), nghĩa là xe B đang đi lên dốc.\n"
         "- Xe A đi theo chiều ngược lại nên xe A đang đi xuống dốc.\n"
         "- Quy tắc giao thông đường bộ quy định: Khi tránh nhau trên đường dốc hẹp, xe đang xuống dốc phải nhường đường cho xe đang lên dốc.\n"
         "Do đó XE A PHẢI NHƯỜNG ĐƯỜNG cho xe B.",

    542: "Quy định cấm quay đầu xe tại nơi có vạch người đi bộ:\n"
         "- Luật Giao thông đường bộ nghiêm cấm: Người lái xe không được phép quay đầu xe ở phần đường dành cho người đi bộ qua đường (vạch ngựa vằn).\n"
         "- Trong hình, xe ô tô con quay đầu xe đè trực tiếp lên vạch kẻ đường dành cho người đi bộ qua đường.\n"
         "Do đó hành vi quay đầu của xe con là VI PHẠM quy tắc giao thông.",

    543: "Đối chiếu biển báo làn đường trên giá long môn với vị trí thực tế của từng xe:\n"
         "- Làn 1 (ngoài cùng bên trái): Biển chỉ dẫn làn dành cho xe ô tô -> Xe khách (A) đi đúng.\n"
         "- Làn 2: Biển chỉ dẫn làn dành cho xe ô tô -> Xe tải (B) đi đúng; Xe mô tô (C) đi vào làn ô tô là SAI LÀN.\n"
         "- Làn 3: Biển chỉ dẫn làn dành cho xe mô tô -> Xe ô tô con (E) đi vào làn mô tô là SAI LÀN.\n"
         "- Làn 4: Biển chỉ dẫn làn dành cho xe mô tô -> Xe mô tô (D) đi đúng.\n"
         "Vậy hai xe vi phạm quy tắc giao thông là: Xe con (E), xe mô tô (C).",

    544: "Quy tắc sa hình 'Nhất chớm':\n"
         "- Xe ô tô con màu đỏ phía trước đã vượt qua vạch dừng của người đi bộ, đi sâu vào tâm giao lộ và đang chuyển hướng rẽ trái ('nhất chớm').\n"
         "- Luật quy định xe đã vào trong nơi giao nhau trước được quyền ưu tiên thoát khỏi giao lộ trước các phương tiện đến sau.\n"
         "- Xe của bạn đi thẳng nhưng đến sau nên bắt buộc PHẢI NHƯỜNG XE CON RẼ TRÁI TRƯỚC rồi mới tiếp tục đi.",

    545: "Phân tích biển báo cấm tại ngã ba/ngã tư từ góc nhìn người lái:\n"
         "- Lối vào hướng 3 có cắm biển P.102 'Cấm đi ngược chiều' -> Cấm đi vào hướng 3.\n"
         "- Lối vào hướng 4 có cắm biển P.123b 'Cấm rẽ phải' -> Cấm rẽ vào hướng 4.\n"
         "- Hướng 1 (rẽ trái) và hướng 2 (đi thẳng) không có biển cấm.\n"
         "Do đó người lái xe ĐƯỢC PHÉP ĐI THEO HƯỚNG 1 VÀ HƯỚNG 2.",

    546: "Quy tắc chuyển làn đường an toàn:\n"
         "- Luật Giao thông đường bộ quy định: Phương tiện khi chuyển làn đường phải có tín hiệu báo trước, quan sát bảo đảm an toàn và phải nhường đường cho phương tiện đang chạy trên làn đường định chuyển sang.\n"
         "- Xe con (B) đang bật đèn tín hiệu xin chuyển làn sang làn bên phải (làn xe con A đang chạy).\n"
         "- Xe con (A) đang đi thẳng trên làn đường thông suốt của mình.\n"
         "Do đó XE CON (B) PHẢI NHƯỜNG ĐƯỜNG cho xe con (A).",

    547: "Quy tắc nhường đường tại nơi giao nhau có đèn tín hiệu:\n"
         "- Dù xe của bạn đang có đèn xanh nhưng bạn đang chuẩn bị rẽ trái qua giao lộ.\n"
         "- Xe tải đã cán vạch, đi vào ngã rẽ (đã chớm vào nơi giao nhau trước) nên theo nguyên tắc 'Nhất chớm', xe tải được quyền ưu tiên đi tiếp để thoát khỏi giao lộ.\n"
         "- Xe buýt đi thẳng từ hướng đối diện, được quyền ưu tiên đi trước xe rẽ trái theo quy tắc hướng đi (Đi thẳng > Rẽ trái).\n"
         "Do đó, dù đang là đèn xanh thì bạn vẫn phải NHƯỜNG ĐƯỜNG CHO CẢ XE BUÝT VÀ XE TẢI.",

    548: "Đối chiếu biển phân làn trên giá long môn với vị trí thực tế của từng xe:\n"
         "- Làn 1 (bên trái): Làn dành cho ô tô con -> Xe con (A) đi đúng.\n"
         "- Làn 2: Làn dùng chung cho ô tô và mô tô -> Xe con (B) và xe mô tô (C) đi đúng.\n"
         "- Làn 3: Làn dành cho xe mô tô -> Xe con (E) đi vào làn mô tô là SAI LÀN.\n"
         "- Làn 4 (bên phải): Làn dành cho xe ô tô con -> Xe mô tô (D) đi vào làn ô tô là SAI LÀN.\n"
         "Vậy những xe vi phạm quy tắc giao thông là: Xe con (E), xe mô tô (D).",

    549: "Phân tích biển báo ưu tiên tại nơi giao nhau:\n"
         "- Phía trước xe của bạn có cắm biển tam giác ngược W.208 'Giao nhau với đường ưu tiên' (báo hiệu bạn đang đi từ đường nhánh, không ưu tiên ra đường chính).\n"
         "- Xe tải đang chạy thẳng trên trục đường chính (đường ưu tiên cắt ngang).\n"
         "Do đó XE TẢI ĐƯỢC QUYỀN ĐI TRƯỚC xe của bạn.",

    550: "Quy tắc quay đầu xe tại nơi đường giao nhau:\n"
         "- Trước ngã tư có cắm biển P.123a 'Cấm rẽ trái'. Theo Quy chuẩn 41:2019, biển cấm rẽ trái KHÔNG CẤM quay đầu xe.\n"
         "- Hướng B: Điểm quay đầu đè trực tiếp lên vạch kẻ đường dành cho người đi bộ qua đường (Luật nghiêm cấm quay đầu xe tại đây).\n"
         "- Hướng A: Xe tiến qua vạch người đi bộ vào trong ngã tư an toàn rồi mới vòng đầu xe -> Đúng luật.\n"
         "Do đó người lái xe CHỈ ĐƯỢC QUAY ĐẦU THEO HƯỚNG A.",

    551: "Phân tích biển báo ưu tiên và hướng di chuyển của các xe:\n"
         "- Xe của bạn: Phía trước có cắm biển W.207a 'Giao nhau với đường không ưu tiên' (đang đi trên đường ưu tiên) và xe đi thẳng nên được quyền đi trước.\n"
         "- Xe con: Ở đường không ưu tiên nhưng rẽ phải, hướng rẽ không giao cắt hay xung đột với xe của bạn nên có thể đi cùng lúc với xe của bạn.\n"
         "- Xe tải: Ở đường không ưu tiên và rẽ trái (cắt qua luồng ưu tiên) nên phải nhường đường và đi sau cùng.\n"
         "Thứ tự đúng: Xe của bạn và xe con, xe tải.",

    552: "Quy tắc vượt xe an toàn theo Luật Giao thông đường bộ:\n"
         "Khi muốn vượt xe phía trước (xe tải), người lái xe phải:\n"
         "1. Quan sát an toàn phía trước, phía sau qua gương chiếu hậu.\n"
         "2. Bật tín hiệu báo hiệu xin vượt bằng đèn hoặc còi.\n"
         "3. Khi đủ điều kiện an toàn (không có chướng ngại vật, không có xe ngược chiều) mới tăng tốc cho xe chạy vượt qua dứt khoát.\n"
         "Đáp án đúng: Bật tín hiệu báo hiệu bằng đèn hoặc còi, khi đủ điều kiện an toàn, tăng tốc cho xe chạy vượt qua.",

    553: "Quan sát hệ thống đèn tín hiệu giao thông:\n"
         "- Làn xe khách và xe mô tô đang có tín hiệu ĐÈN XANH -> Được phép đi.\n"
         "- Làn xe tải và xe con đang có tín hiệu ĐÈN ĐỎ -> Bắt buộc phải dừng lại trước vạch dừng.\n"
         "Đáp án đúng: Xe con, xe tải.",

    554: "Quan sát vị trí xe chạy so với các vạch kẻ đường:\n"
         "- Xe con (B) và Xe tải (D) vi phạm vì chạy cán/đè lên vạch kẻ đường (xe B chạy đè vạch đôi màu vàng ở tim đường, xe D chạy đè vạch liền màu trắng).\n"
         "- Các xe còn lại gồm Xe con (A), Xe con (C), Xe con (E) và Xe buýt (G) đều đi đúng trong phần làn đường quy định, không đè vạch.\n"
         "Do đó các xe chấp hành đúng quy tắc giao thông là: Xe con (A), xe con (C), xe con (E), xe buýt (G).",

    555: "Quy định cấm vượt xe theo Luật Giao thông đường bộ:\n"
         "- Tại nơi đường giao nhau và trên đường có phần đường (làn) dành cho người đi bộ cắt qua thì nghiêm cấm vượt xe.\n"
         "- Ngoài ra, tại đây còn có vạch tim đường nét liền màu vàng cấm lấn làn, đè vạch.\n"
         "Do đó người lái xe CẤM VƯỢT xe tải trong trường hợp này.",

    556: "Quy định cấm vượt xe theo Luật Giao thông đường bộ:\n"
         "- Tại nơi đường giao nhau (có cắm biển W.208 giao nhau với đường ưu tiên) và trên đường có làn dành cho người đi bộ cắt qua thì nghiêm cấm vượt xe.\n"
         "- Vượt xe tại nơi đường giao nhau và vạch đi bộ tiềm ẩn nguy cơ cao xảy ra va chạm và tai nạn giao thông.\n"
         "Do đó bạn KHÔNG ĐƯỢC VƯỢT xe mô tô phía trước.",

    557: "Phân tích phạm vi hiệu lực của biển cấm dừng đỗ kết hợp biển phụ:\n"
         "- Biển chính là biển P.130 'Cấm dừng xe và đỗ xe'.\n"
         "- Biển phụ S.508a đặt bên dưới có hình mũi tên chỉ về phía sau lưng biển (hướng xuống), biểu thị biển chỉ có hiệu lực CẤM Ở PHÍA SAU MẶT BIỂN (vị trí A).\n"
         "- Vị trí B và C nằm ở phía trước mặt biển, không thuộc phạm vi hiệu lực của biển cấm.\n"
         "Do đó người lái xe dừng đúng tại: Vị trí B và C.",

    558: "Phân tích phạm vi hiệu lực của biển cấm có biển phụ mũi tên hai đầu:\n"
         "- Biển P.130 'Cấm dừng xe và đỗ xe' có gắn kèm biển phụ S.508b vẽ mũi tên hai đầu (chỉ cả phía trước và phía sau).\n"
         "- Biển này có hiệu lực cấm dừng xe và đỗ xe ở CẢ PHÍA TRƯỚC VÀ PHÍA SAU vị trí cắm biển.\n"
         "- Vị trí A (sau biển) và vị trí B (trước biển) đều nằm trong phạm vi cấm.\n"
         "Do đó bạn KHÔNG ĐƯỢC DỪNG ở cả vị trí A và B.",

    559: "Xét hiệu lệnh của biển báo giao thông:\n"
         "- Phía trước ngã tư có cắm biển hiệu lệnh R.301a 'Các phương tiện chỉ được đi thẳng'.\n"
         "- Quan sát đèn tín hiệu của hai phương tiện:\n"
         "  + Xe con bật đèn xi-nhan bên trái chuẩn bị rẽ trái.\n"
         "  + Xe mô tô bật đèn xi-nhan bên phải chuẩn bị rẽ phải.\n"
         "Cả hai xe đều không tuân thủ hiệu lệnh chỉ được đi thẳng của biển báo R.301a.\n"
         "Do đó CẢ HAI XE ĐỀU VI PHẠM quy tắc giao thông.",

    560: "Xét đèn tín hiệu và chỉ dẫn hướng đi trên làn đường:\n"
         "- Xe khách ở làn trong cùng rẽ trái gặp đèn đỏ đang dừng lại -> Chấp hành đúng.\n"
         "- Xe con ở làn ngoài cùng rẽ phải có đèn xanh rẽ phải -> Rẽ phải đúng.\n"
         "- Xe tải ở làn giữa là làn đi thẳng có đèn xanh đi thẳng, nhưng xe lại rẽ trái đè sang làn khác -> Vi phạm hướng đi của làn đường.\n"
         "Do đó chỉ có duy nhất XE TẢI VI PHẠM.",

    561: "Xét hiệu lệnh đèn tín hiệu và mũi tên chỉ hướng làn đường:\n"
         "- Xe khách ở làn rẽ trái nhưng mũi tên lại đi thẳng -> Vi phạm hướng đi của làn đường.\n"
         "- Xe tải ở làn đi thẳng nhưng mũi tên lại rẽ trái -> Vi phạm hướng đi của làn đường.\n"
         "- Xe con rẽ phải đúng làn đèn xanh; xe mô tô chấp hành đúng.\n"
         "Do đó các xe vi phạm là: Xe khách, xe tải.",

    562: "Kiểm tra vi phạm theo tín hiệu đèn và hướng mũi tên:\n"
         "- Xe tải ở làn đi thẳng gặp đèn đỏ nhưng lại vượt đèn đỏ rẽ trái -> Vi phạm.\n"
         "- Xe khách ở làn rẽ trái gặp đèn xanh rẽ trái nhưng lại đi thẳng -> Vi phạm hướng làn.\n"
         "- Xe mô tô ở làn rẽ phải gặp đèn đỏ nhưng lại vượt đèn đỏ rẽ phải/trái -> Vi phạm.\n"
         "- Xe con đi đúng làn đèn xanh rẽ phải -> Chấp hành đúng.\n"
         "Vậy các xe vi phạm quy tắc giao thông gồm: Xe tải, xe khách, xe mô tô.",

    563: "Xét vi phạm hướng đi theo vạch chỉ hướng trên mặt đường:\n"
         "- Xe khách ở làn rẽ trái nhưng lại đi thẳng -> Vi phạm chỉ dẫn làn đường.\n"
         "- Xe tải ở làn đi thẳng nhưng lại rẽ trái -> Vi phạm chỉ dẫn làn đường.\n"
         "- Xe con ở làn rẽ phải, đi đúng theo hướng mũi tên rẽ phải -> Đúng.\n"
         "Do đó những xe vi phạm quy tắc giao thông là: Xe khách, xe tải.",

    564: "Kỹ năng xử lý an toàn khi gặp xe bị sự cố phía trước:\n"
         "Khi phát hiện xe tải phía trước bị hỏng đột xuất dừng đỗ trên làn đường của mình:\n"
         "1. Quan sát cẩn thận tình hình giao thông phía trước và phía sau qua gương chiếu hậu.\n"
         "2. Khi thấy đủ điều kiện an toàn (không có xe ngược chiều tới gần, không có xe phía sau vượt lên), bật tín hiệu xin vượt bằng đèn xi-nhan hoặc còi.\n"
         "3. Sau đó mới cho xe lách sang trái vượt qua xe hỏng an toàn.\n"
         "Đáp án đúng: Quan sát phía trước, phía sau, khi đủ điều kiện an toàn, bật tín hiệu bằng đèn hoặc còi rồi cho xe chạy vượt qua.",

    565: "Kiểm tra xe nào chấp hành đúng quy tắc giao thông:\n"
         "- Phía bên phải: Xe con ở làn rẽ phải gặp đèn đỏ nhưng rẽ phải là sai; Xe tải ở làn đi thẳng rẽ trái là sai.\n"
         "- Xe khách: Ở làn đi thẳng có đèn xanh đi thẳng -> Chấp hành đúng.\n"
         "- Xe mô tô: Ở làn rẽ phải có đèn xanh rẽ phải -> Chấp hành đúng.\n"
         "Do đó những xe chấp hành đúng quy tắc giao thông là: Xe khách, xe mô tô.",

    566: "Đối chiếu biển phân làn trên giá long môn với vị trí các xe:\n"
         "- Làn 1 (trái cùng): Làn dành cho xe ô tô tải và khách -> Xe con (B) đi vào làn này là SAI LÀN.\n"
         "- Làn 2: Làn dành cho xe ô tô con -> Xe con (A) đi đúng.\n"
         "- Làn 3: Làn dành cho xe ô tô con -> Xe con (C) và xe con (E) đi đúng.\n"
         "- Làn 4 (phải cùng): Làn dành cho xe mô tô -> Xe tải (D) đi vào làn mô tô là SAI LÀN.\n"
         "Vậy hai xe vi phạm quy tắc giao thông là: Xe tải (D), xe con (B).",

    567: "Phân tích biển báo ưu tiên tại ngã ba:\n"
         "- Phía trước xe của bạn có cắm biển tam giác ngược W.208 'Giao nhau với đường ưu tiên' kèm biển phụ S.506b thể hiện hướng đường ưu tiên bẻ cong từ nhánh xe mô tô sang nhánh đối diện. Xe của bạn đang ở đường không ưu tiên nên PHẢI ĐI CUỐI CÙNG.\n"
         "- Xe mô tô nằm trên trục đường ưu tiên, rẽ trái theo hướng đường ưu tiên nên được đi đầu tiên.\n"
         "- Xe con đi thẳng qua ngã ba đi thứ 2.\n"
         "Thứ tự đúng: Xe mô tô -> Xe con -> Xe của bạn.",

    568: "Áp dụng quy tắc ngã ba đồng cấp (không có biển báo, không có xe ưu tiên):\n"
         "Áp dụng quy tắc 'Bên phải không vướng' và hướng đi ưu tiên:\n"
         "1. Xe con màu xanh tím bên phải rẽ phải (hướng bên phải không vướng xe nào) -> Được quyền đi đầu tiên.\n"
         "2. Sau khi xe con đã đi qua, hướng bên phải của xe bạn hoàn toàn trống -> Xe của bạn đi thẳng đi thứ 2.\n"
         "3. Xe mô tô rẽ trái đi sau cùng (thứ 3).\n"
         "Thứ tự đúng: Xe con -> Xe của bạn -> Xe mô tô.",

    569: "Quan sát tín hiệu đèn giao thông từ vị trí lái xe:\n"
         "- Xe ô tô con màu xanh phía trước đang đi thẳng tới ngã tư có cột tín hiệu ĐÈN ĐỎ -> Bắt buộc xe con phải dừng lại trước vạch dừng.\n"
         "- Xe của bạn đang ở nhánh rẽ phải có làn rẽ riêng không bị khống chế bởi đèn đỏ đi thẳng, mũi tên chỉ dẫn rẽ phải.\n"
         "Do đó xe phải dừng lại trong trường hợp này là: XE CON.",

    570: "Phân tích vạch sơn chỉ hướng trên mặt đường làn xe bạn đang chạy:\n"
         "- Tại giao lộ, làn đường xe bạn đang đứng có kẻ vạch sơn màu trắng kết hợp hình mũi tên: ĐI THẲNG VÀ RẼ TRÁI.\n"
         "- Đèn tín hiệu giao thông đang bật màu xanh.\n"
         "Do đó xe của bạn được phép đi theo hướng: ĐI THẲNG, RẼ TRÁI.",

    571: "Xử lý tình huống theo vạch kẻ đường và đèn tín hiệu:\n"
         "- Xe của bạn đang dừng ở làn đường có mũi tên chỉ hướng đi thẳng hoặc rẽ trái.\n"
         "- Cột đèn tín hiệu chính đang bật ĐÈN ĐỎ (chỉ có đèn phụ mũi tên màu xanh rẽ phải là sáng cho làn rẽ phải).\n"
         "- Vì bạn đang ở làn đi thẳng/rẽ trái nên không được rẽ phải và không được vượt đèn đỏ.\n"
         "Cách xử lý đúng: Dừng lại trước vạch dừng và đi thẳng hoặc rẽ trái khi đèn xanh.",

    572: "Kỹ năng nhường đường khi rẽ phải tại nơi giao nhau:\n"
         "- Xe của bạn chuẩn bị rẽ phải vào đường cắt ngang.\n"
         "- Trên đường cắt ngang, xe tải và người đi xe đạp đang đi thẳng trên làn đường thông suốt.\n"
         "- Khi chuyển hướng rẽ phải, bạn bắt buộc phải nhường đường cho các phương tiện đang đi thẳng trên trục đường chính.\n"
         "Cách xử lý đúng: Giảm tốc độ, rẽ phải sau xe tải và xe đạp.",

    573: "Kỹ năng nhường đường cho người đi bộ và phương tiện chuyển hướng:\n"
         "- Phía trước đầu xe có người đi bộ đang qua đường trên vạch kẻ đường dành cho người đi bộ.\n"
         "- Xe con màu xanh phía trước đã nhập vào ngã rẽ trước.\n"
         "- Người lái xe phải luôn chấp hành quy tắc an toàn: Nhường đường cho người đi bộ qua đường trước, sau đó rẽ theo sau xe con màu xanh.\n"
         "Cách xử lý đúng: Giảm tốc độ, để người đi bộ qua đường và rẽ phải sau xe con màu xanh.",

    574: "Áp dụng quy tắc hướng rẽ ưu tiên tại ngã tư đồng cấp:\n"
         "- Xe của bạn chuẩn bị rẽ trái tại ngã tư.\n"
         "- Phía đối diện có người đi xe đạp đi thẳng và xe ô tô khách rẽ phải.\n"
         "- Theo quy tắc hướng đi ưu tiên ('Phải > Thẳng > Trái'): Xe rẽ phải (xe khách) và xe đi thẳng (xe đạp) đều có quyền đi trước xe rẽ trái (xe bạn).\n"
         "Do đó bạn phải: Nhường đường cho xe đạp và xe khách.",

    575: "Phân tích biển báo ưu tiên và hướng đi:\n"
         "- Phía trước xe của bạn có cắm biển W.207 'Giao nhau với đường không ưu tiên' (bạn đang trên đường ưu tiên).\n"
         "- Xe con phía trước đi thẳng trên cùng trục đường ưu tiên.\n"
         "- Xe tải từ đường nhánh bên trái có cắm biển tam giác ngược W.208 'Giao nhau với đường ưu tiên' và đang rẽ trái.\n"
         "Do đó phương tiện ở đường nhánh là XE TẢI PHẢI NHƯỜNG ĐƯỜNG.",

    576: "Quy tắc tránh nhau nơi có chướng ngại vật:\n"
         "- Luật Giao thông đường bộ quy định: 'Nơi đường hẹp hoặc có chướng ngại vật, xe có chướng ngại vật phía trước phải nhường đường cho xe không có chướng ngại vật đi trước'.\n"
         "- Phía trước làn đường của xe bạn có rào chắn thi công công trường (chướng ngại vật).\n"
         "- Xe đi ngược chiều đang lưu thông thuận lợi trên làn đường thông suốt.\n"
         "Do đó XE CỦA BẠN PHẢI NHƯỜNG ĐƯỜNG cho xe ngược chiều đi qua trước.",

    577: "Quy định bảo đảm an toàn với đoàn người có tổ chức:\n"
         "- Luật Giao thông đường bộ nghiêm cấm: Xe cơ giới không được vượt các đoàn xe tang, đoàn người đi bộ hoặc đoàn người đi xe đạp có tổ chức diễu hành.\n"
         "- Việc cố tình lấn làn vượt qua đoàn người đông đúc tiềm ẩn nguy cơ tai nạn giao thông rất lớn.\n"
         "Do đó bạn xử lý: Không được vượt những người đi xe đạp.",

    578: "Kỹ năng xử lý tình huống linh hoạt khi phía trước có chướng ngại vật:\n"
         "Khi phát hiện xe phía trước đang lùi vào nơi đỗ và xe con đang lách sang làn trái để vượt qua:\n"
         "- Ý 1: Nếu quan sát gương chiếu hậu phía sau an toàn (không có xe xin vượt), bạn bật tín hiệu chuyển sang làn đường bên trái để tiếp tục di chuyển.\n"
         "- Ý 2: Nếu phía sau có xe đang xin vượt thì phải chủ động giảm tốc độ, giữ làn đường và dừng lại khi cần thiết để bảo đảm an toàn.\n"
         "Đáp án đúng: Ý 1 và ý 2.",

    579: "Kỹ năng phòng ngừa nguy hiểm khi xe khác lùi ra khỏi nơi đỗ:\n"
         "- Xe ô tô phía trước đang lùi từ trong nhà/nơi đỗ ra đường thường có tầm nhìn bị hạn chế và phần đuôi xe chiếm dụng lòng đường.\n"
         "- Người lái xe đến gần phải chủ động phán đoán nguy hiểm, giảm tốc độ và dừng lại nhường đường nếu cần thiết để tránh va chạm.\n"
         "Đáp án đúng: Giảm tốc độ, dừng lại nhường đường.",

    580: "Xử lý khẩn cấp khi xe ngược chiều lấn làn vượt ẩu:\n"
         "- Xe màu xanh đi ngược chiều đang lấn hẳn sang làn đường của bạn để vượt xe tải/xe vàng.\n"
         "- Tình huống đối đầu trực diện cực kỳ nguy hiểm trong tích tắc.\n"
         "- Biện pháp duy nhất an toàn: Lập tức phanh xe giảm tốc độ và chủ động đánh lái nép sát lề đường bên phải để nhường đường và tránh va chạm trực diện.\n"
         "Đáp án đúng: Phanh xe giảm tốc độ và đi sát lề đường bên phải.",

    581: "Kỹ năng ứng xử khi xe tải phía trước xin chuyển làn:\n"
         "- Xe tải phía trước đã bật đèn xi-nhan xin chuyển làn đường sang bên phải/trái.\n"
         "- Do xe tải có kích thước lớn và điểm mù rộng, việc bấm còi cố vượt hoặc đánh lái lấn làn vượt gấp là rất nguy hiểm.\n"
         "- Cách xử lý an toàn chuẩn mực: Phanh xe giảm tốc độ, giữ khoảng cách an toàn chờ xe tải phía trước chuyển làn hoàn tất rồi mới tiếp tục hành trình.\n"
         "Đáp án đúng: Phanh xe giảm tốc độ chờ xe tải phía trước chuyển làn đường.",

    582: "Kỹ năng điều khiển xe qua ngã tư khi đèn xanh:\n"
         "- Dù đèn tín hiệu đang xanh và phía trước giao lộ tương đối thông thoáng, người lái xe vẫn phải tuân thủ nguyên tắc an toàn cơ bản:\n"
         "- Không được chủ quan tăng tốc độ phóng nhanh qua ngã tư; cần chủ động giảm tốc độ, quan sát xung quanh đề phòng các phương tiện vượt ẩu từ đường nhánh rồi mới đi thẳng qua.\n"
         "Đáp án đúng: Giảm tốc độ và đi thẳng qua ngã tư.",

    583: "Áp dụng quy tắc hướng đi ưu tiên tại ngã ba đồng cấp:\n"
         "- Ngã ba cùng cấp không có biển báo hiệu, áp dụng thứ tự ưu tiên hướng đi ('Phải > Thẳng > Trái'):\n"
         "  1. Người đi xe đạp rẽ phải -> Được đi đầu tiên.\n"
         "  2. Xe mô tô đi thẳng -> Được đi thứ 2.\n"
         "  3. Xe của bạn rẽ trái (bật đèn xi-nhan trái) -> Đi sau cùng (thứ 3).\n"
         "Thứ tự đúng: Xe đạp -> Xe mô tô -> Xe của bạn.",

    584: "Phân tích biển báo ưu tiên và hướng đi của xe:\n"
         "- Trước mặt xe của bạn có cắm biển hình thoi I.401 'Bắt đầu đường ưu tiên' kèm biển phụ S.506b thể hiện đường ưu tiên rẽ trái. Xe của bạn bật xi-nhan rẽ trái đi theo đúng hướng đường ưu tiên nên ĐƯỢC QUYỀN ĐI ĐẦU TIÊN (thứ 1).\n"
         "- Giữa xe con và xe tải: Xe con rẽ phải đi thứ 2; xe tải ở đường không ưu tiên đi sau cùng (thứ 3).\n"
         "Thứ tự đúng: Xe của bạn -> Xe con -> Xe tải.",

    585: "Phân tích biển báo ưu tiên tại nơi giao nhau:\n"
         "- Phía trước xe của bạn có cắm biển tam giác ngược W.208 'Giao nhau với đường ưu tiên' kèm biển phụ S.506b chỉ hướng ưu tiên cong sang nhánh bên trái. Bạn đang ở trên đường nhánh không ưu tiên.\n"
         "- Xe con màu xanh đang lưu thông trên trục đường chính ưu tiên.\n"
         "Do đó XE CỦA BẠN PHẢI NHƯỜNG ĐƯỜNG cho xe con đi trước.",

    586: "Phân tích biển báo qua đoạn đường hẹp chui qua hầm:\n"
         "- Xe của bạn đang tiến đến hầm chui đường bộ qua cầu hẹp.\n"
         "- Bên phải xe của bạn có cắm biển P.132 'Nhường đường cho xe cơ giới đi ngược chiều qua đường hẹp' (biển tròn viền đỏ, mũi tên màu đỏ bên phải chỉ chiều xe của bạn).\n"
         "- Xe ô tô con màu đỏ ở chiều ngược lại có biển ưu tiên qua đường hẹp I.406.\n"
         "Do đó XE CỦA BẠN PHẢI NHƯỜNG ĐƯỜNG cho xe con đi qua hầm trước.",

    587: "Kỹ năng nhường đường cho người đi bộ qua đường:\n"
         "- Luật Giao thông đường bộ quy định: Tại nơi có vạch kẻ đường dành cho người đi bộ, người lái xe phải quan sát, giảm tốc độ và nhường đường cho người đi bộ đang qua đường.\n"
         "- Trong hình, người đi bộ đang bước trên vạch qua đường ngay trước mũi xe của bạn.\n"
         "Cách xử lý đúng: Giảm tốc độ, để người đi bộ sang đường trước, sau đó cho xe đi qua vạch người đi bộ sang đường.",

    588: "Phân tích biển báo đường ưu tiên:\n"
         "- Phía trước xe của bạn có cắm biển W.207 'Giao nhau với đường không ưu tiên' (đỉnh tam giác hướng lên trên), báo hiệu xe bạn đang lưu thông trên đường ưu tiên.\n"
         "- Xe con màu vàng đi từ đường nhánh ra (gặp biển tam giác ngược W.208) phải nhường đường cho xe trên đường ưu tiên.\n"
         "Do đó XE CỦA BẠN ĐƯỢC ĐI TRƯỚC xe con.",

    589: "Áp dụng quy tắc 'Bên phải không vướng' tại ngã tư đồng cấp:\n"
         "- Nơi giao nhau không có biển báo, không có xe ưu tiên, các phương tiện cùng cấp.\n"
         "- Hướng đi của các xe: Xe tải đi thẳng, xe con đi thẳng, xe của bạn rẽ trái (đèn xi-nhan trái bật sáng).\n"
         "- Xét quyền ưu tiên bên phải:\n"
         "  1. Phía bên phải của Xe tải (nhánh đường bên trái xe bạn) hoàn toàn trống -> Xe tải đi đầu tiên.\n"
         "  2. Sau khi xe tải đi qua, phía bên phải của Xe con không còn vướng -> Xe con đi thứ 2.\n"
         "  3. Sau khi xe con đi qua, bên phải xe của bạn thông thoáng. Đồng thời xe của bạn rẽ trái nên đi sau cùng.\n"
         "Thứ tự đúng: Xe tải -> Xe con -> Xe của bạn.",

    590: "Kỹ năng xử lý an toàn khi gặp xe ngược chiều và người đi xe đạp cùng chiều:\n"
         "- Phía trước có xe ô tô ngược chiều đang tiến tới và có người đi xe đạp cùng chiều bên phải.\n"
         "- Mặt đường hẹp không đủ điều kiện để lấn làn vượt xe đạp mà không đối đầu với xe ngược chiều.\n"
         "- Biện pháp an toàn duy nhất: Giảm tốc độ, không lấn làn, đi nối đuôi sát về phần đường bên phải phía sau xe đạp cho đến khi xe ngược chiều đi qua an toàn.\n"
         "Đáp án đúng: Giảm tốc độ cho xe đi sát phần đường bên phải.",

    591: "Quy tắc hướng đi ưu tiên tại nơi có đèn tín hiệu giao thông:\n"
         "- Cả xe tải và xe của bạn đều đang gặp tín hiệu ĐÈN XANH nên đều được phép di chuyển.\n"
         "- Xe tải đi thẳng qua ngã tư.\n"
         "- Xe của bạn rẽ trái (đèn xi-nhan trái bật sáng).\n"
         "- Theo quy tắc hướng đi: Xe đi thẳng có quyền ưu tiên cao hơn xe rẽ trái.\n"
         "Do đó XE TẢI ĐƯỢC ĐI TRƯỚC xe của bạn.",

    592: "Quy tắc khoảng cách dừng đỗ an toàn trước đường sắt:\n"
         "- Luật Giao thông đường bộ quy định: Khi qua nơi đường bộ giao nhau với đường sắt không có rào chắn, người lái xe phải dừng xe cách đường ray gần nhất TỐI THIỂU 5 MÉT.\n"
         "- Xe con dừng cách đường ray 6 mét (6m > 5m) -> Đảm bảo khoảng cách an toàn, DỪNG ĐÚNG.\n"
         "- Xe mô tô dừng cách đường ray 3 mét (3m < 5m) -> Vi phạm khoảng cách an toàn tối thiểu, DỪNG SAI.\n"
         "Do đó chỉ có duy nhất XE CON DỪNG ĐÚNG.",

    593: "Áp dụng quy tắc 'Bên phải không vướng' tại ngã ba đồng cấp:\n"
         "- Ngã ba cùng cấp không có biển báo hiệu, áp dụng thứ tự ưu tiên:\n"
         "  1. Hướng bên phải của xe bạn hoàn toàn trống (không có đường, không có xe) -> Xe của bạn đi thẳng ĐƯỢC ĐI ĐẦU TIÊN.\n"
         "  2. Sau khi xe của bạn đã đi qua, hướng bên phải của xe tải trở nên thông thoáng -> Xe tải rẽ phải đi thứ 2.\n"
         "  3. Xe đạp rẽ trái đi sau cùng (thứ 3).\n"
         "Thứ tự đúng: Xe của bạn -> Xe tải -> Xe đạp.",

    594: "Quy tắc mở cua an toàn khi rẽ trái tại ngã ba:\n"
         "- Luật Giao thông đường bộ quy định: Khi rẽ trái, người lái xe phải cho xe chạy chậm và mở cua rộng tại tâm đường, không được cắt xéo góc cua lấn sang phần đường xe ngược chiều.\n"
         "- Hướng 1: Xe chạy đúng phần đường bên phải, đến điểm giao cắt rồi mới rẽ trái an toàn.\n"
         "- Hướng 2: Cắt xéo góc cua, chạy thẳng vào làn đường của xe đi ngược chiều cực kỳ nguy hiểm.\n"
         "Do đó để điều khiển xe rẽ trái, bạn chọn: HƯỚNG 1.",

    595: "Kỹ năng ứng phó khi bị xe ngược chiều rọi đèn pha chói mắt:\n"
         "- Khi lái xe ban đêm bị đèn pha (chiếu xa) của xe ngược chiều chiếu thẳng vào mắt gây lóa tầm nhìn:\n"
         "- Tuyệt đối không bật đèn pha trả đũa hay tăng tốc vượt xe cùng chiều vì không quan sát được chướng ngại vật.\n"
         "- Biện pháp đúng: Giữ nguyên đèn chiếu gần (cốt), giảm tốc độ xe chạy và đi an toàn phía sau xe cùng chiều phía trước.\n"
         "Đáp án đúng: Giữ nguyên đèn chiếu gần, giảm tốc độ, đi sau xe phía trước.",

    596: "Quy tắc an toàn tại nơi đường sắt giao nhau khi rào chắn đang dịch chuyển:\n"
         "- Luật Giao thông đường bộ quy định: Khi có chuông báo hiệu hoặc rào chắn đang dịch chuyển đóng lại, tất cả người tham gia giao thông phải dừng lại ở phần đường của mình và trước rào chắn một khoảng cách an toàn, cấm vượt qua.\n"
         "- Tuyệt đối không được cố tăng ga phóng qua hay nhờ người gác chắn kéo chậm barie.\n"
         "Đáp án đúng: Dừng lại trước rào chắn một khoảng cách an toàn.",

    597: "Quy tắc nhập làn đường cao tốc an toàn:\n"
         "- Khi nhập vào đường cao tốc, xe phải chạy trên làn đường tăng tốc đến khi đạt tốc độ lưu thông quy định, quan sát an toàn và nhường đường cho các xe đang chạy trên đường cao tốc rồi mới chuyển làn tại đoạn vạch nét đứt.\n"
         "- Trong hình, xe con màu đỏ nhập làn cắt xéo góc đè qua vạch xương cá (vạch kênh hóa dòng xe) và vạch liền, tạt đầu xe khác trên cao tốc là vi phạm nghiêm trọng quy tắc an toàn.\n"
         "Đáp án đúng: SAI.",

    598: "Quy tắc an toàn cấm vượt xe đang vượt:\n"
         "- Luật Giao thông đường bộ nghiêm cấm hành vi: 'Cấm vượt xe khi xe phía trước đang vượt xe khác' (tránh tình huống 3 xe dàn hàng ngang chiếm hết lòng đường).\n"
         "- Trong hình, xe con màu xanh đang lấn sang làn bên cạnh để vượt xe tải thùng phía trước.\n"
         "- Xe con màu đỏ đi sau tuyệt đối không được phép vượt xe con màu xanh lúc này.\n"
         "Đáp án đúng: Không được vượt.",

    599: "Phân tích vạch kẻ đường và hành vi vượt xe an toàn:\n"
         "- Vạch phân chia hai chiều xe chạy là VẠCH NÉT ĐỨT MÀU VÀNG (vạch 1.1), cho phép phương tiện đè vạch để vượt khi an toàn.\n"
         "- Xe con màu vàng đã bật đèn xi-nhan xin vượt, phía trước làn đối diện có xe ô tô màu xanh ở khoảng cách rất xa, bảo đảm an toàn.\n"
         "Do đó hành vi vượt của xe con màu vàng là ĐÚNG quy tắc giao thông.",

    600: "Hiểu rõ góc quét đuôi và điểm mù của xe container/xe siêu trường:\n"
         "- Xe đầu kéo sơ mi rơ-moóc (container) có chiều dài cơ sở rất lớn. Khi chuyển hướng rẽ phải, đầu xe phải mở rộng vòng cua sang trái và phần đuôi rơ-moóc sẽ quét hẹp bó sát vỉa hè, tạo ra vùng điểm mù khổng lồ và góc kẹt nguy hiểm.\n"
         "- Xe con màu xanh và xe máy nếu cố vượt lên (dù bên trái hay bên phải) đều có nguy cơ bị cuốn vào gầm hoặc bị ép chèn vào lề đường.\n"
         "Cách xử lý an toàn: Giảm tốc độ chờ xe container rẽ xong rồi tiếp tục đi."
}
