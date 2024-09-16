import requests as req
import logging
from typing import Union


logger = logging.getLogger(__name__)

class BaseAPICalls:

    def __init__(self):
        logger.debug("instantiating BaseAPICalls class")

    def get_request(self, url: str, data: list[tuple, ...]) -> Union[list | None]:
        headers = {
            'cache-control': 'no-store',
            'pragma': 'no-cache'
        }
        try:
            logger.debug(f'sending get request with endpoint, {url}')
            response = req.get(url=url, params=data, headers=headers)
            if response.ok:
                logger.debug(f'status code, {response.status_code} returned from {url}')
                print(f'status code, {response.status_code} returned from {url}')
                return response
            logger.debug(f'status code, {response.status_code} returned from {url}')
            print(f'status code, {response.status_code} returned from {url}')
            return None
        except Exception as e:
            logger.debug(f'exception, {e} with endpoint, {url}')
            print(f'exception, {e} with endpoint, {url}')
            return None
