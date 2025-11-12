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


#table of dish in menu
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
def search_dish(keyword):
    print(f"Kết quả tìm kiếm cho: {keyword}")
    search=False
    for cat, items in dish_data.items():
        for i in items:
            if keyword.lower() in i[1].lower():
                print(f"{i[0]} - {i[1]} {i[3]:,}")
                search=True
    if not search:
        print("Không tìm thấy món phù hợp trong menu!")



list_orders=[]# create list empty contains content order
#customer order dish in menu
def order_dish(customer):
    see_menu()
    code=input("Nhập mã món muốn đặt: ").upper()
    quantity=int(input("Số lượng: "))
    note=input("Ghi chú: ")
    delivery=input("Hình thức (tại chỗ/mang đi): ")

    #trường hợp thêm 
    table_code=None
    if delivery.lower()=="tại chỗ":
        while True: #lập đến khi có bàn trống
            table_code=input("Nhập số bàn: ").upper()
            search_table=False
            for cat, tables in table_data.items():
                for t in tables:
                    if (t[0]==table_code):
                        search_table=True
                        if (t[2]=="Trống"):
                            break
                        elif (t[2]=="Đã có khách"):
                            break
                        else:
                            print("Bàn đã có khách chọn bàn khác!")
                            table_code=None
            if search_table and table_code:
                break
            elif not search_table:
                print("Mã bàn không hợp lệ, vui lòng nhập lại!")

    for cat, items in dish_data.items():
        for i in items:
            if i[0]==code:
                total=i[3]*quantity# tính tổng giá món * số lượng món
                order={
                    "Họ và tên":customer,
                    "Tên món":i[1],
                    "Số lượng":quantity,
                    "Ghi chú":note,
                    "Phương thức":delivery,
                    "Bàn":table_code if table_code else "giao hàng",
                    "Tính tổng":total,
                    "Trạng thái":"Mới đặt" 
                }
                list_orders.append(order)
                print(f"Đặt món {i[1]} thành công, tổng: {total:,} - bàn {order['table']} - Hình thức: {delivery} - Trạng thái: {order['status']}")

#testing        
if __name__=="__main__":
    see_menu()
    search_dish('cua')
    order_dish('Nguyễn Trung Kiên')
