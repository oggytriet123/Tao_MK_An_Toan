import os, json, base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MASTER_FILE = "master_vault.json"

def setup_master():
    """Tạo master password, sinh key bằng PBKDF2, mã hóa xác nhận bằng AES-256"""
    master = input("🔑 Tạo Master Password mới: ")
    confirm = input("Nhập lại để xác nhận: ")
    if master != confirm:
        print("❌ Mật khẩu không khớp!")
        return

    salt = os.urandom(16)
    iterations = 200_000

    # Sinh key từ password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    key = kdf.derive(master.encode())

    # Mã hóa xác nhận
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, b"MASTER_OK", None)

    # Ghi ra file JSON
    data = {
        "salt": base64.b64encode(salt).decode(),
        "iterations": iterations,
        "nonce": base64.b64encode(nonce).decode(),
        "encrypted": base64.b64encode(encrypted).decode()
    }

    with open(MASTER_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Master Password đã được tạo và mã hóa an toàn!\n")


def verify_master():
    """Yêu cầu nhập master password, kiểm tra bằng AES-256"""
    if not os.path.exists(MASTER_FILE):
        print("⚠️ Chưa có master password, cần tạo mới trước.")
        setup_master()
        return

    with open(MASTER_FILE, "r") as f:
        data = json.load(f)

    salt = base64.b64decode(data["salt"])
    iterations = data["iterations"]
    nonce = base64.b64decode(data["nonce"])
    encrypted = base64.b64decode(data["encrypted"])

    password = input("🔐 Nhập Master Password để mở vault: ")

    # Sinh lại key từ master password nhập vào
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )

    try:
        key = kdf.derive(password.encode())
        aesgcm = AESGCM(key)
        decrypted = aesgcm.decrypt(nonce, encrypted, None)
        if decrypted == b"MASTER_OK":
            print("✅ Xác thực thành công! Vault đã mở.\n")
            return True
    except Exception:
        pass

    print("🚫 Sai Master Password! Không thể truy cập vault.\n")
    return False
