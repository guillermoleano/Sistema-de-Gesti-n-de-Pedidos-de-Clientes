import time
from utils import function1_client_registration 
from utils import function2_product_registration
from utils import function3_order_creation
from utils import function4_consulting_order_registered
from utils import function5_daily_revenue_calculation
from utils import function6_final_report_generation

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
    if option == 1:
        client = function1_client_registration()
        product = function2_product_registration()
        total = function3_order_creation(client, product)
    if option == 2:
        function4_consulting_order_registered(client, product, total)
        function5_daily_revenue_calculation()
    if option == "3":
        function6_final_report_generation()
    if option == "4":
        print("Goodbye!")
        
