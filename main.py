# main.py
from acount import register, login, forget_password
from customer import customer_menu
from staff import staff_menu
from admin import admin_menu

def main():
    while True:
        print("\n=== RESTAURANT ORDERING SYSTEM ===")
        print("1. Register")
        print("2. Log in")
        print("3. Forgot password")
        print("0. Leave")
        choice = input("Select(0-3): ").strip()

        if choice=="1":
            # Đăng ký
            user=register()
            if user:
                print(f"Registered successfully: {user.name} ({user.role})")
        elif choice=="2":
            # Đăng nhập
            user=login()
            if user:
                print(f"Log in successfully: {user.name} ({user.role})")
                # Phân quyền menu theo vai trò
                if user.role=="customer":
                    customer_menu(user)
                elif user.role=="staff":
                    staff_menu(user)
                elif user.role=="admin":
                    admin_menu(user)
            else:
                print("Wrong email or password!")
        elif choice=="3":
            # Quên mật khẩu
            forget_password()
        elif choice=="0":
            print("Exit the system")
            break
        else:
            print("Invalid selection! Please select again.")

if __name__=="__main__":
    main()
