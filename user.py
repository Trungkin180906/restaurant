class User:
    def __init__(self, name, phone, email, password, role="customer", gender="khác"):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.role = role
        self.gender = gender

class Customer(User):
    def __init__(self, name, phone, email, password, gender="khác"):
        super().__init__(name, phone, email, password, "customer", gender)

class Staff(User):
    def __init__(self, name, phone, email, password, gender="khác"):
        super().__init__(name, phone, email, password, "staff", gender)

class Admin:#admin ko kế thừa từ user nên ko dùng supper()
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.role = "admin"


        

