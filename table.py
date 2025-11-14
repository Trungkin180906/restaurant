#tạo list table
from tabulate import tabulate
table_data={
    'A':[("A1", 10, "Trống"),
         ("A2", 10, "Trống"),
         ("A3", 12, "Trống"),
         ("A4", 15, "Trống"),
         ("A5", 20, "Trống"),
         ("A6", 20, "Trống"),
         ],
    'B':[("B1", 5, "Trống"),
         ("B2", 5, "Trống"),
         ("B3", 5, "Trống"),
         ("B4", 7, "Trống"),
         ("B5", 6, "Trống"),
         ],
    'C':[("C1", 3, "Trống"),
         ("C2", 2, "Trống"),
         ("C3", 4, "Trống"),
         ("C4", 3, "Trống"),
    ],
}

def see_table():
    print("\n========== DANH SÁCH BÀN ==========")
    for cat, items in table_data.items():
        table=[]
        for i in items:
            table.append([i[0], i[1], i[2]]) 
        header=["Mã", "Số Ghế", "Tình trạng"]
        print(f"\n----- {cat.upper()} -----")
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))
