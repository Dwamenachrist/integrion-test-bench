def get_user_data(user_id):
    # Potential SQL Injection if used in DB query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

def process_payment(amount, card_number):
    # CRITICAL: Secret logging
    print(f"Processing payment of {amount} for card {card_number}")
    return True
