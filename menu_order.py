# tạo dữ liệu món ăn 
from tabulate import tabulate
dish_data={
    "Lẩu":[("L001", "Gánh Lẩu Cua Đồng", "Ngọt thanh, vị ngon từ đồng quê", 278000, "còn", 40),
           ("L002", "Gánh Lẩu Chua Cay", "Chua cay, đậm đà", 278000, "còn", 50),
           ("L003", "Gánh Lẩu Cà Chua Thảo Mộc", "Ngọt thanh, thơm mùi quế hồi", 315000, "còn", 30),
           ("L004", "Mẹt Lẩu Cua Đồng", "Ngọt thanh, vị ngon từ đồng quê", 248000, "còn", 80),
    ],
    "Món Miệt Vườn":[("M001", "Mẹt Đồng Quê", "Đậm đà đồng quê, hài hòa cùng vị chua cay mặn ngọt", 208000, "còn", 15),
                     ("M002", "Mẹt Dân Dã", "Mặn mà, cay nhẹ, đậm đà hương vị Nam Bộ", 158000, "còn", 20),
                     ("M003", "Bánh Bột Lọc", "Dai, mặn ngọt hài hòa, thơm tôm thịt", 42000, "còn", 60),
                     ("M004", "Bánh ít Trần Tôm Thịt", "Béo bùi, mặn ngọt hòa nguyện cùng nhân tôm thịt", 42000, "còn", 65),
                     ("M005", "Bánh Đúc Chén", "Ngọt thanh, béo nhẹ đậm đà nước mắm", 32000, "còn", 40),
                     ("M006", "Ôc Nhồi Mai Cua", "Cay nhẹ, hình ảnh bắt mắt từ mai cua đồng", 55000, "còn", 52),
                     ("M007", "Hoành Thánh Tôm Thịt", "Thơm, béo nhẹ hòa nguyện cùng sốt chấm xí muội", 52000, "còn", 40),
                     ("M008", "Cơm Cháy Chả Tôm", "Giòn, thơm hòa nguyện cùng sốt chấm xí muội", 62000, "còn", 50),
                     ("M009", "Cua Đồng Rang Me", "Chua ngọt thơm vị cua đồng", 58000, "còn", 70),
                     ("M010", "Cua Đồng Sốt Trứng Muối", "Béo giòn, đậm đà vị trứng muối", 68000, "còn", 70),
    ],
    "Gỏi Đồng Quê":[("G001", "Gỏi Đu Đủ Cua Đồng", "Chua cay nhẹ, ngọt thanh, giòn sần sật, ăn kèm bánh phòn tôm",  68000, "còn", 15),
                    ("G002", "Gỏi Tép Rong Hoa Đồng Nội", "Chua ngọt, thơm nhẹ, ăn kèm bánh phòng tôm", 85000, "còn", 20),
                    ("G003", "Gỏi Khoai Môn Tôm Tươi", "Béo thơm, giòn chua ngọt, ăn kèm bánh phòng tôm", 78000, "còn", 20),
    ],
    "Tráng Miệng":[("T001", "Chè Sương Sa Hạt Lựu", "Ngọt thanh, thơm béo vị nước cốt dừa", 32000, "còn", 10),
                   ("T002", "Sương Sáo Hạt Chia Nước Cốt Dừa", "Mát lạnh, thơm béo ngọt thanh vị nước cốt dừa", 28000, "còn", 12),
                   ("T003", "Sương Sáo Bánh Lọt", "Dai giòn, thơm lá dứa, béo vị nước cốt dừa", 28000, "còn", 8),
                   ("T004", "Khoai Môn Bánh Lọt", "Dai, giòn, thơm lá dứa thanh mát", 28000, "còn", 8)
                  ],
    "Giải Khát":[("N001", "Thảo Dược Rong Biển Hạt Chia", "Ngọt thanh, mát lạnh, thơm thảo mộc", 28000, "còn", 120),
                 ("N002", "Mía Lau Rau Bắp Thạch Dứa", "Ngọt nhẹ, thanh mát, giòn thạch", 28000, "còn", 150),
                 ("N003", "Trà Ô Long Bông Cúc Hạt Chia", "Đậm vị trà, ngọt nhẹ, thanh mát", 28000, "còn", 90),
                 ("N004", "Atiso Đỏ Xí Muội Thạch Dứa", "Chua ngọt, thơm xí muội, atiso", 28000, "còn", 120),
                 ("N005", "Tắc Tươi Xí Muội", "Chua ngọt, thơm xí muội, tắc tươi", 28000, "còn", 90),
    ],
}

list_orders=[]# danh sách đơn hàng
cart=[]#danh sách giỏ hàng món ăn

