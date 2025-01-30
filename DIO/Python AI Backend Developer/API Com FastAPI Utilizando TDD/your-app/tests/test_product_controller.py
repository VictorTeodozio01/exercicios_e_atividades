from flask import json
from app.main import app

def test_create_product(client):
    response = client.post('/products', json={'name': 'Laptop', 'quantity': 10, 'price': 7500, 'status': 'available'})
    assert response.status_code == 200
    assert response.json['name'] == 'Laptop'

def test_update_product_not_found(client):
    response = client.patch('/products/12345', json={'name': 'New Laptop'})
    assert response.status_code == 404
    assert response.json == {'error': 'Product not found'}
