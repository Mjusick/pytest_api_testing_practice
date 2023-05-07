import pytest

from apitesting.src.utilities.requests_utility import RequestUtility


@pytest.mark.tcid30
def test_get_all_customers():
    request_utility = RequestUtility()
    param = {"per_page": 100}
    response = request_utility.get("customers", payload=param)
    assert response.text
