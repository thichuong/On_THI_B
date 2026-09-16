# scripts/explanations/part8.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 361 đến Câu 420
Chương 5: Báo hiệu đường bộ (Phần 2: Biển nguy hiểm, chỉ dẫn & hiệu lệnh)
"""

PART8_EXPLANATIONS = {
    361: "Biển 1 (DP.134) là biển 'Hết hạn chế tốc độ tối đa' (vòng tròn viền xanh có các vạch gạch chéo qua số giới hạn). Biển 2 là biển hết mọi lệnh cấm.",
    
    362: "Biển 1 là biển chỉ dẫn tốc độ tối thiểu (nền xanh). Biển 2 (P.127) tròn viền đỏ chữ đen là biển báo cấm: 'Hạn chế tốc độ tối đa cho phép', bắt buộc các xe không được vượt quá số ghi trên biển.",
    
    363: "Biển 1 báo hiệu hết đường ưu tiên. Biển 2 có hình cầu vượt/cao tốc với vạch đỏ gạch chéo là biển 'Kết thúc đường cao tốc'. Biển 3 hết đường dành cho ô tô.",
    
    364: "Biển P.127 hình tròn viền đỏ có số '50': Báo hiệu 'Tốc độ tối đa cho phép' của các phương tiện là 50 km/h.",
    
    365: "Biển 2 có hình phân tách các làn đường kèm biển báo tốc độ trên từng làn: Chỉ dẫn bắt đầu vào đường cao tốc có phân làn theo từng dải tốc độ khác nhau.",
    
    366: "Biển R.306 hình tròn nền xanh chữ trắng '60': Báo hiệu 'Tốc độ tối thiểu cho phép' là 60 km/h, các phương tiện không được chạy chậm hơn tốc độ này trong điều kiện bình thường.",
    
    367: "Biển 1 (W.224) hình tam giác viền đỏ là biển báo nguy hiểm: 'Đường người đi bộ cắt ngang', người lái xe phải giảm tốc độ và nhường đường cho người đi bộ qua đường. Biển 2 cấm người đi bộ; Biển 3 đường dành cho người đi bộ.",
    
    368: "Biển 3 (R.305) hình tròn nền xanh vẽ người đi bộ: Là biển hiệu lệnh 'Đường dành cho người đi bộ', các loại phương tiện cơ giới và thô sơ KHÔNG ĐƯỢC PHÉP đi vào.",
    
    369: "Biển 1 (R.304) hình tròn nền xanh vẽ chiếc xe đạp: Là biển hiệu lệnh 'Đường dành cho xe thô sơ' (xe đạp, xe lăn...) và người đi bộ.",
    
    370: "Cả ba biển đều là biển báo nguy hiểm cảnh báo sắp đến chỗ giao nhau: Biển 1 giao với đường sắt có rào chắn; Biển 2 giao với đường ưu tiên; Biển 3 giao nhau có đèn tín hiệu. Vì vậy cả 3 biển đều báo sắp đến chỗ giao nhau nguy hiểm.",
    
    371: "Biển 1 (W.210) vẽ hình hàng rào: Báo hiệu 'Giao nhau với đường sắt có rào chắn'. Biển 2 giao nhau đường sắt không rào chắn; Biển 3 giao nhau với tàu điện.",
    
    372: "Biển 3 (W.209) vẽ cột đèn tín hiệu 3 màu: Báo hiệu 'Giao nhau có tín hiệu đèn' giao thông.",
    
    373: "Biển 1 vẽ hàng rào (giao nhau đường sắt có rào chắn). Biển 3 vẽ đầu tàu hỏa (giao nhau đường sắt không rào chắn). Cả hai biển 1 và 3 đều báo hiệu nguy hiểm giao nhau với đường sắt.",
    
    374: "Biển 2 vẽ đầu máy xe lửa và Biển 3 là biển chữ X cắt ngang: Cả hai biển này đều báo hiệu 'Giao nhau với đường sắt KHÔNG CÓ RÀO CHẮN'. (Biển 1 có rào chắn).",
    
    375: "Biển 1 (W.211a) vẽ đầu tàu hỏa: Báo hiệu sắp đến nơi giao nhau giữa đường bộ và đường sắt không có rào chắn. Biển 2 giao nhau đường ưu tiên; Biển 3 giao nhau có đèn tín hiệu.",
    
    376: "Biển 2 vẽ hình vòm hầm tròn khoét sâu: Báo hiệu sắp đến 'Cửa chui' để người lái xe chú ý chiều cao giới hạn. Biển 1 là cầu vồng; Biển 3 là đường hầm.",
    
    377: "Hai biển chữ X (Biển 242a một đường ray và 242b từ hai đường ray trở lên): Đặt tại nơi ĐƯỜNG SẮT GIAO VUÔNG GÓC VỚI ĐƯỜNG BỘ không có rào chắn.",
    
    378: "Biển 1 và Biển 2 (ký hiệu chữ X đơn và chữ X kép): Báo hiệu nơi đường sắt giao vuông góc với đường bộ (Biển 1: một đường ray; Biển 2: từ 2 đường ray trở lên).",
    
    379: "Các biển có các vạch đỏ nghiêng chéo đặt cách nhau: Báo trước sắp đến vị trí ĐƯỜNG SẮT GIAO KHÔNG VUÔNG GÓC với đường bộ, không có rào chắn và không có người gác.",
    
    380: "Biển 1 là đường giao nhau cùng cấp; Biển 2 giao nhau với đường không ưu tiên; Biển 3 hình thoi có vạch đen gạch chéo là biển I.402 'Hết đoạn đường ưu tiên'.",
    
    381: "Biển 1 (W.207a - tam giác mũi tên lớn cắt nhánh nhỏ) và Biển 3 (I.401 - hình thoi vàng) đều báo hiệu xe ĐƯỢC QUYỀN ƯU TIÊN QUA NƠI GIAO NHAU. (Biển 2 tam giác ngược phải nhường đường).",
    
    382: "Biển 1 (W.207a) có trục đường chính thẳng đứng to cắt ngang nhánh nhỏ hai bên: Báo hiệu 'Giao nhau với đường không ưu tiên'.",
    
    383: "Biển 2 (W.208) hình tam giác ngược đỉnh chúc xuống: Báo hiệu 'Giao nhau với đường ưu tiên', người lái xe đi trên đường này bắt buộc phải giảm tốc độ và nhường đường cho xe trên đường ưu tiên.",
    
    384: "Biển 1 báo hiệu đường bị thu hẹp cả hai bên. Biển 2 báo hiệu đường bị thu hẹp về phía bên trái. Biển 3 là chỗ ngoặt nguy hiểm.",
    
    385: "Gặp Biển 2 (đường hẹp bên trái) và Biển 3 (đường hẹp bên phải): Người lái xe phải giảm tốc độ, xe đi ở phía làn đường bị hẹp phải chủ động dừng lại nhường đường cho xe đi ngược chiều.",
    
    386: "Biển 3 (W.208) hình tam giác ngược đỉnh chúc xuống: Là biển 'Giao nhau với đường ưu tiên'.",
    
    387: "Biển 1 (W.205a) có hình dấu cộng (+) các nét đậm bằng nhau: Báo hiệu 'Đường giao nhau của các tuyến đường cùng cấp' (ngã tư đồng cấp).",
    
    388: "Biển 2 (W.207c) vẽ đường chính to và có đường nhánh không ưu tiên rẽ ra bên phải: Báo hiệu 'Giao nhau với đường không ưu tiên'.",
    
    389: "Biển 1 (W.204) tam giác vàng có 2 mũi tên đỏ-đen thẳng đứng: Báo hiệu 'Đường hai chiều'. Biển 2 bắt đầu đường đôi; Biển 3 giao nhau đường 2 chiều.",
    
    390: "Biển 2 (P.132) hình tròn viền đỏ mũi tên đỏ bên chiều đi: Báo hiệu 'Phải giảm tốc độ, nhường đường cho xe cơ giới đi ngược chiều qua đường hẹp'.",
    
    391: "Biển 3 (I.406) hình vuông nền xanh, mũi tên trắng to đi thẳng: Là biển chỉ dẫn 'Được ưu tiên qua đường hẹp'.",
    
    392: "Biển 2 (W.212) tam giác vàng có biểu tượng dải phân cách (cái ly) ở PHÍA TRÊN đỉnh hai mũi tên: Báo hiệu 'Bắt đầu đường đôi'.",
    
    393: "Biển 3 (W.212) là biển báo hiệu 'Đường đôi' (dải phân cách nằm ở phía trên chia hai luồng xe).",
    
    394: "Biển 3 (W.213) có biểu tượng dải phân cách nằm ở PHÍA DƯỚI đáy hai mũi tên: Báo hiệu 'Kết thúc đường đôi' (chuyển sang đường hai chiều không có dải phân cách giữa).",
    
    395: "Biển 1 (W.204) có 2 mũi tên nằm ngang hai đầu: Báo hiệu 'Giao nhau với đường hai chiều'.",
    
    396: "Biển 2 (W.204) tam giác vàng có hai mũi tên thẳng đứng ngược chiều: Báo hiệu 'Đường hai chiều'.",
    
    397: "Biển 2 có hai mũi tên nằm ngang đối xứng: Báo hiệu sắp đến nơi 'Giao nhau với đường hai chiều'.",
    
    398: "Biển 2 (vòng tránh sang hai bên) và Biển 3 (vòng tránh sang bên trái): Báo hiệu 'Chú ý chướng ngại vật' phía trước trên đường chạy.",
    
    399: "Biển 2 có hình ô tô lao lên dốc đệm cát lánh nạn màu đỏ: Là biển chỉ dẫn 'Vị trí và khoảng cách có làn đường cứu nạn (làn thoát xe khẩn cấp)' khi xe bị mất phanh đổ đèo.",
    
    400: "Biển 2 (W.240) hình cửa hầm tối có ánh sáng phía xa: Báo hiệu sắp vào 'Đường hầm'. (Biển 1 là cầu vồng; Biển 3 là cửa chui).",
    
    401: "Biển 2 (W.214) vẽ hình hai thành cầu hẹp thắt lại ở giữa: Báo hiệu 'Cầu hẹp'. Biển 1 cầu tạm; Biển 3 cầu quay.",
    
    402: "Biển 3 vẽ nhịp cầu đang quay tách đôi cho tàu thuyền qua: Báo hiệu 'Cầu quay - cầu cất'.",
    
    403: "Biển 1 vẽ chiếc ô tô đang rơi chúi đầu thẳng xuống mép vực nước: Báo hiệu 'Kè, vực sâu phía trước'.",
    
    404: "Biển 3 vẽ xe đang lao xuống vực nước nằm ở PHÍA BÊN TRÁI của đường: Báo hiệu 'Kè, vực sâu bên đường phía bên trái'.",
    
    405: "Biển 2 vẽ xe đang rơi xuống vực nước nằm ở PHÍA BÊN PHẢI: Báo hiệu 'Kè, vực sâu bên đường phía bên phải'.",
    
    406: "Biển 2 (W.222a) vẽ chiếc xe bị trượt lết để lại hai vệt bánh ngoằn ngoèo: Báo hiệu 'Đường trơn', lái xe cần đi số thấp và không phanh gấp.",
    
    407: "Biển 2 vẽ xe ô tô bị sụt bánh nghiêng bên mép lề đường: Báo hiệu 'Lề đường nguy hiểm' (lề đất yếu hoặc sạt lở).",
    
    408: "Biển 1 (W.227) vẽ hình công nhân đang cầm xẻng xúc đất: Báo hiệu 'Đoạn đường đang tiến hành thi công sửa chữa'.",
    
    409: "Biển 2 có hình 2 ô tô đâm vào nhau và dấu chấm than: Cảnh báo nguy hiểm 'Đoạn đường thường xảy ra tai nạn'.",
    
    410: "Biển 2 vẽ hình nhiều xe ô tô nối đuôi san sát nhau: Báo hiệu 'Đoạn đường hay xảy ra ùn tắc giao thông'.",
    
    411: "Biển 2 (W.225) vẽ hai em nhỏ đang dắt tay nhau: Cảnh báo 'Đoạn đường thường có trẻ em đi ngang qua' (gần trường học, khu vui chơi), lái xe phải đi chậm và đề phòng trẻ chạy bất ngờ.",
    
    412: "Biển 2 (I.423a) hình vuông nền xanh vẽ người đi bộ trên vạch: Chỉ dẫn 'Vị trí bắt đầu đoạn đường dành cho người đi bộ sang đường'.",
    
    413: "Biển 2 (W.225) hình tam giác viền đỏ vẽ hai trẻ em: Báo hiệu gần đến đoạn đường thường có trẻ em đi ngang qua.",
    
    414: "Biển 1 (W.231) vẽ hình chiếc túi vải đón gió: Cảnh báo 'Gió ngang thổi mạnh', người lái xe cần giảm tốc độ để tránh bị gió bạt lật xe.",
    
    415: "Mẹo nhớ dốc: Đọc từ trái sang phải như đọc chữ viết: Biển 1 có vạch dốc tụt xuống (số 10%) là 'Dốc xuống nguy hiểm'.",
    
    416: "Mẹo nhớ dốc: Đọc từ trái sang phải: Biển 2 có vạch dốc ngửa lên (số 9%) là 'Dốc lên nguy hiểm'.",
    
    417: "Biển W.201a vẽ xe tải nghiêng bên phải trên khúc cua ngoặt sang trái: Báo hiệu 'Chỗ ngoặt nguy hiểm có nguy cơ lật xe bên phải khi đường cong vòng sang trái' do lực ly tâm.",
    
    418: "Biển W.215b vẽ chiếc ô tô đỗ trên phà nổi trên mặt nước: Báo hiệu 'Sắp đến bến phà'.",
    
    419: "Biển 1 (W.221a) có HAI gợn sóng lồi lõm: Báo hiệu 'Đoạn đường có ổ gà, lồi lõm'.",
    
    420: "Biển 2 (W.221b) có MỘT ụ nổi gồ lên ở giữa mặt đường: Báo hiệu 'Đoạn đường có gờ giảm tốc phía trước' để cưỡng bức giảm tốc độ."
}

