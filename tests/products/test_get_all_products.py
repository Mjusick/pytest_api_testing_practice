import pytest

from apitesting.src.dao.products_dao import ProductsDAO
from apitesting.src.helpers.products_helper import ProductsHelper


pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    products_helper = ProductsHelper()
    response = products_helper.get_all_products()
    assert response, "Get all products endpoint response is empty."


@pytest.mark.tcid25
def test_get_product_by_id():
    products_helper = ProductsHelper()
    random_product = ProductsDAO().get_random_products_from_db(1)
    db_product_name = random_product[0]["post_title"]
    random_product_id = random_product[0]["ID"]

    api_product = products_helper.get_product_by_id(random_product_id)
    api_product_name = api_product["name"]
    assert db_product_name == api_product_name, f"Get product by ID returned wrong product. " \
                                                f"Should be {db_product_name}, was {api_product_name} "
