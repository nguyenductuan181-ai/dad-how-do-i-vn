import os

repo_dir = "/root/dad-how-do-i-vn"

# 1. Tạo README.md (Trang chủ)
readme_content = """# BỐ ƠI, LÀM CÁI NÀY THẾ NÀO? (Dad, How Do I?)
> **50 Kỹ Năng Thực Chiến Đời Sống Dành Cho Con**  
> *Nguyên tác: Rob Kenney | Biên soạn & Việt hóa: Tinh gọn 80/20 chuẩn Human Writing*

---

### Lời nhắn gửi của Bố:
Chào con! Cuộc sống tự lập bên ngoài sẽ có vô vàn những tình huống bất ngờ: bồn cầu trào ngược lúc nửa đêm, bóng đèn phụt tắt, chiếc xe thủng lốp giữa đường đèo, hay những cú vấp ngã khiến con hoang mang mất phương hướng.

Cuốn sổ tay này không có những lý thuyết giáo điều xa vời hay tự truyện dông dài. Bố đúc kết đúng **50 kỹ năng thực chiến sinh tồn và đời sống cốt lõi** theo nguyên lý 80/20. Mọi thứ được giải thích mộc mạc, chi tiết từng bước, dùng đúng ngôn ngữ đời thường của người Việt để con đọc là làm được ngay.

Dù con đang ở đâu, hãy nhớ rằng: **Không có việc gì người đàn ông bình tĩnh lại không xử lý được.**

---

### 5 Trụ Cột Kỹ Năng Cốt Lõi:

* 💧 **Module 1: Điện Nước & Gia Dụng Cơ Bản (Bài 01 - 10)**  
  Thông tắc bồn cầu, xử lý vòi rò rỉ, thay aptomat, đấu phích cắm, chống chập cháy điện nước.
* 🛠️ **Module 2: Sửa Chữa Nhà Cửa & Đồ Đạc (Bài 11 - 20)**  
  Khoan tường bắt kệ, trám vá lỗ thủng thạch cao, bôi trơn bản lề kêu, dán gối chân bàn ghế, xử lý cửa kẹt.
* 🚗 **Module 3: Xe Cộ & Di Chuyển An Toàn (Bài 21 - 30)**  
  Thay lốp dự phòng ô tô, câu bình ắc-quy, thăm dầu máy, tăng xích xe máy, sơ cứu xe ngập nước.
* 🧰 **Module 4: Bộ Đồ Nghề Của Người Đàn Ông (Bài 31 - 40)**  
  Kỹ thuật đóng đinh không cong ngón, dùng mỏ lết không trượt cạnh, chọn mũi khoan chuẩn, hộp đồ nghề 10 món tối giản.
* 👔 **Module 5: Kỹ Năng Quý Ông & Quản Trị Cuộc Đời (Bài 41 - 50)**  
  Ủi áo sơ mi 5 phút, thắt cà vạt Half-Windsor, cạo râu không rát, sơ cứu bỏng nhiệt, quy tắc tài chính sống dưới mức thu nhập và giữ tâm bất động trước biến cố.

---
*Chúc con luôn vững vàng và tự tin trên mỗi bước chân trưởng thành!*
"""

