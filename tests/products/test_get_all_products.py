import pytest

from apitesting.src.helpers.products_helper import ProductsHelper


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    products_helper = ProductsHelper()
    response = products_helper.get_all_products()
    assert response, "Get all products endpoint response is empty."
