import logging
from typing import Union
from api_calls.base_api_calls import BaseAPICalls
from api_calls.constants import BASE_ZIPCODE_URL
from helpers.helper_functions import assemble_zipcode_query_param


logger = logging.getLogger(__name__)

class ZipcodeAPI:

    def __init__(self):
        logger.debug("instantiating API class")
        self.base = BaseAPICalls()

    def send_get_request_zipcode(self, zipcode: str, api_key: str) -> Union[list | None]:
        params = assemble_zipcode_query_param(zipcode)
        logger.debug(f'passing zipcode data, {zipcode} and api key to base class get request')
        response = self.base.get_request(BASE_ZIPCODE_URL,
                                         [("zip", params),
                                          ("appid", api_key)]
                                         )
        logger.debug(f'send_get_request_zipcode got response code, {response}')
        if response is not None:
            logger.debug(f'send_get_request_zipcode returning, {response.text}')
            return response.json()
        else:
            logger.debug(f'send_get_request_zipcode returning, None')
            return None
