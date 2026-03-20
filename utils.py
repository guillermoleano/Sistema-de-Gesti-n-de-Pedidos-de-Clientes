def function1_client_registration():
    client_registration : {
        "client_id":client_id
        "client_name":client_name
        "email":email
    }
    return client_registration
def function2_product_registration():
    product_registration = (product_id, product_name, unit_price, quantity) 
    return product_registration
def function3_order_creation(client, product):
    unit_price =product[2] # buscar valor de la tupla (unit_price)en posicion product[2] y añadir a variable unit_price
    quantity = product[3] # buscar valor de la tupla (quantity)en posicion product[3] y añadir a variable quantity
    order_total = unit_price * quantity
    return order_total
def function4_consulting_order_registered(client, product, total):
    
      
def function5_daily_revenue_calculation():
def function6_final_report_generation():
