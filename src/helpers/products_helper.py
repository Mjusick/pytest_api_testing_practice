from apitesting.src.utilities.requests_utility import RequestUtility


class ProductsHelper:

    def __init__(self):
        self.requests_util = RequestUtility()

    def get_all_products(self, payload=None):
        response = self.requests_util.get("products", payload=payload, expected_status_code=200)
        return response.json()

    def get_product_by_id(self, product_id):
        response = self.requests_util.get(f"products/{product_id}", expected_status_code=200)
        return response.json()

    def create_product(self, payload):
        response = self.requests_util.post("products", payload=payload, expected_status_code=201)
        return response.json()
