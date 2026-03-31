import random
from cart import Cart
from product import Product
from product_manager import ProductManager


productsInventory = ProductManager()

    # products 
p1 = Product("Smartphone", 1200, 3)
p2 = Product("SmartTV", 3400, 3)
p3 = Product("USB Drive", 25, 10)

    # add products
productsInventory.add_products(p1)
productsInventory.add_products(p2)
productsInventory.add_products(p3)

    # display products
# print("Inventory products:")
# for product in productsInventory.product_list:
#     print(product.info_about_product())

    # total products
print("\nTotal number of products:", productsInventory.display_total_products())

#     # total value stock
# print("Total inventory value:", productsInventory.total_values_products(), "euros")




# creare instanta cart
cart = Cart()


# alegere produse
selected_products = random.sample(ProductManager.product_list, 3)


# adaugare in cos
for product in selected_products:
    cart.add_to_cart(product)

# afisare cos si plata totala
cart.display_cart()

total = cart.calculate_total()
print(f"\nTotal de plata: {total} lei")



