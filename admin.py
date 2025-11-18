from menu_order import see_menu, dish_data
from acount import acount_staff, acount_customer
from user import Staff, Customer

#DISH
#search dish
def find_dish(code):
    code=code.strip().upper()
    for cat, items in dish_data.items():
        for index, i in enumerate(items):#giúp lấy số index và phần tử i (duyệt qua từng danh mục món)
            if i[0].upper()==code:
                return cat, index, i
    return None

#add dish
def add_dish():
    cat=input("Nhóm món: ").strip()
    code=input("Mã món: ").strip().upper()
    name=input("Tên món: ").strip()
    taste=input("Khẩu vị: ").strip()
    price_input=input("Giá: ").strip()
    if not price_input.isdigit():
        print("Giá không hợp lệ!")
        return
    price=int(price_input)
    status=input("Tình trạng: ").strip()
    quantity_input=int(input("Số lượng: ").strip())
    if not quantity_input.isdigit():
        quantity=0
    quantity=int(quantity_input)
    dish=(code, name, taste, price, status, quantity)
    dish_data.setdefault(cat, []).append(dish)#lấy giá trị trả về trong trường hợp key không tồn tại
    print(f"Đã thêm {code} - {name} vào nhóm {cat}")

#xóa món ăn khỏi menu
def remove_dish():
    code=input("Nhập mã món cần xóa: ").strip().upper()
    cat, index, i=find_dish(code)#cat tên danh mục, index, vị trí món trong list, i thông tin của món ăn
    if not i:#nếu i là None
        print("Không tìm thấy mã món!")
        return
    dish_data[cat].pop(index)#ngược lại sẽ truy cập vào mục và xóa món theo vị trí đã chỉ định

def update_dish():
    code=input("Nhập mã món cần cập nhật: ").strip().upper()
    cat, index, i=find_dish(code)
    if not i:
        print("Không tìm thấy mã món!")
        return
    name=input(f"Tên [{i[1]}]: ").strip()
    taste=input(f"Khẩu vị [{i[2]}]: ").strip()

    price_in=input(f"Giá [{i[3]}]")
    price=int(price_in) if price_in else i[3]
    status=input(f"Trạng thái {i[4]}: ").strip() or i[4]
    stock_in=input(f"Số tồn {i[4]}: ").strip()
    stock=int(stock_in) if stock_in.isdigit() else i[4]
    dish_data[cat][index]=(i[0], name, taste, price, status, stock)
    print(f"Đã cập nhất món {i[0]}")



#STAFF
#xem dánh sách nhân viên
def see_staff():
    print("\n===== DANH SÁCH NHÂN VIÊN =====")
    if not acount_staff:
        print("Chua có nhân viên vào")
        return
    for i, staff in enumerate(acount_staff, 1):
        print(f"{i}.{staff.name} - {staff.phone} - {staff.email} - {getattr(staff, 'gender', 'khác')}")#dùng getattr trả về giá trị của thuộc tính muốn tìm

#thêm nhân viên
def add_staff():
    print("\n===== THÊM NHÂN VIÊN =====")
    name=input("Nhập Họ và tên: ").strip()
    phone=input("Nhập SĐT: ").strip()
    email=input("Nhập Email: ").strip()
    gender=input("Giới tính (nam/nữ): ").lower().strip()
    if gender not in ["nam", "nữ"]:
        gender = "khác"
    password = input("Password: ").strip()
    staff = Staff(name, phone, email, password, gender)
    acount_staff.append(staff)
    print(f"Đã thêm nhân viên: {name}")

#xóa nhân viên
def remove_staff():
    see_staff()
    i=input("Nhập số thứ tự nhân viên muốn xóa: ").strip()
    if not i.isdigit():
        print("Phải nhập số hợp lệ")
        return
    i=int(i)-1
    if 0<=i<len(acount_staff):
        removed=acount_staff.pop(i)
        print(f"Đã xóa nhân viên {removed.name} khỏi hệ thống")
    else:   
            print("Số thứ tự không hợp lệ!")

#CUSTOMER
#xem danh sách khách hàng
def see_customer():
    print("\n===== XEM DANH SÁCH KHÁCH HÀNG =====")
    if not acount_customer:
        print("Chưa có khách hàng nào")
        return
    for i, customer in enumerate(acount_customer, 1):
        print(f"{i}.{customer.name} - {customer.phone} - {customer.email}")

#xóa khách hàng
def remove_customer():
    see_customer()
    i=input("Nhập số thứ tự khách hàng muốn xóa: ").strip()
    if not i.isdigit():
        print("Phải nhập số hợp lệ")
        return
    i=int(i)-1
    if 0<=i<len(acount_customer):
        removed=acount_customer.pop(i)
        print(f"Đã xóa khách hàng {removed.name} khỏi hệ thống")
    else:
        print("Số thứ tự không hợp lệ!")

#MANAGEMENT STAFF
def management_staff():
    while True:
        print("\n======= MANAGEMENT STAFF ======")
        print("1. Xem danh sách nhân viên")
        print("2. Thêm nhân viên")
        print("3. Xóa nhân viên")
        print("0. Thoát")
        choose=input("Chọn(0-3): ")

        if choose=='1':
            see_staff()
        elif choose=='2':
            add_staff()
        elif choose=='3':
            remove_staff()
        elif choose=='0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

#MANAGEMENT MENU
def management_menu():
    while True:
        print("\n=== MANAGEMENT MENU  ===")
        print("1. Xem danh sách món ăn")
        print("2. Thêm món")
        print("3. Xóa món")
        print("4. Cập nhật món")
        print("0. Thoát!")
        choose=input("Chọn(0-4): ")

        if choose=='1':
            see_menu()
        elif choose=='2':
            add_dish()
        elif choose=='3':
            remove_dish()
        elif choose=='4':
            update_dish()
        elif choose=='0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

#MANAGEMENT CUSTOMER
def managenet_customer():
    while True:
        print("\n===== MANAGEMENT CUSTOMER =====")
        print("1. Xem danh sách khách hàng")
        print("2. Xóa khách hàng")
        print("0. Thoát")
        choose=input("Chọn(0-2): ").strip()
        if choose=='1':
            see_customer()
        elif choose=='2':
            remove_customer()
        elif choose=='0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

#admin chọn chức năng quản lý của mình
def admin_menu(admin):
    while True:
        print("\n===== LỰA CHỌN CỦA ADMIN =====")
        print("1. Quản lý món ăn")
        print("2. Quản lý nhân viên")
        print("3. Quản lý khách hàng")
        print("0. Thoát")
        choose=input("Chọn(0-2): ")
        if choose=='1':
            management_menu()
        elif choose=='2':
            management_staff()
        elif choose=='3':
            management_menu()
        elif choose=='0':
            break
        else:
            print("Lựa chọn không hợp lệ!")
        
