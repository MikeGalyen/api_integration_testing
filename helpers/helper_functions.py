import logging
import re
from typing import Union
from os import getenv


logger = logging.getLogger(__name__)

def get_api_key() -> Union[str | None]:
    logger.debug("Getting api key from local env")
    # doesn't need to have try/except if you don't replace with an env var grab
    try:
        # replace this with a call to get an env var
        return getenv("FETCH_API_KEY")
        logger.debug("api key retrieved")
    except Exception as e:
        logger.debug(f'an exception occurred trying to retrieve the api key environment variable: {e}')
        exit(-1)

def zipcode_validator(zipcode: str) -> Union[str | None]:
    zipcode_pattern = r'[0-9]{5}'
    if re.match(zipcode_pattern, zipcode):
        logger.debug(f"validated zipcode provided by user as, {zipcode}")
        return zipcode
    else:
        logger.debug('user didn\'t provide a valid zipcode')
        return None

def city_state_validator(city_state: str) -> Union[str | None]:
    city_state_pattern = r"[a-zA-Z ]{1,45}, {1}[a-zA-Z]{2}"
    if re.match(city_state_pattern, city_state):
        logger.debug(f"validated city, state provided by user as, {city_state}")
        return city_state
    else:
        logger.debug('user didn\'t provide a valid city and state')
        return None

def split_city_state(city_state: str) -> list:
    try:
        logger.debug(f'splitting city and state data, {city_state} on ", "')
        return city_state.split(', ')
    except Exception as e:
        logger.debug(f'there was an error splitting city and state data, {city_state} on ", "')

def assemble_city_state_country_query_param(city, state):
    city_state_country = (city, state, 'US')
    logger.debug(f'joining city, state, and country data with format, {city}, {state}, US')
    return ','.join(city_state_country)

def assemble_zipcode_query_param(zipcode):
    zipcode_and_country = (zipcode, 'US')
    logger.debug(f'joining zipcode and country data with format, {zipcode}, US')
    return ','.join(zipcode_and_country)

def format_print_location_data(data: list) -> None:
    logger.debug(f'formatting and printing location data received from external api')
    for item in data:
        if type(item) is dict:
            logger.debug(f'response data type is dict')
            if 'name' in item.keys():
                logger.debug(f'key, name, was found in external api response, printing {item["name"]}')
                print(item['name'])
            if 'zip' in item.keys():
                logger.debug(f'key, zip, was found in external api response, printing {item["zip"]}')
                print(' - Zip', item['zip'])
            if 'lat' in item.keys():
                logger.debug(f'key, lat, was found in external api response, printing {item["lat"]}')
                print(' - Latitude', item['lat'])
            if 'lon' in item.keys():
                logger.debug(f'key, lon, was found in external api response, printing {item["lon"]}')
                print(' - Longitude', item['lon'])
            # if 'state' in item.keys():
            #     print(' - State', item['state'])
        if type(item) is list:
            logger.debug(f'response data type is list')
            if 'name' in item[0].keys():
                logger.debug(f'key, name, was found in external api response, printing {item[0]["name"]}')
                print(item[0]['name'])
            if 'zip' in item[0].keys():
                logger.debug(f'key, zip, was found in external api response, printing {item[0]["zip"]}')
                print(' - Zip', item[0]['zip'])
            if 'lat' in item[0].keys():
                logger.debug(f'key, lat, was found in external api response, printing {item[0]["lat"]}')
                print(' - Latitude', item[0]['lat'])
            if 'lon' in item[0].keys():
                logger.debug(f'key, lon, was found in external api response, printing {item[0]["lon"]}')
                print(' - Longitude', item[0]['lon'])

