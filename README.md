# 🔐 Trình Tạo Mật Khẩu An Toàn

Ứng dụng dòng lệnh giúp người dùng tạo, kiểm tra, lưu trữ và quản lý mật khẩu một cách bảo mật. Dự án sử dụng mã hóa AES-GCM, xác thực bằng Master Password, và hỗ trợ xuất/nhập dữ liệu để sao lưu hoặc phục hồi vault.

---

## 🧩 Tính năng nổi bật

- 🔐 Tạo mật khẩu ngẫu nhiên mạnh
- 📊 Kiểm tra độ mạnh của mật khẩu và gợi ý cải thiện
- 📁 Quản lý vault lưu trữ mật khẩu (xem, thêm, xóa)
- 🧩 Tạo mật khẩu theo mẫu (email, ngân hàng, mạng xã hội…)
- 📈 Phân tích hàng loạt mật khẩu
- 🛡 Đổi Master Password
- 📤 Xuất/Nhập dữ liệu từ file `.txt`

---

## 🗂 Cấu trúc thư mục
Tao_MK_An_Toan/
├── main.py                  # Giao diện dòng lệnh chính
├── master_manager.py        # Quản lý Master Password
├── vault_manager.py         # Mã hóa và quản lý vault
├── password_tool.py         # Tạo và kiểm tra mật khẩu
├── strength_analyzer.py     # Phân tích độ mạnh mật khẩu
├── README.md                # Tài liệu mô tả dự án
│
├── vault/                   # (tùy chọn) chứa file vault
├── gui_app/                 # (tùy chọn) giao diện người dùng
├── utils/                   # Các tiện ích phụ trợ
└── __pycache__/             # File cache của Python
---

## ⚙️ Cách sử dụng

### 1. Cài đặt thư viện cần thiết

```bash
pip install cryptography
## ⚙️ Cách sử dụng

### 1. Chạy chương trình
Dòng lệnh thông thường:
```bash
python main.py
🔐 Bảo mật

Mật khẩu được mã hóa bằng AES-GCM.

Master Password được xác thực bằng PBKDF2.

Vault lưu dưới dạng JSON, không lưu mật khẩu thô.
📤 Xuất/Nhập dữ liệu

Xuất: Tạo file vault_export.txt chứa danh sách mật khẩu đã giải mã.

Nhập: Đọc từ file vault_export.txt và lưu lại vào vault.