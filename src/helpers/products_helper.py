from apitesting.src.utilities.requests_utility import RequestUtility


class ProductsHelper:

    def __init__(self):
        self.requests_util = RequestUtility()

    def get_all_products(self):
        response = self.requests_util.get("products")
        return response.json()
