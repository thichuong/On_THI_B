# scripts/explanations/part10.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 486 đến Câu 540
Chương 6: Giải thế sa hình và kỹ năng xử lý tình huống (Phần 1)
"""

PART10_EXPLANATIONS = {
    486: "Xét theo đèn và hướng mũi tên: Xe con ở làn rẽ phải có đèn xanh và rẽ phải -> đúng. Xe khách ở làn rẽ trái nhưng đi thẳng -> sai. Xe tải ở làn đi thẳng nhưng rẽ trái -> sai. Xe mô tô vượt đèn đỏ -> sai. Do đó CHỈ CÓ XE CON chấp hành đúng quy tắc giao thông.",
    
    487: "Áp dụng thứ tự ưu tiên: 1. Xe ưu tiên (xe công an) được đi trước tiên; 2. Tiếp theo xét biển báo: xe con nằm trên đường ưu tiên nên được đi thứ hai; 3. Xe tải và xe khách nằm trên đường không ưu tiên đi sau.",
    
    488: "Thứ tự sa hình: 1. Xe công an (xe ưu tiên) đi đầu tiên; 2. Xe con nằm trên đường ưu tiên (biển hình thoi) đi thứ hai; 3. Xe tải đi thẳng đi thứ ba; 4. Xe khách rẽ trái đi cuối cùng.",
    
    489: "Thứ tự đi: 1. Xe công an là xe ưu tiên đi trước tiên; 2. Xe tải đi trên đường ưu tiên đi thứ hai; 3. Xe khách và xe con cùng ở đường không ưu tiên, xe khách đi thẳng đi trước, xe con rẽ trái đi sau cùng.",
    
    490: "Ngã tư không có biển báo (đồng cấp): Áp dụng quy tắc 'Bên phải không vướng' -> Xe mô tô bên phải không vướng đi đầu tiên; sau khi mô tô đi thì bên phải xe con trống nên xe con đi thứ hai; cuối cùng là xe tải.",
    
    491: "Xét biển báo: Xe con gặp biển tam giác ngược W.208 'Giao nhau với đường ưu tiên', do đó xe con đang ở trên đường không ưu tiên và PHẢI NHƯỜNG ĐƯỜNG cho xe tải.",
    
    492: "Xét biển báo: Xe con nằm trên đường ưu tiên (biển hình thoi kèm biển phụ hướng đường ưu tiên rẽ trái). Xe mô tô gặp biển tam giác ngược W.208 (đường nhánh) phải nhường đường. Do đó xe con được quyền đi trước.",
    
    493: "Thứ tự sa hình: 1. Xe con (A) đã CHỚM VÀO GIAO LỘ trước nên được quyền đi trước tiên ('Nhất chớm'); 2. Tiếp theo là xe cứu thương (xe ưu tiên); 3. Cuối cùng là xe con (B).",
    
    494: "Thứ tự ưu tiên xe ưu tiên: 'HỎA - SỰ - CÔNG - THƯƠNG' -> Xe chữa cháy có quyền ưu tiên cao hơn xe cứu thương. Do đó thứ tự là: Xe chữa cháy -> Xe cứu thương -> Xe con.",
    
    495: "Quyền ưu tiên: Xe cứu thương đang đi làm nhiệm vụ cấp cứu là xe ưu tiên theo luật định, được quyền đi trước xe mô tô.",
    
    496: "Xét biển báo: Xe tải và xe con nằm trên đường ưu tiên đi trước. Xe khách nằm trên đường không ưu tiên (gặp biển tam giác ngược W.208) nên PHẢI NHƯỜNG ĐƯỜNG ĐI CUỐI CÙNG.",
    
    497: "Tại nơi giao nhau: Xe con gặp biển tam giác ngược W.208 'Giao nhau với đường ưu tiên', do đó xe con bắt buộc PHẢI NHƯỜNG ĐƯỜNG cho xe tải.",
    
    498: "Thứ tự xe ưu tiên theo Luật: Xe chữa cháy đi làm nhiệm vụ chữa cháy được quyền ưu tiên đi trước xe công an đi làm nhiệm vụ khẩn cấp ('Hỏa đứng trước Công').",
    
    499: "Nhìn tín hiệu đèn giao thông: Hướng của xe con và xe khách có ĐÈN XANH nên được phép đi. Hướng xe mô tô có ĐÈN ĐỎ phải dừng lại.",
    
    500: "Xét tín hiệu đèn và hướng mũi tên: Làn xe con có đèn xanh rẽ phải -> đúng. Làn xe tải có đèn đỏ dừng lại -> đúng. Làn xe khách đèn đỏ nhưng vượt -> sai. Do đó xe con và xe tải đi đúng quy tắc giao thông.",
    
    501: "Thứ tự xe ưu tiên: Xe quân sự đi làm nhiệm vụ khẩn cấp có quyền ưu tiên đi trước xe công an ('Hỏa - Sự - Công - Thương').",
    
    502: "Nhìn đèn tín hiệu và biển báo: Làn xe tải có đèn xanh phụ hình mũi tên rẽ phải (hướng 1). Đèn chính màu đỏ cấm đi thẳng. Do đó xe tải CHỈ ĐƯỢC ĐI THEO HƯỚNG 1.",
    
    503: "Xét vi phạm: Xe khách ở làn rẽ trái nhưng đi thẳng -> vi phạm. Xe tải ở làn đi thẳng nhưng rẽ trái -> vi phạm. Xe mô tô ở làn rẽ phải nhưng rẽ trái -> vi phạm. Xe con rẽ phải đúng làn đèn xanh. Vậy các xe vi phạm là: Xe khách, xe tải, xe mô tô.",
    
    504: "Thứ tự đi: 1. Xe mô tô rẽ phải đi đầu tiên ('ngũ hướng: phải - thẳng - trái'); 2. Xe tải đi thẳng đi thứ hai; 3. Xe khách rẽ trái đi thứ ba; 4. Xe con quay đầu đi cuối cùng.",
    
    505: "Xét biển báo cấm đỗ xe: Có biển phụ vẽ hình ô tô tải bên dưới, nghĩa là biển này CHỈ CẤM RIÊNG XE TẢI ĐỖ. Xe con và mô tô đỗ bình thường. Do đó chỉ có XE TẢI ĐỖ VI PHẠM.",
    
    506: "Tại ngã tư đồng cấp: Cả 3 xe đều rẽ, áp dụng quy tắc bên phải không vướng -> Bên phải xe con (B) không có xe (trống) nên XE CON (B) ĐƯỢC ĐI TRƯỚC; tiếp theo xe con (A), cuối cùng là xe tải.",
    
    507: "Biển 2 cấm xe mô tô (không cấm xe gắn máy). Biển 3 cấm xe ô tô. Xe gắn máy (dưới 50 cm3) không bị cấm bởi cả 3 biển, do đó XE GẮN MÁY ĐƯỢC PHÉP ĐI CẢ 3 HƯỚNG.",
    
    508: "Biển cấm dừng và cấm đỗ xe (hai vạch đỏ) có biển phụ mũi tên hai đầu (chỉ cả trước và sau biển): Cấm dừng đỗ ở cả trước và sau vị trí đặt biển. Do đó CẢ HAI XE (xe tải và xe mô tô) ĐỀU ĐỖ VI PHẠM.",
    
    509: "Biển cấm đỗ xe có biển phụ xe tải: cấm xe tải đỗ -> xe tải vi phạm. Xe con và xe mô tô đỗ trên vạch kẻ đường dành cho người đi bộ qua đường -> vi phạm luật dừng đỗ. Do đó CẢ BA XE ĐỀU VI PHẠM.",
    
    510: "Luật giao thông nghiêm cấm xe ô tô đang kéo một xe khác lại kéo thêm rơ moóc hoặc kéo phương tiện thứ hai. Do đó xe tải kéo xe mô tô ba bánh như hình là KHÔNG ĐÚNG quy tắc giao thông.",
    
    511: "Tại ngã tư có cắm biển R.301 'Hướng đi thẳng và rẽ phải phải theo'. Hướng 1 là hướng quay đầu xe ngược lại không nằm trong hiệu lệnh, do đó CHỈ HƯỚNG 1 LÀ KHÔNG ĐƯỢC PHÉP ĐI.",
    
    512: "Hướng 3 có cắm biển P.102 'Cấm đi ngược chiều'. Do đó xe ô tô KHÔNG ĐƯỢC PHÉP ĐI VÀO HƯỚNG 3.",
    
    513: "Xét vạch kẻ đường: Vạch tim đường là VẠCH NÉT ĐỨT, cả xe con và xe khách đều vượt mà không có xe chạy ngược chiều và không vi phạm biển cấm, do đó CẢ HAI XE ĐỀU VƯỢT ĐÚNG.",
    
    514: "Biển R.301 đặt trước ngã tư là biển hiệu lệnh: Bắt buộc xe chỉ được phép đi theo HƯỚNG 2 (đi thẳng) HOẶC HƯỚNG 3 (rẽ trái), cấm rẽ phải sang hướng 1.",
    
    515: "Biển báo cấm xe ô tô kéo rơ moóc đặt ở đầu đường: Xe tải đang kéo theo một xe khác đi vào đoạn đường có biển này là VI PHẠM quy tắc giao thông.",
    
    516: "Xe khách đi trên đường có chướng ngại vật phía trước (chiếc xe con bị hỏng) nên bắt buộc PHẢI NHƯỜNG ĐƯỜNG cho xe tải đi ngược chiều đang lưu thông thuận lợi.",
    
    517: "Xe con rẽ trái phải nhường đường cho XE MÔ TÔ ĐI THẲNG. Theo quy tắc hướng đi ưu tiên (Phải - Thẳng - Trái), xe đi thẳng được quyền đi trước xe rẽ trái.",
    
    518: "Đoạn đường có cắm biển P.103a 'Cấm xe ô tô kéo rơ moóc'. Việc xe ô tô tải kéo theo xe khác đi vào đường này là KHÔNG ĐÚNG quy định.",
    
    519: "Hướng 2 có biển cấm xe ô tô con đi vào. Các hướng 1 (rẽ phải), hướng 3 (rẽ trái) và hướng 4 (quay đầu) không có biển cấm. Do đó xe con ĐƯỢC PHÉP ĐI CÁC HƯỚNG 1, 3 VÀ 4.",
    
    520: "Tại ngã tư đồng cấp: 1. Xe mô tô và xe đạp rẽ phải đi đầu tiên; 2. Xe con (A) đi thẳng đi thứ hai; 3. Xe con (B) rẽ trái đi sau cùng. Thứ tự: Xe mô tô + xe đạp -> Xe con (A) -> Xe con (B).",
    
    521: "Biển hiệu lệnh R.301 đặt dưới có biển phụ vẽ xe tải: Biển này chỉ có hiệu lực với xe tải, bắt buộc xe tải CHỈ ĐƯỢC PHÉP ĐI THEO HƯỚNG 1 (rẽ phải).",
    
    522: "Hướng 1 có biển cấm xe tải. Hướng 2 và hướng 3 không có biển cấm. Do đó xe tải ĐƯỢC PHÉP ĐI HƯỚNG 2 VÀ HƯỚNG 3.",
    
    523: "Hướng 2 có biển cấm xe ô tô con (cấm luôn xe tải). Hướng 3 cấm xe tải. Hướng 4 cấm máy kéo (không cấm tải). Hướng 1 và hướng 5 không có biển cấm. Do đó xe tải ĐƯỢC PHÉP ĐI HƯỚNG 1 VÀ HƯỚNG 5.",
    
    524: "Hướng 2 có cấm xe tải (biển cấm máy kéo kéo moóc và biển cấm xe tải). Các hướng 1, 3, 4 đều được phép đi. Do đó xe tải được đi các hướng TRỪ HƯỚNG 2.",
    
    525: "Tại ngã ba: Xe mô tô đi trên đường ưu tiên (biển hình thoi) nên ĐƯỢC QUYỀN ĐI TRƯỚC xe con (gặp biển tam giác ngược phải nhường).",
    
    526: "Biển R.301 hiệu lệnh bắt buộc các xe 'Chỉ được đi thẳng'. Xe ô tô con rẽ sang đường hoặc quay đầu là VI PHẠM quy tắc giao thông.",
    
    527: "Vạch tim đường phân làn là VẠCH LIỀN NÉT MÀU VÀNG. Xe con vượt xe tải mà đè qua vạch liền là VI PHẠM QUY TẮC GIAO THÔNG.",
    
    528: "Hiệu lệnh CSGT giơ tay thẳng đứng: TẤT CẢ CÁC XE Ở MỌI HƯỚNG PHẢI DỪNG LẠI trước ngã tư, chỉ những xe đã chớm vào trong ngã tư mới được phép tiếp tục đi.",
    
    529: "Hiệu lệnh CSGT giang hai tay sang ngang: Các xe ở phía bên phải và bên trái của người điều khiển giao thông (xe mô tô và xe tải) ĐƯỢC PHÉP ĐI; các xe ở phía trước và sau phải dừng lại.",
    
    530: "Xe tải phía trước đang có tín hiệu rẽ trái và đang rẽ trái sang làn bên kia đường, để lại khoảng trống an toàn bên phải. Xe con vượt lên bên phải trong trường hợp này là ĐÚNG quy tắc giao thông.",
    
    531: "Xe con vượt xe tải ở đoạn đường vạch tim nét đứt -> đúng. Xe tải vượt xe khách đè lên vạch tim nét liền -> sai. Do đó CHỈ CÓ XE CON VƯỢT ĐÚNG.",
    
    532: "Xe chữa cháy là xe ưu tiên cao nhất, được phép đi vào đường ngược chiều. Xe tải đi vào đường cấm là VI PHẠM quy tắc giao thông.",
    
    533: "Quy tắc hướng đi (Phải - Thẳng - Trái): 1. Xe tải rẽ phải đi trước; 2. Xe khách đi thẳng đi thứ hai; 3. Xe con rẽ trái đi sau cùng. Thứ tự: Xe tải -> Xe khách -> Xe con.",
    
    534: "Xe khách và xe tải đều đi trên đường ưu tiên: Xe khách đi thẳng và xe tải rẽ phải đi đồng thời trước tiên; xe con đi trên đường không ưu tiên đi sau cùng.",
    
    535: "Hướng 4 có biển cấm ô tô tải rẽ phải. Hướng 1 (quay đầu), hướng 2 (đi thẳng), hướng 3 (rẽ trái) không bị cấm. Do đó xe tải ĐƯỢC ĐI CÁC HƯỚNG TRỪ HƯỚNG 4.",
    
    536: "Thứ tự đi: 1. Xe công an (ưu tiên) đi đầu tiên; 2. Xe con đi thẳng trên đường ưu tiên đi thứ hai; 3. Xe tải đi thẳng đi thứ ba; 4. Xe khách rẽ trái đi sau cùng.",
    
    537: "Hướng 2 có biển cấm xe tải. Các hướng 1, 3, 4 không có biển cấm xe tải. Do đó xe tải ĐƯỢC PHÉP ĐI CÁC HƯỚNG 1, 3 VÀ 4.",
    
    538: "Quan sát đèn và hướng xe: Xe khách đèn xanh rẽ trái -> đúng; xe tải đèn đỏ dừng lại -> đúng; xe con đèn xanh rẽ phải -> đúng; xe mô tô dừng đèn đỏ -> đúng. Do đó TẤT CẢ CÁC LOẠI XE TRÊN đều chấp hành đúng.",
    
    539: "Hướng 2 có biển cấm mô tô. Hướng 1 và hướng 3 không bị cấm. Do đó xe mô tô ĐƯỢC PHÉP ĐI HƯỚNG 1 VÀ HƯỚNG 3.",
    
    540: "Thứ tự xe ưu tiên: Xe quân sự được quyền ưu tiên đi trước xe công an ('Quân sự trước Công an'). Sau đó xe con và xe mô tô đi cùng lúc. Thứ tự: Xe quân sự -> Xe công an -> Xe con + xe mô tô."
}

