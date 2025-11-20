# tạo dữ liệu món ăn 
from tabulate import tabulate
dish_data = {
    "Lau":[
        ("L001", "Ganh Lau Cua Dong", "Ngot thanh, vi ngon tu dong que", 278000, "con", 40),
        ("L002", "Ganh Lau Chua Cay", "Chua cay, dam da", 278000, "con", 50),
        ("L003", "Ganh Lau Ca Chua Thao Moc", "Ngot thanh, thom mui que hoi", 315000, "con", 30),
        ("L004", "Met Lau Cua Dong", "Ngot thanh, vi ngon tu dong que", 248000, "con", 80),
    ],
    "Mon Miet Vuon":[
        ("M001", "Met Dong Que", "Dam da dong que, hai hoa cung vi chua cay man ngot", 208000, "con", 15),
        ("M002", "Met Dan Da", "Man ma, cay nhe, dam da huong vi Nam Bo", 158000, "con", 20),
        ("M003", "Banh Bot Loc", "Dai, man ngot hai hoa, thom tom thit", 42000, "con", 60),
        ("M004", "Banh it Tran Tom Thit", "Beo bui, man ngot hoa nguyen cung nhan tom thit", 42000, "con", 65),
        ("M005", "Banh Duc Chen", "Ngot thanh, beo nhe dam da nuoc mam", 32000, "con", 40),
        ("M006", "Oc Choi Mai Cua", "Cay nhe, hinh anh bat mat tu mai cua dong", 55000, "con", 52),
        ("M007", "Hoanh Thanh Tom Thit", "Thom, beo nhe hoa nguyen cung sot cham xi muoi", 52000, "con", 40),
        ("M008", "Com Chay Cha Tom", "Gion, thom hoa nguyen cung sot cham xi muoi", 62000, "con", 50),
        ("M009", "Cua Dong Rang Me", "Chua ngot thom vi cua dong", 58000, "con", 70),
        ("M010", "Cua Dong Sot Trung Muoi", "Beo gion, dam da vi trung muoi", 68000, "con", 70),
    ],
    "Goi Dong Que":[
        ("G001", "Goi Du Du Cua Dong", "Chua cay nhe, ngot thanh, gion san sat, an kem banh phon tom", 68000, "con", 15),
        ("G002", "Goi Tep Rong Hoa Dong Noi", "Chua ngot, thom nhe, an kem banh phong tom", 85000, "con", 20),
        ("G003", "Goi Khoai Mon Tom Tuoi", "Beo thom, gion chua ngot, an kem banh phong tom", 78000, "con", 20),
    ],
    "Trang Mieng":[
        ("T001", "Che Suong Sa Hat Luu", "Ngot thanh, thom beo vi nuoc cot dua", 32000, "con", 10),
        ("T002", "Suong Sao Hat Chia Nuoc Cot Dua", "Mat lanh, thom beo ngot thanh vi nuoc cot dua", 28000, "con", 12),
        ("T003", "Suong Sao Banh Lot", "Dai gion, thom la dua, beo vi nuoc cot dua", 28000, "con", 8),
        ("T004", "Khoai Mon Banh Lot", "Dai, gion, thom la dua thanh mat", 28000, "con", 8)
    ],
    "Giai Khat":[
        ("N001", "Thao Duoc Rong Bien Hat Chia", "Ngot thanh, mat lanh, thom thao moc", 28000, "con", 120),
        ("N002", "Mia Lau Rau Bap Thach Dua", "Ngot nhe, thanh mat, gion thach", 28000, "con", 150),
        ("N003", "Tra O Long Bong Cuc Hat Chia", "Dam vi tra, ngot nhe, thanh mat", 28000, "con", 90),
        ("N004", "Atiso Do Xi Muoi Thach Dua", "Chua ngot, thom xi muoi, atiso", 28000, "con", 120),
        ("N005", "Tac Tuoi Xi Muoi", "Chua ngot, thom xi muoi, tac tuoi", 28000, "con", 90),
    ],
}

list_orders=[]# danh sách đơn hàng
cart=[]#danh sách giỏ hàng món ăn

