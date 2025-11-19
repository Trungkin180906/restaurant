from menu_order import list_orders
from table import see_table, table_data
def staff_menu(staff):
    while True:
        print("\n===== NHIỆM VỤ NHÂN VIÊN =====")
        print("1. Xem các đơn hàng")
        print("2. Cập nhật trạng thái đơn hàng")
        print("3. Chỉ định bàn cho đơn hàng")
        print("0. Thoát!")
        choose=input("Chọn công việc (0-3): ")

        if choose=='1':
            if not list_orders:
                print("Chưa có đơn hàng")
                continue
            print("\n===== DANH SÁCH ĐƠN HÀNG =====")
            for i,order in enumerate(list_orders, start=1):#dùng enumerate duyệt cái phần tử trong tuple, list, dict qua for
                print(f"{i}. Mã đơn {order['ID']}")
                print(f"Khách hàng   :{order['Họ và tên']}")
                print(f"Phương thức  :{order['Phương thức']}")
                if order['Phương thức'].lower()=='mang đi':
                    print(f"Địa chỉ giao        :{order.get('Địa chỉ', 'không có')}")
                    print(f"SDT nhân            :{order.get('SDT nhận', 'không có')}")
                    print(f"Thời gian dự kiến   :{order.get('Thời gian', 'Không có')}")
                    print(f"Ghi chú cho shipper :{order.get('Ghi chú', 'không có')}")
                print(f"Bàn          :{order.get('Bàn', 'Chưa gán')}")
                print(f"Trạng thái   :{order.get('Trạng thái', 'Mới đặt')}")
                print(f"Thanh toán   :{order.get('Phương thức thanh toán', 'Chưa thanh toán')}")
        elif choose=='2':
            if not list_orders:
                print("Chưa có đơn để cập nhật!")
                continue
            index=input("Nhập số thứ tự đơn cần cập nhật: ").strip()
            if not index.isdigit():#kiểm tra xem có phải số
                print("Vui lòng nhập số!")
                continue
            idx=int(index)-1 
            if 0<=idx<len(list_orders):
                order=list_orders[idx]
                print(f"Đơn hiện tại: {order['ID']} - Trang thái: {order['Trạng thái']}")
                new_status=input("Trạng thái mới (xác nhận/chế biến/hoàn tất/hủy): ").lower().strip()
                if new_status=='hủy':
                    if not order.get('Yêu cầu hủy'):#kiểm tra xem khách đã gửi yêu cầu hay chưa
                        print("Khách chưa gửi yêu cầu hủy đơn")
                        continue
                    #lưu thông tin hoàn tiền cho khách
                    refund_money=order.get("Tính tổng")
                    order['Trạng thái']='Đã hủy'
                    order['Hoàn tiền']=refund_money
                    order['Thông báo']=f"Bạn đã hủy đơn {order['ID']} thành công"
                    list_orders.pop(idx)#xóa khỏi danh sách đơn hàng staff
                    print(order['Thông báo'])
                else:
                    order['Trạng thái']=new_status
                    print(f"Đã cập nhật thành công đơn hàng {new_status}")
            else:
                print("Cập nhật đơn hàng không thành công!")
        elif choose=='3':
            if not list_orders:
                print("Chưa có đơn để chỉ định bàn!")
                continue
            index = input("Nhập số thứ tự đơn cần chỉ định bàn: ").strip()
            if not index.isdigit():
                print("Vui lòng nhập số!")
                continue
            idx = int(index) - 1
            if not (0 <= idx < len(list_orders)):
                print("Không tồn tại đơn hàng!")
                continue
            order = list_orders[idx]
            if order["Phương thức"].lower()!="tại chỗ":
                print("Đơn mang đi - không cần bàn")
                continue
            see_table()
            table_code = input("Nhập mã bàn: ").strip().upper()
            check = False
            for cat, tables in table_data.items():
                for i, t in enumerate(tables):#dùng enumerate duyệt chỉ số i cho là key và t là value
                    t=list(t)#chuyển tuple thành list
                    if t[0].upper() == table_code:
                        check = True
                        if t[2] == "Trống":
                            t[2]="Đã có khách"
                            tables[i]=t #cập nhật lại trong danh sách bàn
                            order["Bàn"] = table_code
                            order["Trạng thái"] = "Đang phục vụ"
                            print(f"Đã gán bàn {table_code} cho đơn {order['ID']}")
                        else:
                            print("Bàn đã có khách, chọn bàn khác!")
                        break
                if check:
                    break
            if not check:
                print("Mã bàn không tồn tại!")
        elif choose=='0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

#staff_menu() 
  
