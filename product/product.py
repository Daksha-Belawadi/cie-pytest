def get_product_details():
    name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity available: "))

    return {
        "name": name,
        "id": product_id,
        "quantity": quantity
    }


def display_product(product):
    print("\n========== PRODUCT DETAILS ==========")
    print(f"Product Name : {product['name']}")
    print(f"Product ID   : {product['id']}")
    print(f"Quantity     : {product['quantity']}")

    if product['quantity'] < 10:
        print(" WARNING: Stock is low!")

    print("=====================================")


if __name__ == "__main__":
    product = get_product_details()
    display_product(product)