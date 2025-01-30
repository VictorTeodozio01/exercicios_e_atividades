def validate_product(data):
    if not data['name'] or data['quantity'] < 0:
        raise ValueError("Invalid product data")
    return data
