import os, json, base64
from tkinter import simpledialog, messagebox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MASTER_FILE = "master_vault.json"

def setup_master():
    password = simpledialog.askstring("Tạo Master Password", "🔐 Nhập mật khẩu mới:", show="*")
    confirm = simpledialog.askstring("Xác nhận", "🔁 Nhập lại mật khẩu:", show="*")
    if not password or not confirm or password != confirm:
        messagebox.showerror("Lỗi", "❌ Mật khẩu không khớp hoặc bị bỏ trống.")
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

    messagebox.showinfo("Thành công", "✅ Master Password đã được tạo!")
    return True

def verify_master():
    if not os.path.exists(MASTER_FILE):
        messagebox.showinfo("Thông báo", "⚠️ Chưa có Master Password. Đang tạo mới...")
        return setup_master()

    with open(MASTER_FILE, "r") as f:
        data = json.load(f)

    salt = base64.b64decode(data["salt"])
    iterations = data["iterations"]
    nonce = base64.b64decode(data["nonce"])
    encrypted = base64.b64decode(data["encrypted"])

    password = simpledialog.askstring("Xác thực", "🔐 Nhập Master Password để mở vault:", show="*")
    if not password:
        return False

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
            return True
    except Exception:
        messagebox.showerror("Lỗi", "❌ Sai Master Password! Không thể truy cập vault.")
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

    password = simpledialog.askstring("Xác thực", "🔐 Nhập lại Master Password để lấy key:", show="*")
    if not password:
        return None

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
        messagebox.showerror("Lỗi", "🚫 Sai mật khẩu, không thể tạo key.")
        return None


def change_master_password():
    if not verify_master():
        return

    new_master = simpledialog.askstring("Đổi mật khẩu", "🔄 Nhập Master Password mới:", show="*")
    confirm = simpledialog.askstring("Xác nhận", "🔁 Nhập lại mật khẩu mới:", show="*")
    if not new_master or not confirm or new_master != confirm:
        messagebox.showerror("Lỗi", "❌ Mật khẩu mới không khớp hoặc bị bỏ trống.")
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

    messagebox.showinfo("Thành công", "✅ Master Password đã được đổi thành công!")

    