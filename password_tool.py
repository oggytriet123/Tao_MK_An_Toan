import secrets
import string
import re
import hashlib
import os
import base64
import getpass

SPECIAL = "!@#$%^&*()_"
COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin", "letmein",
                    "12345678", "password1", "123456789", "welcome", "111111"]
KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcv", "1234", "abcd"]
DE_NHAM = "01lI"
MASTER_FILE = "master.hash"


# ------------------------------
# Gợi ý mật khẩu thông minh
# ------------------------------
def suggest_smart(password: str, num_suggestions=3):
    suggestions = []
    match = re.match(r"([A-Za-z]+)(\d*)$", password)
    letters, numbers = match.groups() if match else (password, "")
    letters_cap = letters.capitalize()

    while len(suggestions) < num_suggestions:
        symbol = secrets.choice(SPECIAL)
        shuffled = ''.join(secrets.choice(numbers) for _ in range(len(numbers))) if numbers else str(secrets.randbelow(1000))
        pattern = secrets.choice([
            f"{letters_cap}{symbol}{shuffled}",
            f"{letters_cap}.{symbol}{shuffled}",
            f"{letters_cap}{shuffled}{symbol}",
            f"{letters_cap}{symbol}{shuffled}!"
        ])
        if pattern not in suggestions:
            suggestions.append(pattern)
    return suggestions


# ------------------------------
# Tạo mật khẩu ngẫu nhiên
# ------------------------------
def random_password(length=16):
    characters = ''.join(c for c in string.ascii_letters + string.digits + string.punctuation if c not in DE_NHAM)
    return ''.join(secrets.choice(characters) for _ in range(length))


# ------------------------------
# Kiểm tra độ mạnh mật khẩu
# ------------------------------
def kiem_tra_do_dai(password: str, common_passwords: list) -> tuple:
    score = 0
    length = len(password)

    # Chiều dài
    score += 40 if length >= 16 else 30 if length >= 12 else 20 if length >= 8 else 10

    # Thành phần
    if any(c.islower() for c in password): score += 15
    if any(c.isupper() for c in password): score += 15
    if any(c.isdigit() for c in password): score += 15
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/`~" for c in password): score += 15

    # Giảm điểm
    if any(password[i] == password[i+1] == password[i+2] for i in range(len(password)-2)):
        score -= 15
    if any(pattern in password.lower() for pattern in KEYBOARD_PATTERNS):
        score -= 15
    if password.lower() in common_passwords:
        score -= 30

    score = max(0, min(100, score))

    # Đánh giá
    if score < 30:
        return score, "🔴 Mật khẩu yếu !!! ⚠️", random_password(16)
    elif score < 60:
        return score, "🟡 Mật khẩu trung bình 🙂", random_password(16)
    elif score < 80:
        return score, "🟢 Mật khẩu mạnh ! 💪", "Mật khẩu này đã đủ mạnh! 👍"
    else:
        return score, "🔒 Mật khẩu rất mạnh !! 🚀", "Mật khẩu này rất mạnh! 🚀"



