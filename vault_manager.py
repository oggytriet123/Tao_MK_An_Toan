import json, os, base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

VAULT_FILE = "vault.json"

def load_vault(key):
    """Giải mã và tải toàn bộ vault"""
    if not os.path.exists(VAULT_FILE):
        return {}
    try:
        with open(VAULT_FILE, "r") as f:
            data = json.load(f)
        aesgcm = AESGCM(key)
        vault = {}
        for name, item in data.items():
            nonce = base64.b64decode(item["nonce"])
            encrypted = base64.b64decode(item["encrypted"])
            decrypted = aesgcm.decrypt(nonce, encrypted, None).decode()
            vault[name] = decrypted
        return vault
    except Exception as e:
        print(f"🚫 Lỗi khi tải vault: {e}")
        return {}

def save_password(name, password, key):
    """Mã hóa và lưu mật khẩu mới vào vault"""
    try:
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        encrypted = aesgcm.encrypt(nonce, password.encode(), None)
        item = {
            "nonce": base64.b64encode(nonce).decode(),
            "encrypted": base64.b64encode(encrypted).decode()
        }

        data = {}
        if os.path.exists(VAULT_FILE):
            with open(VAULT_FILE, "r") as f:
                data = json.load(f)

        data[name] = item
        with open(VAULT_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Đã lưu mật khẩu cho: {name}")
    except Exception as e:
        print(f"🚫 Không thể lưu mật khẩu: {e}")

def delete_password(name):
    """Xóa mật khẩu theo tên khỏi vault"""
    if not os.path.exists(VAULT_FILE):
        print("⚠️ Vault trống.")
        return
    try:
        with open(VAULT_FILE, "r") as f:
            data = json.load(f)
        if name in data:
            del data[name]
            with open(VAULT_FILE, "w") as f:
                json.dump(data, f, indent=4)
            print(f"🗑 Đã xóa mật khẩu cho: {name}")
        else:
            print("❌ Không tìm thấy tên này trong vault.")
    except Exception as e:
        print(f"🚫 Lỗi khi xóa mật khẩu: {e}")


def export_vault(key, filename="vault_export.txt"):
    vault = load_vault(key)
    if not vault:
        print("📂 Vault trống, không có gì để xuất.")
        return
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for name, pw in vault.items():
                f.write(f"{name}:{pw}\n")
        print(f"✅ Đã xuất dữ liệu ra file: {filename}")
    except Exception as e:
        print(f"🚫 Lỗi khi xuất dữ liệu: {e}")

def import_vault(key, filename="vault_export.txt"):
    if not os.path.exists(filename):
        print("❌ File không tồn tại:", filename)
        return
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            if ":" in line:
                name, pw = line.strip().split(":", 1)
                save_password(name, pw, key)
        print(f"✅ Đã nhập dữ liệu từ file: {filename}")
    except Exception as e:
        print(f"🚫 Lỗi khi nhập dữ liệu: {e}")