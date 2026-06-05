from products import add_product

while True:
    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("1. Add Product")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        break
