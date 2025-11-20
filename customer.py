from menu_order import see_menu, add_dish_cart, view_cart, remove_dish_cart, print_order, confirm_order, list_orders, cancel_order, sort_dish, search_name_dish

#cập nhật thông tin khách hàng
def update_customer(customer):
    print("\n===== UPDATE PERSONAL ACCOUNT =====")
    print(f"Email (cannot changes): {customer.email}")
    name=input("Name: ").strip()
    phone=input("Phone number: ").strip()
    gender=input(f"Sex ({customer.gender}): ").lower().strip()
    password=input("Password: ")
    if name:
        customer.name=name
    if phone:
        customer.phone=phone
    if gender in ["male", "female"]:
        customer.gender=gender
    else:
        customer.gender='other'
    if password:
        customer.password=password
    print("Information updated successfully")

def customer_menu(customer):
    while True:
        print("\n===== CUSTOMER MENU =====")
        print("1. View and update personal information")
        print("2. View menu and sort by price")
        print("3. Find and add dishes to shopping cart")
        print("4. View shopping cart")
        print("5. delete dish in shopping cart")
        print("6. comfirm order")
        print("7. View order")
        print("8. Cancel order")
        print("0. Leave!")
        choose=input("Select(0-8): ")

        if choose=='1':
            print("\n===== CUSTOMER INFORMATION =====")
            print(f"Name: {customer.name}")
            print(f"Phone number: {customer.phone}")
            print(f"Email: {customer.email}")
            print(f"Sex: {customer.gender}")
            update_info=input("Would you like to update your information? (y/n): ").strip()
            if update_info=='y':
                update_customer(customer)
        elif choose=='2':
            see_menu()
            sort_input=input("Do you want to sort by price? (y/n): ").strip()
            if sort_input=='y':
                category=input("Enter the group of dish to be sorted: ").strip()
                sort_dish(category)
        elif choose=='3':
            keyword=input("Enter dish name or keyword: ").strip()
            if not keyword:
                print("Dish code not found")
            else:
                result=search_name_dish(keyword)
                if not result:
                    print(f"No dish found with the word: {keyword}")
                else:
                    print("\n===== SEARCH RESULTS =====")
                    for i in result:
                        print(f"{i['Code']}. {i['Dish name']} - {i['Price']}")
                    code=input("Enter the dish code you want to add to your shopping cart: ").upper().strip()
                    dish=None
                    for i in result:
                        if i['Code'].upper()==code:
                            dish=i
                            break
                    if dish:
                        quantity=int(input("Quantity: "))
                        note=input("Note: ")
                        add_dish_cart(dish['Dish name'], dish['Price'], quantity, note)
                    else:
                        print("Invalid dish code!")
        elif choose=='4':
            view_cart()
        elif choose=='5':
            index=input("Enter the location of the dish to be deleted: ").strip()
            if index.isdigit():
                remove_dish_cart(int(index))
            else:
                print("Invalid location!")
        elif choose=='6':
            delivery=input("Method: (for here/takeaway): ").strip()
            confirm_order(customer.name, delivery)
        elif choose=='7':
            if not list_orders:
                print("No orders yet")
            else:
                for order in list_orders:
                    print_order(order)
        elif choose=='8':
            cancel_order(customer.name)
        elif choose=='0':
            break
        else:
            print("Invalid selection!")

             
#customer_menu("nguyễn trung kiên")
