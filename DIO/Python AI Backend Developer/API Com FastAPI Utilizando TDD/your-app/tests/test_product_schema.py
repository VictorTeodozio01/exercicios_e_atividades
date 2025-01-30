import pytest
from app.schemas.product_schema import validate_product

def test_validate_product_success():
    valid_input = {'name': 'Laptop', 'quantity': 10, 'price': 7500, 'status': 'available'}
    assert validate_product(valid_input) == valid_input

def test_validate_product_failure():
    invalid_input = {'name': '', 'quantity': -1, 'price': 7500, 'status': 'available'}
    with pytest.raises(ValueError):
        validate_product(invalid_input)