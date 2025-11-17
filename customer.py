from menu_order import see_menu, search_dish, add_dish_cart, view_cart, remove_dish_cart, print_order, confirm_order, list_orders, cart
def customer_menu(customer):
    customer=input("Nhập Họ và tên: ").strip()
    while True:
        print("\n===== MENU MÓN ĂN =====")
        print("1. Xem menu")
        print("2. Thêm món vào giỏ hàng ")
        print("3. Xem giỏ hàng")
        print("4. Xóa món trong giỏ hàng")
        print("5. Xác nhận đặt hàng")
        print("6. Xem tất cả đơn hàng")
        print("0. Thoát!")
        choose=input("Chọn (0-6): ").strip()

        if choose=='1':
            see_menu()
        elif choose=='2':
            see_menu()
            code=input("Nhập mã món: ").strip().upper()
            dish_name, price=search_dish(code)
            if dish_name:
                quantity=int(input("Số lượng: "))
                note=input("Ghi chú: ")
                add_dish_cart(dish_name, price, quantity, note)
            else:
                print("Mã món không hợp lệ")
        elif choose=='3':
                view_cart()
        elif choose=='4':
            view_cart()
            index=input("Nhập số thứ tự món cần xóa: ").strip()
            if index.isdigit():
                idx=int(index)-1
                remove_dish_cart(idx)
        elif choose=='5':
            if not cart:
                print("Giỏ hàng trống, vui lòng thêm món vào trước khi đặt hàng")
                continue
            delivery=input("Hình thức (tại chỗ/mang đi): ").lower().strip()
            if delivery not in ['tại chỗ', 'mang đi']:
                print("Hình thức không hợp lệ, mặc định là 'mang đi")
                delivery='mang đi'
            confirm_order(customer, delivery)
        elif choose=='6':
            if not list_orders:
                print("Chưa có đơn hàng nào")
            else:
                for i in list_orders:
                    print_order(i)
        else:
            break
#customer_order("nguyễn trung kiên")


