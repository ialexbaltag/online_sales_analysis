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
    
    