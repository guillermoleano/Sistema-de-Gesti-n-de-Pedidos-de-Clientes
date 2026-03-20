print("Welcome to the Customer Order Management System")

while = True:
    option = input("""
    Please select an option:
    --------------------------------
    1. Create orders
    2. Consult orders
    3. Generate report
    4. Exit
    --------------------------------
    """)
    if option == "1":
        client = function1_client_registration()
        product = function2_product_registration()
        order_total, quantity = function3_order_creation(client, product)
    if option == "2":
        function4_consulting_order_registered(client, product, quantity, order_total)
        function5_daily_revenue_calculation()
    if option == "3":
        function6_final_report_generation()
    if option == "4":
        print("Goodbye!")
        
