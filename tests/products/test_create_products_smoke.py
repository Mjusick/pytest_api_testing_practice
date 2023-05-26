import pytest

from apitesting.src.dao.products_dao import ProductsDAO
from apitesting.src.helpers.products_helper import ProductsHelper
from apitesting.src.utilities.generic_utilities import generate_random_string

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.matk.tcid26
def test_create_one_product():

    # create product data
    payload = dict()
    product_name = generate_random_string()
    payload["name"] = product_name
    payload["type"] = "simple"
    payload["regular_price"] = "10.99"

    # make a call to API to create product
    products_helper = ProductsHelper()
    response = products_helper.create_product(payload=payload)

    # verify response is not empty
    assert response, f"Create product response is empty. Payload {payload}"
    assert response["name"] == product_name, f"Response has unexpected name of the product. Should be {product_name}, but was {response['name']}"

    # verify product is in db
    products_dao = ProductsDAO()
    assert products_dao.get_product_from_db_by_name(product_name), f"Product hasn't been created in database. Product name: {product_name}"