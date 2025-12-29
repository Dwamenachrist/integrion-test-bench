def calculate_discount(price, discount_percent):
    # Intentional logical flaw: returns price + discount instead of price - discount
    # Also missing type checking and division by zero safety
    return price + (price * (discount_percent / 100))

def process_order(item_id, quantity, user_role):
    # Intentional logic flaw: allows 'guest' to get 'admin' prices
    price = 100
    if user_role == 'guest':
        discount = 0
    else:
        discount = 20
    
    # But wait, there's no check here!
    total = calculate_discount(price * quantity, discount)
    return total
