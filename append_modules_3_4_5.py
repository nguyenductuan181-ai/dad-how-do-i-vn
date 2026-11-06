import os

modules_data = [
    # Module 3: Xe cộ cơ bản (21-30)
    ("21_thay_lop_xe_du_phong_o_to.md", "Thay bánh xe dự phòng ô tô khi xịt lốp",
"""# Thay bánh xe dự phòng ô tô khi xịt lốp

### Bố bảo này:
Đang lái xe trên cao tốc hay đường vắng mà xe bị dính đinh xịt lốp là tình huống người đàn ông phải bước xuống giải quyết dứt khoát và bình tĩnh. Không cần chờ cứu hộ cả tiếng đồng hồ nếu con nắm chắc quy trình an toàn này.

### Đồ nghề có sẵn trên xe:
* Bánh xe dự phòng.
* Con đội nâng xe (kích chữ X hoặc kích thủy lực).
* Cần tuýp mở ốc bánh xe (chữ L hoặc chữ thập).
* Biển tam giác cảnh báo phản quang.

### 5 bước làm chuẩn xác:
1. **Đỗ xe an toàn tuyệt đối:** Tấp xe vào lề phẳng, bật đèn cảnh báo nguy hiểm (đèn hazard). Kéo phanh tay hết cỡ, về số P (xe tự động) hoặc số 1/số lùi (xe số sàn). Đặt biển cảnh báo phía sau xe ít nhất 30-50m.
2. **NỚI LỎNG ỐC KHI BÁNH CÒN TRÊN MẶT ĐẤT (Cực kỳ quan trọng):** Đặt đầu tuýp vào ốc tắc-kê, xoay ngược chiều kim đồng hồ để nới lỏng từng ốc khoảng 1 vòng (không tháo rời hẳn). Nếu ốc chặt quá, có thể dùng trọng lượng cơ thể đạp dứt khoát một chân lên cán tuýp để phá khóa ren.
3. **Kê con đội nâng xe:** Tìm đúng gờ thép chịu lực dưới gầm xe gần bánh bị xịt (có 2 khấc định vị nhỏ trên thanh dầm). Quay kích nâng xe lên cho đến khi đáy lốp cách mặt đất khoảng 3-5 cm.
4. **Thay lốp dự phòng:** Tháo hết các ốc ra, nhấc bánh xịt ra ngoài và luồn ngay chiếc bánh xịt vào dưới gầm xe cạnh con đội (biện pháp an toàn lỡ kích bị sụp gầm). Lắp bánh dự phòng vào trục, vặn các ốc bằng tay kịch ren.
5. **Hạ xe và siết ốc đối xứng hình ngôi sao:** Hạ kích cho bánh chạm mặt đất rồi rút kích ra. Dùng cần tuýp siết chặt các ốc theo **thứ tự đối xứng chéo nhau hình ngôi sao** để mâm xe áp đều vào may-ơ, không bị vênh.

### Lời dặn an toàn:
Bánh xe dự phòng thường là loại bánh nhỏ tạm thời, chỉ nên chạy với tốc độ tối đa dưới 80 km/h và phải ghé ngay tiệm vá lốp gần nhất để vá lại bánh chính.
"""),

    ("22_cau_binh_ac_quy_o_to.md", "Kỹ thuật câu bình kích điện ắc-quy ô tô",
"""# Kỹ thuật câu bình kích điện ắc-quy ô tô

### Bố bảo này:
Quên tắt đèn pha qua đêm hoặc xe để cả tháng không đi sẽ làm ắc-quy cạn sạch điện, vặn chìa khóa chỉ nghe tiếng tạch tạch bất lực. Kẹp nhầm cực khi câu bình có thể làm cháy nổ bình ắc-quy và phá hủy hộp điều khiển ECU điện tử của xe. Con phải thuộc nằm lòng thứ tự kẹp dây này.

### Quy tắc bất biến: ĐỎ DƯƠNG (+) - ĐEN ÂM (-)

### 4 bước kẹp dây chuẩn xác:
1. **Chuẩn bị:** Đỗ xe mồi (xe khỏe) đối diện hoặc song song xe hết điện, tắt máy cả hai xe, kéo phanh tay.
2. **Kẹp theo thứ tự chuẩn:**
   * Kẹp kẹp màu ĐỎ vào **cực DƯƠNG (+)** của ắc-quy xe hết điện.
   * Kẹp đầu kẹp màu ĐỎ còn lại vào **cực DƯƠNG (+)** của ắc-quy xe mồi.
   * Kẹp kẹp màu ĐEN vào **cực ÂM (-)** của ắc-quy xe mồi.
   * Kẹp đầu kẹp màu ĐEN còn lại vào **khung kim loại trần hoặc khối động cơ** của xe hết điện (đoạn kim loại không sơn, cách xa bình ắc-quy ít nhất 30cm để tránh tia lửa điện bén vào khí hydro bốc ra từ bình).
3. **Kích nổ:** Nổ máy xe mồi trước, đạp ga nhẹ giữ vòng tua khoảng 2.000 vòng/phút trong 3-5 phút để nạp điện qua xe cạn. Sau đó, bước sang xe hết điện và đề nổ máy.
4. **Tháo dây theo THỨ TỰ NGƯỢC LẠI hoàn toàn:**
   * Tháo kẹp ĐEN khỏi khung xe hết điện → Tháo kẹp ĐEN khỏi cực âm xe mồi.
   * Tháo kẹp ĐỎ khỏi xe mồi → Tháo kẹp ĐỎ khỏi xe hết điện.

### Lời dặn của Bố:
Sau khi nổ máy thành công, để xe nổ máy chạy liên tục ít nhất 20-30 phút để máy phát điện kịp sạc lại ắc-quy, đừng vội tắt máy ngay.
"""),

    ("23_kiem_tra_va_cham_dau_dong_co.md", "Cách thăm que dầu và châm nhớt động cơ",
"""# Cách thăm que dầu và châm nhớt động cơ

### Bố bảo này:
Dầu nhớt chính là máu nuôi sống động cơ xe. Thiếu dầu sẽ làm các piston bó kẹt gãy tay biên, sửa lại mất hàng chục đến hàng trăm triệu. Thăm dầu xe định kỳ mỗi tháng một lần là thói quen của người chủ xe có trách nhiệm.

### 4 bước thăm dầu chuẩn xác:
1. **Đậu xe trên mặt phẳng:** Tắt máy và chờ khoảng 5-10 phút cho toàn bộ dầu trên dàn cam chảy dồn hết về đáy các-te.
2. **Rút que thăm lần 1 để lau sạch:** Mở nắp capo, tìm que thăm dầu (thường có vòng nhựa màu vàng hoặc cam nổi bật). Rút que thăm ra, lấy khăn sạch hoặc giấy ăn lau khô hoàn toàn đoạn vạch đo ở đầu que.
3. **Cắm que thăm lần 2 để đo:** Cắm que thăm ngập sâu trở lại vị trí cũ đến kịch nấc, sau đó rút ra lại.
4. **Đọc mức dầu:**
   * Mức dầu nằm ở **giữa vạch MIN và MAX** (hoặc giữa 2 lỗ tròn nhỏ): Hoàn hảo.
   * Mức dầu nằm ở **dưới vạch MIN**: Đang thiếu dầu nghiêm trọng, phải châm thêm ngay.
   * Quan sát màu dầu: Màu hổ phách trong hoặc nâu nhạt là tốt; nếu màu đen đặc quánh như hắc ín và có mùi khét là đã đến lúc phải thay dầu mới cùng lọc dầu.

### Cách châm dầu:
Mở nắp châm nhớt trên đỉnh máy (có biểu tượng bình dầu nhỏ). Châm từng lượng nhỏ khoảng 200-300ml, chờ 2 phút rồi rút que thăm lại, không đổ ào ạt vượt quá vạch MAX kẻo làm nặng máy và sủi bọt nhớt.
"""),

    ("24_cham_nuoc_lam_mat_va_nuoc_rua_kinh.md", "Châm nước làm mát và nước rửa kính chắn gió",
"""# Châm nước làm mát và nước rửa kính chắn gió

### Bố bảo này:
Nắp bình nước làm mát là một trong những vị trí nguy hiểm nhất dưới nắp capo nếu con không biết nguyên lý áp suất hơi nước. Rất nhiều người đã bị bỏng nước sôi rộp cả cánh tay chỉ vì vội vàng mở nắp két nước khi máy còn nóng.

### CẢNH BÁO TỐI QUAN TRỌNG:
**Tuyệt đối không bao giờ mở nắp két nước kim loại khi động cơ vừa hoạt động xong.** Hệ thống làm mát là bình kín áp suất cao, nước bên trong nóng hơn 100 độ C. Mở ra nước sôi sẽ phụt thẳng vào mặt như núi lửa. Phải chờ máy nguội hoàn toàn sau ít nhất 45 phút.

### Cách châm nước làm mát đúng cách:
1. Chỉ châm vào **Bình nước phụ** (bình nhựa màu trắng trong có vạch MIN - MAX), không cần mở nắp két sắt chính.
2. Mở nắp bình nhựa, châm dung dịch nước làm mát chuyên dụng (loại màu xanh lá hoặc màu đỏ/hồng có pha chất chống đông và ức chế rỉ sét) đến mức nằm giữa vạch MIN và MAX.
3. Trong trường hợp khẩn cấp giữa đường không có nước làm mát, có thể châm tạm nước tinh khiết đóng chai (Aquafina/Lavie), sau đó phải súc rửa thay lại nước làm mát chuẩn sớm.

### Châm nước rửa kính chắn gió:
* Tìm nắp bình nhựa có biểu tượng kính chắn gió và tia nước phun hình quạt.
* Châm nước rửa kính chuyên dụng (hoặc nước sạch pha vài giọt nước rửa chén) đầy đến gần cổ bình rồi đóng chặt nắp.
"""),

    ("25_thay_can_gat_mua_o_to.md", "Cách tự tháo và thay lưỡi cần gạt mưa ô tô",
"""# Cách tự tháo và thay lưỡi cần gạt mưa ô tô

### Bố bảo này:
Mùa mưa đến mà cần gạt mưa gạt qua để lại những vệt nước nhòe nhoẹt hay kêu rít ken két trên kính lái sẽ làm tầm nhìn bị mù mịt cực kỳ nguy hiểm khi chạy đêm. Thay lưỡi gạt mưa mất đúng 3 phút và tiết kiệm được tiền công thợ.

### Đồ nghề cần chuẩn bị:
* Cặp lưỡi gạt mưa mới đúng kích thước theo xe (đo chiều dài bằng inch, vd: 24 inch bên lái và 16 inch bên phụ).
* 1 chiếc khăn tắm dày lót kính.

### 4 bước làm dứt điểm:
1. **Lót khăn bảo vệ kính lái (Bắt buộc):** Trải chiếc khăn tắm dày ngay dưới chân cần gạt trên kính lái. Lực lò xo của cần gạt kim loại rất mạnh; nếu tuột tay làm cần gạt bật thẳng vào kính chắn gió sẽ gây nứt vỡ kính ngay lập tức.
2. **Dựng cần gạt:** Nâng cần gạt mưa đứng vuông góc với mặt kính. Xoay lưỡi gạt ngang ra để lộ khớp nối móc chữ U (chuẩn móc phổ biến nhất trên xe ô tô).
3. **Bấm lẫy tháo lưỡi cũ:** Tìm cái lẫy nhựa nhỏ ở khớp móc chữ U, dùng ngón tay bấm thụt lẫy xuống đồng thời kéo lưỡi gạt trượt dọc xuống phía dưới để nhả móc chữ U ra ngoài.
4. **Gài lưỡi mới:** Luồn đầu móc chữ U vào ngàm của lưỡi gạt mưa mới, kéo mạnh ngược lên phía trên cho đến khi nghe tiếng "tách" giòn giã là ngàm đã khóa chặt. Nhẹ nhàng hạ cần gạt tựa vào kính rồi thử xịt nước gạt kiểm tra.

### Lời dặn của Bố:
Mỗi khi rửa xe, dùng khăn ẩm lau sạch bụi cát bám dọc lưỡi cao su gạt mưa, tuổi thọ của gạt sẽ tăng gấp đôi.
"""),

    ("26_kiem_tra_ap_suat_va_bom_lop.md", "Đo áp suất lốp xe và bơm lốp đúng chuẩn tải trọng",
"""# Đo áp suất lốp xe và bơm lốp đúng chuẩn tải trọng

### Bố bảo này:
Lốp non hơi làm xe chạy ỳ ạch, ăn tốn xăng thêm 15% và dễ bị nổ lốp do ma sát sinh nhiệt uốn gập thành lốp liên tục. Lốp quá căng lại làm xe nảy xóc tung người và mất độ bám đường khi phanh gấp.

### Xem chỉ số áp suất lốp chuẩn ở đâu?
Không xem con số in trên hông lốp (đó là áp suất tối đa lốp chịu được). Hãy mở cửa lái xe ô tô ra, nhìn vào miếng tem kim loại dán trên **cột B cạnh ghế lái**. Ở đó ghi rõ áp suất khuyên dùng (thường là 2.2 đến 2.4 bar, tương đương 32 đến 35 PSI).

### 4 bước bơm lốp chuẩn:
1. **Đo khi lốp nguội:** Đo áp suất chuẩn nhất là vào buổi sáng trước khi lăn bánh hoặc sau khi xe đã đỗ nghỉ ít nhất 2 tiếng. Lốp chạy nóng lên áp suất sẽ tăng ảo khoảng 3-4 PSI.
2. **Tháo nắp van lốp:** Xoay nắp van cao su ngược chiều kim đồng hồ. Cắm chặt đầu đồng hồ đo áp suất vào ti van, ấn dứt khoát không để xì hơi xè xè ra ngoài để đọc chỉ số.
3. **Bơm hơi:** Cắm tẩu bơm điện mini vào cổng 12V trên xe (nhớ nổ máy xe để không cạn ắc-quy). Cài đặt áp suất tự ngắt theo thông số chuẩn (vd: 2.3 bar). Bấm nút bơm cho máy chạy đến khi tự ngắt.
4. **Vặn chặt nắp van:** Đậy nắp van lại ngay để ngăn cát bụi lọt vào làm kẹt ti van xì hơi ngầm.

### Lời dặn của Bố:
Đừng quên kiểm tra và bơm luôn cả bánh xe dự phòng dưới cốp sau mỗi 3 tháng, tránh tình huống khi cần đến thì bánh dự phòng cũng xẹp lép.
"""),

    ("27_tang_xich_va_tra_dau_xe_may.md", "Cách tăng sên xích và tra dầu bôi trơn nhông sên đĩa xe máy",
"""# Cách tăng sên xích và tra dầu bôi trơn nhông sên đĩa xe máy

### Bố bảo này:
Chiếc xe máy số chạy qua gờ giảm tốc nghe tiếng xích văng đập "lạch cạch" vào hộp bảo vệ là dấu hiệu sên đã bị chùng quá mức. Xích quá chùng rất dễ bị tuột xích hoặc đứt xích khóa cứng bánh sau khi đang chạy tốc độ cao.

### Đồ nghề cần chuẩn bị:
* Cờ-lê hoặc tròng 17mm (bên tán trục) và 14mm hoặc 19mm (tùy dòng xe Honda/Yamaha).
* Cờ-lê nhỏ 10mm hoặc 12mm để vặn ốc tăng sên.
* Chai xịt dưỡng xích hoặc chai nhớt xe sạch.

### 4 bước làm dứt điểm:
1. **Dựng chân chống đứng:** Dựng xe thăng bằng trên nền phẳng vững chãi, trả số về N (mo) để bánh sau quay tự do.
2. **Nới lỏng trục bánh sau:** Dùng cờ-lê tròng nới lỏng con tán trục bánh sau khoảng 1-2 vòng (chỉ nới lỏng để bánh dịch chuyển được, không tháo rời). Nới lỏng ốc giữ pát thắng (phanh) sau nếu có.
3. **Tăng sên đều 2 bên:** Dùng cờ-lê nhỏ vặn ốc tăng sên ở hai bên càng xe theo chiều kim đồng hồ. **Quan trọng nhất:** Nhìn vào các vạch khấc chia độ dập trên càng xe, số vạch ở bên trái và bên phải phải chính xác tuyệt đối bằng nhau để bánh sau không bị lệch tâm.
4. **Đo độ chùng chuẩn:** Dùng ngón tay đẩy nhánh xích dưới lên xuống: Độ võng dao động chuẩn từ **2cm đến 3cm** là vừa đẹp. Siết chặt tán trục bánh sau lại hết lực tay. Xoay tròn bánh sau kiểm tra xem xích có điểm nào bị căng quá không rồi xịt một lớp dầu dưỡng sên mỏng lên mặt trong của mắt xích.

### Lời dặn an toàn:
Tuyệt đối không nổ máy gài số cho bánh sau tự quay khi đang tra dầu xích bằng tay hoặc giẻ lau, lực cuốn của đĩa xích có thể nghiền nát ngón tay con trong chớp mắt. Hãy quay bánh bằng tay trần.
"""),

    ("28_thay_bong_den_pha_xe_may.md", "Thay bóng đèn pha xe máy bị cháy",
"""# Thay bóng đèn pha xe máy bị cháy

### Bố bảo này:
Đang chạy xe buổi tối trên đường quốc lộ không đèn đường mà đèn pha vụt tắt là tình huống cực kỳ nguy hiểm. Tự biết cách thay bóng đèn pha xe máy sẽ giúp con chủ động trên mọi hành trình phượt hay công tác.

### Đồ nghề cần chuẩn bị:
* Bóng đèn pha mới đúng chuẩn chân cắm (xe số phổ thông thường là chân M5 hoặc H4 12V 35W/35W).
* Tua-vít 4 cạnh.
* Khăn sạch khô.

### 4 bước làm dứt điểm:
1. **Tháo ốp đầu xe:** Tháo 4 đến 6 con ốc 4 cạnh giữ phần mặt nạ đầu xe và bợ cổ. Nhẹ nhàng bóp các lẫy nhựa để tách phần ốp nhựa ra mà không làm gãy gờ ngàm.
2. **Rút giắc cắm và chụp cao su:** Rút giắc cắm điện 3 chân phía sau đuôi đèn. Tháo chụp cao su chống nước bao quanh đuôi bóng đèn ra.
3. **Mở chốt cài lò xo:** Dùng ngón tay ấn nhẹ thanh lẫy cài lò xo bằng thép xuống và gạt sang một bên để mở khóa ngàm. Rút bóng đèn cũ bị đứt tóc ra ngoài.
4. **Lắp bóng mới (Bí quyết giữ độ bền):** Đặt bóng mới vào đúng 3 ngấn định vị trên chóa đèn. **LƯU Ý:** Tuyệt đối không dùng ngón tay trần chạm trực tiếp vào phần bầu thủy tinh của bóng đèn mới; mồ hôi và dầu từ da bám vào thủy tinh khi bật đèn sáng nhiệt độ cao sẽ làm bóng bị đen và nổ tim rất nhanh. Hãy cầm bóng bằng khăn sạch hoặc cầm phần đế kim loại. Cài lại chốt lò xo, chụp kín lại chụp cao su và cắm lại giắc điện.

### Lời dặn của Bố:
Trước khi bắt vít ốp đầu xe lại, hãy nổ máy bật thử cả pha (chiếu xa) và cos (chiếu gần) xem tim đèn có sáng chuẩn xác không.
"""),

    ("29_xu_ly_xe_may_ngap_nuoc_chet_may.md", "Xử lý xe máy bị chết máy khi lội đường ngập nước",
"""# Xử lý xe máy bị chết máy khi lội đường ngập nước

### Bố bảo này:
Đường phố Sài Gòn hay Hà Nội vào mùa mưa ngập như sông. Khi xe bị nước tràn vào ống xả hoặc bu-gi làm chết máy, cách hành xử trong 60 giây đầu tiên quyết định xe con chỉ tốn 50k vệ sinh hay phải rã máy tốn cả chục triệu.

### ĐIỀU CẤM KỴ DUY NHẤT:
**Tuyệt đối KHÔNG cố bấm đề nổ máy lại nhiều lần khi xe vừa chết máy trong vũng nước ngập.** Nếu nước đã lọt vào buồng đốt, hành động đề máy sẽ gây ra hiện tượng "thủy kích", piston đâm vào khối nước không nén được làm cong gãy tay biên nứt vỡ lốc máy ngay lập tức.

### 4 bước cấp cứu xe tại chỗ:
1. **Dắt xe lên chỗ khô ráo:** Tắt khóa điện ngay lập tức, dắt xe thoát khỏi vùng ngập nước lên vỉa hè cao ráo.
2. **Dựng đứng xe dốc nước ống pô:** Dựng chân chống đứng, dùng tay nhấc bổng đầu xe lên cao để nước lọt vào trong cổ ống xả (ống pô) chảy dốc hết ra ngoài đằng đuôi pô.
3. **Tháo và lau khô bu-gi:** Dùng tuýp mở bu-gi (nằm trong bộ đồ nghề theo xe) tháo bu-gi ra. Lấy khăn giấy lau thật khô đầu đánh lửa. Đạp cần khởi động 5-10 lần (không bật chìa khóa) để piston đẩy toàn bộ hơi nước đọng trong xi-lanh xịt ra ngoài qua lỗ bu-gi.
4. **Lắp bu-gi và nổ máy:** Lắp bu-gi lại, bật chìa khóa, kéo nhẹ ga và đạp cần khởi động bằng chân dứt khoát. Khi máy nổ được, giữ ga đều tay trong 3 phút để hơi nóng sấy khô hoàn toàn động cơ.

### Lời dặn của Bố:
Về đến nhà, rút que thăm nhớt kiểm tra ngay: Nếu dầu nhớt biến thành **màu trắng đục như sữa đậu nành**, nghĩa là nước đã tràn vào các-te hòa lẫn với nhớt. Phải đi thay ngay can nhớt mới và súc rửa lốc máy, không được tiếp tục chạy xe.
"""),

    ("30_rua_xe_dung_cach_khong_xuoc_son.md", "Rửa xe 2 xô đúng cách không xước xoáy sơn",
"""# Rửa xe 2 xô đúng cách không xước xoáy sơn

### Bố bảo này:
Mang xe ra tiệm rửa nhanh người ta thường dùng một chiếc giẻ lau đầy cát chà khắp từ gầm bánh lên đến nắp capo, làm bề mặt sơn bóng nhẫy những vết xước xoáy mạng nhện dưới ánh mặt trời. Chiếc xe sạch bóng là niềm kiêu hãnh của người đàn ông.

### Phương pháp 2 Xô kinh điển:
* **Xô 1:** Chứa nước sạch pha xà bông rửa xe chuyên dụng (độ pH trung tính).
* **Xô 2:** Chỉ chứa nước lã sạch để giặt xả giẻ bẩn.

### 4 bước rửa chuẩn chuyên gia:
1. **Xịt xả bùn đất thô:** Dùng vòi xịt nước rửa từ trên nóc xe xuống dưới gầm để làm trôi hết các hạt cát to và bùn đất bám ngoài. Tuyệt đối không chạm tay hay giẻ vào sơn lúc này.
2. **Quy tắc rửa từ trên xuống dưới:** Nhúng găng tay rửa xe sợi microfiber mềm vào Xô 1, lau nhẹ nhàng phần nóc xe, kính và nắp capo trước. Lau theo đường thẳng song song, không chà xoay tròn (vì chà tròn sẽ tạo vết xước quầng mạng nhện).
3. **Giặt giẻ liên tục ở Xô 2:** Sau mỗi mảng lau, nhúng găng vào Xô 2 giũ thật mạnh cho cát bẩn rơi lắng xuống đáy, vắt khô rồi mới nhúng lại vào Xô 1 lấy bọt xà phòng tiếp tục lau mảng khác.
4. **Lau khô dứt điểm bằng khăn bản to:** Xịt sạch bọt xà phòng bằng nước lã. Dùng khăn lau xe chuyên dụng bản lớn trải phẳng trên bề mặt sơn và kéo nhẹ một đường để hút hết nước đọng, không để các giọt nước tự khô dưới nắng tạo thành vết ố cặn canxi loang lổ.

### Lời dặn của Bố:
Dùng riêng một chiếc giẻ cũ chuyên biệt cho mâm lốp và gầm xe, không bao giờ dùng chung giẻ đó lên bề mặt sơn vỏ xe.
"""),

    # Module 4: Bộ Đồ Nghề Đàn Ông Cần Có (31-40)
    ("31_chiec_bua_va_ky_thuat_dong_dinh.md", "Chiếc búa và kỹ thuật đóng đinh không cong ngón",
"""# Chiếc búa và kỹ thuật đóng đinh không cong ngón

### Bố bảo này:
Chiếc búa là công cụ nguyên thủy và quyền năng nhất của người thợ. Đóng một chiếc đinh thẳng tắp, cắn ngập vào thớ gỗ mà không làm cong đinh hay dập tím móng tay là bài học vỡ lòng đầu tiên của sự khéo léo.

### Chọn búa chuẩn:
Nên chọn loại **búa nhổ đinh (Claw Hammer)** nặng khoảng 450g đến 500g (16 oz), cán bằng sợi thủy tinh bọc cao su hoặc cán gỗ đầm chắc, đầu có đuôi cong xẻ rãnh chữ V để bẩy nhổ đinh.

### 3 bước đóng đinh chuẩn xác:
1. **Cầm búa đúng vị trí (Lỗi 90% người mới mắc):** Không cầm sát vào đầu kim loại của búa. Hãy cầm tay lùi hẳn về phía **đuôi cán búa**. Cầm ở đuôi cán mới tận dụng được tối đa cánh tay đòn tạo lực gõ uy lực mà tốn ít sức nhất.
2. **Định vị đinh nhẹ nhàng:** Dùng ngón cái và ngón trỏ giữ nhẹ thân đinh vuông góc 90 độ với mặt gỗ. Gõ nhẹ 2-3 nhịp ngắn bằng lực cổ tay cho mũi đinh cắm ngập chắc vào gỗ khoảng vài milimet.
3. **Rút tay và vung búa dứt khoát:** Rút bàn tay giữ đinh ra xa. Vung búa bằng sự phối hợp nhịp nhàng giữa khớp khuỷu tay và cổ tay, gõ vuông góc mặt búa vào đúng tâm mũ đinh. Lực gõ dứt khoát và chuẩn xác sẽ đóng chiếc đinh ngập sâu phẳng mặt gỗ chỉ sau 3 nhát búa.

### Mẹo nhổ đinh không xước gỗ:
Khi dùng đuôi búa bẩy nhổ đinh cũ, hãy chêm một mẩu gỗ vụn hoặc miếng bìa các-tông dày dưới đầu búa. Mẩu gỗ sẽ làm điểm tựa nâng cao lực bẩy đòn gánh và chống làm móp méo bề mặt gỗ xung quanh.
"""),

    ("32_tuoc_no_vit_hai_canh_va_bon_canh.md", "Sử dụng tuốc-nơ-vít đúng cỡ đầu ốc để không trờn ren",
"""# Sử dụng tuốc-nơ-vít đúng cỡ đầu ốc để không trờn ren

### Bố bảo này:
Một con ốc bị trờn toét rãnh ren (tuôn đầu ốc) thành hình tròn là cơn ác mộng lớn nhất trong sửa chữa cơ khí. Nguyên nhân duy nhất gây trờn ốc là dùng sai kích cỡ tuốc-nơ-vít hoặc chỉ biết vặn mà không biết ấn.

### Phân biệt 2 loại đầu thông dụng:
* **Đầu dẹp (Slotted / 2 cạnh):** Dùng cho ốc rãnh đơn thẳng hàng.
* **Đầu bake (Phillips / 4 cạnh):** Thường có các cỡ chuẩn PH0, PH1, PH2, PH3. Đa số ốc trong đồ gia dụng, xe cộ là cỡ **PH2**. Dùng mũi PH1 nhỏ cắm vào ốc PH2 lỏng lẻo sẽ làm toét đầu ốc ngay nhát vặn đầu tiên.

### Quy tắc vàng: 70% LỰC ẤN - 30% LỰC XOAY
1. Đặt mũi tuốc-nơ-vít cắm thẳng đứng 90 độ ngập sâu hoàn toàn vào rãnh ốc.
2. Dồn 70% lực của cả bàn tay và trọng lượng cơ thể **ấn miết mạnh về phía trước** để giữ mũi vít không bị trượt nẩy ra ngoài rãnh.
3. Chỉ dùng 30% lực còn lại của cổ tay để xoay ngược chiều kim đồng hồ (mở ra) hoặc thuận chiều kim đồng hồ (siết vào).

### Cách cứu con ốc bị trờn đầu:
Đặt một mẩu dây thun cao su dày (dây chun buộc tiền) hoặc một mẩu giấy ráp đè lên trên đầu con ốc bị toét, sau đó cắm đầu tuốc-nơ-vít đè chặt lên miếng thun rồi vặn. Cao su sẽ lấp đầy khe hở và tạo ma sát cực lớn giúp vặn ốc ra dễ dàng.
"""),

    ("33_mo_let_va_co_le_vong_mieng.md", "Mỏ lết và cờ-lê: Cách siết và nhả bu-lông không trượt",
"""# Mỏ lết và cờ-lê: Cách siết và nhả bu-lông không trượt

### Bố bảo này:
Mỏ lết đa năng rất tiện vì chỉnh được mọi kích cỡ ốc, nhưng nếu không biết ngàm nào chịu lực thì con sẽ làm toét cạnh bu-lông và trượt tay đập mạnh khớp ngón tay vào khung sắt chảy máu.

### Quy tắc chiều quay của mỏ lết:
Mỏ lết có 2 ngàm: Một ngàm cố định liền với thân cán và một ngàm di động chạy trên con lăn ren.
* **Luôn xoay mỏ lết về phía NGÀM CỐ ĐỊNH chịu lực kéo.** 
* Tuyệt đối không để ngàm di động chịu lực bẻ chính, vì ngàm di động chịu lực quá tải sẽ bị há miệng nứt gãy và làm trượt cạnh ốc.

### Kỹ thuật thao tác an toàn:
1. **Chỉnh khít khao:** Đút ngàm mỏ lết ngập sâu ôm trọn các cạnh của bu-lông, sau đó dùng ngón tay cái lăn con lăn siết chặt hai ngàm ép sát vào mặt ốc, không để có khe hở lỏng lẻo.
2. **KÉO chứ không ĐẨY:** Hãy luôn chọn góc đứng sao cho con dùng lực **kéo cán cờ-lê về phía mình**. Nếu con dùng lực đẩy mỏ lết ra xa, lỡ bu-lông đột ngột bung ren hoặc trượt ngàm, cả bàn tay con sẽ lao thẳng theo quán tính đập vào các góc nhọn sắc bén của kim loại.
3. **Cờ-lê tròng (vòng miệng):** Với những bu-lông bị rỉ sét siết cực chặt, hãy ưu tiên dùng đầu tròng hình tròn có 12 cạnh ôm khít toàn bộ chu vi bu-lông thay vì dùng mỏ lết hở miệng.
"""),

    ("34_cac_loai_kim_co_ban.md", "3 loại kìm cơ bản: Kìm điện, kìm nhọn và kìm mỏ quạ",
"""# 3 loại kìm cơ bản: Kìm điện, kìm nhọn và kìm mỏ quạ

### Bố bảo này:
Đôi bàn tay đàn ông dù khỏe đến đâu cũng không thể bẻ gập sợi thép hay vặn chặt một đai ốc kim loại trơn tuột. Ba cây kìm này là phần nối dài sức mạnh của những ngón tay con.

### 1. Kìm điện (Kìm vạn năng - Linesman Pliers):
* **Đặc điểm:** Đầu kìm vuông vức, phẳng và rất nặng đầm tay. Phần đầu có răng cưa để kẹp giữ, phía trong cổ kìm có hai lưỡi dao thép tôi cứng dùng để cắt đứt dây điện, đinh nhỏ và sợi cáp thép.
* **Công dụng:** Kẹp xoắn các mối nối dây điện to, bẻ gập thanh kim loại, dùng thay búa gõ nhẹ khi cần.

### 2. Kìm nhọn (Kìm mũi dài - Needle-Nose Pliers):
* **Đặc điểm:** Hai mỏ kìm thuôn dài và nhọn dần về phía đầu.
* **Công dụng:** Luồn sâu vào những góc hẹp, khe máy móc sâu hoắm mà ngón tay không thể thò vào được. Dùng để uốn cong sợi dây đồng thành móc tròn bắt vào ốc cọc bình ắc-quy hoặc nhặt các chi tiết ốc vít bị rơi kẹt.

### 3. Kìm mỏ quạ (Kìm nước - Groove Joint Pliers):
* **Đặc điểm:** Đầu kìm cong khoằm như mỏ quạ, có rãnh trượt ở khớp nối cho phép thay đổi độ mở rộng của hàm kẹp từ nhỏ đến rất lớn.
* **Công dụng:** Chuyên gia trị các đường ống nước tròn, bầu xiphông, rắc-co và các đai ốc kích thước lớn mà cờ-lê thông thường không ôm vừa.

### Lời dặn bảo dưỡng:
Định kỳ nhỏ vài giọt dầu máy vào chốt trục giữa của các cây kìm để kìm luôn đóng mở nhẹ nhàng bằng một tay, không bị rỉ sét kẹt cứng.
"""),

    ("35_may_khoan_cam_tay_va_mui_khoan.md", "Máy khoan cầm tay: Chọn mũi khoan tường, gỗ, kim loại",
"""# Máy khoan cầm tay: Chọn mũi khoan tường, gỗ, kim loại

### Bố bảo này:
Cầm chiếc máy khoan bấm hết tốc lực vào tường mà thấy khói bốc mù mịt, mũi khoan đỏ lựng mà không vào được milimet nào nghĩa là con đang lắp nhầm mũi khoan sắt để khoan tường bê tông, hoặc chưa gạt sang chế độ búa.

### Phân biệt 3 loại mũi khoan cơ bản:
1. **Mũi khoan tường / bê tông (Masonry bit):** Đầu mũi có hàn thêm một miếng hợp kim cứng nhô bè sang hai bên như hình mũi tên hoặc đầu xẻng nhỏ. Chuyên dùng để đập vỡ vụn vữa xi măng và đá.
2. **Mũi khoan kim loại / sắt (HSS bit):** Đầu mũi vát chéo nhọn góc 118 độ, toàn thân có các rãnh xoắn sắc bén bóng loáng từ đầu đến đuôi.
3. **Mũi khoan gỗ (Brad point bit):** Chính giữa đỉnh đầu mũi có một cái gai nhọn li ti nhô ra trước để ghim định vị tâm lỗ khoan không bị trượt trên thớ gỗ.

### Chọn chế độ trên thân máy khoan:
* **Biểu tượng cái Búa:** Dùng cho **KHOAN TƯỜNG / BÊ TÔNG**. Cơ cấu bên trong sẽ tạo ra hàng nghìn nhịp đập búa tịnh tiến về phía trước để phá vỡ khối đá.
* **Biểu tượng Mũi khoan:** Dùng cho **KHOAN GỖ, SẮT, NHỰA**. Máy chỉ quay tròn êm ái với tốc độ cao mà không rung đập.

### Lời dặn an toàn:
Khi khoan tường gạch men nhà tắm: Dán một miếng băng dính giấy đè lên mặt men gạch bóng để mũi khoan không bị trượt trầy xước gạch, tắt chế độ búa khoan mồi thủng lớp men bóng trước rồi mới bật chế độ búa khoan sâu vào trong.
"""),

    ("36_thuoc_cuon_va_thuoc_thuy_nivo.md", "Thước cuộn và thước thủy nivo: Bí quyết đo đâu chuẩn đấy",
"""# Thước cuộn và thước thủy nivo: Bí quyết đo đâu chuẩn đấy

### Bố bảo này:
Các cụ thợ mộc xưa có câu: *"Đo hai lần, cắt một lần"*. Cắt hụt một thanh gỗ hay tấm đá dù chỉ 5 milimet là vứt đi cả trăm ngàn tiền vật tư và hỏng cả công trình.

### Bí mật của cái móc đầu thước cuộn:
Nhiều người tưởng cái móc sắt ở đầu thước cuộn bị lỏng lẻo lắc lư là hàng lỗi. Không phải đâu con. Độ rơ lắc lư đó được tính toán chính xác bằng đúng **độ dày của lá móc sắt** (khoảng 1mm):
* Khi con **kéo móc vào cạnh ngoài** vật thể: Lá móc thụt ra để bù trừ độ dày móc.
* Khi con **đẩy ép móc vào góc tường**: Lá móc ép thụt vào để đo chính xác từ mặt trong của thước. Nhờ vậy dù kéo hay đẩy thì chỉ số đo luôn chuẩn từng milimet.

### Cách đọc thước thủy nivo trong 1 giây:
Thước thủy có một ống thủy tinh chứa dung dịch màu xanh lá và một bọt khí tròn nhỏ bên trong:
* **Mặt phẳng nằm ngang:** Đặt thước nằm ngang, bọt khí nằm lọt đúng vào giữa hai vạch đen là phẳng tuyệt đối. Bọt khí lệch về bên nào nghĩa là bên đó đang bị cao hơn.
* **Mặt phẳng thẳng đứng:** Nhìn vào ống thủy tinh dọc, bọt khí nằm giữa hai vạch là cột thẳng đứng 90 độ so với mặt đất.
"""),

    ("37_dao_roc_giay_va_cua_tay.md", "Dao rọc giấy và cưa tay: Cắt an toàn không văng phôi",
"""# Dao rọc giấy và cưa tay: Cắt an toàn không văng phôi

### Bố bảo này:
Lưỡi dao rọc giấy sắc như dao mổ và rất mỏng giòn. Tai nạn đứt tay sâu hoắm do gãy lưỡi dao rọc giấy xảy ra nhiều hơn bất kỳ loại dụng cụ nào trong xưởng làm việc.

### Quy tắc an toàn sống còn với dao rọc giấy:
1. **Chỉ thò ra 1 đốt lưỡi:** Khi cắt bìa các-tông, thảm hay dây thừng, chỉ đẩy lưỡi dao thò ra ngoài miệng kẹp đúng **1 khấc đốt** (khoảng 1-1.5cm). Đẩy lưỡi dao thò ra quá dài khi tì lực mạnh lưỡi thép sẽ bị uốn cong gãy bắn phắt vào mắt hoặc cứa vào tay.
2. **Luôn cắt hướng ra xa người:** Đường đi của lưỡi dao phải luôn hướng ra phía ngoài cơ thể con, tuyệt đối không kéo lưỡi dao hướng ngược về phía bụng hay ngực mình. Tay giữ thước nhôm phải thu gọn các đầu ngón tay lùi vào trong mép thước.
3. **Bẻ đốt dao cũ:** Khi mũi dao bị cùn, kéo lưỡi dao thò ra 1 đốt, dùng khe rãnh ở nắp đuôi dao bẻ cụt đốt cùn theo đúng đường khía rãnh vát. Gói đốt dao gãy vào băng keo trước khi vứt vào thùng rác.

### Cách dùng cưa tay cắt gỗ:
Bắt đầu đường cưa bằng cách kéo cưa ngược về phía mình 2-3 nhịp để tạo một rãnh định vị dẫn hướng. Khi đẩy cưa đi thì không cần đè lực quá nặng, để trọng lượng và răng cưa tự ăn sâu vào thớ gỗ.
"""),

    ("38_bang_keo_dien_va_bang_keo_duc_tape.md", "Băng dính bạc (Duct Tape) và băng keo đen: Cứu cánh tạm thời",
"""# Băng dính bạc (Duct Tape) và băng keo đen: Cứu cánh tạm thời

### Bố bảo này:
Dân kỹ thuật Mỹ có một câu đùa kinh điển nhưng cực kỳ thực tế: *"Nếu một thứ gì đó chuyển động mà nó không nên chuyển động, hãy dùng Duct Tape. Nếu một thứ không chịu chuyển động mà nó nên chuyển động, hãy dùng WD-40"*.

### 1. Băng dính bạc sợi vải (Duct Tape):
* **Đặc tính:** Lớp ngoài chống nước tuyệt đối, lớp giữa dệt bằng các sợi lưới vải chịu lực kéo xé hàng chục kilôgam, lớp keo dính siêu chắc trên mọi bề mặt nhựa, kim loại, gỗ, kính.
* **Ứng dụng:** Cứu cánh dán tạm ống thông gió bị rách, vá bạt che mưa, gia cố cản xe ô tô bị xệ nứt gãy tạm thời để chạy về gara, dán cố định dây điện trên sàn nhà tránh vấp ngã.

### 2. Băng keo đen cách điện (Electrical Tape):
* **Đặc tính:** Làm từ màng nhựa PVC dẻo đàn hồi có khả năng cách ly điện áp lên đến 600V và chịu nhiệt tốt, tự co giãn ôm khít.
* **Cách quấn mối nối điện đúng kỹ thuật:** Khi quấn quanh mối nối dây đồng, phải vừa quấn vừa **kéo căng giãn băng keo ra** khoảng 30% để lớp nhựa co thắt ép chặt vào lõi dây, quấn phủ đè lên nhau 50% diện tích và quấn tràn qua lớp vỏ nhựa cách điện của dây ít nhất 2cm về mỗi phía.
"""),

    ("39_den_pin_sieu_sang_va_den_doi_dau.md", "Đèn pin siêu sáng và đèn đội đầu khi thao tác góc khuất",
"""# Đèn pin siêu sáng và đèn đội đầu khi thao tác góc khuất

### Bố bảo này:
Con không thể sửa chữa một thứ gì đó một cách an toàn và chuẩn xác nếu con không nhìn thấy rõ nó. Dùng miệng ngậm chiếc đèn pin bằng sắt hoặc bật đèn flash điện thoại vừa làm rơi vỡ màn hình vừa cực kỳ bất tiện.

### Giải pháp tối ưu: Chiếc đèn pin đội đầu (Headlamp)
Một chiếc đèn pin đội đầu nhỏ gọn dùng pin sạc type-C có giá chỉ hơn 100 ngàn đồng là vật dụng cứu nguy giá trị nhất khi:
* Cúp điện toàn khu vực giữa đêm tối mịt.
* Chui vào gầm chậu rửa bát tối tăm để sửa ống nước.
* Trèo lên trần thạch cao kiểm tra chuột cắn dây điện.
* Cúi đầu soi gầm xe ô tô giữa đường đèo vắng.

### Lợi ích cốt lõi:
Đèn đội đầu giải phóng hoàn toàn **cả hai bàn tay** để con tự do cầm búa, kìm, tua-vít. Hơn nữa, chùm sáng luôn tự động rọi thẳng vào đúng điểm mắt con đang nhìn tới mà không cần chỉnh góc.

### Lời dặn của Bố:
Luôn kiểm tra và sạc đầy pin cho đèn pin sau mỗi lần sử dụng. Đừng để đến lúc nhà mất điện tối thui mới phát hiện đèn pin đã cạn sạch pin từ nửa năm trước.
"""),

    ("40_hop_do_nghe_toi_gian_cho_can_ho.md", "Xây dựng hộp đồ nghề tối giản cho một căn hộ",
"""# Xây dựng hộp đồ nghề tối giản cho một căn hộ

### Bố bảo này:
Không cần phải sắm nguyên một xưởng mộc cồng kềnh chiếm nửa gian nhà. Một người đàn ông hiện đại sống trong căn hộ chỉ cần đúng một chiếc hộp nhựa đồ nghề nhỏ gọn chứa đủ 10 món binh khí tinh nhuệ này là đủ tự tin giải quyết 95% sự cố lặt vặt trong tổ ấm:

### Danh mục 10 món đồ nghề tối giản:
1. **1 cây búa nhổ đinh (450g):** Đóng đinh, gõ nắn, nhổ đinh.
2. **1 chiếc mỏ lết 200mm (8 inch):** Xử lý vòi nước, đai ốc gia dụng.
3. **1 cây kìm điện đa năng (cắt và kẹp):** Tuốt dây, bẻ kim loại.
4. **1 cây tua-vít đảo đầu (có cả đầu dẹp và 4 cạnh PH2):** Tháo mở hầu hết ốc vít trong nhà.
5. **1 chiếc bút thử điện:** Soi rò điện, kiểm tra ổ cắm có điện không.
6. **1 thước cuộn thép 5 mét:** Đo đạc kích thước mua sắm nội thất.
7. **1 dao rọc giấy lưỡi bẻ:** Rọc mở thùng hàng, gọt cạo ron keo.
8. **1 cuộn băng tan cao su non + 1 cuộn băng keo đen cách điện:** Chống rỉ nước và băng bó điện.
9. **1 chai xịt bôi trơn chống rỉ RP7 nhỏ:** Chống kẹt ổ khóa, chống cửa kêu cọt kẹt.
10. **1 hộp nhỏ đựng ốc vít, tắc-kê nhựa nở và đinh thép:** Luôn có sẵn phụ kiện thay thế.

### Lời dặn của Bố:
Mượn đồ nghề ở đâu thì trả về đúng chỗ đó. Làm xong việc, lau sạch dầu mỡ trên dụng cụ rồi xếp ngay ngắn vào hộp đồ nghề. Đó là tác phong của một người đàn ông kỷ luật.
"""),

    # Module 5: Kỹ Năng Đàn Ông & Quản Trị Cuộc Đời (41-50)
    ("41_ui_ao_so_mi_va_quan_tay.md", "Ủi phẳng áo sơ mi và quần tây trong 5 phút",
"""# Ủi phẳng áo sơ mi và quần tây trong 5 phút

### Bố bảo này:
Người ta có thể tha thứ cho một chiếc áo sơ mi bình dân, nhưng không ai đánh giá cao một người đàn ông mặc chiếc áo nhăn nhúm như lò xo bước vào phòng họp hay buổi hẹn quan trọng. Chiếc áo phẳng phiu thể hiện sự tôn trọng chính mình và người đối diện.

### Thứ tự ủi áo sơ mi chuẩn không nhăn ngược:
Nhiều người ủi vạt áo trước rồi mới ủi cổ và tay, kết quả là ủi xong cổ thì vạt áo lại bị đè nhăn nhúm. Quy tắc đúng là: **Ủi từ chi tiết nhỏ đến mảng lớn.**

1. **Cổ áo:** Trải phẳng mặt sau cổ áo, ủi từ hai đầu mép ngoài vuốt dần vào chính giữa gáy cổ (ủi thế này vải không bị đùn nếp nhăn ở góc ve cổ). Lật mặt trước ủi lại tương tự.
2. **Cổ tay và cầu vai:** Tháo cúc tay áo, ủi phẳng cổ tay. Lồng phần cầu vai áo vào đầu nhọn của bàn ủi để là phẳng phần đệm vai.
3. **Hai cánh tay áo:** Trải phẳng ống tay theo đường chỉ may dưới nách, ủi một đường thẳng tắp từ nách xuống cổ tay tạo đường li sắc nét.
4. **Hai vạt trước và lưng áo:** Ủi vạt áo có hàng cúc trước (dùng mũi bàn ủi luồn vào giữa các cúc áo), sau đó trải phẳng toàn bộ mảng lưng áo lớn ủi một lượt phẳng lỳ từ trên xuống dưới.

### Ủi quần tây tạo nẹp li sắc nét:
Chập 2 đường chỉ may gấu quần lại khớp nhau để định hình đường li trước ống chân. Đặt một chiếc khăn ẩm mỏng đè lên trên ống quần trước khi đặt bàn ủi nóng lên ấn mạnh: Hơi nước bốc ra sẽ tạo nếp li sắc như dao cạo mà vải không bao giờ bị bóng cháy sờn sợi vải.
"""),

    ("42_that_ca_vat_chuan_gentleman.md", "Thắt cà vạt chuẩn Half-Windsor không nhăn cổ áo",
"""# Thắt cà vạt chuẩn Half-Windsor không nhăn cổ áo

### Bố bảo này:
Kiểu thắt cà vạt Half-Windsor là kiểu thắt đa năng, đẹp mắt và cân đối nhất của một quý ông. Nút thắt hình tam giác đều đặn, không quá to thô như Full-Windsor và không bị méo lệch lỏng lẻo như Four-in-Hand.

### Quy chuẩn độ dài:
Sau khi thắt xong, **mũi nhọn của đuôi cà vạt phải chạm đúng ngay mép trên của khóa thắt lưng da**. Đuôi cà vạt lửng lơ trên rốn trông như chú hề; đuôi cà vạt dài thòng lòng qua đũng quần trông cực kỳ luộm thuộm.

### 5 bước thắt chuẩn xác:
1. Đặt cà vạt quanh cổ, bản to nằm bên tay phải, bản nhỏ bên tay trái. Kéo bản to dài hơn bản nhỏ khoảng 30cm.
2. Vắt bản to đè chéo qua phía trước bản nhỏ sang bên trái.
3. Luồn bản to vòng ra phía sau bản nhỏ sang bên phải.
4. Kéo bản to lên trên và luồn ngược vào trong vòng cổ áo kéo xuống phía dưới bên trái để tạo một nút thắt tam giác mồi.
5. Vắt bản to ngang qua mặt trước của nút thắt sang bên phải. Luồn bản to từ dưới lên qua vòng cổ áo, rồi nhét đuôi bản to trượt xuống dưới cái khe nẹp ngang vừa tạo ở bước trước. Kéo nhẹ bản to xuống đồng thời tay kia giữ nút thắt đẩy trượt nhẹ lên sát cổ áo.

### Điểm nhấn của người sành điệu (Dimple):
Trước khi siết chặt nút thắt, dùng ngón trỏ ấn nhẹ một vết lõm chữ V nhỏ ngay chính giữa phía dưới nút thắt. Nếp lún (dimple) tự nhiên này làm chiếc cà vạt có chiều sâu và đẳng cấp hơn hẳn.
"""),

    ("43_cao_rau_sach_khong_rat_da.md", "Kỹ thuật cạo râu mềm da, không xước, không rát",
"""# Kỹ thuật cạo râu mềm da, không xước, không rát

### Bố bảo này:
Cạo râu xong mà mặt đỏ ửng như tôm luộc, rát buốt khi rửa nước lạnh hay mọc đầy những nốt mụn viêm lỗ chân lông là do cạo râu khi da còn khô cứng và cạo ngược hướng sợi lông quá sớm.

### 4 bước cạo râu êm ru:
1. **Làm mềm râu bằng nước ấm:** Cạo râu lý tưởng nhất là ngay sau khi tắm nước ấm xong, hoặc lấy một chiếc khăn thấm nước nóng đắp lên cằm trong 1-2 phút. Hơi nóng và nước sẽ mở rộng lỗ chân lông và làm sợi râu mềm đi 70%.
2. **Đánh bọt kem cạo râu:** Thoa đều kem hoặc bọt cạo râu lên cằm và má, xoa tròn bằng đầu ngón tay để bọt nâng đỡ các sợi râu đứng thẳng lên.
3. **CẠO XUÔI THEO CHIỀU LÔNG MỌC LƯỢT 1:** Lấy tay sờ cằm: Vuốt thấy êm là chiều xuôi lông mọc, vuốt thấy ráp nhám tay là chiều ngược. Lượt cạo đầu tiên, **luôn cạo xuôi theo chiều lông mọc**. Lưỡi dao lướt nhẹ nhàng, không ấn tì mạnh vào da. Rửa lưỡi dao dưới vòi nước sau mỗi đường cạo.
4. **Cạo ngang hoặc ngược nhẹ lượt 2:** Thoa lại một lớp bọt mỏng, lúc này râu đã ngắn sát chân mới cạo chéo ngang hoặc cạo ngược nhẹ để làm sạch nhẵn bóng hoàn toàn.

### Bước khóa ẩm sau khi cạo:
Rửa mặt lại bằng **nước lạnh** để se khít các lỗ chân lông. Vỗ nhẹ một chút dung dịch dưỡng sau cạo (Aftershave có cồn nhẹ hoặc kem dưỡng ẩm) để khử trùng và làm dịu da ngay lập tức.
"""),

    ("44_dinh_lai_cuc_ao_bi_dut.md", "Tự xỏ kim đính lại cúc áo sơ mi bị đứt",
"""# Tự xỏ kim đính lại cúc áo sơ mi bị đứt

### Bố bảo này:
Đang chuẩn bị đi gặp đối tác quan trọng mà chiếc cúc áo ngực bị đứt tuột ra ngoài. Đừng vứt chiếc áo xịn đi hay chạy khắp phố tìm tiệm may vá. Tự tay xỏ kim đính lại chiếc cúc áo chỉ mất 3 phút của một người đàn ông tự lập.

### Đồ nghề cần chuẩn bị:
* 1 cây kim may tay nhỏ.
* 1 đoạn chỉ may cùng màu áo dài khoảng 40-50cm.
* Chiếc cúc áo bị đứt (hoặc lấy chiếc cúc dự phòng may sẵn ở vạt trong dưới cùng của áo sơ mi).
* 1 que tăm nhỏ.

### 4 bước đính cúc chắc chắn:
1. **Xỏ chỉ đôi:** Xỏ chỉ qua lỗ kim, kéo hai đầu bằng nhau rồi thắt một nút gút tròn ở đuôi chỉ.
2. **Kê que tăm tạo khoảng hở (Bí quyết thợ may):** Đặt cúc vào vị trí mép áo. Đặt một que tăm nằm ngang đè lên trên mặt cúc áo.
3. **Khâu chéo hình chữ X (với cúc 4 lỗ):** Đâm kim từ mặt sau của vải áo lên qua lỗ cúc thứ nhất, vắt qua que tăm đâm xuống lỗ đối diện chéo nhau. Lặp lại 4-5 lần cho mỗi cặp lỗ chéo để tạo thành hình chữ X vững chắc.
4. **Quấn chân cúc tạo độ đệm:** Rút que tăm ra ngoài (lúc này cúc sẽ hơi lỏng có một khoảng hở nhỏ so với mặt vải). Đâm kim lên mặt trước nhưng không xuyên qua lỗ cúc mà nằm dưới đáy cúc. Dùng sợi chỉ quấn chặt 3-4 vòng quanh cuống các sợi chỉ bên dưới cúc để tạo thành một "chân cúc" đệm tròn vững chãi. Đâm kim ngược về mặt sau vải, thắt nút giấu mối chỉ rồi cắt chỉ.

### Lời dặn của Bố:
Có chân cúc đệm thì khi con cài cúc qua nẹp áo dày, khuy áo sẽ nằm phẳng êm ru không bao giờ bị nhăn nhúm hay cấn đứt chỉ.
"""),

    ("45_danh_xi_giay_da_bong_guong.md", "Đánh xi và bảo dưỡng giày da bền đẹp",
"""# Đánh xi và bảo dưỡng giày da bền đẹp

### Bố bảo này:
Người xưa bảo: *"Muốn biết tính cách một người đàn ông, hãy nhìn vào đôi giày anh ta đi dưới chân"*. Một bộ vest đắt tiền cũng trở nên rẻ rúng nếu đi cùng một đôi giày da bám bụi đất bẩn thỉu và mốc meo nứt nẻ.

### Đồ nghề cần chuẩn bị:
* 1 bàn chải lông ngựa mềm.
* 1 hộp xi kem (Shoe Cream - dùng để cấp ẩm và phục hồi màu da) hoặc xi sáp (Shoe Wax - dùng để tạo độ bóng gương).
* 1 chiếc khăn cotton mềm sạch (có thể dùng mảnh áo thun cũ).

### 3 bước đánh giày chuẩn:
1. **Làm sạch bụi bẩn khô:** Tháo dây giày ra. Dùng bàn chải lông ngựa chải mạnh toàn bộ bề mặt thân giày, đường chỉ may và kẽ đế giày để hất sạch cát bụi bám ngoài. Lấy khăn hơi ẩm lau qua bề mặt da rồi để khô tự nhiên.
2. **Thoa xi kem dưỡng da:** Quấn góc khăn cotton quanh ngón trỏ và ngón giữa, chấm một lượng xi kem nhỏ bằng hạt đậu. Thoa đều lên bề mặt da theo những vòng tròn nhỏ li ti. Để nguyên trong 10-15 phút cho dầu dưỡng ngấm sâu vào nuôi các thớ da bò không bị khô nứt gãy.
3. **Đánh bóng dứt điểm:** Dùng bàn chải lông ngựa đưa qua đưa lại thật nhanh và đều tay với lực vừa phải. Nhiệt sinh ra từ ma sát sẽ làm tan chảy lớp sáp xi và tạo nên một bề mặt da bóng bẩy, sâu màu và sang trọng.

### Mẹo giữ form giày:
Khi không đi giày, luôn nhét một đôi cây giữ form giày bằng gỗ (Shoe Trees) vào trong. Gỗ sẽ hút sạch mồ hôi chân ẩm ướt và căng phẳng các nếp nhăn gãy ở mũi giày.
"""),

    ("46_so_cuu_vet_bong_va_vet_dut_tay.md", "Sơ cứu vết bỏng nhiệt và vết đứt tay chảy máu",
"""# Sơ cứu vết bỏng nhiệt và vết đứt tay chảy máu

### Bố bảo này:
Khi xảy ra tai nạn thương tích trong gia đình, sự hoảng loạn của người xung quanh sẽ làm tình hình tồi tệ hơn. Người đàn ông phải là mỏ neo bình tĩnh nhất: nắm chắc nguyên tắc sơ cứu y khoa chuẩn xác, không tin vào các mẹo dân gian truyền miệng nguy hiểm.

### 1. Sơ cứu vết bỏng nhiệt (Bỏng nước sôi, bỏng pô xe, bỏng dầu ăn):
* **SAI LẦM CẤM KỴ:** Tuyệt đối không bôi kem đánh răng, mỡ trăn, nước mắm hay chườm đá lạnh trực tiếp lên vết bỏng. Đá lạnh làm co mạch đột ngột gây bỏng lạnh hoại tử da; kem đánh răng chứa kiềm làm vết bỏng loét sâu hơn.
* **HÀNH ĐỘNG DUY NHẤT:** Đặt ngay vùng da bị bỏng dưới **vòi nước mát chảy nhẹ** liên tục trong ít nhất **15 đến 20 phút**. Nước mát sẽ hạ nhiệt độ sâu dưới mô da, ngăn tổn thương lan rộng và giảm đau rát cực nhanh.
* Sau đó băng nhẹ bằng gạc vô trùng sạch. Tuyệt đối không chọc vỡ các bọng nước phồng rộp.

### 2. Sơ cứu vết đứt tay chảy máu:
* **HÀNH ĐỘNG CỐT LÕI: ÉP TRỰC TIẾP LÊN VẾT THƯƠNG.**
* Lấy một miếng gạc sạch hoặc khăn tay sạch ấn chặt trực tiếp lên miệng vết thương đứt rách. Giữ nguyên tay ép chặt liên tục trong ít nhất 5-10 phút (không nhấc khăn lên xem liên tục vì sẽ làm vỡ cục máu đông đang hình thành).
* Nâng cao vùng tay bị thương lên cao hơn mức của tim để giảm áp lực bơm máu đến vết cắt.
* Khi máu đã ngừng chảy, rửa sạch vết thương bằng nước muối sinh lý, bôi thuốc sát trùng povidine và băng lại bằng băng gạc cá nhân Urgo.
"""),

    ("47_kiem_soat_chi_tieu_song_duoi_muc_thu_nhap.md", "Quản lý tiền nong: Quy tắc sống dưới mức thu nhập",
"""# Quản lý tiền nong: Quy tắc sống dưới mức thu nhập

### Bố bảo này:
Một người đàn ông kiếm được 100 triệu một tháng nhưng tiêu hết 98 triệu thì bản chất vẫn là một kẻ nghèo túng và dễ tổn thương trước một cơn bão kinh tế. Tự do tài chính không nằm ở việc con kiếm được bao nhiêu tiền, mà nằm ở việc con **giữ lại được bao nhiêu** và sống thảnh thơi mà không bị nợ nần bóp nghẹt.

### 3 nguyên tắc thép về tiền nong:
1. **Trả cho bản thân mình trước tiên (Pay yourself first):** Ngày nhận lương đầu tháng, trích ngay **20% thu nhập** chuyển thẳng vào một tài khoản tiết kiệm tách biệt không có thẻ ATM quẹt. Đừng chờ chi tiêu cả tháng xong thừa đồng nào mới tiết kiệm; con sẽ không bao giờ thừa đâu.
2. **Quy tắc quỹ khẩn cấp 6 tháng:** Người đàn ông không bao giờ được phép để tài khoản về 0. Con phải luôn có một khoản tiền mặt dự phòng tương đương ít nhất 6 tháng sinh hoạt phí cơ bản của gia đình. Khoản tiền này nằm đó không phải để đầu tư sinh lời, mà để con có được sự bình thản, không phải quỵ lụy hay chấp nhận những điều sỉ nhục chỉ vì miếng cơm manh áo khi công việc gặp biến cố.
3. **Quy tắc chờ 72 giờ trước khi mua sắm đồ đắt tiền:** Khi muốn mua một món đồ công nghệ hay thời trang đắt tiền không thiết yếu, bắt buộc phải dừng lại chờ đúng 3 ngày (72 giờ). Sau 3 ngày mà cơn hưng phấn dopamine qua đi và con vẫn thấy nó thật sự cần thiết cho công việc thì mới mua. 80% trường hợp sau 3 ngày con sẽ nhận ra mình không hề cần nó.

### Lời dặn của Bố:
Đừng vay mượn tiền để mua những món đồ hào nhoáng bên ngoài chỉ nhằm gây ấn tượng với những người con thậm chí còn không hề quen biết hay tôn trọng.
"""),

    ("48_loi_xin_loi_chan_thanh_cua_nguoi_dan_ong.md", "Lời xin lỗi chân thành: Chịu trách nhiệm, không viện cớ",
"""# Lời xin lỗi chân thành: Chịu trách nhiệm, không viện cớ

### Bố bảo này:
Một cậu bé thì cố cãi chày cãi cối, đổ lỗi cho hoàn cảnh hoặc giận dỗi ngược lại khi mình làm sai. Một người đàn ông trưởng thành có đủ bản lĩnh và sự tự tin từ bên trong để đứng thẳng lưng nhìn vào mắt người khác và nói một lời xin lỗi chân thành.

### Cấu trúc một lời xin lỗi chân thành chuẩn mực:
Một lời xin lỗi thật sự chỉ có 3 phần dứt khoát, không bao giờ chứa từ **"NHƯNG"** hay **"TẠI VÌ"**:

1. **Thừa nhận sự thật và nhận 100% trách nhiệm:**
   * *"Anh/Bố đã sai khi làm việc đó. Anh/Bố hoàn toàn nhận trách nhiệm về mình."* (Không nói: *"Anh xin lỗi nhưng tại vì em làm anh bực mình..."* — từ 'nhưng' sẽ xóa sạch toàn bộ lời xin lỗi trước đó).
2. **Thấu cảm cảm xúc của đối phương:**
   * *"Anh hiểu việc làm đó của anh đã khiến em tổn thương / thất vọng / lo lắng đến mức nào."*
3. **Hành động khắc phục thực tế ngay lập tức:**
   * *"Bây giờ anh sẽ làm việc A và việc B để sửa chữa sai lầm này, và anh cam kết sẽ không để việc này tái diễn nữa."*

### Sức mạnh của lời xin lỗi:
Xin lỗi không làm con thấp kém đi. Ngược lại, chỉ những người có nội lực cực kỳ vững vàng và sự tự trọng cao mới dám đối diện với sai lầm của chính mình mà không cần chiếc khiên phòng thủ của cái tôi giả tạo.
"""),

    ("49_cai_bat_tay_va_phong_thai_gap_go.md", "Cái bắt tay đĩnh đạc và ánh mắt khi chào hỏi người khác",
"""# Cái bắt tay đĩnh đạc và ánh mắt khi chào hỏi người khác

### Bố bảo này:
Ấn tượng đầu tiên về một người đàn ông được định hình chỉ trong 7 giây đầu tiên của cuộc gặp gỡ, trước khi con kịp cất tiếng nói khoe khoang về tài năng hay học thức của mình. Một cái bắt tay mềm nhũn như con cá chết hay ánh mắt đảo láo liên sẽ phá hủy toàn bộ uy tín của con.

### 3 nguyên tắc vàng trong giao tiếp cơ thể:
1. **Ánh mắt nhìn thẳng ấm áp (Eye Contact):** Khi bước tới chào hỏi, hãy nhìn thẳng vào mắt người đối diện với một nụ cười mỉm nhẹ nhàng tự nhiên. Không nhìn xuống đất (thể hiện sự tự ti), không nhìn lơ đễnh qua vai họ (thể hiện sự khinh thường). Nhìn thẳng chứng minh con là người chính trực, tự tin và không có điều gì phải che giấu.
2. **Cái bắt tay đĩnh đạc, chắc chắn:**
   * Đưa bàn tay thẳng đứng, mở rộng phần màng giữa ngón cái và ngón trỏ để ôm khít sâu vào màng tay của đối phương (bắt tay cả lòng bàn tay, không chỉ nắm hờ mấy đầu ngón tay).
   * Dùng một lực siết đầm chắc, vừa phải (không bóp nghiến làm đau tay người khác, cũng không lỏng lẻo mềm nhũn).
   * Lắc nhẹ dứt khoát 1-2 nhịp từ cùi chỏ rồi buông tay.
3. **Tư thế đứng thẳng lưng:** Hai vai mở rộng tự nhiên, lồng ngực vươn cao, cằm song song với mặt đất. Người đàn ông đứng thẳng không chỉ trông đĩnh đạc hơn mà dáng đứng này còn tự động gửi tín hiệu sinh học lên não bộ giúp con giải tỏa sự lo âu và tăng cường sự tự tin.
"""),

    ("50_giu_tam_bat_dong_truoc_bien_co.md", "Giữ tâm bất động: Khi mọi thứ sụp đổ, người đàn ông thở sâu và vào việc",
"""# Giữ tâm bất động: Khi mọi thứ sụp đổ, người đàn ông thở sâu và vào việc

### Bố bảo này:
Cuộc đời này sẽ có những ngày mọi kế hoạch sụp đổ tan tành: xe hỏng giữa trời mưa bão, tiền bạc thất thoát, công việc kinh doanh đổ vỡ, người thân gặp nạn trong bệnh viện. Khi giông bão ập đến, tất cả mọi người xung quanh (vợ con, nhân viên, gia đình) sẽ nhìn vào phản ứng của con đầu tiên. Nếu con hoảng loạn, la hét, đập phá đồ đạc hay đổ lỗi, con thuyền sẽ chìm ngay lập tức.

### Nguyên tắc Khắc Kỷ của người đàn ông:
Con không thể kiểm soát những gì xảy ra với cuộc đời mình, nhưng con hoàn toàn kiểm soát được **CÁCH CON PHẢN ỨNG** với nó. Sự hoảng loạn không làm hóa đơn biến mất, không làm máy móc tự sửa lành, và không làm người bệnh khỏe lại. Nó chỉ làm đầu óc con tê liệt.

### Quy trình 3 bước xử lý khủng hoảng:
1. **Dừng lại và thở sâu 3 nhịp (Box Breathing):** Khi biến cố ập đến, đóng chặt miệng lại, hít sâu bằng mũi 4 giây, giữ hơi 4 giây, thở ra từ từ 4 giây. Động tác sinh học này lập tức hạ nồng độ adrenaline trong máu, kéo não bộ thoát khỏi trạng thái hoảng loạn của thú dữ để trở về với lý trí tỉnh táo.
2. **Tách biệt cảm xúc khỏi sự thật khách quan:** Hỏi bản thân một câu hỏi duy nhất: *"Việc tồi tệ nhất đã xảy ra rồi. Bây giờ, điều hữu ích NHẤT mà mình có thể làm trong 15 phút tới là gì?"*
3. **Tập trung vào hành động tiếp theo (The Next Right Thing):** Đừng ngồi than vãn "Tại sao lại là tôi?". Hãy đứng dậy, xắn tay áo lên và bắt đầu từ bước nhỏ nhất: Gọi cuộc điện thoại cần gọi, khóa van nước đang xả, lấy hộp đồ nghề ra, hoặc nắm chặt tay người bên cạnh và nói một câu bình thản: *"Không sao cả. Có anh/bố ở đây rồi. Mọi chuyện sẽ ổn thôi."*

### Lời nhắn nhủ cuối cùng của Bố:
Giá trị lớn nhất của một người đàn ông không nằm ở những lúc vinh quang thuận buồm xuôi gió, mà nằm ở sự vững chãi như một tảng đá giữa đại dương khi phong ba bão táp gầm rú xung quanh. Hãy luôn là chỗ dựa bình yên nhất cho những người con yêu thương.
""")
]

for fname, title, content in modules_data:
    fpath = os.path.join("/root/dad-how-do-i-vn/chapters", fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print(f"Completed all chapters! Total files in /root/dad-how-do-i-vn/chapters: {len(os.listdir('/root/dad-how-do-i-vn/chapters'))}")
