from apitesting.src.utilities.generic_utilities import generate_random_email_and_password
from apitesting.src.utilities.requests_utility import RequestUtility


class CustomerHelper:

    def __init__(self):
        self.requests_util = RequestUtility()

    def create_customer(self, email: str = None, password: str = "Password1", **kwargs):
        if not email:
            random_info = generate_random_email_and_password()
            email = random_info["email"]

        payload = dict()
        payload["email"] = email
        payload["password"] = password
        payload.update(**kwargs)

        response = self.requests_util.post("customers", payload=payload)
        return response.json()
