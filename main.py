print("🔍 Đang chạy file:", __file__)
# main.py
from gui_app import PasswordApp
import tkinter as tk
from tkinter import ttk

def configure_styles(root):
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

if __name__ == "__main__":
    root = tk.Tk()
    configure_styles(root)
    app = PasswordApp(root)
    root.mainloop()