# main.py
from acount import register, login, forget_password
from customer import customer_menu
from staff import staff_menu
from admin import admin_menu

def main():
    while True:
        print("\n=== HỆ THỐNG ĐẶT MÓN NHÀ HÀNG ===")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Quên mật khẩu")
        print("0. Thoát")
        choice = input("Chọn(0-3): ").strip()

        if choice=="1":
            # Đăng ký
            user=register()
            if user:
                print(f"Đăng ký thành công: {user.name} ({user.role})")
        elif choice=="2":
            # Đăng nhập
            user=login()
            if user:
                print(f"Đăng nhập thành công: {user.name} ({user.role})")
                # Phân quyền menu theo vai trò
                if user.role=="customer":
                    customer_menu(user)
                elif user.role=="staff":
                    staff_menu(user)
                elif user.role=="admin":
                    admin_menu(user)
            else:
                print("Sai email hoặc mật khẩu!")
        elif choice=="3":
            # Quên mật khẩu
            forget_password()
        elif choice=="0":
            print("Thoát hệ thống")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại")

if __name__=="__main__":
    main()
