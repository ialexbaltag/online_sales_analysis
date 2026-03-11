from product import Product
from product_manager import ProductManager


productsInventory = ProductManager()

    # products 
p1 = Product("Laptop", 1200, 5)
p2 = Product("Mouse", 25, 20)
p3 = Product("Keyboard", 70, 10)

    # add products
productsInventory.add_products(p1)
productsInventory.add_products(p2)
productsInventory.add_products(p3)

    # display products
print("Inventory products:")
for product in productsInventory.product_list:
    print(product.info_about_product())

    # total products
print("\nTotal number of products:", productsInventory.display_total_products())

    # total value stock
print("Total inventory value:", productsInventory.total_values_products(), "euros")

productsInventory.remove_product_by_name("Mouse")

