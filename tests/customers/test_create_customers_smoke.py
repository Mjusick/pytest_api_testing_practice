import pytest

from apitesting.src.dao.customers_dao import CustomersDAO
from apitesting.src.helpers.customers_helper import CustomerHelper
from apitesting.src.utilities.generic_utilities import generate_random_email_and_password


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    rand_info = generate_random_email_and_password()
    email = rand_info["email"]
    password = rand_info["password"]
    customer_helper = CustomerHelper()
    customer = customer_helper.create_customer(email, password)
    assert customer[
               "email"] == email, f"Create customer returned wrong email. Should be {email}, but was {customer['email']}"
    assert customer["first_name"] == "", f"First name should be an empty string, but returned {customer['first_name']}"

    customer_dao = CustomersDAO()
    customer_db_info = customer_dao.get_customer_by_email(email)

    customer_id_db = customer_db_info[0]["ID"]
    customer_id_api = customer["id"]
    assert customer_id_api == customer_id_db, f"Create customer ID response is not the same as in DB, where customer email: {email}."
