from password_tool import  kiem_tra_do_dai,COMMON_PASSWORDS, suggest_smart
from master_manager import setup_master,verify_master

def main() :
    print("=== 🔒 BẮT ĐẦU CHƯƠNG TRÌNH KIỂM TRA MẬT KHẨU ===")
    verify_master()  # 🧩 Bắt buộc xác thực trước khi tiếp tục

    print("🔐 Kiểm tra độ mạnh mật khẩu 🔐")
    print("----------------------------------")
    password = input("Nhập mật khẩu của bạn: ")

    score, level, suggestion = kiem_tra_do_dai(password, COMMON_PASSWORDS)

    print(f"\nĐiểm đánh giá: {score}/100")
    print(f"Đánh giá: {level}")
    if "trung bình" in level.lower() or "yếu" in level.lower() :
         print("\n🤖 Gợi ý mật khẩu thông minh dựa trên mật khẩu bạn nhập:")
         smart_suggestions = suggest_smart(password,5)
         for s in smart_suggestions :
             print("👉",s)

if __name__ == "__main__":
    main()