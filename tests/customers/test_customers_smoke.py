from pytest import mark
import logging as logger

from apitesting.src.helpers.customers_helper import CustomerHelper
from apitesting.src.utilities.generic_utilities import generate_random_email_and_password


@mark.tcid29
def test_create_customer_only_email_password():
    logger.info("This is a log.....")
    rand_info = generate_random_email_and_password()
    email = rand_info["email"]
    password = rand_info["password"]

    customer_helper = CustomerHelper()
    customer = customer_helper.create_customer(email, password)

    assert customer["email"] == email, f"Create customer returned wrong email. Should be {email}, but was {customer['email']}"
    assert customer["first_name"] == "", f"First name should be an empty string, but returned {customer['first_name']}"
