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
    cat=input("Dish group: ").strip()
    code=input("Dish code: ").strip().upper()
    name=input("Dish name: ").strip()
    taste=input("Taste: ").strip()
    price_input=input("Price: ").strip()
    if not price_input.isdigit():
        print("Price is not valid!")
        return
    price=int(price_input)
    status=input("Status: ").strip()
    quantity_input=input("Quantity: ").strip()
    if not quantity_input.isdigit():
        quantity=0
    quantity=int(quantity_input)
    dish=(code, name, taste, price, status, quantity)
    dish_data.setdefault(cat, []).append(dish)#lấy giá trị trả về trong trường hợp key không tồn tại
    print(f"Added {code} - {name} to {cat}")

#xóa món ăn khỏi menu
def remove_dish():
    code=input("Enter the code of the dish you want to delete: ").strip().upper()
    cat, index, i=find_dish(code)#cat tên danh mục, index, vị trí món trong list, i thông tin của món ăn
    if not i:#nếu i là None
        print("Dish code not found!")
        return
    dish_data[cat].pop(index)#ngược lại sẽ truy cập vào mục và xóa món theo vị trí đã chỉ định

def update_dish():
    code=input("Enter the dish code that needs to be updated: ").strip().upper()
    cat, index, i=find_dish(code)
    if not i:
        print("Dish code not found!")
        return
    name=input(f"Name [{i[1]}]: ").strip()
    taste=input(f"Taste [{i[2]}]: ").strip()

    price_in=input(f"Price [{i[3]}]")
    price=int(price_in) if price_in else i[3]
    status=input(f"Status {i[4]}: ").strip() or i[4]
    stock_in=input(f"quantity {i[4]}: ").strip()
    stock=int(stock_in) if stock_in.isdigit() else i[4]
    dish_data[cat][index]=(i[0], name, taste, price, status, stock)
    print(f"Updated the dish {i[0]}")



#STAFF
#xem dánh sách nhân viên
def see_staff():
    print("\n===== EMPLOYEE LIST =====")
    if not acount_staff:
        print("empty")
        return
    for i, staff in enumerate(acount_staff, 1):
        print(f"{i}.{staff.name} - {staff.phone} - {staff.email} - {getattr(staff, 'sex', 'other')}")#dùng getattr trả về giá trị của thuộc tính muốn tìm

#thêm nhân viên
def add_staff():
    print("\n===== ADD EMPLOYEE =====")
    name=input("Name: ").strip()
    phone=input("Phone number: ").strip()
    email=input("Email: ").strip()
    gender=input("Sex (male/female): ").lower().strip()
    if gender not in ["male", "female"]:
        gender = "other"
    password = input("Password: ").strip()
    staff = Staff(name, phone, email, password, gender)
    acount_staff.append(staff)
    print(f"Added staff: {name}")

#xóa nhân viên
def remove_staff():
    see_staff()
    i=input("Enter the staff number you want to delete: ").strip()
    if not i.isdigit():
        print("Must enter a valid number")
        return
    i=int(i)-1
    if 0<=i<len(acount_staff):
        removed=acount_staff.pop(i)
        print(f"deleted staff {removed.name} from to system")
    else:   
            print("Invalid serial number!")

#CUSTOMER
#xem danh sách khách hàng
def see_customer():
    print("\n===== VIEW CUSTOMER LIST =====")
    if not acount_customer:
        print("no customer yet")
        return
    for i, customer in enumerate(acount_customer, 1):
        print(f"{i}.{customer.name} - {customer.phone} - {customer.email}")

#xóa khách hàng
def remove_customer():
    see_customer()
    i=input("Enter the customer number want to delete: ").strip()
    if not i.isdigit():
        print("Must enter a valid number")
        return
    i=int(i)-1
    if 0<=i<len(acount_customer):
        removed=acount_customer.pop(i)
        print(f"deleted customer {removed.name} from to system")
    else:
        print("Invalid serial number!")

#MANAGEMENT STAFF
def management_staff():
    while True:
        print("\n===== MANAGEMENT STAFF =====")
        print("1. View list of staff")
        print("2. Add staff")
        print("3. Delete staff")
        print("0. Leave")
        choose=input("Select(0-3): ")

        if choose=='1':
            see_staff()
        elif choose=='2':
            add_staff()
        elif choose=='3':
            remove_staff()
        elif choose=='0':
            break
        else:
            print("Invalid selection!")

#MANAGEMENT MENU
def management_menu():
    while True:
        print("\n===== MANAGEMENT MENU  =====")
        print("1. View dish list")
        print("2. Add dish")
        print("3. Delete dish")
        print("4. Update dish")
        print("0. Leave!")
        choose=input("Select(0-4): ")

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
            print("Invalid selection!")

#MANAGEMENT CUSTOMER
def management_customer():
    while True:
        print("\n===== MANAGEMENT CUSTOMER =====")
        print("1. View customer list")
        print("2. Delete customer")
        print("0. Leave")
        choose=input("Select(0-2): ").strip()
        if choose=='1':
            see_customer()
        elif choose=='2':
            remove_customer()
        elif choose=='0':
            break
        else:
            print("Invalid selection!")

#admin chọn chức năng quản lý của mình
def admin_menu(admin):
    while True:
        print("\n===== ADMIN SELECT FUNCTION =====")
        print("1. Dish management")
        print("2. Staff management")
        print("3. Customer management")
        print("0. Leave")
        choose=input("Select(0-3): ")
        if choose=='1':
            management_menu()
        elif choose=='2':
            management_staff()
        elif choose=='3':
            management_customer()
        elif choose=='0':
            break
        else:
            print("Invalid selection!")
        
