class User:
    def __init__(self, name, phone, email, password, role="customer"):
        self.name=name
        self.phone=phone
        self.email=email
        self.password=password
        self.role=role
#super() Cho phép tham chiếu đến Parent Class
class Customer(User):
    def __init__(self, name, phone, email, password):
        super().__init__(name, phone, email, password, "customer")
    
class Staff(User):
    def __init__(self, name, phone, birthday, email, password):
        super().__init__(name, phone, birthday, email, password, "Staff")

class Admin(User):
     def __init__(self, name, phone, email, password):
        super().__init__(name, phone, email, password, "Admin")
        
