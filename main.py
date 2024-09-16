import argparse
import logging
from datetime import datetime
from get_data.get_geolocation_data import GetGeolocationData


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt="%a, %d %b %y %H:%M:%S",
                    filename=f"logs/{datetime.now()}.log",
                    filemode="w")

class Main:

    def __init__(self):
        get_geo_location = GetGeolocationData()
        get_geo_location.get_data(args.location)
        get_geo_location.display_data()


if __name__ == "__main__":
    logger.debug(f"running main")

    # get_geo_location = GetGeolocationData()

    logger.debug('creating parser for command line args')
    parser = argparse.ArgumentParser(description='Make api calls to https://openweathermap.org/api/geocoding-api'
                                                 'to get geolocation data based on a zip code of city, state'
                                                 'combo like, -z 90210 or -c "Beverley Hills, CA"')

    logger.debug('creating --location flag from command line args')
    parser.add_argument('--location',
                        type=str,
                        nargs='+',
                        help='enter 5 digit US zipcode like "90210" or city, state like, '
                             '"Beverley Hills, CA" or a combination of the two'
                        )

    logger.debug('getting command line args')
    args = parser.parse_args()

    logger.debug('passing args to get_geo_location.get_data')

    Main()
