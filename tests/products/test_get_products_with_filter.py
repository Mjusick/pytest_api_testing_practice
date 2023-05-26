from datetime import datetime,timedelta

import pytest

from apitesting.src.helpers.products_helper import ProductsHelper


@pytest.mark.regression
class TestListProductsWithFilter:

    def test_list_products_with_filter_after(self):

        x_days_before_today = 30
        after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_before_today)
        after_created_date_format = after_created_date.isoformat()
        payload = dict()
        payload["after"] = after_created_date

        response = ProductsHelper().get_all_products(payload=payload)

        assert response, "Empty response for 'list products with filter'"