#xem menu
def see_menu():
    print("\n===== DISH LIST =====")
    for cat, items in dish_data.items():
        table=[]#bảng rỗng để lưu trữ dữ liệu món ăn
        for i in items:
            table.append([i[0], i[1], i[2], f"{i[3]:,}", i[4]])#thêm dữ liệu món ăn vào bảng
        header=["Code", "Dish name", "Taste", "Price", "Status"]#
        print(f"\n----- {cat.upper()} -----")
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))#in dữ liệu dạng bảng

#search Dish name in items
def search_name_dish(keyword):
    keyword=keyword.lower()
    result=[]
    for cat, items in dish_data.items():
        for i in items:
            if keyword.lower() in i[1].lower():
                result.append({
                    "Code":i[0],
                    "Dish name":i[1],
                    "Price":i[3]
                })
    return result

#sort dish
def sort_dish(category_name):
    search_key = category_name.strip().lower()#chuẩn hóa chuỗi nhập vào và gán cho biến mới
    found_key = None
    for key in dish_data:
        if key.lower() == search_key:
            found_key = key#
            break
    if found_key:#nếu tìm thấy nhóm món
        # Lấy danh sách món ăn của nhóm đó
        # Thêm [:] để tạo bản sao, tránh làm lộn xộn menu gốc
        items_list = dish_data[found_key][:] 
        n = len(items_list)#số lượng món trong nhóm
        for i in range(n):#duyệt từng món trong nhóm
            for j in range(0, n - i - 1):#duyệt từ món đầu tiên đến món kế cuối
                price_current = items_list[j][3]#so sánh giá món hiện tại
                price_next = items_list[j+1][3]#so sánh giá món kế tiếp
                if price_current > price_next:#nếu món hiện tại giá cao hơn món kế
                    items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]#thực hiện đổi chỗ
        print(f"\n--- Group '{found_key.upper()}' (MANUAL SORTING ASCRIPTION) ---")
        
        table = []#bảng rỗng lưu trữ món ăn đã sắp xếp
        for i in items_list:
            table.append([i[0], i[1], i[2], f"{i[3]:,}", i[4]])           
        headers = ["Code", "Dish name", "Taste", "Price", "Status"]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))#in ra bảng món ăn đã sắp xếp
    else:
        print(f"Error: cant found group '{category_name}'.")
        print("Existing groups: " + ", ".join(dish_data.keys()))

#thêm món ăn vào giỏ hàng
def add_dish_cart(dish_name, price, quantity, note):
    cart.append({#tạo mục chứa món ăn
        "Name dish": dish_name,
        "Price": price,
        "Quantity": quantity,
        "Note": note
    })
    print(f"Added: {quantity} - {dish_name} to shopping cart")

#xem giỏ hàng
def view_cart():
    if not cart:
        print("Shopping cart is empty!")
        return
    print("\n===== YOUR SHOPPING CART =====")
    total = 0
    for i, item in enumerate(cart, 1):
        money = item['Price'] * item['Quantity']
        total += money
        print(f"{i}: {item['Name dish']} - Quantity: {item['Quantity']} - Note: {item['Note']} - Price: {money:,}VND")
    print(f"Total amount: {total:,} VND")

#xóa món ăn khỏi giỏ hàng
def remove_dish_cart(i):
    index=i-1#vị trí đơn trong giỏ hàng
    if 0<=index<len(cart):#kiểm tra vị trí món ăn
        remove = cart.pop(index)
        print(f"Removed {remove['Name dish']} from cart.") 
    else:
        print("Invalid dish removal!")

