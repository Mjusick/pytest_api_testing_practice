import pymysql as pymysql

from apitesting.src.utilities.credentials_utility import CredentialsUtility
import logging as logger


class DBUtility:

    def __init__(self):
        credentials_helper = CredentialsUtility()
        self.host = "localhost"
        self.credentials = credentials_helper.get_db_credentials()

    def create_connection(self):
        connection = pymysql.connect(user=self.credentials["db_user"], password=self.credentials["db_password"],
                                     host=self.host, port=8889)
        return connection

    def execute_select_query(self, query):
        connection = self.create_connection()

        try:
            logger.debug(f"Executing sql query: {query}")
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            response_dict = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f"Failed running sql query: {query}. Error: {e}")
        finally:
            connection.close()

        return response_dict

    def execute_sql(self, sql):
        pass
