import secrets
import string

COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin", "letmein",
                    "12345678", "password1", "123456789", "welcome", "111111"]

KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcv", "1234", "abcd"]

def random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

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

    if any(c.islower() for c in password): score += 15
    if any(c.isupper() for c in password): score += 15
    if any(c.isdigit() for c in password): score += 15
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/`~" for c in password): score += 15

    if any(password[i] == password[i+1] == password[i+2] for i in range(len(password)-2)):
        score -= 15

    for pattern in KEYBOARD_PATTERNS:
        if pattern in password.lower():
            score -= 15

    if password.lower() in common_passwords:
        score -= 30

    score = max(0, min(100, score))

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


def hien_thi_progress(score: int, length: int = 20) -> str:
    filled = int((score / 100) * length)
    bar = "█" * filled + "░" * (length - filled)
    return f"[{bar}] {score}/100"

if __name__ == "__main__":
    # Kiểm tra mật khẩu người dùng nhập
    pwd = input("Nhập mật khẩu: ")
    score, level, suggestion = KiemTraDoDai(pwd, COMMON_PASSWORDS)
    
    # Hiển thị thanh tiến trình
    print(hien_thi_progress(score))
    print(f"Đánh giá: {level}")
    
    # Gợi ý mật khẩu nếu mật khẩu yếu hoặc trung bình
    print(f"Gợi ý mật khẩu: {suggestion}")

#F7r$K8&bTz!qLp4z