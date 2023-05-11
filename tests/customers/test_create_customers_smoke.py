import pytest

from apitesting.src.dao.customers_dao import CustomersDAO
from apitesting.src.helpers.customers_helper import CustomerHelper
from apitesting.src.utilities.generic_utilities import generate_random_email_and_password
from apitesting.src.utilities.requests_utility import RequestUtility


@pytest.mark.customers
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


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    customer_dao = CustomersDAO()
    existing_customer = customer_dao.get_random_customers()
    existing_email = existing_customer[0]["user_email"]
    payload = {"email": existing_email, "password": "Password1"}
    request_util = RequestUtility()
    customer_api_info = request_util.post(endpoint="customers", payload=payload, expected_status_code=400)
    assert customer_api_info.json()["code"] == "registration-error-email-exists", f"Create customer with existing user error 'code' is not correct. Expected 'registration-error-email-exists', Actual: {customer_api_info['code']}"
    assert "Konto z Twoim adresem e-mail jest już zarejestrowane." in customer_api_info.json()["message"]
