class ProductManager:
    
    product_list=[]
    
    def __init__(self):
        self.product_list = []
    
    
    def add_products(self, product):
        self.product_list.append(product)

    
    def display_total_products(self):
        return len(self.product_list)
    
    def total_values_products(self):
        total = 0
        for product in self.product_list:
            total += product.price * product.quantity
        return total


    def remove_product_by_name(self, name):
        for product in self.product_list:
            if product.name.lower() == name.lower():
                self.product_list.remove(product)
                print(f"Product '{name}' removed from inventory.")
                return
        print(f"Product '{name}' not found.")
    
