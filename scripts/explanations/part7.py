# scripts/explanations/part7.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 301 đến Câu 360
Chương 5: Báo hiệu đường bộ (Phần 1: Biển báo cấm)
"""

PART7_EXPLANATIONS = {
    301: "Biển 1 (P.103a 'Cấm xe ô tô'): Cấm xe ô tô là gồm tất cả xe 4 bánh, 3 bánh đi vào (trừ xe mô tô hai bánh, xe gắn máy và các loại xe ưu tiên theo quy định). Biển 2 cấm xe tải, Biển 3 cấm xe khách.",
    
    302: "Biển 1 (P.103a 'Cấm xe ô tô'): Cấm xe ô tô là gồm tất cả xe 4 bánh, 3 bánh (bao gồm cả xe tải). Biển 2 (P.107) cấm xe khách và xe tải, trực tiếp cấm ô tô tải. Biển 3 (P.120) chỉ cấm ô tô kéo rơ moóc, không cấm ô tô tải thông thường. Do đó Biển 1 và Biển 2 cấm xe ô tô tải.",
    
    303: "Biển 1 cấm xe mô tô hai bánh. Biển 2 (P.106a 'Cấm xe ô tô tải'): Cấm xe tải thì gồm cả xe đầu kéo, máy kéo, do đó Biển 2 cấm máy kéo. Biển 3 (P.108) trực tiếp cấm máy kéo. Do đó Biển 2 và Biển 3 cấm máy kéo.",
    
    304: "Biển 1 (P.104) cấm mô tô 2 bánh và 3 bánh. Biển 2 (P.103a 'Cấm xe ô tô'): Cấm xe ô tô là gồm tất cả xe 4 bánh, 3 bánh nên cấm cả mô tô 3 bánh. Biển 3 cấm xe tải không cấm mô tô 3 bánh. Vì vậy Biển 1 và Biển 2 cấm xe mô tô ba bánh chở hàng.",
    
    305: "Xe gắn máy (dung tích xi-lanh dưới 50 cm3 hoặc xe máy điện) KHÔNG PHẢI là xe mô tô hai bánh và cũng không phải ô tô. Biển 1 cấm mô tô hai bánh, Biển 2 cấm ô tô con -> cả hai biển đều KHÔNG CẤM xe gắn máy, xe gắn máy được đi vào cả 2 biển.",
    
    306: "Biển 1 có hình vẽ chiếc mô tô hai bánh là biển 'Cấm xe mô tô hai bánh đi vào' (Biển P.104). Biển 2 cấm ô tô, Biển 3 cấm xe tải.",
    
    307: "Biển 1 cấm mô tô 2 bánh. Biển 2 (cấm ô tô) và Biển 3 (cấm xe tải) không có tác dụng cấm xe mô tô hai bánh. Do đó khi gặp Biển 2 và Biển 3 xe mô tô hai bánh được đi vào.",
    
    308: "Biển 1 hết cấm vượt (cho phép vượt). Biển 2 cấm ô tô con vượt (cấm mọi ô tô vượt). Biển 3 cấm ô tô tải vượt (không cấm xe con). Do đó xe ô tô con được phép vượt khi gặp Biển 1 và Biển 3.",
    
    309: "Biển 2 (P.125) có vẽ hình hai chiếc ô tô con cạnh nhau (xe màu đỏ bên trái) là biển 'Cấm vượt' chung cho tất cả các loại ô tô, do đó không cho phép ô tô con vượt.",
    
    310: "Biển 1 là biển 'Hết cấm vượt'. Biển 2 (P.125 'Cấm vượt'): Cấm xe ô tô vượt là gồm tất cả xe 4 bánh, 3 bánh vượt nhau (bao gồm cả ô tô tải). Biển 3 (P.126) trực tiếp cấm xe ô tô tải vượt. Do đó Biển 2 và Biển 3 cấm xe ô tô tải vượt.",
    
    311: "Cả hai biển đều cấm xe tải vượt: Biển 1 cấm mọi ô tô vượt (cấm cả xe tải); Biển 2 là biển cấm riêng ô tô tải vượt.",
    
    312: "Biển 1 (P.125 'Cấm vượt') cấm tất cả xe ô tô 4 bánh, 3 bánh vượt nhau nên cấm ô tô con vượt. Biển 2 (P.126) chỉ áp dụng cấm riêng xe ô tô tải vượt, không cấm ô tô con. Do đó xe ô tô con hoàn toàn ĐƯỢC PHÉP VƯỢT khi gặp Biển 2.",
    
    313: "Biển 1 là biển cấm rẽ trái (theo quy chuẩn mới, cấm rẽ trái KHÔNG cấm quay đầu). Biển 2 là biển hình chữ U gạch chéo đỏ, trực tiếp CẤM QUAY ĐẦU XE.",
    
    314: "Biển 1 (P.123a) là biển 'Cấm rẽ trái' (mũi tên rẽ trái bị gạch chéo đỏ). Biển 2 là biển cấm quay đầu xe (không cấm rẽ trái).",
    
    315: "Biển 1 cấm rẽ trái. Biển 2 chỉ cấm quay đầu xe mà KHÔNG CẤM RẼ TRÁI (theo Quy chuẩn QCVN 41:2019 và mới nhất, biển cấm quay đầu không cấm rẽ trái). Do đó gặp Biển 2 xe được rẽ trái.",
    
    316: "Biển 1 cấm ô tô rẽ trái. Biển 2 cấm ô tô rẽ trái VÀ cấm ô tô quay đầu. Cả hai biển này đều cấm xe ô tô rẽ trái.",
    
    317: "Biển 1 cấm tất cả phương tiện rẽ phải. Biển 2 cấm rẽ phải và cấm quay đầu. Biển 3 chỉ cấm riêng ô tô rẽ phải. Đề bài hỏi 'phương tiện' chung, do đó Biển 1 và Biển 2 cấm các phương tiện rẽ phải.",
    
    318: "Biển 1 cấm rẽ trái. Biển 2 cấm rẽ trái và cấm quay đầu. Biển 3 chỉ cấm riêng ô tô con rẽ trái. Do đó Biển 1 và Biển 2 cấm chung các phương tiện rẽ trái.",
    
    319: "Biển 1 vẽ hình ô tô con và mũi tên chữ U gạch chéo: biển này CHỈ CẤM RIÊNG XE Ô TÔ QUAY ĐẦU (xe máy, mô tô vẫn được quay đầu). Biển 2 cấm ô tô quay đầu và rẽ trái. Biển 3 cấm ô tô rẽ phải.",
    
    320: "Biển 2 kết hợp mũi tên rẽ trái và mũi tên quay đầu chữ U có gạch chéo đỏ: Biển này cấm xe ô tô đồng thời cả hai hành vi: RẼ TRÁI VÀ QUAY ĐẦU.",
    
    321: "Biển 1 cấm ô tô con chung (cấm cả taxi). Biển 2 có thêm chữ 'TAXI' bên dưới chiếc ô tô: Biển này chỉ cấm riêng xe taxi mà không cấm các loại phương tiện ô tô khác.",
    
    322: "Biển 1 cấm rẽ trái. Biển 2 là biển 'Khu vực quay đầu xe' (nền xanh, có mũi tên quay đầu): biển này chỉ dẫn khu vực được quay đầu và xe ĐƯỢC PHÉP RẼ TRÁI.",
    
    323: "Biển 1 cấm rẽ trái nhưng theo luật mới KHÔNG cấm quay đầu. Biển 2 là biển chỉ dẫn khu vực quay đầu xe đương nhiên được quay đầu. Do đó cả hai biển xe đều không bị cấm quay đầu.",
    
    324: "Biển 1 cấm rẽ trái (nhưng ĐƯỢC PHÉP quay đầu). Biển 2 cấm quay đầu xe (nhưng được phép rẽ trái). Đề bài hỏi 'được phép quay đầu nhưng không được rẽ trái' -> Chọn Biển 1.",
    
    325: "Biển 1 là biển 'Đường cấm' (vòng tròn đỏ nền trắng). Biển 2 là biển 'Cấm đi ngược chiều' (vòng tròn đỏ, có vạch ngang màu trắng ở giữa). Biển 3 là biển cấm đỗ xe.",
    
    326: "Biển 1 (Đường cấm) cấm tất cả phương tiện cơ giới và thô sơ đi vào (trừ xe ưu tiên). Biển 2 (Cấm đi ngược chiều) cấm các phương tiện đi vào theo chiều đặt biển. Cả hai biển này các phương tiện đều không được phép đi vào.",
    
    327: "Biển 1 cấm đỗ xe mọi ngày (cả chẵn và lẻ). Biển 3 có 2 vạch trắng đứng gạch chéo là biển 'Cấm đỗ xe ngày chẵn'. Do đó vào ngày chẵn, người lái xe không được đỗ xe ở cả Biển 1 và Biển 3.",
    
    328: "Biển 1 cấm đỗ xe tất cả các ngày. Biển 2 có 1 vạch trắng đứng gạch chéo là biển 'Cấm đỗ xe ngày lẻ'. Do đó vào ngày lẻ, không được đỗ xe khi gặp Biển 1 và Biển 2.",
    
    329: "Biển 2 có hình bát giác nền đỏ chữ trắng 'STOP' (DỪNG LẠI). Đây là biển báo duy nhất mà TẤT CẢ CÁC XE, KỂ CẢ XE ƯU TIÊN THEO LUẬT ĐỊNH (cứu hỏa, cứu thương, công an...) ĐỀU PHẢI DỪNG LẠI quan sát an toàn mới được đi tiếp.",
    
    330: "Biển 1 (P.101 'Đường cấm') cấm tất cả phương tiện cơ giới và thô sơ đi lại trên đoạn đường đó, trừ các loại xe ưu tiên theo luật định (như cứu thương, cứu hỏa, công an...).",
    
    331: "Biển 1 là biển P.110a 'Cấm xe đạp'. Biển 2 cấm xe đạp thồ, Biển 3 cấm xe mô tô. Do đó Biển 1 cấm người đi xe đạp.",
    
    332: "Biển 1 cấm xe lam. Biển 2 cấm xích lô máy (có gắn động cơ). Biển 3 cấm xích lô đạp. Gặp Biển 1 và Biển 2 thì xe xích lô đạp vẫn được phép đi vào bình thường.",
    
    333: "Biển 1 cấm xe lam, Biển 2 cấm xích lô máy. Biển 3 chỉ cấm xích lô đạp (xe thô sơ) nên xe lam và xe xích lô máy ĐƯỢC PHÉP ĐI VÀO khi gặp Biển 3.",
    
    334: "Biển vẽ hình người dắt gia súc (ngựa, bò) kéo xe: Báo hiệu đường cấm súc vật vận tải hàng hóa hoặc hành khách dù là kéo xe hay chở trên lưng đi qua.",
    
    335: "Biển tròn viền đỏ, nền đen có chữ trắng '70' và phụ đề biểu tượng mặt trăng/giờ đêm: Báo hiệu tốc độ tối đa cho phép về ban đêm đối với các phương tiện là 70 km/h.",
    
    336: "Các biển hạn chế tải trọng, khổ giới hạn chiều cao: Xe ưu tiên nếu có tải trọng hoặc chiều cao vượt quá chỉ số ghi trên biển TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP ĐI QUA để tránh gây sập cầu hoặc sập hầm đường bộ.",
    
    337: "Biển 1 có hai mũi tên đối đầu theo chiều dọc kẹp số '3,5m' ở giữa: Báo hiệu HẠN CHẾ CHIỀU CAO của xe và hàng hóa (tối đa 3,5 mét). Biển 2 hạn chế tải trọng trục (7 tấn), Biển 3 hạn chế tải trọng toàn bộ xe (10 tấn).",
    
    338: "Biển số 2 vẽ hình một trục bánh xe và số '7T': Báo hiệu hạn chế tải trọng trên trục xe, cho phép các xe có tải trọng phân bổ trên trục xe từ 7 tấn trở xuống được phép đi qua.",
    
    339: "Biển số 3 vẽ hình xe ô tô tải có chữ '10T': Báo hiệu cấm các loại xe (cả xe cơ giới và xe kéo) có tổng tải trọng toàn bộ (khối lượng bản thân xe cộng hàng hóa) vượt quá 10 tấn đi qua.",
    
    340: "Biển 1 (P.120) cấm tất cả các loại xe cơ giới kéo theo rơ moóc (bao gồm cả máy kéo kéo rơ moóc). Biển 2 (P.108) cấm tất cả các loại máy kéo đi vào (dù có kéo hay không kéo rơ moóc). Do đó CẢ HAI BIỂN đều cấm máy kéo kéo theo rơ moóc.",
    
    341: "Biển số 1 (P.120 'Cấm ô tô kéo rơ moóc') chỉ có hiệu lực cấm các phương tiện có kéo theo rơ moóc, hoàn toàn KHÔNG CẤM ô tô tải thông thường không kéo moóc. Vì vậy xe ô tô tải ĐƯỢC PHÉP ĐI VÀO.",
    
    342: "Biển 1 cấm ô tô kéo moóc, Biển 2 cấm máy kéo kéo moóc. Hai biển này chỉ có hiệu lực với xe có kéo theo rơ moóc, hoàn toàn KHÔNG CÓ HIỆU LỰC đối với xe ô tô tải không kéo moóc.",
    
    343: "Biển 1 chỉ cấm xe kéo theo rơ moóc. Biển 2 (P.108) trực tiếp cấm máy kéo. Biển 3 (P.106a 'Cấm xe ô tô tải'): Cấm xe tải thì gồm cả xe đầu kéo, máy kéo, do đó Biển 3 cũng cấm máy kéo. Do đó Biển 2 và Biển 3 cấm máy kéo.",
    
    344: "Biển cấm ô tô và cấm mô tô (gắn biển phụ mũi tên 2 hướng rẽ trái và phải): Biển này cấm tất cả các loại xe cơ giới từ 2 bánh, 3 bánh đến 4 bánh rẽ sang trái hoặc rẽ sang phải. Mô tô 3 bánh chở hàng không được phép rẽ.",
    
    345: "Biển có hình ô tô bên trái và mô tô 2 bánh bên phải: Biển P.105 cấm tất cả các loại xe cơ giới và mô tô đi vào (bao gồm cả xe mô tô hai bánh và ba bánh chở hàng).",
    
    346: "Biển P.105 (cấm xe cơ giới và xe mô tô) kết hợp biển phụ mũi tên rẽ hai hướng: Có ý nghĩa cấm các loại xe cơ giới và xe mô tô (trừ xe ưu tiên) đi về hướng bên trái và bên phải.",
    
    347: "Biển cấm bóp còi có biển phụ ghi '500m' có hai mũi tên dọc hai bên: Báo hiệu CHIỀU DÀI ĐOẠN ĐƯỜNG 500m từ vị trí đặt biển bắt đầu áp dụng lệnh cấm bấm còi.",
    
    348: "Gặp biển cấm bấm còi có biển phụ chiều dài 500m: Trong phạm vi 500 mét tính từ biển báo, người lái xe tuyệt đối KHÔNG ĐƯỢC PHÉP BẤM CÒI.",
    
    349: "Biển 1 cấm ô tô (không cấm mô tô). Biển 2 cấm mô tô 2 bánh. Biển 3 cấm xe tải (không cấm mô tô). Do đó xe mô tô hai bánh được đi vào khi gặp Biển 1 và Biển 3.",
    
    350: "Biển 2 có hình chiếc mô tô hai bánh là biển P.104 'Cấm xe mô tô', do đó xe mô tô hai bánh không được phép đi vào Biển 2.",
    
    351: "Biển phụ đặt dưới biển tròn cấm (P.101 'Đường cấm'): Biển phụ vẽ hình loại xe nào thì biển cấm sẽ CÓ HIỆU LỰC CẤM RIÊNG ĐỐI VỚI LOẠI XE ĐÓ đi vào.",
    
    352: "Biển báo cự ly tối thiểu giữa 2 xe (chữ 8m) có biển phụ ghi '500m' và CÓ 2 MŨI TÊN DỌC HAI BÊN (Biển 1): Báo hiệu 'Chiều dài đoạn đường' phải giữ cự ly tối thiểu giữa hai xe.",
    
    353: "Biển 2 chỉ ghi '200m' (KHÔNG CÓ hai mũi tên dọc): Báo hiệu khoảng cách thực tế từ nơi đặt biển đến vị trí bắt đầu áp dụng cự ly tối thiểu giữa hai xe.",
    
    354: "Biển cấm dừng và đỗ xe (hai vạch chéo đỏ) có biển phụ mũi tên chỉ sang phải: Có ý nghĩa CẤM DỪNG VÀ ĐỖ XE THEO HƯỚNG BÊN PHẢI từ sau vị trí cắm biển.",
    
    355: "Gặp biển cấm dừng đỗ có biển phụ mũi tên chỉ sang phải: Người lái xe KHÔNG ĐƯỢC PHÉP dừng xe hay đỗ xe theo hướng bên phải của biển.",
    
    356: "Biển vẽ hình xe tải kéo sơ mi rơ moóc có ghi '14m': Cấm các phương tiện và đoàn xe có tổng chiều dài (cả hàng hóa) vượt quá 14 mét đi qua. Xe có chiều dài lớn hơn 14m KHÔNG ĐƯỢC PHÉP ĐI VÀO.",
    
    357: "Quy định an toàn xếp dỡ hàng: Hàng chở trên xe ô tô tải vượt quá phía trước và sau thùng xe quá 10% chiều dài toàn bộ xe là VI PHẠM QUY TẮC XẾP HÀNG AN TOÀN, do đó không được phép lưu thông.",
    
    358: "Biển vẽ hình chiếc xe khách nhìn ngang: Là biển P.107a 'Cấm xe ô tô khách' đi vào (không cấm xe buýt chạy tuyến cố định).",
    
    359: "Biển có hai mũi tên nằm ngang hướng vào nhau kẹp số '2,3m' ở giữa: Báo hiệu HẠN CHẾ CHIỀU NGANG (chiều rộng) của xe và hàng hóa (tối đa 2,3 mét).",
    
    360: "Biển 1 có nền đen, chữ trắng và biểu tượng ban đêm: Là biển báo 'Tốc độ tối đa cho phép về ban đêm'."
}

