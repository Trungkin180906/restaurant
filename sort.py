from menu_order import dish_data
from tabulate import tabulate


#sort dish in menu
def sort_menu(data):
    sorted_menu={} #tạo một dict mới để duyệt từng giá trị vào đây

    # 2. Duyệt qua từng nhóm
    for category_name, dish_list in data.items():
        # 3. Sắp xếp danh sách món ăn của nhóm đó
        sorted_dish_list = sorted(dish_list, key=lambda dish: dish[3])
        
        # 4. Thêm vào menu mới
        sorted_menu[category_name] = sorted_dish_list
    return sorted_menu    
# --- SỬ DỤNG HÀM ---
menu_da_sap_xep = sort_menu(dish_data)

# In thử kết quả của nhóm "Tráng Miệng"
def menu_sorted(key2):
    if key2 in menu_da_sap_xep:
        # Sử dụng f-string và .upper() để in tên nhóm
        print(f"\n--- NHÓM '{key2.upper()}' ĐÃ SẮP XẾP ---")
        
        headers = ["ID", "Tên Món", "Mô tả", "Giá", "Trạng thái", "Tồn kho"]
        print(tabulate(menu_da_sap_xep[key2], headers=headers, tablefmt="grid"))
    else:
        # Báo lỗi nếu người dùng nhập sai tên nhóm
        print(f"Lỗi: Không tìm thấy nhóm món ăn nào có tên là '{key2}'.")

