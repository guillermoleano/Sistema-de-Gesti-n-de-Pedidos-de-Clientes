order_created = ()
import time
from utils import function1_client_registration 
from utils import function2_product_registration
from utils import function3_order_creation
from utils import function4_consulting_order_registered
from utils import function5_daily_revenue_calculation
from utils import function6_final_report_generation

print("Welcome to the Customer Order Management System")

while True:
    option = int(input("""
    Please select an option:
    --------------------------------
    1. Create orders
    2. Consult orders
    3. Daily Revenue Calculation
    4. Final Report                
    5. Exit
    --------------------------------
    Enter your choice:"""))
    
    if option == 1:
        client = function1_client_registration()
        print(f"Success! Customer {client['client_name']} registered.")  
        product = function2_product_registration()
        print(f"Success! Product  registered for {client['client_name']} .")
        total = function3_order_creation(client, product)
        #print(f"Success! Order created for {client['client_name'] with total: {total}")
        order_created = order_created + (client, product, total)
        #print(order_created)
    if option == 2:
        function4_consulting_order_registered(order_created)
    if option == 3:
        revenue = function5_daily_revenue_calculation(order_created)
    if option == 4:
        function6_final_report_generation(order_created)
    if option == 5:
        print("Goodbye!")
        break
    
    
