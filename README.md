#This is currently under development - Please check back for updates

## I designed the api calls to work with the openweathermap.org apis

##How to use this repo:

##1 - Clone this repo and cd to the root directory
```bash
cd api_integration_testing
```
##2 - Set up a python virtual environment
```bash
python3 -m venv env_name
```
##3 - Install the dependncies
```bash
pip3 install -r requirements.txt
```
##4 - Sign up for an account at OpenWeatherAPI to get an an api key: https://home.openweathermap.org/users/sign_up
##5 - Set up an Environment variable with the api key
```bash
export VARNAME="api key"
```
##6 - Run the program
```bash
python3.12 main.py --location 90210
```
###or
```bash
python3.12 main.py --location "New York, NY"
```
###or
```bash
python3.12 main.py --location 90210 "New York, NY"
```
##7 - Test the program
```bash
pytest tests/integration_test.py
```
