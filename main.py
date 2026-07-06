import json

products = []

def login():
    print("===== LOGIN =====")

    password = input("Enter admin password: ")

    if password != "admin123":
        print("Access Denied ❌")
        exit()
    else:
        print("Login Successful ✅")

users = []
orders = []

#================= SAVE ===================

def save_products():
    with open("products.json", "w") as f:
        json.dump(products, f, indent=4)

#================= LOAD PRODUCTS==============

def load_products():
    global products
    try:
        with open("products.json", "r") as f:
            products = json.load(f)
    except FileNotFoundError:
        products = []

#================= SAVE ORDERS ===================

def save_orders():
    with open("orders.json", "w") as f:
        json.dump(orders, f, indent=4)

#================= LOAD ORDERS ===================

def load_orders():
    global orders
    try:
        with open("orders.json", "r") as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = []        

#=================== ADD ==================== 

def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Product Quantity: "))

    product = {
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    save_products()
    print("Product added successfully!")

#====================== VIEW =====================

def view_products():
    if len(products) == 0:
        print("No products found!")
        return

    print("\n===== PRODUCT LIST =====")
    for i, p in enumerate(products, start=1):
      print(f"{i}. ID: {p['product_id']} | Name: {p['name']} | Price: {p['price']} | Qty: {p['quantity']}")
#======================= DELETE ====================

def delete_product():
    view_products()
    
    if len(products) == 0:
        return

    try:
        num = int(input("\nEnter product number to delete: "))
        
        if 1 <= num <= len(products):
            removed = products.pop(num - 1)
            save_products()
            print(f"{removed['name']} deleted successfully!")
        else:
            print("Invalid product number")

    except ValueError:
        print("Please enter a valid number")

#======================= UPDATE ======================

def update_product():
    view_products()

    if len(products) == 0:
        return

    try:
        num = int(input("\nEnter product number to update: "))

        if 1 <= num <= len(products):
            product = products[num - 1]

            print("\nLeave blank if you don't want to change")

            new_name = input(f"New name ({product['name']}): ")
            new_price = input(f"New price ({product['price']}): ")
            new_qty = input(f"New quantity ({product['quantity']}): ")

            if new_name:
                product['name'] = new_name
            if new_price:
                product['price'] = float(new_price)
            if new_qty:
                product['quantity'] = int(new_qty)

            save_products()
            print("Product updated successfully!")

        else:
            print("Invalid product number")

    except ValueError:
        print("Invalid input")

#=================== SEARCH ====================

def search_product():
    keyword = input("Enter product name to search: ").lower()

    found = False

    print("\n===== SEARCH RESULTS =====")
    for p in products:
        if keyword in p['name'].lower():
            print(f"Name: {p['name']} | Price: {p['price']} | Qty: {p['quantity']}")
            found = True

    if not found:
        print("No matching product found!")

#=================== TOTAL VALUE =================

def total_value():
    total = 0

    for p in products:
        total += p['price'] * p['quantity']

    print("\n===== TOTAL STOCK VALUE =====")
    print("Total Value:", total)

#==================== GENERATE BILL ===================

def generate_bill():
    if len(products) == 0:
        print("No products available!")
        return

    cart = []
    total = 0

    view_products()

    print("\n👉 Enter product number and quantity (0 to stop)")

    while True:
        try:
            num = int(input("Product number: "))

            if num == 0:
                break

            if 1 <= num <= len(products):
                qty = int(input("Quantity: "))
                p = products[num - 1]

                item_total = p['price'] * qty
                total += item_total

                cart.append({
                    "name": p['name'],
                    "qty": qty,
                    "price": p['price'],
                    "total": item_total
                })
            else:
                print("Invalid product number")

        except ValueError:
            print("Enter valid numbers only")
    
    if len(cart) == 0:
        print("No items selected!")
        return

    orders.append({
    "items": cart,
    "total": total
    })

    save_orders()

    # BILL PRINT
    print("\n===== 🧾 BILL RECEIPT =====")
    for item in cart:
        print(f"{item['name']} x {item['qty']} = {item['total']}")

    print("----------------------")
    print("TOTAL AMOUNT:", total)
    print("======================")

#==================== VIEW ORDERS =================

def view_orders():
    if len(orders) == 0:
        print("No orders found!")
        return

    print("\n===== ORDER HISTORY =====")

    for i, order in enumerate(orders, start=1):
        print(f"\nOrder {i}")
        for item in order["items"]:
            print(f"{item['name']} x {item['qty']} = {item['total']}")
        print("Total Amount:", order["total"])
        print("-------------------------")

#==================== MAIN PROGRAM =================

load_products()
load_orders()
login()

print("===== MAIN MENU =====")

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. Update Product")
    print("5. Search Product")
    print("6. Total Stock Value")
    print("7. Generate Bill")
    print("8. View Orders")
    print("9. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        delete_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        search_product()
    elif choice == "6":
        total_value()
    elif choice == "7":
        generate_bill()
    elif choice == "8":
        view_orders()
    elif choice == "9":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")