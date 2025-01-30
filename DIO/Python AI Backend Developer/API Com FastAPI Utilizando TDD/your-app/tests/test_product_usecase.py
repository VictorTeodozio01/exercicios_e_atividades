import pytest
from app.usecases.product_usecase import create_product, update_product
from app.models.product_model import ProductModel

def test_create_product_success(mocker):
    mocker.patch('app.models.product_model.ProductModel.insert_one')
    product_data = {'name': 'Laptop', 'quantity': 10, 'price': 7500, 'status': 'available'}
    assert create_product(product_data) == product_data

def test_update_product_not_found(mocker):
    mocker.patch('app.models.product_model.ProductModel.find_one', return_value=None)
    with pytest.raises(Exception):
        update_product('12345', {'name': 'New Laptop'})
