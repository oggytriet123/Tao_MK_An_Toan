import os, json, base64, getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MASTER_FILE = "master_vault.json"

def setup_master():
    password = getpass.getpass("🔐 Tạo Master Password mới: ")
    confirm = getpass.getpass("🔁 Nhập lại để xác nhận: ")
    if password != confirm:
        print("❌ Mật khẩu không khớp. Thử lại.")
        return False

    salt = os.urandom(16)
    iterations = 200_000
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    key = kdf.derive(password.encode())
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, b"MASTER_OK", None)

    data = {
        "salt": base64.b64encode(salt).decode(),
        "iterations": iterations,
        "nonce": base64.b64encode(nonce).decode(),
        "encrypted": base64.b64encode(encrypted).decode()
    }

    with open(MASTER_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Master Password đã được tạo!\n")
    return True

def verify_master():
    if not os.path.exists(MASTER_FILE):
        print("⚠️ Chưa có Master Password. Đang tạo mới...")
        return setup_master()

    with open(MASTER_FILE, "r") as f:
        data = json.load(f)

    salt = base64.b64decode(data["salt"])
    iterations = data["iterations"]
    nonce = base64.b64decode(data["nonce"])
    encrypted = base64.b64decode(data["encrypted"])

    password = getpass.getpass("🔐 Nhập Master Password để mở vault: ")

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
            print("✅ Xác thực thành công!\n")
            return True
    except Exception:
        print("❌ Sai Master Password! Không thể truy cập vault.\n")
        return False

def get_key_from_master():
    if not os.path.exists(MASTER_FILE):
        return None

    with open(MASTER_FILE, "r") as f:
        data = json.load(f)

    salt = base64.b64decode(data["salt"])
    iterations = data["iterations"]
    nonce = base64.b64decode(data["nonce"])
    encrypted = base64.b64decode(data["encrypted"])

    password = getpass.getpass("🔐 Nhập lại Master Password để lấy key: ")

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
            return key
    except Exception:
        print("🚫 Sai mật khẩu, không thể tạo key.")
        return None

def change_master_password():
    if not verify_master():
        return

    print("🔄 Đổi Master Password")
    new_master = getpass.getpass("Nhập Master Password mới: ")
    confirm = getpass.getpass("Xác nhận lại: ")
    if new_master != confirm:
        print("❌ Mật khẩu mới không khớp!")
        return

    salt = os.urandom(16)
    iterations = 200_000
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    key = kdf.derive(new_master.encode())
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, b"MASTER_OK", None)

    data = {
        "salt": base64.b64encode(salt).decode(),
        "iterations": iterations,
        "nonce": base64.b64encode(nonce).decode(),
        "encrypted": base64.b64encode(encrypted).decode()
    }

    with open(MASTER_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Master Password đã được đổi thành công!\n")