with open(os.path.join(repo_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

# 2. Tạo _sidebar.md (Menu mục lục lật trang bên trái)
sidebar_content = """* [📖 Lời Tựa Của Bố](README.md)

* **Module 1: Điện Nước Cơ Bản**
  * [01. Thông tắc bồn cầu dứt điểm](chapters/01_thong_tac_bon_cau.md)
  * [02. Xử lý vòi nước bị rò rỉ](chapters/02_xu_ly_voi_nuoc_ro_ri.md)
  * [03. Thông xiphông chậu rửa bát](chapters/03_thong_xiphong_chau_rua_bat.md)
  * [04. Khóa van nước tổng khẩn cấp](chapters/04_khoa_van_nuoc_tong_khan_cap.md)
  * [05. Bật lại aptomat bị nhảy](chapters/05_kiem_tra_aptomat_nhay_dien.md)
  * [06. Đấu nối phích cắm điện](chapters/06_thay_phich_cam_dien_bi_chay.md)
  * [07. Nối dây điện chữ X chuẩn thợ](chapters/07_noi_day_dien_an_toan.md)
  * [08. Kiểm tra ổ cắm bằng bút thử điện](chapters/08_dung_but_thu_dien.md)
  * [09. Thay đui đèn và bóng đèn LED](chapters/09_thay_dui_den_va_bong_led.md)
  * [10. Xử lý bình nóng lạnh không nóng](chapters/10_reset_binh_nong_lanh.md)

* **Module 2: Đồ Đạc & Nhà Cửa**
  * [11. Khoan tường bắt tắc-kê nở nhựa](chapters/11_khoan_tuong_bat_tac_ke.md)
  * [12. Trám vá lỗ thủng tường thạch cao](chapters/12_tram_lo_thung_tuong_thach_cao.md)
  * [13. Xử lý bản lề cửa kêu cọt kẹt](chapters/13_chua_ban_le_cua_keu_cot_ket.md)
  * [14. Chỉnh cánh cửa tủ bếp bị xệ](chapters/14_chinh_canh_cua_tu_bep_xe.md)
  * [15. Trị ổ khóa cửa bị kẹt rít](chapters/15_tri_o_khoa_cua_bi_ket_rit.md)
  * [16. Cố định chân bàn ghế khập khiễng](chapters/16_sua_chan_ban_ghe_khap_khieng.md)
  * [17. Tẩy sạch keo 502 và băng dính](chapters/17_tay_keo_502_va_bang_dinh_hai_mat.md)
  * [18. Sơn dặm mảng tường bị ố mốc](chapters/18_son_dam_mang_tuong_bong_troc.md)
  * [19. Treo tranh nặng phẳng nivo](chapters/19_treo_tranh_nang_chuan_thuy_nivo.md)
  * [20. Dán ron cao su chống ồn ngăn bụi](chapters/20_dan_ron_cao_su_chan_cua_ngan_bui.md)

* **Module 3: Xe Cộ & An Toàn**
  * [21. Thay lốp dự phòng ô tô](chapters/21_thay_lop_xe_du_phong_o_to.md)
  * [22. Kỹ thuật câu bình ắc-quy ô tô](chapters/22_cau_binh_ac_quy_o_to.md)
  * [23. Thăm que dầu và châm nhớt máy](chapters/23_kiem_tra_va_cham_dau_dong_co.md)
  * [24. Châm nước làm mát & nước rửa kính](chapters/24_cham_nuoc_lam_mat_va_nuoc_rua_kinh.md)
  * [25. Tự thay cần gạt mưa ô tô](chapters/25_thay_can_gat_mua_o_to.md)
  * [26. Đo áp suất & bơm lốp chuẩn tải](chapters/26_kiem_tra_ap_suat_va_bom_lop.md)
  * [27. Tăng sên xích & tra dầu xe máy](chapters/27_tang_xich_va_tra_dau_xe_may.md)
  * [28. Thay bóng đèn pha xe máy](chapters/28_thay_bong_den_pha_xe_may.md)
  * [29. Sơ cứu xe máy ngập nước chết máy](chapters/29_xu_ly_xe_may_ngap_nuoc_chet_may.md)
  * [30. Rửa xe 2 xô không xước xoáy](chapters/30_rua_xe_dung_cach_khong_xuoc_son.md)

* **Module 4: Bộ Đồ Nghề Đàn Ông**
  * [31. Kỹ thuật búa & đóng đinh](chapters/31_chiec_bua_va_ky_thuat_dong_dinh.md)
  * [32. Dùng tuốc-nơ-vít không trờn ren](chapters/32_tuoc_no_vit_hai_canh_va_bon_canh.md)
  * [33. Mỏ lết & cờ-lê không trượt](chapters/33_mo_let_va_co_le_vong_mieng.md)
  * [34. 3 loại kìm cơ bản](chapters/34_cac_loai_kim_co_ban.md)
  * [35. Máy khoan & phân biệt mũi khoan](chapters/35_may_khoan_cam_tay_va_mui_khoan.md)
  * [36. Thước cuộn & thước thủy nivo](chapters/36_thuoc_cuon_va_thuoc_thuy_nivo.md)
  * [37. Dao rọc giấy & cưa tay an toàn](chapters/37_dao_roc_giay_va_cua_tay.md)
  * [38. Băng dính bạc Duct Tape & băng keo điện](chapters/38_bang_keo_dien_va_bang_keo_duc_tape.md)
  * [39. Đèn đội đầu soi góc khuất](chapters/39_den_pin_sieu_sang_va_den_doi_dau.md)
  * [40. Hộp đồ nghề tối giản 10 món](chapters/40_hop_do_nghe_toi_gian_cho_can_ho.md)

* **Module 5: Kỹ Năng Quý Ông & Cuộc Sống**
  * [41. Ủi phẳng áo sơ mi 5 phút](chapters/41_ui_ao_so_mi_va_quan_tay.md)
  * [42. Thắt cà vạt chuẩn Half-Windsor](chapters/42_that_ca_vat_chuan_gentleman.md)
  * [43. Cạo râu mềm da không rát](chapters/43_cao_rau_sach_khong_rat_da.md)
  * [44. Tự đính lại cúc áo bị đứt](chapters/44_dinh_lai_cuc_ao_bi_dut.md)
  * [45. Đánh xi & bảo dưỡng giày da](chapters/45_danh_xi_giay_da_bong_guong.md)
  * [46. Sơ cứu vết bỏng & vết đứt tay](chapters/46_so_cuu_vet_bong_va_vet_dut_tay.md)
  * [47. Sống dưới mức thu nhập](chapters/47_kiem_soat_chi_tieu_song_duoi_muc_thu_nhap.md)
  * [48. Lời xin lỗi chân thành của đàn ông](chapters/48_loi_xin_loi_chan_thanh_cua_nguoi_dan_ong.md)
  * [49. Cái bắt tay đĩnh đạc & ánh mắt](chapters/49_cai_bat_tay_va_phong_thai_gap_go.md)
  * [50. Giữ tâm bất động trước biến cố](chapters/50_giu_tam_bat_dong_truoc_bien_co.md)
"""

with open(os.path.join(repo_dir, "_sidebar.md"), "w", encoding="utf-8") as f:
    f.write(sidebar_content)

# 3. Tạo index.html (Docsify single page app với theme hiện đại, font tiếng Việt đẹp)
index_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Dad, How Do I? — 50 Bài Học Của Bố (Bản Thực Chiến Việt Nam)</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="50 kỹ năng thực chiến đời sống cho người đàn ông - Rob Kenney (Dad How Do I) bản Việt hóa tinh gọn 80/20">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --theme-color: #d97706;
      --base-font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    body {
      font-family: var(--base-font-family);
      font-size: 16px;
      line-height: 1.75;
      color: #1f2937;
    }
    .markdown-section h1 {
      font-weight: 700;
      color: #111827;
      border-bottom: 2px solid #f3f4f6;
      padding-bottom: 0.5rem;
    }
    .markdown-section h3 {
      color: #b45309;
      font-weight: 600;
      margin-top: 1.5rem;
    }
    .markdown-section blockquote {
      border-left: 4px solid #d97706;
      background: #fffbeb;
      padding: 12px 18px;
      border-radius: 4px;
      color: #92400e;
    }
    .sidebar {
      font-family: var(--base-font-family);
    }
    .sidebar-nav strong {
      color: #374151;
      font-size: 0.95rem;
    }
    .sidebar-nav li a {
      font-size: 0.9rem;
      color: #4b5563;
    }
    .sidebar-nav li a:hover {
      color: #d97706;
    }
  </style>
</head>
<body>
  <div id="app">Đang mở cẩm nang của Bố...</div>
  <script>
    window.$docsify = {
      name: 'Dad, How Do I? (VN)',
      repo: '',
      loadSidebar: true,
      subMaxLevel: 2,
      auto2top: true,
      search: {
        maxAge: 86400000,
        paths: 'auto',
        placeholder: 'Tìm kỹ năng (vd: bồn cầu, bugi, cà vạt...)',
        noData: 'Không tìm thấy bài học phù hợp!',
        depth: 3
      },
      copyCode: {
        buttonText: 'Sao chép',
        errorText: 'Lỗi',
        successText: 'Đã chép'
      },
      pagination: {
        previousText: 'Bài trước',
        nextText: 'Bài tiếp theo',
        crossChapter: true,
        crossChapterText: true
      }
    }
  </script>
  <!-- Docsify v4 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <!-- Plugins -->
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify-copy-code/dist/docsify-copy-code.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify-pagination/dist/docsify-pagination.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>
</body>
</html>
"""

with open(os.path.join(repo_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# 4. Tạo .nojekyll
with open(os.path.join(repo_dir, ".nojekyll"), "w", encoding="utf-8") as f:
    f.write("")

print("Docsify site built successfully!")
