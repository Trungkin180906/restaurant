from menu_order import see_menu, search_dish, order_dish, list_orders
def customer_order(customer):
    while True:
        print("\n========== MENU MÓN ĂN ==========")
        print("1. Xem menu")
        print("2. Tìm kiếm món")
        print("3. Đặt món")
        print("4. Xem đơn hàng")
        print("5. Hủy đơn")
        print("0. Thoát!")
        choose=input("Chọn (0-5): ")

        if choose=='1':
            see_menu()
        elif choose=='2':
            key=input("Nhập món ăn bạn muốn tìm: ").strip()#tránh khoảng trắng
            search_dish(key)
        elif choose=='3':
            order_dish(customer)
        elif choose=='4':
            for i in list_orders:
                if (i["customer"]==customer):
                    print(i)
        elif choose=='5':
            name=customer
            for i in list_orders:
                if i["customer"]==name and i["status"]=="Mới đặt":
                    list_orders.remove(i)
                    print("Hủy đơn thành công")
                    break
                else:
                    print("Hủy đơn không thành công!")
        else:
            break
print(customer_order("nguyễn trung kiên"))


