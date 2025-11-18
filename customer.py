from menu_order import see_menu, search_dish, add_dish_cart, view_cart, remove_dish_cart, print_order, confirm_order, list_orders, cancel_order, search_name_dish,sort_dish
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
        print("1. Xem thông tin cá nhân")
        print("2. Cập nhật thông tin cá nhân")
        print("3. Xem menu")
        print("4. Tìm - thêm món vào giỏ hàng ")
        print("5. Xem giỏ hàng")
        print("6. Xóa món trong giỏ hàng")
        print("7. Xác nhận đặt hàng")
        print("8. Xem đơn hàng")
        print("9. Hủy đơn hàng")
        print("10. tìm theo tên")
        print("11. sắp xếp tăng dần theo giá")
        print("0. Thoát!")
        choose=input("Chọn (0-11): ")

        if choose=='1':
            print(f"Họ tên: {customer.name}")
            print(f"SDT: {customer.phone}")
            print(f"Email: {customer.email}")
            print(f"Giới tính: {customer.gender}")
        elif choose=='2':
            update_customer(customer)
        elif choose=='3':
            see_menu()
        elif choose=='4':
            code=input("Nhập mã món: ").strip().upper()
            dish_name, price=search_dish(code)
            if dish_name:
                quantity=int(input("Số lượng: "))
                note=input("Ghi chú: ")
                add_dish_cart(dish_name, price, quantity, note)
            else:
                print("Mã món không hợp lệ")
        elif choose=='5':
            view_cart()
        elif choose=='6':
            index=input("Nhập vị trí món cần xóa")
            if index.isdigit():
                remove_dish_cart(int(index))
            else:
                print("Vị trí không hợp lệ!")
        elif choose=='7':
            delivery=input("Phương thức: (tại chỗ/mang đi): ").strip()
            confirm_order(customer.name, delivery)
        elif choose=='8':
            print("\n===== TẤT CẢ ĐƠN HÀNG CỦA KHÁCH =====")
            if not list_orders:
                print("Chưa có đơn nào!")
            else:
                for order in list_orders:
                    print_order(order)
        elif choose=='9':
            cancel_order(customer)
        elif choose=="10":
            key=input("nhập tên món ăn: ").strip()
            search_name_dish(key)
        elif choose=="11":
            print("Lẩu / Món Miệt Vườn / Gỏi Đồng Quê / Tráng Miệng / Giải Khát ")
            key2 = input("Nhập nhóm món ăn bạn muốn sắp xếp: ").strip()
            sort_dish(key2)
        elif choose=='0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

             
#customer_order("nguyễn trung kiên")
