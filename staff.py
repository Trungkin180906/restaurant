from menu_order import list_orders
from table import see_table, table_data

def staff_menu(staff):
    while True:
        print("\n===== STAFF DUTIES =====")
        print("1. View all orders")
        print("2. Update order status")
        print("3. Assign table to order")
        print("0. Exit!")
        choose = input("Select task (0-3): ")

        if choose == '1':
            if not list_orders:
                print("No orders yet.")
                continue
            print("\n===== ORDER LIST =====")
            for i, order in enumerate(list_orders, start=1):#duyệt từng đơn hàng mặc định từ 1
                print(f"{i}. Order ID {order['ID']}")
                print(f"Customer      : {order['Customer Name']}")
                print(f"Method        : {order['Delivery Method']}")
                if order['Delivery Method'].lower()=="takeaway":#nếu đơn mang đi
                    print(f"Delivery Address      : {order.get('Address', 'Not available')}")
                    print(f"Recipient Phone       : {order.get('Phone', 'Not available')}")
                    print(f"Estimated Time        : {order.get('Time', 'Not available')}")
                    print(f"Note for Shipper      : {order.get('Note for Shipper', 'None')}")
                print(f"Table         : {order.get('Table', 'Not assigned')}")
                print(f"Status        : {order.get('Status', 'New Order')}")
                print(f"Payment       : {order.get('Payment Method', 'Not paid')}")
        elif choose == '2':
            if not list_orders:
                print("No orders to update!")
                continue
            index = input("Enter the sequence number of the order to update: ").strip()
            if not index.isdigit():
                print("Please enter a number!")
                continue
            idx = int(index) - 1 
            if 0<=idx<len(list_orders):
                order=list_orders[idx]#lấy đơn hàng cần cập nhật
                print(f"Current Order: {order['ID']} - Status: {order['Status']}")
                new_status = input("New status (confirm/processing/completed/cancel): ").lower().strip()
                if new_status == 'cancel':
                    if not order.get('Cancellation Request'):#kiểm tra khách đã yêu cầu hủy chưa
                        print("Customer has not submitted a cancellation request.")
                        continue
                    #lưu thông tin hoàn tiền cho khách
                    refund_money = order.get("Total Amount")
                    order['Status'] = 'Cancelled'
                    order['Refund Amount'] = refund_money
                    order['Notification'] = f"Order {order['ID']} cancelled successfully."
                    
                    list_orders.pop(idx)#xóa khỏi danh sách đơn hàng của nhân viên
                    print(order['Notification'])
                    
                elif new_status in ['confirm', 'processing', 'completed']:#nếu trạng thái hợp lệ
                    #cập nhật thông tin trạng thái đơn hàng
                    if new_status == 'confirm':
                        final_status = 'Confirmed'
                    elif new_status == 'processing':
                        final_status = 'In Processing'
                    elif new_status == 'completed':
                        final_status = 'Completed'
                    
                    order['Status'] = final_status
                    print(f"Successfully updated order status to {final_status}.")
                else:
                    print("Invalid status option.") 
            else:
                print("Order update failed (Invalid order number)!")
                
        elif choose == '3':
            if not list_orders:
                print("No orders to assign a table to!")
                continue

            index = input("Enter the sequence number of the order to assign a table: ").strip()
            if not index.isdigit():
                print("Please enter a number!")
                continue
            idx = int(index) - 1
            if not (0<=idx<len(list_orders)):
                print("Order does not exist!")
                continue   
            order = list_orders[idx]#lấy đơn hàng cần chỉ định bàn
            if order["Delivery Method"].lower() != "for here":
                print("Take away order - no table needed.")
                continue
                
            see_table()#xem danh sách bàn
            table_code = input("Enter table code: ").strip().upper()
            check = False
            for cat, tables in table_data.items():
                for i, t in enumerate(tables):#duyệt i là mã bàn t là thông tin bàn
                    t = list(t)#chuyển tuple thành list 
                    if t[0].upper()==table_code:
                        check = True
                        if t[2] == "empty":#kiểm tra tình trạng bàn
                            t[2] = "Occupied"
                            tables[i]=t#cập nhật lại danh sách bàng
                            order["Table"] = table_code
                            order["Status"] = "Serving"
                            print(f"Successfully assigned table {table_code} to order {order['ID']}")
                        else:
                            print("Table is occupied, choose another table!")
                        break
                if check:
                    break
            if not check:
                print("Table code does not exist!")
        elif choose == '0':
            break
        else:
            print("Invalid choice!")

#staff_menu()s
