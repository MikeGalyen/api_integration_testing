import logging
from typing import Union
from api_calls.base_api_calls import BaseAPICalls
from api_calls.constants import BASE_CITY_STATE_URL
from helpers.helper_functions import assemble_city_state_country_query_param, split_city_state


logger = logging.getLogger(__name__)

class CityStateAPI:

    def __init__(self):
        logger.debug("instantiating API class")
        self.base = BaseAPICalls()

    def send_get_request_city_state(self, city_state: str, api_key: str) -> Union[list | None]:
        separated_city_state_list = split_city_state(city_state)
        params = assemble_city_state_country_query_param(separated_city_state_list[0],
                                                         separated_city_state_list[1])
        logger.debug(f'passing city and state data, {separated_city_state_list} and api key to base class get request')
        response = self.base.get_request(BASE_CITY_STATE_URL,
                                         [('q', params),
                                          ('appid', api_key)]
                                         )
        logger.debug(f'send_get_request_city_state got response code, {response}')
        if response is not None:
            logger.debug(f'send_get_request_city_state returning, {response.text}')
            return response.json()
        else:
            logger.debug(f'send_get_request_city_state returning, None')
            return None
