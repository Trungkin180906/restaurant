from menu_order import see_menu, add_dish_cart, view_cart, remove_dish_cart, print_order, confirm_order, list_orders, cancel_order, sort_dish, search_name_dish
def update_customer(customer):
    print("\n===== CẬP NHẬT TÀI KHOẢN CÁ NHÂN =====")
    print(f"Email (không thể thay đổi): {customer.email}")
    name=input("Họ và tên: ").strip()
    phone=input("SDT: ").strip()
    gender=input(f"Giới tính ({customer.gender}): ").lower().strip()
    password=input("Password: ")
    if name:
        customer.name=name
    if phone:
        customer.phone=phone
    if gender in ["nam", "nữ"]:
        customer.gender=gender
    else:
        customer.gender='khác'
    if password:
        customer.password=password
    print("Cập nhật thông tin thành công")

def customer_menu(customer):
    while True:
        print("\n===== MENU KHÁCH HÀNG =====")
        print("1. Xem & cập thông tin cá nhân")
        print("2. Xem menu & sắp xếp theo giá món")
        print("3. Tìm & thêm món vào giỏ hàn")
        print("4. Xem giỏ hàng")
        print("5. Xóa món trong giỏ hàng")
        print("6. Xác nhận đặt hàng")
        print("7. Xem đơn hàng")
        print("8. Hủy đơn hàng")
        print("0. Thoát!")
        choose=input("Chọn (0-8): ")

        if choose=='1':
            print("\n===== THÔNG TIN KHÁCH HÀNG =====")
            print(f"Họ tên: {customer.name}")
            print(f"SDT: {customer.phone}")
            print(f"Email: {customer.email}")
            print(f"Giới tính: {customer.gender}")
            update_info=input("Bạn có muốn cập nhật thông tin không (y/n): ").strip()
            if update_info=='y':
                update_customer(customer)
        elif choose=='2':
            see_menu()
            sort_input=input("Bạn có muốn sắp xếp theo giá không (y/n): ").strip()
            if sort_input=='y':
                category=input("Nhập nhóm món cần sắp xếp: ").strip()
                sort_dish(category)
        elif choose=='3':
            keyword=input("Nhập tên món hoặc từ khóa: ").strip()
            if not keyword:
                print("Mã món không tìm thấy")
            else:
                result=search_name_dish(keyword)
                if not result:
                    print(f"Không tìm thấy món có từ {keyword}")
                else:
                    print("\n===== KẾT QUẢ CHO TÌM KIẾM =====")
                    for i in result:
                        print(f"{i['Mã']}. {i['Tên món']} - {i['Giá']}")
                    code=input("Nhập mã món muốn thêm vào giỏ hàng: ").upper().strip()
                    dish=None
                    for i in result:
                        if i['Mã'].upper()==code:
                            dish=i
                            break
                    if dish:
                        quantity=int(input("Số lượng: "))
                        note=input("Ghi chú: ")
                        add_dish_cart(dish['Tên món'], dish['Giá'], quantity, note)
                    else:
                        print("Mã món không hợp lệ!")
        elif choose=='4':
            view_cart()
        elif choose=='5':
            index=input("Nhập vị trí món cần xóa: ").strip()
            if index.isdigit():
                remove_dish_cart(int(index))
            else:
                print("Vị trí không hợp lệ!")
        elif choose=='6':
            delivery=input("Phương thức: (tại chỗ/mang đi): ").strip()
            confirm_order(customer.name, delivery)
        elif choose=='7':
            if not list_orders:
                print("Chưa có đơn hàng nào")
            else:
                for order in list_orders:
                    print_order(order)
        elif choose=='8':
            cancel_order(customer.name)
        elif choose=='0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

             
#customer_menu("nguyễn trung kiên")
