print("🔍 Đang chạy file:", __file__)
import getpass
import os

def menu():
    print("\n========== TRÌNH TẠO MẬT KHẨU AN TOÀN ==========")
    print("1. Tạo mật khẩu mới")
    print("2. Kiểm tra độ mạnh mật khẩu")
    print("3. Quản lý mật khẩu đã lưu")
    print("4. Tạo mật khẩu theo mẫu")
    print("5. Phân tích batch passwords")
    print("6. Cài đặt bảo mật")
    print("7. Xuất/Nhập dữ liệu")
    print("8. Thoát")
    return input("Chọn chức năng (1-8): ")

def vault_menu(key):
    while True:
        print("\n📁 QUẢN LÝ MẬT KHẨU ĐÃ LƯU 📁")
        print("1. Xem danh sách mật khẩu")
        print("2. Thêm mật khẩu mới")
        print("3. Xóa mật khẩu")
        print("0. Quay lại menu chính")
        choice = input("Chọn chức năng (0-3): ")

        if choice == "1":
            vault = load_vault(key)
            if not vault:
                print("📂 Vault trống.")
            else:
                print("📋 Danh sách mật khẩu:")
                for name, pw in vault.items():
                    print(f"🔑 {name}: {pw}")
        elif choice == "2":
            name = input("Tên tài khoản (ví dụ: Gmail, Facebook): ")
            pw = getpass.getpass("Nhập mật khẩu cần lưu: ")
            save_password(name, pw, key)
        elif choice == "3":
            name = input("Nhập tên tài khoản cần xóa: ")
            delete_password(name)
        elif choice == "0":
            break
        else:
            print("⚠️ Vui lòng chọn từ 0 đến 3.")


# Import từ các module chức năng
from password_tool import (
    random_password,
    kiem_tra_do_dai,
    COMMON_PASSWORDS,
    suggest_smart,
    tao_mat_khau_theo_mau,
    phan_tich_batch
)

from master_manager import (
    verify_master,
    change_master_password,
    get_key_from_master
)

from vault_manager import (
    load_vault,
    save_password,
    delete_password,
    export_vault,
    import_vault
)

def main():
    if not verify_master():
        return

    from master_manager import get_key_from_master
    key = get_key_from_master()

    while True:
        choice = menu()
        if choice == "1":
            print("🔐 Mật khẩu mới của bạn là:")
            print("👉", random_password())
        elif choice == "2":
            pw = input("Nhập mật khẩu cần kiểm tra: ")
            score, level, suggestion = kiem_tra_do_dai(pw, COMMON_PASSWORDS)
            print(f"Điểm: {score}/100\nĐánh giá: {level}")
            if "yếu" in level.lower() or "trung bình" in level.lower():
                print("🤖 Gợi ý mật khẩu thông minh:")
                for s in suggest_smart(pw, 5):
                    print("👉", s)
        elif choice == "3":
            vault_menu(key)
        elif choice == "4":
            print("🧩 Tạo mật khẩu theo mẫu")
            mau = input("Nhập mẫu (email, nganhang, facebook, zalo, github): ")
            mk_mau = tao_mat_khau_theo_mau(mau)
            print(f"👉 Mật khẩu theo mẫu '{mau}': {mk_mau}")
        elif choice == "5":
            print("📊 Phân tích batch passwords")
            raw = input("Nhập các mật khẩu cách nhau bởi dấu phẩy: ")
            danh_sach = [pw.strip() for pw in raw.split(",")]
            ket_qua = phan_tich_batch(danh_sach)
            for item in ket_qua:
                print(f"🔑 {item['password']} → {item['level']} ({item['score']}/100)")
        elif choice == "6":
            print("🛡 Cài đặt bảo mật")
            change_master_password()
        elif choice == "7":
            print("📤 Xuất/Nhập dữ liệu")
            print("1. Xuất vault ra file")
            print("2. Nhập vault từ file")
            sub = input("Chọn chức năng (1-2): ")
            if sub == "1":
                export_vault(key)
            elif sub == "2":
                import_vault(key)
            else:
                 print("⚠️ Vui lòng chọn 1 hoặc 2.")

        elif choice == "8":
            print("👋 Tạm biệt!")
            break
        else:
            print("⚠️ Vui lòng chọn từ 1 đến 8.")
if __name__ == "__main__":
    main()
