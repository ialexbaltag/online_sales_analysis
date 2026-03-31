class Product:
        
    name=""
    price=0.0
    quantity=0
    
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    
    def info_about_product(self):
        return f"Product: {self.name}, Price: {self.price} euros , Quantity: {self.quantity}"

    def update_quantity_products(self, amount):
        if self.quantity + amount < 0:
            print("Stock negative!")
        else:
            self.quantity += amount