#xem menu
def see_menu():
    print("\n===== DANH SÁCH MÓN ĂN =====")
    for cat, items in dish_data.items():
        table=[]
        for i in items:
            table.append([i[0], i[1], i[2], f"{i[3]:,}", i[4]]) 
        header=["Mã", "Tên Món", "Khẩu Vị", "Giá", "Tình Trạng"]
        print(f"\n----- {cat.upper()} -----")
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))


#search dish in items
def search_dish(code):
    code=str(code).upper()
    for cat, items in dish_data.items():
        for i in items:
            if str(i[0]).upper()==code.upper():
                return i[1], i[3]
    return None, None        

#search name dish in items
def search_name_dish(keyword):
    print(f"Kết quả tìm kiếm cho: {keyword}")
    search=False
    for cat, items in dish_data.items():
        for i in items:
            if keyword.lower() in i[1].lower():
                print(f"{i[0]} - {i[1]} {i[3]:,}")
                search=True
    if not search:
        print("Không tìm thấy món phù hợp trong menu!")

#sort dish
def sort_dish(category_name):
    # 1. TÌM NHÓM (Giữ nguyên logic tìm kiếm thông minh đã sửa lúc nãy)
    search_key = category_name.strip().lower()
    found_key = None

    for key in dish_data:
        if key.lower() == search_key:
            found_key = key
            break
    
    # 2. NẾU TÌM THẤY -> TIẾN HÀNH SẮP XẾP THỦ CÔNG
    if found_key:
        # Lấy danh sách món ăn của nhóm đó
        # Thêm [:] để tạo bản sao, tránh làm lộn xộn menu gốc
        items_list = dish_data[found_key][:] 
        
        # --- BẮT ĐẦU THUẬT TOÁN BUBBLE SORT (NỔI BỌT) ---
        n = len(items_list)
        
        # Vòng lặp lớn: Duyệt qua toàn bộ danh sách
        for i in range(n):
            # Vòng lặp con: So sánh các cặp liền kề
            for j in range(0, n - i - 1):
                # So sánh GIÁ (index 3) của món trước (j) và món sau (j+1)
                price_current = items_list[j][3]
                price_next = items_list[j+1][3]
                
                # Nếu món trước đắt hơn món sau -> Đổi chỗ (Swap)
                if price_current > price_next:
                    # Thực hiện đổi chỗ
                    items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]
        # --- KẾT THÚC THUẬT TOÁN ---

        # 3. IN KẾT QUẢ (Dùng danh sách items_list đã được sắp xếp ở trên)
        print(f"\n--- NHÓM '{found_key.upper()}' (SẮP XẾP THỦ CÔNG TĂNG DẦN) ---")
        
        table = []
        for i in items_list:
            table.append([i[0], i[1], i[2], f"{i[3]:,}", i[4]])
            
        headers = ["Mã", "Tên Món", "Khẩu Vị", "Giá", "Tình Trạng"]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        
    else:
        print(f"Lỗi: Không tìm thấy nhóm '{category_name}'.")
        print("Các nhóm hiện có: " + ", ".join(dish_data.keys()))

#thêm món ăn vào giỏ hàng
def add_dish_cart(dish_name, price, quantity, note):
    cart.append({
        "Tên món":dish_name,
        "Giá":price,
        "Số lượng":quantity,
        "Ghi chú":note
    })
    print(f"Đã thêm: {quantity} - {dish_name} vào giỏ hàng")

#xem giỏ hàng
def view_cart():
    if not cart:
        print("Giỏ hàng trống!")
        return
    print("\nGIỎ HÀNG CỦA BẠN")
    total=0
    for i, item in enumerate(cart):
        money=item['Giá']*item['Số lượng']
        total+=money
        print(f"{i}: {item['Tên món']} - Số lượng:{item['Số lượng']} - Ghi chú: {item['Ghi chú']} - Giá{money:,}đ")
    print(f"Tổng số tiền {total}VND")

#xóa món ăn khỏi giỏ hàng
def remove_dish_cart(i):
    if 0<=i<len(cart):
        remove=cart.pop(i)
        print(f"Đã xóa {remove['Tên món']} khỏi giỏ hàng")
    else:
        print("Xóa món ăn ko hợp lê!")

