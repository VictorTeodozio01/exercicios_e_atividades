from flask import request, jsonify, Blueprint
from app.usecases.product_usecase import create_product, update_product

product_bp = Blueprint('products', __name__)

@product_bp.route('/products', methods=['POST'])
def create():
    product_data = request.get_json()
    try:
        created_product = create_product(product_data)
        return jsonify(created_product), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/products/<product_id>', methods=['PATCH'])
def update(product_id):
    try:
        updated_product = update_product(product_id, request.get_json())
        return jsonify(updated_product), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404 if 'not found' in str(e).lower() else 400
