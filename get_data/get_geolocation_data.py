import logging
from api_calls.city_state_api import CityStateAPI
from api_calls.zipcode_api import ZipcodeAPI
from helpers.helper_functions import zipcode_validator, city_state_validator, format_print_location_data, get_api_key


logger = logging.getLogger(__name__)

class GetGeolocationData:

    def __init__(self):
        logger.debug("instantiating GetGeolocationData class")
        self.city_state_api = CityStateAPI()
        self.zipcode_api = ZipcodeAPI()
        self.location_data_accumulator = []
        self.api_key = get_api_key()

    def get_data(self, zipcode_or_city_state: list) -> None:
        for location in zipcode_or_city_state:
            if zipcode_validator(location):
                logger.debug(f'calling send_get_request_zipcode with {location}')
                response = self.zipcode_api.send_get_request_zipcode(location, self.api_key)
                self.location_data_accumulator.append(response)
            elif city_state_validator(location):
                logger.debug(f'calling send_get_request_city_state with {location}')
                response = self.city_state_api.send_get_request_city_state(location, self.api_key)
                self.location_data_accumulator.append(response)
            else:
                logger.debug('argument did not follow an expected input pattern')
                print('argument did not follow an expected input pattern')

    def display_data(self):
        format_print_location_data(self.location_data_accumulator)


