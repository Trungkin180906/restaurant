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
            
            # Using enumerate to loop through the list of orders
            for i, order in enumerate(list_orders, start=1):
                print(f"{i}. Order ID {order['ID']}")
                print(f"Customer      : {order['Customer Name']}")
                print(f"Method        : {order['Delivery Method']}")
                
                if order['Delivery Method'].lower() == 'take away':
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
            
            if not index.isdigit():  # Check if it is a number
                print("Please enter a number!")
                continue
                
            idx = int(index) - 1 
            
            if 0 <= idx < len(list_orders):
                order = list_orders[idx]
                print(f"Current Order: {order['ID']} - Status: {order['Status']}")
                
                new_status = input("New status (confirm/processing/completed/cancel): ").lower().strip()
                
                if new_status == 'cancel':
                    # Check if the customer has sent a cancellation request
                    if not order.get('Cancellation Request'):
                        print("Customer has not submitted a cancellation request.")
                        continue
                        
                    # Save refund info for the customer
                    refund_money = order.get("Total Amount")
                    order['Status'] = 'Cancelled'
                    order['Refund Amount'] = refund_money
                    order['Notification'] = f"Order {order['ID']} cancelled successfully."
                    
                    list_orders.pop(idx)  # Remove from staff order list
                    print(order['Notification'])
                    
                elif new_status in ['confirm', 'processing', 'completed']:
                    # Map input status to standardized English status names
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
            
            if not (0 <= idx < len(list_orders)):
                print("Order does not exist!")
                continue
                
            order = list_orders[idx]
            
            if order["Delivery Method"].lower() != "at venue":
                print("Take away order - no table needed.")
                continue
                
            see_table()  # Function from imported module
            table_code = input("Enter table code: ").strip().upper()
            check = False
            
            for cat, tables in table_data.items():
                # Using enumerate to loop through the index (i) and value (t)
                for i, t in enumerate(tables):
                    t = list(t)  # Convert tuple to list for modification
                    
                    if t[0].upper() == table_code:
                        check = True
                        if t[2] == "Trống": # Assuming table_data uses "Trống" for empty
                            t[2] = "Occupied"
                            tables[i] = tuple(t) # Update back as tuple/list depending on table_data structure
                            
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