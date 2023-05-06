from apitesting.src.utilities.db_utility import DBUtility


class CustomersDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql_query = f"SELECT * FROM shopsiteschema.wp_users WHERE user_email = '{email}';"
        db_response = self.db_helper.execute_select_query(sql_query)
        return db_response
