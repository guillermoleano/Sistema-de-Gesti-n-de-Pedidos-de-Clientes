from pprint import pprint


register_customer = {}
register_product = {}


def registering_customer():
    print("\n--- Register New Customer ---")
    id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    
    while True:
        email = input("Enter customer email: ")
        if "@" in email:
            break  
        else:
            print("Error: Your email must have an @ to be registered.")

    
    register_customer = {
        "client_name": name,
        "client_email": email,
        "client_id": id,
    }
    print(f"Success! Customer {register_customer} registered.")
    return register_customer

def registering_product():
    print("\n--- Register New Product ---")
    product_name = input("Enter product name: ")
    try:
        price = float(input("Enter unit price: "))
    except ValueError:
        print("Invalid price. Using 0.0")
        price = 0.0
    
    
    product_id = len(register_product) + 1
    
    
    register_product[product_id] = {
        "name": product_name,
        "price": price
        
    }
    print(f"Product '{product_name}' registered with ID: {product_id}")

registering_customer()







