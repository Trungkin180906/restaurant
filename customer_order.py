# tạo dữ liệu món ăn 
from tabulate import tabulate
from table import table_data

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
    print("\n========== DANH SÁCH MÓN ĂN ==========")
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
        print(f"{i}: {item['Tên món']} - Số lượng:{item['Số lượng']} - {item['Ghi chú']} - {money:,}VND")
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
        "Bàn": "Đợi gán bàn" if delivery.lower()!="Tại chỗ" else "Không cần bàn",  # Nhân viên sẽ gán sau
        "Trạng thái": "Mới đặt"
    }

    list_orders.append(order)#thêm vào danh sách dơn hàng
    cart.clear()#xóa giỏ hàng
    print("Đặt hàng thành công")
    payment(order)

def payment(order):
    print("\n=== THANH TOÁN ===")
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

#in đơn hàng 
def print_order(order):
    print("\nĐơn hàng của bạn")
    print(f"Mã đơn      :{order['ID']}")
    print(f"Khách hàng  :{order['Họ và tên']} ")
    for i, item in enumerate(order["Items"],1):
        print(f"{i}: {item['Tên món']} - {item['Số lượng']} - {item['Ghi chú']} - {item['Giá']:,}đ")
    print(f"Phương thức :{order['Phương thức']}")
    print(f"Bàn         :{order['Bàn']}")
    if "Phương thức thanh toán" in order:
        print(f"Thanh toán   :{order['Phương thức thanh toán']}")
    print(f"Tính tổng   :{order['Tính tổng']}VND") 
    print(f"Trạng thái  :{order['Trạng thái']}")  
    print("==================================")

#tạo hàm xem id đơn hàng
def find_order_by_id(order_id):
    for order in list_orders:
        if order["ID"] == order_id:
            return order
    return None



