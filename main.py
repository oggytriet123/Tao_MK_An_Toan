from password_tool import verify_master, KiemTraDoDai, COMMON_PASSWORDS, suggest_smart

def main() :
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

if __name__ == "__main__":
    main()