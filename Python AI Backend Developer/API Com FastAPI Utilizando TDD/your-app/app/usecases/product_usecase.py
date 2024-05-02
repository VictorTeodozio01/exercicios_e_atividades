from app.models.product_model import ProductModel

def create_product(product_data):
    return ProductModel.insert_one(product_data)

def update_product(product_id, update_data):
    result = ProductModel.find_one({'_id': product_id})
    if not result:
        raise Exception("Product not found")
    ProductModel.update_one({'_id': product_id}, {'$set': update_data})
    return update_data