#xác nhận đơn hàng
def confirm_order(customer, delivery):
    if not cart:
        print("Không có món trong giỏ hàng")
        return
    order_id=len(list_orders)+1
    total=sum(i['Giá']*i['Số lượng'] for i in cart)
    order_items=[]#danh sách món cho đơn hàng
    for i in cart:
        order_items.append({#tạo đơn hàng
            "Tên món":i['Tên món'],
            "Số lượng":i['Số lượng'],
            "Giá":i['Giá'],
            "Ghi chú":i['Ghi chú'] 
        })
    # Tạo order
    order = {
        "ID": f"DH{order_id:03d}",
        "Họ và tên": customer,
        "Items": order_items,
        "Tính tổng": total,
        "Phương thức": delivery,
        "Trạng thái": "Mới đặt"
    }
    if delivery.lower()=="tại chỗ":
        order['Bàn']="Đợi gán bàn"
    #nếu đơn mang đi sẽ nhập thêm thông tin mang đi
    if delivery.lower()=='mang đi':
        print("\n===== THÔNG TIN GIAO HÀNG =====")
        address=input("Nhập địa chỉ nhận hàng: ").strip()
        phone=input("Nhập SDT nhận hàng: ").strip()
        time=input("Thời gian dự kiến: ").strip()
        note_shipper=input("Ghi chú: ").strip()
        #lưu vào order
        order["Địa chỉ"]=address
        order["Phone"]=phone
        order["Thời gian"]=time
        order["Ghi chú"]=note_shipper
    list_orders.append(order)#thêm vào danh sách dơn hàng
    cart.clear()#xóa giỏ hàng
    print("Đặt hàng thành công")
    payment(order)

def payment(order):
    print("\n===== THANH TOÁN =====")
    print(f"Tổng tiền: {order['Tính tổng']:,} VND")
    while True:
        print("Phương thức thanh toán:")
        print("1. Tiền mặt")
        print("2. Thẻ")
        print("3. Ví điện tử")
    
        choice = input("Chọn phương thức (1/2/3): ").strip()
        if choice == "1":
            method = "Tiền mặt"
            break
        elif choice == "2":
            method = "Thẻ"
            break
        elif choice == "3":
            method = "Ví điện tử"
            break
        else:
            print("Lựa chọn không hợp lệ, mặc định tiền mặt")
            method = "Tiền mặt"
    order["Phương thức thanh toán"] = method
    order["Trạng thái"] = "Đã thanh toán"
    print(f"Thanh toán thành công bằng {method}")
    print_order(order)

#trả về danh sách đơn hàng của khách hàng
def get_customer_order(customer):
    orders=[]
    for order in list_orders:
        orders.append(order)
    return orders
#hủy đơn hàng nếu khách hàng mới đặt 
def cancel_order(customer):
    customer_order=get_customer_order(customer)
    if not customer_order:
        print("Chưa có đơn hàng nào")
        return
    print("\n===== DANH SÁCH ĐƠN HÀNG CỦA BẠN =====")
    for i, order in enumerate(customer_order, 1):
        print(f"{i}. Mã đơn: {order['ID']} - Trạng thái: {order['Trạng thái']} - Tổng tiền: {order['Tính tổng']:,}VND")
    choose=input("Nhập số thứ tự đơn muốn hủy: ").strip()
    if not choose.isdigit():
        print("Phải nhập số hợp lệ")
        return 
    choose=int(choose)-1
    if 0<=choose<len(customer_order):
        cancel=customer_order[choose]
        if cancel['Trạng thái']!='Mới đặt':
            print("Đơn này không thể hủy, đã được chế biến")
            return
        list_orders.remove(cancel)
        print(f"Đã hủy đơn hàng {cancel['ID']} thành công")
    else:
        print("Số thứ tự không hợp lệ!")

#in đơn hàng 
def print_order(order):
    print("\n===== ĐƠN HÀNG CỦA BẠN =====")
    print(f"Mã đơn      :{order['ID']}")
    print(f"Khách hàng  :{order['Họ và tên']} ")
    for i, item in enumerate(order["Items"],1):
        print(f"{i}: {item['Tên món']} - số lượng: {item['Số lượng']} - ghi chú: {item['Ghi chú']} - giá: {item['Giá']:,}đ")
    #nếu đơn mang đi thì sẽ in ra thông tin thêm
    if order['Phương thức'].lower()=='mang đi':
        print(f"Địa chỉ giao        :{order.get('Địa chỉ', 'Chưa có')}")
        print(f"SDT nhận            :{order.get('Phone', 'Chưa có')}")
        print(f"Thời gian dự kiến   :{order.get('Thời gian', 'Chưa có')}")
        print(f"Ghi chú cho shipper :{order.get('Ghi chú', 'Không có')}")
    else:  # đơn tại chỗ
        print(f"Bàn          :{order['Bàn']}")

    if "Phương thức thanh toán" in order:
        print(f"Thanh toán  :{order['Phương thức thanh toán']}")
    print(f"Tính tổng   :{order['Tính tổng']}VND") 
    print(f"Trạng thái  :{order['Trạng thái']}")  
    print("==================================")


