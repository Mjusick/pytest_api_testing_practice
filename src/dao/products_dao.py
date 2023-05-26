import random

from apitesting.src.utilities.db_utility import DBUtility


class ProductsDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_products_from_db(self, quantity: int = 1):
        sql_query = "SELECT * FROM shopsiteschema.wp_posts WHERE post_type='product' LIMIT 5000;"
        db_response = self.db_helper.execute_select_query(sql_query)
        return random.sample(db_response, quantity)

    def get_product_from_db_by_name(self, product_name):
        sql_query = f"SELECT * FROM shopsiteschema.wp_posts WHERE post_title='{product_name}' LIMIT 5000;"
        db_response = self.db_helper.execute_select_query(sql_query)
        return db_response

