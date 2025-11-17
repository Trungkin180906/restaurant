from menu_order import see_menu, dish_data
from acount import acount_staff
from user import Staff

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
    try:
        price=int(input("Giá: ").strip())
    except Exception:
        print("Giá không hợp lệ!")
        return
    status=input("Tình trạng: ").strip()
    try:
        quantity=int(input("Số lượng: ").strip())
    except Exception:
        quantity=0
    dish=(code, name, taste, price, status, quantity)
    dish_data.setdefault(cat, []).append(dish)#lấy giá trị trả về trong trường hợp key không tồn tại
    print(f"Đã thêm {code} - {name} vào nhóm {cat}")
    
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
    try:
        price_in=input(f"Giá [{i[3]}]")
        price=int(price_in) if price_in else i[3]
    except Exception:
        print("Giá không hợp lệ, giữ nguyên!")
        price=i[3]
    status=input(f"Trạng thái {i[4]}: ").strip()
    try:
        stock_in=input(f"Số tồn {i[4]}: ").strip()
        stock=int(stock_in) if stock_in else i[4]
    except Exception:
        stock=i[4]
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
    try:
        i=int(i)-1
        if 0<=i<len(acount_staff):
            removed=acount_staff.pop(i)
            print(f"Đã xóa nhân viên {removed.name} khỏi hệ thống")
        else:   
            print("Số thứ tự không hợp lệ!")
    except Exception:
        print("Phải nhập số hợp lệ")

#MANAGEMENT STAFF
def management_staff():
    while True:
        print("\n======= MANAGEMENT STAFF ======")
        print("1. Xem danh sách nhân viên")
        print("2. Thêm nhân viên")
        print("3. Xóa nhân viên")
        print("0. Thoát")
        choose=input("Chọn(0-4): ")

        if choose=='1':
            see_staff()
        elif choose=='2':
            add_staff()
        elif choose=='3':
            remove_staff()
        else:
            break

#MANAGEMENT MENU
def management_menu():
    while True:
        print("\n=== MANAGEMENT MENU  ===")
        print("1. Xem danh sách món ăn")
        print("2. Thêm món")
        print("3. Xóa món")
        print("4. Cập nhật món")
        print("0. Thoát!")
        choose=input("Chọn(0-3): ")

        if choose=='1':
            see_menu()
        elif choose=='2':
            add_dish()
        elif choose=='3':
            remove_dish()
        elif choose=='4':
            update_dish()
        else:
            break

#admin chọn chức năng quản lý của mình
def admin_control():
    while True:
        print("\nLỰA CHỌN CỦA ADMIN")
        print("1. Quản lý món ăn")
        print("2. Quản lý nhân viên")
        print("0. Thoát")
        choose=input("Chọn(0-2): ")
        if choose=='1':
            management_menu()
        elif choose=='2':
            management_staff()
        else:
            break


        
