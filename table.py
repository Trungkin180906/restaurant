#tạo list table
from tabulate import tabulate
table_data={
    'A':[("A1", 10, "Empty"),
         ("A2", 10, "Empty"),
         ("A3", 12, "Empty"),
         ("A4", 15, "Empty"),
         ("A5", 20, "Empty"),
         ("A6", 20, "Empty"),
         ],
    'B':[("B1", 5, "Empty"),
         ("B2", 5, "Empty"),
         ("B3", 5, "Empty"),
         ("B4", 7, "Empty"),
         ("B5", 6, "Empty"),
         ],
    'C':[("C1", 3, "Empty"),
         ("C2", 2, "Empty"),
         ("C3", 4, "Empty"),
         ("C4", 3, "Empty"),
    ],
}

def see_table():
    print("\n===== TABLE LIST =====")
    for cat, items in table_data.items():
        table=[]
        for i in items:
            table.append([i[0], i[1], i[2]]) 
        header=["Code", "seat number", "Status"]
        print(f"\n----- {cat.upper()} -----")
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))
