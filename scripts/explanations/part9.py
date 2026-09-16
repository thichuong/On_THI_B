# scripts/explanations/part9.py
# -*- coding: utf-8 -*-
"""
Giải thích đáp án chi tiết cho Câu 421 đến Câu 485
Chương 5: Báo hiệu đường bộ (Phần 3: Biển chỉ dẫn & Vạch kẻ đường)
"""

PART9_EXPLANATIONS = {
    421: "Biển W.228b vẽ chiếc xe ô tô bị nghiêng lún trên nền đường lún gợn sóng: Cảnh báo 'Đoạn nền đường yếu, đoạn đường đang theo dõi lún' có thể gây lật xe nếu chạy tốc độ cao.",
    
    422: "Biển W.228a vẽ đất đá lở từ sườn núi xuống đường: Báo trước gần tới đoạn đường có hiện tượng 'Đất đá từ ta-luy dương sụt lở bất ngờ' gây nguy hiểm.",
    
    423: "Biển W.229 vẽ các viên sỏi đá bắn lên từ lốp xe: Cảnh báo 'Nơi có kết cấu mặt đường rời rạc, sỏi đá văng lên' khi xe chạy qua, người lái xe cần giảm tốc độ và giữ khoảng cách xa xe trước.",
    
    424: "Biển W.230 vẽ hình con bò: Cảnh báo đoạn đường thường có gia súc thả rông trên đường, người lái xe phải đi chậm, quan sát và dừng lại nhường đường, không bấm còi inh ỏi làm gia súc hoảng loạn lao vào xe.",
    
    425: "Biển W.233 vẽ tia sét chéo ngang: Báo hiệu 'Khu vực có đường dây điện cao thế cắt ngang phía trên tuyến đường' để các xe chở hàng cao chú ý an toàn phóng điện.",
    
    426: "Biển 2 (vừa vẽ hình loại xe trên từng làn vừa ghi số tốc độ tối đa cho phép): Báo hiệu các phương tiện phải đi đúng làn đường quy định và tuân thủ tốc độ tối đa cho phép trên làn đó.",
    
    427: "Cả hai biển đều ghi rõ các con số tốc độ (như 60, 50, 40...) tương ứng trên từng làn đường: Báo hiệu các phương tiện phải tuân thủ tốc độ tối đa cho phép trên từng làn đường.",
    
    428: "Biển 1 (R.403a) hình chữ nhật nền xanh vẽ hình ô tô con: Là biển chỉ dẫn 'Đường dành cho xe ô tô'. Biển 2 là biển hết đường dành cho ô tô.",
    
    429: "Biển 2 (R.404a) vẽ hình ô tô có vạch chéo đỏ gạch ngang: Báo hiệu 'Hết đoạn đường dành cho xe ô tô'.",
    
    430: "Biển 1 (R.403b) vẽ hình ô tô và mô tô cạnh nhau: Chỉ dẫn đường dành cho ô tô và mô tô, các loại phương tiện khác KHÔNG ĐƯỢC PHÉP ĐI VÀO.",
    
    431: "Biển R.411 hình chữ nhật nền xanh có các mũi tên phân theo từng làn: Báo hiệu cho người lái xe biết 'Số lượng làn đường trên mặt đường và hướng đi bắt buộc phải theo trên mỗi làn'.",
    
    432: "Biển 1 chỉ được đi thẳng. Biển 2 chỉ được đi thẳng hoặc rẽ phải. Không có biển nào cho phép rẽ sang hướng khác (hướng trái/quay đầu). Do đó chọn: 'Không biển nào'.",
    
    433: "Biển 1 (R.301a) hình tròn nền xanh mũi tên trắng hướng thẳng đứng lên: Là biển hiệu lệnh 'Hướng đi thẳng phải theo'. (Biển 2 hình vuông nền xanh là biển chỉ dẫn đường một chiều).",
    
    434: "Biển 2 (I.407a) hình chữ nhật/vuông nền xanh mũi tên trắng hướng lên: Là biển chỉ dẫn 'Đường một chiều'. (Biển 1 là biển hiệu lệnh hướng đi thẳng phải theo).",
    
    435: "Biển 1 (DP.134) vòng tròn viền xanh có vạch đen chéo ngang số 50: Là biển 'Hết hạn chế tốc độ tối đa cho phép'. (Biển 2 hết mọi lệnh cấm; Biển 3 hết tốc độ tối thiểu).",
    
    436: "Hiệu lực của biển hạn chế tốc độ tối đa sẽ hết tác dụng khi gặp: Biển 1 (Hết hạn chế tốc độ tối đa) HOẶC gặp Biển 2 (Hết mọi lệnh cấm). Do đó chọn Biển 1 và Biển 2.",
    
    437: "Biển 3 (DP.135) hình tròn nền xanh có số 60 màu trắng và vạch chéo đỏ: Là biển báo 'Hết tốc độ tối thiểu'.",
    
    438: "Biển 2 là biển 'Hết mọi lệnh cấm' (hết cấm vượt). Biển 3 là biển 'Hết cấm vượt' (hai ô tô màu xám gạch chéo). Cả Biển 2 và Biển 3 đều báo hiệu hết cấm vượt.",
    
    439: "Biển 2 (DP.135) hình tròn viền xanh có 5 vạch đen nghiêng song song: Là biển báo 'Hết mọi lệnh cấm'.",
    
    440: "Biển 3 (R.301h) hình tròn nền xanh vẽ mũi tên rẽ trái kết hợp quay đầu: Cho phép người lái xe ĐƯỢC PHÉP QUAY ĐẦU XE ĐI THEO HƯỚNG NGƯỢC LẠI khi đặt biển trước nơi giao nhau.",
    
    441: "Biển 1 (R.301d) chỉ cho phép xe đi thẳng hoặc rẽ trái, hoàn toàn KHÔNG CHO PHÉP RẼ PHẢI. Biển 2 chỉ được rẽ phải; Biển 3 được đi thẳng hoặc rẽ phải.",
    
    442: "Biển 1 chỉ được rẽ trái. Biển 2 chỉ được rẽ sang trái hoặc phải. Cả Biển 1 và Biển 2 ĐỀU KHÔNG CHO PHÉP XE ĐI THẲNG, người lái bắt buộc phải rẽ sang hướng khác.",
    
    443: "Biển 1 là biển chỉ dẫn vị trí quay đầu xe. Biển 2 là biển chỉ dẫn khu vực quay đầu xe. Cả hai biển này đều cho phép người lái xe được quay đầu xe.",
    
    444: "Biển 3 có chữ 'AH112' (Asian Highway): Là biển chỉ dẫn mã hiệu và tên đường trên các tuyến đường đối ngoại (đường xuyên Á).",
    
    445: "Biển số 1 có chữ ZONE, biểu tượng đỗ xe (P) theo giờ và vạch gạch chéo: Chỉ dẫn 'Hết hiệu lực cấm đỗ xe theo giờ trong khu vực'.",
    
    446: "Biển số 3 có chữ ZONE và số 50 viền đỏ: Là biển chỉ dẫn 'Hạn chế tốc độ tối đa trong khu vực' (Zone 50).",
    
    447: "Biển 2 (I.414b) có mũi tên thẳng đứng chỉ luồng xe và vẽ hình xe khách ở làn đối diện: Báo hiệu 'Đường phía trước có làn đường dành cho ô tô khách'.",
    
    448: "Biển 3 (I.414c) có mũi tên nằm ngang vẽ hình xe khách: Báo hiệu 'Rẽ ra đường có làn đường dành cho ô tô khách'.",
    
    449: "Biển 1 chỉ dẫn rẽ phải vào đường cụt; Biển 2 chỉ dẫn rẽ trái vào đường cụt. Cả Biển 1 và Biển 2 đều đặt trước ngã ba để chỉ dẫn rẽ vào đường cụt. (Biển 3 là đường cụt phía trước).",
    
    450: "Biển 1 vẽ người đi bộ ĐI LÊN các bậc cầu thang: Chỉ dẫn cho người đi bộ 'Sử dụng cầu vượt qua đường'.",
    
    451: "Biển 2 vẽ người đi bộ ĐI XUỐNG các bậc thang ngầm: Chỉ dẫn cho người đi bộ 'Sử dụng hầm chui qua đường'.",
    
    452: "Biển 2 (I.408a) có chữ P kèm biểu tượng xe lăn của người khuyết tật: Là biển báo 'Nơi đỗ xe dành cho người khuyết tật'.",
    
    453: "Biển phụ vẽ nửa thân xe ô tô nằm trên vỉa hè: Chỉ dẫn người lái xe được phép đỗ xe từ 1/2 THÂN XE TRỞ LÊN TRÊN HÈ PHỐ.",
    
    454: "Biển I.434a 'Trạm Cảnh sát giao thông': Người lái xe phải GIẢM TỐC ĐỘ đến mức an toàn và không được vượt khi đi qua khu vực trạm CSGT.",
    
    455: "Biển R.303 hình tròn nền xanh vẽ mũi tên vòng quanh đảo tròn: Là biển hiệu lệnh BẮT BUỘC người lái xe phải chạy vòng theo đảo an toàn tại vòng xuyến.",
    
    456: "Biển 2 có dòng chữ ghi ranh giới giữa hai tỉnh/thành phố (địa phận): Chỉ dẫn địa giới hành chính giữa các tỉnh, thành phố.",
    
    457: "Biển 1 và Biển 3 có hình vẽ các nhánh rẽ lập thể kết nối qua cầu vượt: Báo hiệu 'Cầu vượt liên thông' cho phép xe chuyển hướng sang các tuyến đường giao nhau. (Biển 2 là cầu vượt cắt qua).",
    
    458: "Biển số 1 vẽ sơ đồ các hướng đi thẳng và rẽ qua các nhánh cầu vượt: Có ý nghĩa báo hiệu 'Cầu vượt liên thông'.",
    
    459: "Biển 1 và Biển 2 có hình cầu thẳng bắc ngang qua đường: Báo hiệu 'Tuyến đường cầu vượt cắt qua' (không có nhánh rẽ liên thông kết nối).",
    
    460: "Biển vẽ hình xe lao lên dốc cứu nạn kèm khoảng cách '300m': Chỉ dẫn khoảng cách đến làn đường cứu nạn (làn thoát xe khẩn cấp).",
    
    461: "Trên biển có hình các vạch phân làn nét đứt kèm hướng đi: Cho phép người lái xe ĐƯỢC PHÉP CHUYỂN SANG LÀN ĐƯỜNG KHÁC khi bảo đảm an toàn.",
    
    462: "Biển R.403a 'Đường dành cho xe ô tô': Áp dụng chung cho tất cả các loại xe ô tô (ô tô con, ô tô khách, ô tô tải). Do đó xe tải và xe khách hoàn toàn ĐƯỢC PHÉP ĐI VÀO.",
    
    463: "Biển chỉ dẫn vẽ riêng hình ô tô con và mô tô: Đoạn đường này CHỈ DÀNH RIÊNG cho xe con và xe máy, do đó xe tải và xe khách KHÔNG ĐƯỢC PHÉP ĐI VÀO.",
    
    464: "Biển 2 có biểu tượng đường cao tốc kèm vạch chéo đỏ: Báo hiệu 'Kết thúc đường cao tốc'.",
    
    465: "Biển vẽ sơ đồ đường gom nhập vào đường chính có ghi chữ '250m': Chỉ dẫn vị trí nhập làn xe cách 250 mét.",
    
    466: "Biển 1 và Biển 2 (nhập làn từ bên phải hoặc từ bên trái): Cả hai biển này đều là biển chỉ dẫn 'Nhập làn xe'.",
    
    467: "Biển chỉ dẫn cao tốc màu xanh lá cây: Báo hiệu bắt đầu đường cao tốc, tên/ký hiệu tuyến cao tốc, cùng với tốc độ tối đa (120 km/h) và tốc độ tối thiểu (60 km/h) được phép chạy.",
    
    468: "Ý nghĩa 4 biểu tượng từ trái qua phải: 1. Cây xăng (xăng dầu); 2. Dao nĩa (ăn uống); 3. Chữ i (thông tin chỉ dẫn); 4. Cờ lê (sửa chữa xe).",
    
    469: "Biển vẽ hình cân tải trọng xe kèm khoảng cách '750m': Chỉ dẫn khoảng cách đến trạm kiểm tra tải trọng xe cách 750 mét.",
    
    470: "Biển 1 có mũi tên màu vàng uốn lượn chếch sang bên trái: Chỉ dẫn người lái xe đi theo HƯỚNG BÊN TRÁI để tránh chướng ngại vật.",
    
    471: "Biển 3 có mũi tên chỉ vòng sang bên phải: Chỉ dẫn người lái xe đi theo HƯỚNG BÊN PHẢI để tránh chướng ngại vật.",
    
    472: "Biển 2 có hai mũi tên tỏa sang cả bên trái và bên phải: Chỉ dẫn người lái xe ĐI ĐƯỢC CẢ HAI HƯỚNG (trái hoặc phải) để tránh chướng ngại vật.",
    
    473: "Biển 1 và Biển 3 có các vạch sơn vàng đen so le nghiêng (biển cảnh báo khúc cua gấp): Báo hiệu người lái xe phải chú ý đổi hướng đi khi sắp vào đường cong nguy hiểm.",
    
    474: "Biển 2 có hai nhánh mũi tên mở sang hai bên: Chỉ dẫn người lái xe có thể đi được cả hai hướng quanh chướng ngại vật.",
    
    475: "Biển hình mũi tên chữ V xếp liên tiếp: Là biển chỉ dẫn hướng rẽ, nhắc nhở người lái xe chuẩn bị đổi hướng khi sắp vào đường cong nguy hiểm có bán kính cong nhỏ.",
    
    476: "Vạch số 3 trên mặt đường kết hợp mũi tên thẳng đứng và mũi tên rẽ phải: Cho phép các xe đi trên làn này 'Chỉ được đi thẳng và rẽ phải'.",
    
    477: "Quy chuẩn màu vạch kẻ đường: VẠCH MÀU TRẮNG dùng để phân chia các làn xe chạy CÙNG CHIỀU nhau. Do đó Vạch 1 và Vạch 2 (đều màu trắng) là vạch phân chia các làn xe cùng chiều.",
    
    478: "Vạch 2 là VẠCH VÀNG NÉT LIỀN (vạch tim đường): Dùng để phân chia hai chiều xe chạy ngược chiều nhau, các phương tiện TUYỆT ĐỐI KHÔNG ĐƯỢC LẤN LÀN VÀ KHÔNG ĐƯỢC ĐÈ VẠCH.",
    
    479: "Quy chuẩn màu vạch: VẠCH MÀU VÀNG là vạch tim đường phân chia hai chiều xe chạy ngược chiều nhau (cả vạch đứt nét 1 và vạch đôi liền nét 3). Do đó chọn Vạch 1 và Vạch 3.",
    
    480: "Các vạch sơn màu vàng: Có tác dụng 'Phân chia hai chiều xe chạy ngược chiều nhau' (vạch tim đường).",
    
    481: "Các vạch sơn màu trắng: Có tác dụng 'Phân chia các làn xe chạy cùng chiều nhau'.",
    
    482: "Quy tắc nét vẽ vạch đường: VẠCH NÉT ĐỨT thì ĐƯỢC PHÉP ĐÈ VẠCH (chuyển làn); vạch nét liền cấm đè vạch. Trong hình, Vạch 1 và Vạch 3 là vạch nét đứt nên các xe được phép đè vạch.",
    
    483: "Vạch các đường ngang song song cắt ngang làn đường với khoảng cách tăng dần (Vạch 7.4): Dùng để 'Xác định khoảng cách an toàn giữa các phương tiện' khi lưu thông trên cao tốc.",
    
    484: "Vạch hình quả trám (hình thoi) màu trắng kẻ trên mặt đường (Vạch 7.6): Báo hiệu 'Sắp đến chỗ có bố trí vạch kẻ đường dành cho người đi bộ qua đường', người lái cần chủ động giảm tốc độ.",
    
    485: "Vạch sơn màu vàng hình chữ M (đường dích dắc) trên mặt đường: Báo hiệu 'Vị trí dừng đón trả khách của các phương tiện giao thông vận tải công cộng' (trạm dừng xe buýt), các xe khác không được dừng đỗ gây cản trở."
}

