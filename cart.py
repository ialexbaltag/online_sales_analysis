class Cart:
    
    def __init__(self):
        self.cart_items = []

    # adaugare produs in cos
    def add_to_cart(self, product):
        self.cart_items.append(product)

    # calcul total
    def calculate_total(self):
        total = 0
        for product in self.cart_items:
            total += product["price"] * product["quantity"]
        return total

    # afisare cos
    def display_cart(self):
        if not self.cart_items:
            print("Cosul este gol.")
            return

        print("Produse in cos:")
        for product in self.cart_items:
            print(f"- {product['name']} | Pret: {product['price']} | Cantitate: {product['quantity']}")