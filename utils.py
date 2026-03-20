
def function1_client_registration():
    print("\n--- Register New Customer ---")
    client_id = input("Enter customer ID: ")
    client_name = input("Enter customer name: ")
    
    while True:
        email = input("Enter customer email: ")
        if "@" in email:
            break 
        else:
            print("Error: Your email must have an @ to be registered.")

    
    client_registration = {
        "client_name": client_name,
        "client_email": email,
        "client_id": client_id,
    }    
    return client_registration
def function2_product_registration():
    product_name = input("Enter product name: ")
    
    try:
        unit_price = float(input("Enter unit price: "))
    except ValueError:
        print("Invalid price. Using 0.0")
        price = 0.0
    
    
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: ")) 

    
    product_registration = (product_id, product_name, unit_price, quantity) 
    return product_registration
def function3_order_creation(client, product):
    #print(product[2])  # ver variable unit_price
    #print(product[3])   # ver variable quantity
    unit_price =product[2] # buscar valor de la tupla (unit_price)en posicion product[2] y añadir a variable unit_price
    quantity = product[3] # buscar valor de la tupla (quantity)en posicion product[3] y añadir a variable quantity
    order_total = unit_price * quantity
    #print(order_total) #test

    return order_total
def function4_consulting_order_registered(order_created):
    #print(order_created)  
    
    for i in range(0, len(order_created), 3):
        client = order_created[i]
        product = order_created[i+1]
        total = order_created[i+2]
        print("-" * 30)
        print("Client:", client)
        print("Product:", product)
        print("Total:", total)
        print("-" * 30)
def function5_daily_revenue_calculation(order_created):
    print(order_created)
    sum_total = 0

    for i in range(0, len(order_created), 3):
        total = order_created[i+2]
        sum_total += total   # to accumulate the total of revenue
    print("Total revenue:", sum_total)
    return sum_total
def function6_final_report_generation(order_created):

    # <-- here prints the number of orders
    print(f"Number of orders: {int(len(order_created)/3)}") 

    # <-- here prints the total revenue
    sum_final_report = 0
    for i in range(0, len(order_created), 3):
        total = order_created[i+2]
        sum_final_report += total   # <-- aquí acumulas
    print("Total revenue:", sum_final_report)


    for i in range(0, len(order_created), 3):
        product = order_created[i+1][1]
        print(f"Product: {product} - Quantity: {order_created[i+1][3]}") # <-- aqui imprimes el producto)

    print(order_created)

    report = {}

    for i in range(0, len(order_created), 3):
        product = order_created[i+1][1]
        quantity = order_created[i+1][3]
        report[product] = report.get(product, 0) + quantity
    print(report)

    #------------------PRINT ORDER GROUPED BY CLIENT
    order_by_client = {}

    for i in range(0, len(order_created), 3):
        client = order_created[i]
        product = order_created[i+1]
        total = order_created[i+2]

        name = client['client_name']

        if name not in order_by_client:
            order_by_client[name] = {
                "products": []
            }

        order_by_client[name]["products"].append({
            "product": product[1],
            "quantity": product[3],
            "total": total
        })

    # Imprimir pedidos agrupados
    for client, info in order_by_client.items():
        print(f"\nClient: {client}" )
        print("Associated products:")
        for p in info["products"]:
            print(f"  - {p['product']} | Quantity: {p['quantity']} | Total: {p['total']}")
