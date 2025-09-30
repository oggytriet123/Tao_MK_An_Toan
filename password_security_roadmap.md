# 🗓 Roadmap 10 ngày – Công cụ kiểm tra & quản lý mật khẩu an toàn (Python)

## ✅ Nguyên tắc
- [ ] Làm từng bước theo thứ tự
- [ ] Code nhỏ trước, gom lại sau
- [ ] Test mỗi phần trước khi sang bước kế tiếp

---

## 🔑 Bước 1: Chiến lược sinh mật khẩu (Ngày 1–2)
- [ ] Viết code sinh mật khẩu random với `secrets.choice`
- [ ] Thêm option: chữ hoa, chữ thường, số, ký tự đặc biệt
- [ ] Loại bỏ ký tự dễ nhầm (0,O,1,l,I)
- [ ] Thêm mode: pronounceable, passphrase
- [ ] Hàm tính entropy (bits) để đo độ mạnh

---

## 🛡 Bước 2: Thuật toán chấm điểm độ mạnh (Ngày 3–4)
- [ ] Kiểm tra cơ bản: độ dài, loại ký tự
- [ ] Phát hiện pattern: lặp (`aaa`, `111`), chuỗi bàn phím (`qwerty`)
- [ ] Kiểm tra dictionary word (common password list)
- [ ] Tính điểm strength (0–100)
- [ ] Trả về mức độ: Yếu / Trung bình / Mạnh / Rất mạnh

---

## 🔒 Bước 3: Lưu trữ an toàn (Ngày 5–6)
- [ ] Yêu cầu Master Password khi mở vault
- [ ] Sinh key bằng PBKDF2/Argon2 + muối + nhiều vòng lặp
- [ ] Mã hóa dữ liệu bằng AES-256 (thư viện `cryptography`)
- [ ] Cấu trúc file JSON (salt, iterations, encrypted_data)
- [ ] Đảm bảo không lưu plaintext password

---

## 📊 Bước 4: Trực quan hóa độ mạnh (Ngày 7)
- [ ] In thanh tiến độ: `█████░░░░` theo điểm
- [ ] Màu: đỏ (yếu), vàng (trung bình), xanh (mạnh)
- [ ] Checklist yêu cầu (có chữ hoa, ký tự đặc biệt…)
- [ ] Ước lượng thời gian bẻ mật khẩu (dựa entropy)

---

## 🌐 Bước 5: Kiểm tra rò rỉ (Ngày 8–9)
- [ ] Hash mật khẩu bằng SHA-1
- [ ] Gửi 5 ký tự đầu hash tới API HaveIBeenPwned
- [ ] So khớp local với kết quả trả về
- [ ] Offline mode: kiểm tra với local breach list
- [ ] Cache kết quả để tránh gọi API nhiều lần

---

## 🧩 Ngày 10: Gom lại chương trình
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

## 📌 Tiến độ cá nhân
- Ngày 1–2: Bước 1 ✅ / ❌  
- Ngày 3–4: Bước 2 ✅ / ❌  
- Ngày 5–6: Bước 3 ✅ / ❌  
- Ngày 7: Bước 4 ✅ / ❌  
- Ngày 8–9: Bước 5 ✅ / ❌  
- Ngày 10: Final tool ✅ / ❌  
