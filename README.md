# Tao_MK_An_Toan
# 🗓 Roadmap 10 ngày – Công cụ kiểm tra & quản lý mật khẩu an toàn (Python)

## ✅ Nguyên tắc
-  Làm từng bước theo thứ tự
- Code nhỏ trước, gom lại sau
- Test mỗi phần trước khi sang bước kế tiếp

---

## 🔑 Bước 1: Chiến lược sinh mật khẩu (Ngày 1–2) [Tuấn Anh]
- [x] Viết code sinh mật khẩu random với `secrets.choice`
- [x] Thêm option: chữ hoa, chữ thường, số, ký tự đặc biệt
- [x] Loại bỏ ký tự dễ nhầm (0,O,1,l,I)

---

## 🛡 Bước 2: Thuật toán chấm điểm độ mạnh (Ngày 3–4) [Kim Anh]
- [X] Kiểm tra cơ bản: độ dài, loại ký tự
- [X] Phát hiện pattern: lặp (`aaa`, `111`), chuỗi bàn phím (`qwerty`)
- [X] Kiểm tra dictionary word (common password list)
- [X] Tính điểm strength (0–100)
- [X] Trả về mức độ: Yếu / Trung bình / Mạnh / Rất mạnh

---

## 🔒 Bước 3: Lưu trữ an toàn (Ngày 5–6) [Tuấn Anh]
- [ ] Yêu cầu Master Password khi mở vault
- [ ] Sinh key bằng PBKDF2/Argon2 + muối + nhiều vòng lặp
- [ ] Mã hóa dữ liệu bằng AES-256 (thư viện `cryptography`)
- [ ] Cấu trúc file JSON (salt, iterations, encrypted_data)
- [ ] Đảm bảo không lưu plaintext password

---

## 📊 Bước 4: Trực quan hóa độ mạnh (Ngày 7) [Kim Anh]
- [X] In thanh tiến độ: `█████░░░░` theo điểm
- [X] Màu: đỏ (yếu), vàng (trung bình), xanh (mạnh)
- [ ] Checklist yêu cầu (có chữ hoa, ký tự đặc biệt…)
- [ ] Ước lượng thời gian bẻ mật khẩu (dựa entropy)

---

## 🌐 Bước 5: Kiểm tra rò rỉ (Ngày 8–9) [ Tuấn Anh]
- [ ] Hash mật khẩu bằng SHA-1
- [ ] Gửi 5 ký tự đầu hash tới API HaveIBeenPwned
- [ ] So khớp local với kết quả trả về
- [ ] Offline mode: kiểm tra với local breach list
- [ ] Cache kết quả để tránh gọi API nhiều lần

---

## 🧩 Ngày 10: Gom lại chương trình [Kim Anh]
- [ ] Xây menu chính:
  1. Tạo mật khẩu mới
  2. Kiểm tra độ mạnh mật khẩu
  3. Quản lý mật khẩu đã lưu
  4. Tạo mật khẩu theo mẫu
  5. Phân tích batch passwords
  6. Cài đặt bảo mật
  7. Xuất/Nhập dữ liệu
  8. Thoát
- [ ] Gom code các phần trước thành tool hoàn chỉnh
- [ ] Viết báo cáo mô tả thuật toán + demo kết quả

---

# 📅 Timeline thực hiện (10 ngày)

| Ngày      | Nhiệm vụ                          | Người phụ trách | Tiến độ |
|-----------|-----------------------------------|-----------------|---------|
| 1 – 2     | Bước 1: Chiến lược sinh mật khẩu  | Tuấn Anh        | [x]     |
| 3 – 4     | Bước 2: Thuật toán chấm điểm      | Kim Anh         | [X]     |
| 5 – 6     | Bước 3: Lưu trữ an toàn           | Tuấn Anh        | [ ]     |
| 7         | Bước 4: Trực quan hóa độ mạnh     | Kim Anh         | [ ]     |
| 8 – 9     | Bước 5: Kiểm tra rò rỉ            | Tuấn Anh        | [ ]     |
| 10        | Gom lại chương trình + báo cáo    | Kim Anh         | [ ]     |

