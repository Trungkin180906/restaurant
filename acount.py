import random
from user import Customer, Staff, Admin

acount_admin = [Admin("Admin Name", "admin@example.com", "admin12345")]#admin đã có sẵn 
acount_customer=[]
acount_staff=[]

def register():
    print("\n===== CREATE ACCOUNT =====")
    name=input("Name: ").strip()
    phone=input("Phone number: ").strip()
    email=input("Email: ").strip()

    gender=input("(male/female): ").lower().strip()
    if gender not in ["male", "female"]:
        gender="other"

    password=input("Password: ").strip()

    for i in acount_customer:
        if i.email==email:
            print("Your email has already been used")
            return

    print("\n===== CHOOSE A ROLE =====")
    print("1. Customer")
    print("2. Staff (authorized by admin)")
    role=input("Enter user role(1/2): ").strip()

    #role customer
    if role=='1':
        user=Customer(name, phone, email, password, gender)
        acount_customer.append(user)
        return user

    #role staff
    elif role=='2':
        print("Cannot register yourself, please contact admin again")
        return
    else:
        print("Invalid selection")

#admin tạo tk cho staff
def admin_create_staff(admin):
    print("\n===== CREATE ACCOUNT FOR STAFF =====")
    name=input("Name: ").strip()
    phone=input("Phone number: ").strip()
    email=input("Email: ").strip()
    password=input("Password: ").strip()
    gender=input("Sex(male/female): ").lower().strip()
    #kiểm tra email trung
    for s in acount_staff:
        if s.email==email:
            print("Your email has already been used")
            return
    staff=Staff(name, phone, email, password, gender)
    acount_staff.append(staff)
    return staff

#đăng nhập tài khoản
def login():
    print("\n===== LOGIN =====")
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    #check admin
    for admin in acount_admin:
        if admin.email==email and admin.password==password:
            return admin
    #check staff
    for staff in acount_staff:
        if staff.email==email and staff.password==password:
            return staff
    #check customer
    for customer in acount_customer:
        if customer.email==email and customer.password==password:
            return customer
    # print("Sai mặt khẩu hoặc email")

#trường hợp người dùng quên mật khẩu
def forget_password():
    print("\n===== FORGOT PASSWORD =====")
    email=input("Enter email to recover password: ").strip()
    user=None
    for i in acount_customer:
        if i.email==email:
            user=i
            break
    if not user:
        print("We couldn't find an account associated with that email address!")
        return
    #tạo otp
    otp=str(random.randint(100000, 999999))
    print(f"Recovery OTP code {otp}")
    user_otp=input("Enter OTP code: ").strip()
    if user_otp != otp:
        print("OTP code is wrong, recovery failed!")
        return
    print("OTP code is correct, please set password")
    new_pass=input("Enter new password: ")
    user.password=new_pass
    print("Password changed successfully")
