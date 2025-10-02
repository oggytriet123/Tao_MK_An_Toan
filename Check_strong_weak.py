import secrets
import string

COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin", "letmein",
                    "12345678", "password1", "123456789", "welcome", "111111"]

KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcv", "1234", "abcd"]

def random_password(length = 12) :
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def KiemTraDoDai(password: str, common_passwords: list) -> tuple:
    score = 0
    # 1. Kiểm tra độ dài
    length = len(password)
    if length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    elif length >= 6:
        score += 10

    # 2. Kiểm tra loại ký tự
    if any(c.islower() for c in password): score += 10
    if any(c.isupper() for c in password): score += 10
    if any(c.isdigit() for c in password): score += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/`~" for c in password): score += 10

    # 3. Lặp kí tự liên tiếp
    if any(password[i] == password[i+1] == password[i+2] for i in range(len(password)-2)):
        score -= 15

    # 4. Chuỗi bàn phím
    for pattern in KEYBOARD_PATTERNS:
        if pattern in password.lower():
            score -= 15

    # 5. Mật khẩu phổ biến
    if password.lower() in common_passwords:
        score -= 30

    # 6. Giới hạn điểm
    score = max(0, min(100, score))

    # 7. Xếp loại với icon
    if score < 30:
        level = "🔴 Mật khẩu yếu !!! ⚠️"
    elif score < 60:
        level = "🟡 Mật khẩu trung bình 🙂"
    elif score < 80:
        level = "🟢 Mật khẩu mạnh ! 💪"
    else:
        level = "🔒 Mật khẩu rất mạnh !! 🚀"

    return score, level


def hien_thi_progress(score: int, length: int = 20) -> str:
    filled = int((score / 100) * length) 
    bar = "█" * filled + "░" * (length - filled)
    return f"[{bar}] {score}/100"

if __name__ == "__main__":
    # Sinh mật khẩu ngẫu nhiên
    random_password = random_password(16)  # Mật khẩu dài 16 ký tự
    print(f"Mật khẩu ngẫu nhiên: {random_password}")
# Chạy thử
if __name__ == "__main__":
    pwd = input("Nhập mật khẩu:")
    score, level = KiemTraDoDai(pwd, COMMON_PASSWORDS)
    print(hien_thi_progress(score))
    print(f"Đánh giá: {level}")
