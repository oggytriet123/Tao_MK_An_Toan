import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from password_tool import random_password, kiem_tra_do_dai, COMMON_PASSWORDS, suggest_smart
from vault_manager import load_vault, save_password, delete_password, export_vault, import_vault
from master_manager import verify_master, get_key_from_master, change_master_password

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Trình Tạo Mật Khẩu An Toàn")
        self.root.geometry("440x480")
        self.root.configure(bg="#0f1c2e")  # nền xanh dương đậm
        self.key = None

        # Nếu muốn test nhanh GUI thì dùng key giả
        # self.key = b"0" * 32

        if not verify_master():
            messagebox.showerror("Lỗi", "Xác thực Master thất bại!")
            root.destroy()
            return

        self.key = get_key_from_master()
        if not self.key:
            messagebox.showerror("Lỗi", "Không thể lấy key từ Master Password.")
            root.destroy()
            return

        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self.root, text="🔐 Trình Tạo Mật Khẩu", style="Title.TLabel")
        title.pack(pady=15)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        buttons = [
            ("Tạo mật khẩu mới", self.tao_mk),
            ("Kiểm tra độ mạnh mật khẩu", self.kiem_tra_mk),
            ("Xem vault", self.xem_vault),
            ("Thêm mật khẩu vào vault", self.them_mk),
            ("Xóa mật khẩu khỏi vault", self.xoa_mk),
            ("Xuất vault ra file", self.export_vault),
            ("Nhập vault từ file", self.import_vault),
            ("Đổi Master Password", self.doi_master),
        ]

        for text, command in buttons:
            ttk.Button(btn_frame, text=text, command=command, style="Main.TButton").pack(fill="x", pady=4, padx=40)

    def tao_mk(self):
        mk = random_password()

        popup = tk.Toplevel(self.root)
        popup.title("🔐 Mật khẩu mới")
        popup.configure(bg="#0f1c2e")
        popup.geometry("300x150")

        label = ttk.Label(popup, text="👉 Mật khẩu của bạn:", style="Title.TLabel")
        label.pack(pady=(10, 5))

        entry = ttk.Entry(popup, font=("Segoe UI", 10))
        entry.insert(0, mk)
        entry.pack(pady=5, padx=20)
        entry.config(state="readonly")

        def copy_to_clipboard():
            self.root.clipboard_clear()
            self.root.clipboard_append(mk)
            messagebox.showinfo("Đã sao chép", "✅ Mật khẩu đã được sao chép!")

        ttk.Button(popup, text="📋 Sao chép", command=copy_to_clipboard, style="Main.TButton").pack(pady=10)

    def kiem_tra_mk(self):
        pw = simpledialog.askstring("Nhập mật khẩu", "Nhập mật khẩu cần kiểm tra:")
        if pw:
            score, level, suggestion = kiem_tra_do_dai(pw, COMMON_PASSWORDS)
            msg = f"Điểm: {score}/100\nĐánh giá: {level}"
            if "yếu" in level.lower() or "trung bình" in level.lower():
                msg += "\n\n🤖 Gợi ý mật khẩu thông minh:\n" + "\n".join(suggest_smart(pw, 3))
            messagebox.showinfo("Kết quả", msg)

    def xem_vault(self):
        vault = load_vault(self.key)
        if not vault:
            messagebox.showinfo("Vault", "📂 Vault trống.")
        else:
            msg = "\n".join([f"{name}: {pw}" for name, pw in vault.items()])
            messagebox.showinfo("Vault", msg)

    def them_mk(self):
        name = simpledialog.askstring("Tên tài khoản", "Nhập tên (ví dụ: Gmail, Facebook):")
        pw = simpledialog.askstring("Mật khẩu", "Nhập mật khẩu cần lưu:")
        if name and pw:
            save_password(name, pw, self.key)
            messagebox.showinfo("Thành công", f"✅ Đã lưu mật khẩu cho: {name}")

    def xoa_mk(self):
        name = simpledialog.askstring("Xóa mật khẩu", "Nhập tên tài khoản cần xóa:")
        if name:
            delete_password(name)
            messagebox.showinfo("Xóa", f"🗑 Đã xóa mật khẩu cho: {name}")

    def export_vault(self):
        export_vault(self.key)

    def import_vault(self):
        import_vault(self.key)

    def doi_master(self):
        change_master_password()

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("Main.TButton",
                    font=("Segoe UI", 10),
                    padding=6,
                    background="#1e3a5f",
                    foreground="white")
    style.map("Main.TButton",
              background=[("active", "#2a4d7c")],
              foreground=[("active", "white")])

    style.configure("Title.TLabel",
                    font=("Segoe UI", 13, "bold"),
                    background="#0f1c2e",
                    foreground="white")

    app = PasswordApp(root)
    root.mainloop()