import secrets
import string
from cryptography.fernet import Fernet
import tkinter as tk

# Tạo mã hóa key mới
def generate_key():
    return Fernet.generate_key()

# Danh sách mật khẩu phổ biến
COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin", "letmein",
                    "12345678", "password1", "123456789", "welcome", "111111"]

KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcv", "1234", "abcd"]

de_nham = "01lI"

# Tạo mật khẩu ngẫu nhiên
def random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    characters = ''.join(c for c in characters if c not in de_nham)
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

# Kiểm tra độ mạnh mật khẩu
def KiemTraDoDai(password: str, common_passwords: list) -> tuple:
    score = 0
    length = len(password)
    if length >= 16:
        score += 40
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    elif length >= 6:
        score += 10

    # Kiểm tra ký tự có trong mật khẩu
    if any(c.islower() for c in password): score += 15
    if any(c.isupper() for c in password): score += 15
    if any(c.isdigit() for c in password): score += 15
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/`~" for c in password): score += 15

    # Kiểm tra ký tự lặp
    if any(password[i] == password[i+1] == password[i+2] for i in range(len(password)-2)):
        score -= 15

    # Kiểm tra mẫu bàn phím dễ đoán
    for pattern in KEYBOARD_PATTERNS:
        if pattern in password.lower():
            score -= 15

    # Kiểm tra mật khẩu phổ biến
    if password.lower() in common_passwords:
        score -= 30

    score = max(0, min(100, score))

    # Xếp loại mật khẩu
    if score < 30:
        level = "🔴 Mật khẩu yếu !!! ⚠️"
        suggestion = random_password(16)
    elif score < 60:
        level = "🟡 Mật khẩu trung bình 🙂"
        suggestion = random_password(16)
    elif score < 80:
        level = "🟢 Mật khẩu mạnh ! 💪"
        suggestion = "Mật khẩu này đã đủ mạnh! 👍"
    else:
        level = "🔒 Mật khẩu rất mạnh !! 🚀"
        suggestion = "Mật khẩu này rất mạnh! 🚀"

    return score, level, suggestion

# Hàm xử lý khi người dùng nhập mật khẩu
def check_password():
    # Lấy mật khẩu người dùng nhập vào
    pwd = entry_password.get()

    # Kiểm tra độ mạnh của mật khẩu
    score, level, suggestion = KiemTraDoDai(pwd, COMMON_PASSWORDS)

    # Cập nhật kết quả vào GUI
    level_label.config(text=f"Đánh giá: {level}")
    suggestion_label.config(text=f"Gợi ý mật khẩu: {suggestion}")

# Tạo cửa sổ GUI
window = tk.Tk()
window.title("Kiểm Tra Mật Khẩu")

# Cài đặt giao diện
window.geometry("500x400")

# Nhãn yêu cầu nhập mật khẩu
label = tk.Label(window, text="Nhập mật khẩu của bạn:")
label.pack(pady=10)

# Vùng nhập mật khẩu
entry_password = tk.Entry(window, show="*", width=30)
entry_password.pack(pady=10)

# Nút kiểm tra mật khẩu
check_button = tk.Button(window, text="Kiểm tra mật khẩu", command=check_password)
check_button.pack(pady=10)

# Nhãn hiển thị đánh giá
level_label = tk.Label(window, text="Đánh giá: ")
level_label.pack(pady=10)

# Nhãn hiển thị gợi ý mật khẩu
suggestion_label = tk.Label(window, text="Gợi ý mật khẩu: ")
suggestion_label.pack(pady=10)

# Khởi chạy giao diện
window.mainloop()
