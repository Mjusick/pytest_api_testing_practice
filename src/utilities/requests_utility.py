import json
import os

from requests import post, get
from requests_oauthlib import OAuth1
import logging as logger

from apitesting.src.configs.hosts_config import API_HOSTS
from apitesting.src.utilities.credentials_utility import CredentialsUtility


class RequestUtility:

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds["wc_key"], wc_creds["wc_secret"])

    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        response = post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        assert response.status_code == expected_status_code,\
            f"Expected status code {expected_status_code}, but was {response.status_code}"
        logger.debug(f"API POST response: {response.json()}")
        return response

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        response = get(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        assert response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code}, but was {response.status_code}"
        logger.debug(f"API GET response: {response.json()}")
        return response