#xác nhận đơn hàng
def confirm_order(customer, delivery):
    if not cart:
        print("No items in the shopping cart.")
        return
        
    order_id = len(list_orders) + 1#tạo mã đơn mới
    total = sum(i['Price'] * i['Quantity'] for i in cart)#duyệt giỏ hàng tính tổng tiền 
    order_items = []#danh sách món trong đơn hàng
    for i in cart:
        order_items.append({
            "Name dish": i['Name dish'],
            "Quantity": i['Quantity'],
            "Price": i['Price'],
            "Note": i['Note']
        })
        
    # tạo đơn hàng
    order_id=len(list_orders)+1
    order = {
        "ID": f"DH{order_id:03d}",
        "Customer Name": customer,
        "Items": order_items,
        "Total Amount": total,
        "Delivery Method": delivery,
        "Status": "New Order"
    }
    if delivery.lower() == "for here":#nếu đơn hàng tại chỗ
        order['Table'] = "Waiting for table assignment"

    if delivery.lower() == "takeaway":#nếu đơn hàng mang đi
        print("\n===== DELIVERY INFORMATION =====") 
        address = input("Enter delivery address: ").strip()
        phone = input("Enter phone number: ").strip()
        time = input("Estimated time: ").strip()
        note_shipper = input("Note for shipper: ").strip()
        #lưu thông tin giao hàng vào đơn hàng
        order["Address"] = address
        order["Phone"] = phone
        order["Time"] = time
        order["Note for Shipper"] = note_shipper
    list_orders.append(order)#thêm đơn hàng vào danh sách đơn hàng
    cart.clear()#xóa giỏ hàng sau khi đặt đơn
    print("Order placed successfully.") 
    payment(order)

def payment(order):
    print("\n===== PAYMENT =====")
    print(f"Total Amount: {order['Total Amount']:,} VND") 
    while True:
        print("Payment Method:")
        print("1. Cash")
        print("2. Card")
        print("3. E-wallet")
        choice = input("Select method (1/2/3): ").strip() 
        
        if choice == "1":
            method = "Cash"
            break
        elif choice == "2":
            method = "Card"
            break
        elif choice == "3":
            method = "E-wallet"
            break
        else:
            print("Invalid choice, defaulting to Cash.") 
            method = "Cash"
    order["Payment Method"] = method
    order["Status"] = "Paid"
    
    print(f"Payment successful with {method}.") 
    print_order(order)

#lấy đơn hàng của lấy hàng
def get_customer_order(customer):
    orders=[]#danh sách đơn hàng của khách hàng
    for order in list_orders:
        if order['Customer Name'] == customer: 
            orders.append(order)
    return orders

# hủy đơn hàng
def cancel_order(customer):
    customer_order = get_customer_order(customer)#gọi đơn hàng của khách hàng
    if not customer_order:
        print("No orders have been placed yet.") 
        return
    print("\n===== YOUR ORDER LIST =====") 
    for i, order in enumerate(customer_order, 1):
        print(f"{i}. Order ID: {order['ID']} - Status: {order['Status']} - Total Amount: {order['Total Amount']:,} VND")
    choose = input("Enter the number of the order to cancel: ").strip() 
    if not choose.isdigit():
        print("Must enter a valid number.") 
        return 
    choose = int(choose) - 1#chuyển sang int
    if 0<=choose<len(customer_order):#kiểm tra vị trí đơn hàng
        cancel = customer_order[choose]
        if cancel.get('Cancellation Request'):#yêu cầu hủy
            print("You have already submitted a cancellation request for this order.")
            return
        cancel['Cancellation Request'] = True
        print(f"You have submitted a cancellation request for order {cancel['ID']}. Please wait for staff approval.")    
    else:
        print("Invalid number!")

# print order
def print_order(order):
    print("\n===== YOUR ORDER =====") 
    print(f"Order ID       :{order['ID']}")
    print(f"Customer       :{order['Customer Name']} ") 
    for i, item in enumerate(order["Items"], 1):#duyệt từng món trong đơn hàng
        print(f"{i}: {item['Name dish']} - Quantity: {item['Quantity']} - Note: {item['Note']} - Price: {item['Price']:,}VND")
    if order['Delivery Method'].lower() == 'takeaway':#nếu đơn mang đi
        print(f"Delivery Address      :{order.get('Address', 'Not available')}")
        print(f"Recipient Phone       :{order.get('Phone', 'Not available')}")
        print(f"Estimated Time        :{order.get('Time', 'Not available')}")
        print(f"Note for Shipper      :{order.get('Note for Shipper', 'None')}")
    else:#đơn tại chỗ
        print(f"Table          :{order['Table']}") 
    if "Payment Method" in order:#phương thức thanh toán
        print(f"Payment        :{order['Payment Method']}")
    print(f"Total Amount   :{order['Total Amount']:,} VND") 
    print(f"Status         :{order['Status']}") 
    print("==================================")
