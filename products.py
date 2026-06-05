from database import connect_db

def add_product():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Product Name: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    sql = """
    INSERT INTO products
    (product_name, category, quantity, price)
    VALUES (%s,%s,%s,%s)
    """

    values = (name, category, quantity, price)

    cursor.execute(sql, values)
    conn.commit()

    print("Product Added Successfully")

    cursor.close()
    conn.close()
