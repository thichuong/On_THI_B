# scripts/explanations/part11.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 541 đến Câu 600
Chương 6: Giải thế sa hình và kỹ năng xử lý tình huống (Phần 2)
"""

PART11_EXPLANATIONS = {
    541: "Xe A đang chuẩn bị chuyển làn đường hoặc vượt xe khác có chướng ngại vật phía trước, trong khi xe B đang đi thẳng trên làn đường thông suốt của mình. Do đó XE A BẮT BUỘC PHẢI NHƯỜNG ĐƯỜNG.",
    
    542: "Xe con quay đầu xe đè lên vạch kẻ đường dành cho người đi bộ qua đường là VI PHẠM nghiêm trọng quy định về an toàn giao thông đường bộ (Luật nghiêm cấm quay đầu trên phần đường dành cho người đi bộ).",
    
    543: "Nhìn biển phân làn xe treo trên giá long môn: Làn 1 dành cho ô tô; Làn 2 dành cho mô tô... Quan sát thấy: Xe con (E) đi vào làn của mô tô; Xe mô tô (C) đi vào làn của ô tô. Do đó HAI XE VI PHẠM là Xe con (E) và Xe mô tô (C).",
    
    544: "Xe con phía trước đã đi vào trong giao lộ và đang thực hiện rẽ trái ('nhất chớm'), xe của bạn đi thẳng đến sau thì bắt buộc PHẢI NHƯỜNG ĐƯỜNG CHO XE CON RẼ TRÁI trước rồi mới tiếp tục đi thẳng.",
    
    545: "Đầu đoạn đường có cắm biển P.102 'Cấm đi ngược chiều' vào hướng 3. Hướng 4 là đường cấm ô tô rẽ. Do đó người lái xe ĐƯỢC PHÉP ĐI THEO HƯỚNG 1 VÀ HƯỚNG 2.",
    
    546: "Phía trước xe con (B) có chướng ngại vật là chiếc xe con đang dừng hỏng. Do đó XE CON (B) PHẢI NHƯỜNG ĐƯỜNG cho xe con (A) đi ngược chiều qua trước.",
    
    547: "Xe của bạn chuẩn bị rẽ trái tại ngã tư: Phải nhường đường cho xe đi thẳng (xe buýt) và xe rẽ phải (xe tải). Quy tắc hướng đi: Phải -> Thẳng -> Trái. Do đó bạn phải NHƯỜNG ĐƯỜNG CHO CẢ XE BUÝT VÀ XE TẢI.",
    
    548: "Đối chiếu biển phân làn trên từng làn: Xe con (E) đi vào làn xe máy; Xe mô tô (D) đi vào làn ô tô. Do đó các xe vi phạm làn đường là: Xe con (E) và xe mô tô (D).",
    
    549: "Xe tải đi thẳng trên đường chính thông suốt; xe của bạn chuẩn bị rẽ sang đường nên XE TẢI ĐƯỢC QUYỀN ĐI TRƯỚC xe của bạn.",
    
    550: "Tại nơi giao nhau, hướng B quay đầu đè lên vạch người đi bộ qua đường (bị cấm). Hướng A quay đầu qua tâm ngã tư bảo đảm an toàn. Do đó người lái xe CHỈ ĐƯỢC QUAY ĐẦU THEO HƯỚNG A.",
    
    551: "Xe của bạn và xe con đều đi trên đường ưu tiên (biển hình thoi). Xe của bạn rẽ phải và xe con đi thẳng đi đồng thời trước tiên; xe tải ở đường không ưu tiên đi sau cùng. Thứ tự: Xe của bạn và xe con -> Xe tải.",
    
    552: "Vượt xe an toàn trên đường: Phải bật tín hiệu báo xin vượt bằng đèn nhấp nháy hoặc còi, chú ý quan sát phía trước và gương chiếu hậu, KHI ĐỦ ĐIỀU KIỆN AN TOÀN mới tăng tốc vượt dứt khoát.",
    
    553: "Nhìn tín hiệu đèn giao thông: Làn của xe con và xe tải có ĐÈN ĐỎ, do đó XE CON VÀ XE TẢI PHẢI DỪNG LẠI. Làn xe khách và mô tô đèn xanh được đi.",
    
    554: "Quan sát các xe trên từng làn đường: Xe tải (D) đi sai làn mô tô; xe con (B) đi sai làn. Các xe: Xe con (A), Xe con (C), Xe con (E) và Xe buýt (G) đều đi đúng làn đường quy định theo biển phân làn.",
    
    555: "Tại nơi giao nhau có vạch người đi bộ và vạch tim đường nét liền, tầm nhìn bị che khuất bởi xe tải: Người lái xe CẤM VƯỢT xe tải để đi thẳng trong trường hợp này.",
    
    556: "Đoạn đường cong cua khuất tầm nhìn có vạch kẻ đường nét liền màu vàng cấm lấn làn: Bạn TUYỆT ĐỐI KHÔNG ĐƯỢC VƯỢT xe mô tô phía trước.",
    
    557: "Biển P.130 cấm dừng xe và đỗ xe có biển phụ mũi tên chỉ về phía sau lưng biển: Cấm dừng xe ở vị trí A (sau biển). Vị trí B và C nằm trước biển báo nên người lái xe DỪNG ĐÚNG TẠI VỊ TRÍ B VÀ C.",
    
    558: "Biển cấm dừng và đỗ xe có biển phụ mũi tên hai chiều (chỉ cả trước và sau biển): Cấm dừng đỗ ở cả vị trí A và vị trí B. Do đó bạn KHÔNG ĐƯỢC DỪNG ở bất kỳ vị trí nào.",
    
    559: "Cả hai xe đều bật đèn xi-nhan (xe con bật xi-nhan trái, xe mô tô bật xi-nhan phải) trong khi trước mặt có cắm biển R.301 'Hiệu lệnh hướng đi thẳng phải theo'. Việc chuẩn bị rẽ khiến CẢ HAI XE ĐỀU VI PHẠM quy tắc giao thông.",
    
    560: "Xe con đi thẳng theo đèn xanh -> đúng. Xe tải ở làn đi thẳng nhưng bật xi-nhan rẽ trái đè lên vạch phân làn -> VI PHẠM. Do đó chỉ có XE TẢI VI PHẠM.",
    
    561: "Xe khách ở làn rẽ trái nhưng đi thẳng -> vi phạm. Xe tải ở làn đi thẳng nhưng rẽ trái -> vi phạm. Xe con rẽ phải đúng làn. Xe mô tô đi đúng. Do đó XE KHÁCH VÀ XE TẢI VI PHẠM.",
    
    562: "Kiểm tra vi phạm: Xe tải đi sai hướng làn; xe khách đi sai hướng làn; xe mô tô vượt đèn đỏ. Do đó các xe vi phạm là: Xe tải, xe khách, xe mô tô.",
    
    563: "Xét tín hiệu đèn và vạch chỉ hướng làn: Xe khách và xe tải đều không tuân thủ hướng đi theo mũi tên quy định trên làn đường nên XE KHÁCH VÀ XE TẢI VI PHẠM.",
    
    564: "Để tránh xe hỏng phía trước: Quan sát gương phía trước và phía sau, khi thấy đường vắng và đủ điều kiện an toàn thì bật xi-nhan báo hiệu rồi mới lách qua xe hỏng.",
    
    565: "Xe tải đi sai làn; xe con đi sai đèn. Chỉ có XE KHÁCH (đi thẳng đúng đèn xanh) và XE MÔ TÔ (chấp hành đúng hướng làn) là CHẤP HÀNH ĐÚNG quy tắc giao thông.",
    
    566: "Đối chiếu biển phân làn: Xe tải (D) đi vào làn mô tô; xe con (B) đi vào làn xe tải/khách. Do đó HAI XE VI PHẠM là Xe tải (D) và Xe con (B).",
    
    567: "Áp dụng quy tắc ngã ba đồng cấp: 1. Xe mô tô rẽ phải đi trước; 2. Xe con đi thẳng đi thứ hai; 3. Xe của bạn rẽ trái đi sau cùng. Thứ tự: Xe mô tô -> Xe con -> Xe của bạn.",
    
    568: "Ngã tư đồng cấp: Xe con bên phải không vướng rẽ phải đi trước; sau đó đến lượt xe của bạn đi thẳng đi thứ hai; cuối cùng là xe mô tô rẽ trái. Thứ tự: Xe con -> Xe của bạn -> Xe mô tô.",
    
    569: "Nhìn tín hiệu đèn giao thông: Hướng của xe con có ĐÈN ĐỎ nên XE CON PHẢI DỪNG LẠI. Hướng xe của bạn có đèn xanh rẽ trái được tiếp tục đi.",
    
    570: "Mũi tên chỉ hướng trên mặt đường của làn xe bạn đang đi là mũi tên kết hợp: ĐI THẲNG VÀ RẼ TRÁI. Do đó xe của bạn được phép đi thẳng hoặc rẽ trái.",
    
    571: "Xe của bạn đang đứng ở làn đường có mũi tên đi thẳng hoặc rẽ trái: Khi đèn tín hiệu chuyển sang màu xanh, xe của bạn DỪNG LẠI TRƯỚC VẠCH VÀ ĐI THẲNG HOẶC RẼ TRÁI khi đèn xanh.",
    
    572: "Xe tải và người đi xe đạp đang đi thẳng trên làn đường ưu tiên cắt ngang: Bạn muốn rẽ phải thì phải GIẢM TỐC ĐỘ, RẼ PHẢI SAU XE TẢI VÀ XE ĐẠP để bảo đảm an toàn.",
    
    573: "Trước mặt có người đi bộ đang qua đường và xe con màu xanh đang rẽ: Bạn phải giảm tốc độ, nhường đường cho người đi bộ qua đường trước và rẽ phải sau xe con màu xanh.",
    
    574: "Tại ngã tư: Bạn chuẩn bị rẽ trái, phải nhường đường cho xe đi thẳng (xe đạp) và xe rẽ phải (xe khách). Do đó bạn phải NHƯỜNG ĐƯỜNG CHO CẢ XE ĐẠP VÀ XE KHÁCH.",
    
    575: "Xe con đi thẳng trên đường ưu tiên; xe của bạn đi thẳng; XE TẢI RẼ TRÁI gặp biển tam giác ngược phải nhường đường. Do đó XE TẢI PHẢI NHƯỜNG ĐƯỜNG.",
    
    576: "Phía trước làn đường của xe bạn có chướng ngại vật là công trường sửa chữa/xe hỏng. Xe đi bên làn đường có chướng ngại vật bắt buộc PHẢI NHƯỜNG ĐƯỜNG cho xe ngược chiều lưu thông qua trước.",
    
    577: "Đoàn người đi xe đạp có tổ chức là đối tượng tham gia giao thông được bảo vệ: Người lái xe ô tô TUYỆT ĐỐI KHÔNG ĐƯỢC VƯỢT qua đoàn người đi xe đạp có tổ chức.",
    
    578: "Gặp chướng ngại vật phía trước (xe đang lùi và xe con lách sang trái): Nếu phía sau an toàn thì bật xi-nhan chuyển làn sang trái; nếu phía sau có xe xin vượt thì giảm tốc độ dừng lại chờ đợi.",
    
    579: "Xe phía trước đang lùi ra khỏi nơi đỗ có thể che khuất tầm nhìn và chiếm dụng lòng đường: Người lái xe phải CHỦ ĐỘNG GIẢM TỐC ĐỘ, DỪNG LẠI NHƯỜNG ĐƯỜNG để phòng ngừa va chạm.",
    
    580: "Thấy xe ngược chiều vượt ẩu lấn sang hẳn làn đường của mình: Cách xử lý an toàn duy nhất là PHANH GIẢM TỐC ĐỘ VÀ ĐI SÁT VÀO LỀ ĐƯỜNG BÊN PHẢI để tránh cú đối đầu trực diện.",
    
    581: "Xe tải phía trước bật xi-nhan xin chuyển làn: Bạn cần PHANH GIẢM TỐC ĐỘ, giữ khoảng cách an toàn nhường cho xe tải chuyển làn xong xuôi mới tiếp tục di chuyển.",
    
    582: "Đèn giao thông đang xanh và ngã tư thông thoáng: Người lái xe GIẢM TỐC ĐỘ đến mức an toàn và ĐI THẲNG QUA NGÃ TƯ.",
    
    583: "Quy tắc nhường đường: Xe đạp rẽ phải đi trước; xe mô tô đi thẳng đi thứ hai; xe của bạn rẽ trái đi sau cùng. Thứ tự: Xe đạp -> Xe mô tô -> Xe của bạn.",
    
    584: "Áp dụng thứ tự ưu tiên: Xe của bạn đi trên đường ưu tiên (biển hình thoi) đi trước; xe con rẽ phải đi thứ hai; xe tải đi trên đường không ưu tiên đi cuối cùng. Thứ tự: Xe của bạn -> Xe con -> Xe tải.",
    
    585: "Tại ngã tư: Xe con đi thẳng bên phải không vướng; xe của bạn rẽ trái phải nhường đường cho xe đi thẳng. Do đó XE CỦA BẠN PHẢI NHƯỜNG ĐƯỜNG.",
    
    586: "Xe của bạn gặp biển báo tam giác ngược W.208 'Giao nhau với đường ưu tiên': Bạn đang đi trên đường nhánh nên XE CỦA BẠN PHẢI NHƯỜNG ĐƯỜNG cho xe con đi trên đường ưu tiên.",
    
    587: "Phía trước có người đi bộ đang bước trên vạch qua đường: Người lái xe bắt buộc phải GIẢM TỐC ĐỘ, DỪNG LẠI ĐỂ NGƯỜI ĐI BỘ SANG ĐƯỜNG TRƯỚC.",
    
    588: "Xe con đang rẽ trái; xe của bạn đi thẳng trên đường bằng thông suốt. Theo quy tắc hướng đi ưu tiên (Thẳng trước Trái), XE CỦA BẠN ĐƯỢC QUYỀN ĐI TRƯỚC.",
    
    589: "Xe tải và xe con đi trên đường ưu tiên đi trước (xe tải đi thẳng đi trước xe con rẽ trái); xe của bạn đi trên đường không ưu tiên (biển tam giác ngược) đi sau cùng. Thứ tự: Xe tải -> Xe con -> Xe của bạn.",
    
    590: "Phía trước ngược chiều có xe ô tô đang tiến lại và có người đi xe đạp cùng chiều: Bạn phải GIẢM TỐC ĐỘ, ĐI SÁT VỀ BÊN PHẢI, không lấn làn vượt xe đạp để tránh đối đầu xe ngược chiều.",
    
    591: "Xe tải nằm trên trục đường chính ưu tiên (biển hình thoi). Xe của bạn gặp biển tam giác ngược phải nhường đường. Do đó XE TẢI ĐƯỢC ĐI TRƯỚC.",
    
    592: "Quy tắc khoảng cách dừng đỗ trước đường sắt: Bắt buộc phải dừng cách ray đường sắt gần nhất TỐI THIỂU 5 MÉT. Xe con dừng cách 6m (> 5m) là đúng; xe mô tô dừng cách 3m (< 5m) là sai phạm quy tắc an toàn. Do đó CHỈ CÓ XE CON DỪNG ĐÚNG.",
    
    593: "Xe của bạn và xe tải đi trên đường ưu tiên: Xe của bạn đi thẳng đi trước xe tải rẽ trái; xe đạp ở đường nhánh đi sau cùng. Thứ tự: Xe của bạn -> Xe tải -> Xe đạp.",
    
    594: "Muốn rẽ trái tại ngã ba: Người lái xe phải chọn HƯỚNG 1 (đi đúng phần đường bên phải rồi mới mở cua rẽ trái). Hướng 2 cắt xéo góc cua là đi vào đường ngược chiều rất nguy hiểm.",
    
    595: "Bị xe ngược chiều rọi đèn pha chói mắt: Không được bật lại đèn pha hay phóng nhanh vượt ẩu; cần GIỮ NGUYÊN ĐÈN CHIẾU GẦN, GIẢM TỐC ĐỘ và đi nối đuôi sau xe phía trước an toàn.",
    
    596: "Khi rào chắn đường sắt đang dịch chuyển đóng lại: Người lái xe bắt buộc phải DỪNG LẠI TRƯỚC RÀO CHẮN MỘT KHOẢNG CÁCH AN TOÀN, tuyệt đối không tăng ga cố phóng qua.",
    
    597: "Xe con màu đỏ nhập làn cao tốc đè qua vạch xương cá và vạch liền là SAI hoàn toàn quy tắc an toàn. Xe phải chạy hết làn tăng tốc và quan sát an toàn mới được nhập làn.",
    
    598: "Khi xe con màu xanh đang vượt xe tải, tầm nhìn phía trước bị che khuất và làn đường vượt đang bị chiếm dụng: Xe con màu đỏ TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP VƯỢT (cấm vượt xe đang vượt).",
    
    599: "Vạch phân làn xe cùng chiều là VẠCH NÉT ĐỨT MÀU TRẮNG, xe con màu vàng quan sát an toàn phía trước và vượt xe con màu đỏ là ĐÚNG quy tắc giao thông.",
    
    600: "Xe đầu kéo container có chiều dài thân xe rất lớn, khi rẽ phải đuôi xe sẽ quét rộng và tạo ra vùng điểm mù khổng lồ phía sau và bên hông: Xe con màu xanh và xe máy bắt buộc phải GIẢM TỐC ĐỘ CHỜ XE CONTAINER RẼ XONG rồi mới tiếp tục di chuyển."
}

