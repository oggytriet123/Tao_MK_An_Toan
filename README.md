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

###  Cài đặt thư viện cần thiết


🎃 pip install cryptography 🎃

### 1. Chạy chương trình
Dòng lệnh thông thường:

🎃 python main.py 🎃

🔐 Bảo mật
--Mật khẩu được mã hóa bằng AES-GCM.

--Master Password được xác thực bằng PBKDF2.

--Vault lưu dưới dạng JSON, không lưu mật khẩu thô.

📤 Xuất/Nhập dữ liệu

--Xuất: Tạo file vault_export.txt chứa danh sách mật khẩu đã giải mã.

--Nhập: Đọc từ file vault_export.txt và lưu lại vào vault.

2. Các tính năng chính
   
🔑 Tạo mật khẩu ngẫu nhiên mạnh

--Để tạo một mật khẩu ngẫu nhiên mạnh, bạn có thể sử dụng lệnh sau:

🎃 python main.py generate-password 🎃

--Mật khẩu ngẫu nhiên sẽ được tạo và hiển thị trên màn hình. Bạn có thể chỉ định độ dài và loại ký tự muốn sử dụng (chữ hoa, chữ thường, số, ký tự đặc biệt) thông qua tham số của lệnh.

--Ví dụ, để tạo mật khẩu có độ dài 16 ký tự và bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt:

🎃 python main.py generate-password --length 16 --symbols --numbers --upper 🎃
   
🔍 Kiểm tra độ mạnh của mật khẩu

--Để kiểm tra mật khẩu của bạn và nhận gợi ý cải thiện, sử dụng lệnh sau:

🎃 python main.py check-password "mật khẩu của bạn" 🎃

Ứng dụng sẽ phân tích độ mạnh của mật khẩu và đưa ra các khuyến nghị nếu cần thiết.


📁 Quản lý vault lưu trữ mật khẩu

Các mật khẩu sẽ được lưu trữ trong vault. Để thêm mật khẩu mới vào vault, sử dụng lệnh sau:

🎃 python main.py add-password --service "Tên dịch vụ" --password "Mật khẩu" 🎃

Để xem các mật khẩu đã lưu trong vault: 

🎃 python main.py show-vault 🎃

Để xóa mật khẩu khỏi vault: 

🎃 python main.py remove-password 

service "Tên dịch vụ" 🎃


🔒 Đổi Master Password

Để thay đổi Master Password (mật khẩu chủ), sử dụng lệnh sau:

🎃 python main.py change-master-password 🎃

Ứng dụng sẽ yêu cầu bạn nhập Master Password hiện tại và mật khẩu mới.


📤 Xuất/Nhập dữ liệu

Xuất dữ liệu: Bạn có thể xuất tất cả mật khẩu đã lưu trong vault ra một file .txt với lệnh sau:

🎃 python main.py export-vault --file vault_export.txt 🎃

File xuất ra sẽ chứa danh sách mật khẩu đã được giải mã.

Nhập dữ liệu: Nếu bạn có một file .txt chứa mật khẩu cần nhập vào vault, sử dụng lệnh sau:

🎃 python main.py import-vault --file vault_export.txt 🎃

Dữ liệu trong file sẽ được nhập và lưu vào vault.


4. Các tệp và chức năng

✔ main.py:

Chương trình chính cung cấp giao diện dòng lệnh cho người dùng, nơi bạn có thể sử dụng tất cả các tính năng của ứng dụng như tạo mật khẩu, kiểm tra độ mạnh, quản lý vault, và xuất nhập dữ liệu.

✔ master_manager.py:

Quản lý và xác thực Master Password. Đảm bảo rằng chỉ người dùng biết Master Password mới có quyền truy cập vào vault.

✔ vault_manager.py:

Chứa các chức năng liên quan đến việc mã hóa, giải mã và quản lý các mật khẩu trong vault. Sử dụng AES-GCM để bảo mật mật khẩu.

✔ password_tool.py:

Cung cấp các công cụ để tạo mật khẩu ngẫu nhiên và kiểm tra độ mạnh của mật khẩu.

✔ strength_analyzer.py:

Phân tích độ mạnh của mật khẩu và đưa ra các lời khuyên để cải thiện.

✔ README.md:

Hướng dẫn và tài liệu chi tiết về cách sử dụng ứng dụng.

✔ vault/:

Thư mục chứa các file dữ liệu của vault. Các mật khẩu được mã hóa và lưu trữ trong này.

✔ gui_app/:

Thư mục chứa mã nguồn cho phiên bản giao diện người dùng (nếu có). Đây là một phần mở rộng tùy chọn.

✔ utils/:

Chứa các tiện ích hỗ trợ khác như các hàm mã hóa và giải mã, các thao tác file.


6. Lưu ý bảo mật
   
--Mật khẩu chủ (Master Password) là chìa khóa quan trọng để truy cập vào vault. Đảm bảo rằng bạn sử dụng một mật khẩu mạnh và lưu giữ nó một cách an toàn.

--Dữ liệu trong vault được mã hóa sử dụng AES-GCM, đảm bảo rằng chỉ có người dùng biết Master Password mới có thể truy cập vào các mật khẩu đã lưu.

--Đảm bảo rằng bạn không chia sẻ file vault hoặc các file xuất khẩu chứa mật khẩu đã giải mã.
