import secrets
import string
import re
import hashlib
import os

SPEACIAL = "!@#$%^&*()_"

# ------------------------------
# Gợi ý mật khẩu thông minh
# ------------------------------
def suggest_smart(password: str, num_suggestions=3):
    suggestion = []
    match = re.match(r"([A-Za-z]+)(\d*)$", password)
    if match:
        letters = match.group(1)
        numbers = match.group(2)
    else:
        letters = password
        numbers = ""

    letters_cap = letters.capitalize()
    for _ in range(num_suggestions):
        symbol = secrets.choice(SPEACIAL)
        if numbers:
            shuffled = ''.join(secrets.choice(numbers) for _ in range(len(numbers)))
        else:
            shuffled = str(secrets.randbelow(1000))
        pattern = secrets.choice([
            f"{letters_cap}{symbol}{shuffled}",
            f"{letters_cap}.{symbol}{shuffled}",
            f"{letters_cap}{shuffled}{symbol}",
            f"{letters_cap}{symbol}{shuffled}!"
        ])
        if pattern not in suggestion:
            suggestion.append(pattern)
    return suggestion


# ------------------------------
# Danh sách mật khẩu phổ biến
# ------------------------------
COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin", "letmein",
                    "12345678", "password1", "123456789", "welcome", "111111"]

KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcv", "1234", "abcd"]

de_nham = "01lI"

# ------------------------------
# Tạo mật khẩu ngẫu nhiên
# ------------------------------
def random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    characters = ''.join(c for c in characters if c not in de_nham)
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

# ------------------------------
# Kiểm tra độ mạnh mật khẩu
# ------------------------------
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


# ------------------------------
# Quản lý Master Password
# ------------------------------
MASTER_FILE = "master.hash"

def hash_master(password: str) -> str:
    """Hash master password bằng SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def setup_master():
    """Tạo Master Password mới"""
    master = input("Tạo Master Password mới: ")
    confirm = input("Nhập lại để xác nhận: ")
    if master != confirm:
        print("❌ Mật khẩu không khớp!")
        exit()
    with open(MASTER_FILE, "w") as f:
        f.write(hash_master(master))
    print("✅ Đã tạo Master Password thành công!\n")

def verify_master():
    """Yêu cầu nhập Master Password trước khi mở vault"""
    if not os.path.exists(MASTER_FILE):
        setup_master()
    else:
        master = input("🔐 Nhập Master Password để mở vault: ")
        with open(MASTER_FILE, "r") as f:
            saved = f.read().strip()
        if hash_master(master) != saved:
            print("🚫 Sai Master Password! Không thể truy cập vault.")
            exit()
        print("✅ Xác thực thành công! Vault đã mở.\n")


# ------------------------------
# Chạy trong terminal
# ------------------------------
if __name__ == "__main__":
    print("=== 🔒 BẮT ĐẦU CHƯƠNG TRÌNH KIỂM TRA MẬT KHẨU ===")
    verify_master()  # 🧩 Bắt buộc xác thực trước khi tiếp tục

    print("🔐 Kiểm tra độ mạnh mật khẩu 🔐")
    print("----------------------------------")
    password = input("Nhập mật khẩu của bạn: ")

    score, level, suggestion = KiemTraDoDai(password, COMMON_PASSWORDS)

    print(f"\nĐiểm đánh giá: {score}/100")
    print(f"Đánh giá: {level}")
    print(f"Gợi ý mật khẩu ngẫu nhiên: {suggestion}")

    # ✅ Gợi ý thêm bằng AI dựa trên mật khẩu người dùng
    print("\n🤖 Gợi ý mật khẩu thông minh dựa trên mật khẩu bạn nhập:")
    smart_suggestions = suggest_smart(password, 5)
    for s in smart_suggestions:
        print("👉", s)
