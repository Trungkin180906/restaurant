import random
from user import Customer, Staff, Admin

acount_admin = [Admin("Admin Name", "admin@example.com", "admin12345")]#admin đã có sẵn 
acount_customer=[]
acount_staff=[]

def register():
    print("\n===== ĐĂNG KÝ TÀI KHOẢN =====")
    name=input("Nhập Họ và tên: ").strip()
    phone=input("Nhập SĐT: ").strip()
    email=input("Nhập Email: ").strip()

    gender=input("Nhập giới tính(nam/nữ): ").lower().strip()
    if gender not in ["nam", "nữ"]:
        gender="khác"

    password=input("Nhập password: ").strip()

    for i in acount_customer:
        if i.email==email:
            print("Email của bạn đã tồn tại")
            return

    print("\nCHỌN VAI TRÒ")
    print("1. Customer")
    print("2. Staff do admin đăng nhập")
    role=input("Nhập vai trò của người dùng (1/2): ").strip()

    #role customer
    if role=='1':
        user=Customer(name, phone, email, password, gender)
        acount_customer.append(user)
        print("Đăng ký customer thành công")
        return user

    #role staff
    elif role=='2':
        print("Không thể tự đăng ký, vui lòng liên hệ lại admin")
        return
    else:
        print("Lựa chọn không hợp lệ")

#admin tạo tk cho staff
def admin_create_staff(admin):
    print("TẠO TÀI KHOẢN CHO STAFF")
    name=input("Nhập Họ và tên: ").strip()
    phone=input("Nhập SĐT: ").strip()
    email=input("Nhập Email: ").strip()
    password=input("Password: ").strip()
    gender=input("Nhập giới tính(nam/nữ): ").lower().strip()
    #kiểm tra email trung
    for s in acount_staff:
        if s.email==email:
            print("Email đã tồn tại")
            return
    staff=Staff(name, phone, email, password, gender)
    acount_staff.append(staff)
    return staff

#đăng nhập tài khoản
def login():
    print("\n===== ĐĂNG NHẬP TÀI KHOẢN =====")
    email = input("Email: ").strip()
    password = input("Mật khẩu: ").strip()
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
    print("Sai mặt khẩu hoặc email")

#trường hợp người dùng quên mật khẩu
def forget_password():
    print("\n===== QUÊN MẬT KHẨU =====")
    email=input("Nhập email để khôi phục mật khẩu: ").strip()
    user=None
    for i in acount_customer:
        if i.email==email:
            user=i
            break
    if not user:
        print("Không tìm thấy tài khoản với email này!")
        return
    #tạo otp
    otp=str(random.randint(100000, 999999))
    print(f"Mã otp khôi phục {otp}")
    user_otp=input("Nhập mã otp: ").strip()
    if user_otp != otp:
        print("otp không đúng vui, khôi phục thất bại!")
        return
    print("otp chính xác hãy đặt mật khẩu")
    new_pass=input("Nhập mật khẩu mới: ")
    user.password=new_pass
    print("Đổi mật khẩu thành công")
