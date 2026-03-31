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



