import logging
import pytest
# import requests-mock
import requests
from api_calls.constants import BASE_ZIPCODE_URL
from api_calls.constants import BASE_CITY_STATE_URL


logger = logging.getLogger(__name__)

# @requests_mock.Mocker()
class IntegrationTest:

    def correctly_formatted_zipcode_test(self):
        # m.register_uri('GET', BASE_ZIPCODE_URL, text='resp')
        # r = requests.get(BASE_ZIPCODE_URL).text
        # assert r == 'resp'
        assert True

