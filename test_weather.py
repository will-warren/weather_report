# import unittests
from weather import Weather
import json
import requests

zipcode = 27573

weatherundrgrnd_api_key = 'c847353b2b521fd7'


base_url = 'http://api.wunderground.com/api/{}/'.format(weatherundrgrnd_api_key)

features = ['conditions/', 'forecast10day/', 'astronomy/', 'alerts/', 'currenthurricane/']

get = requests.get('{}{}q/{}{}'.format(base_url, features[0], zipcode, ".json"))

print('{}{}{}{}'.format(base_url, features[0], zipcode, ".json"))
print(get.json())

# json prints to screen, go back and make it useful for project demands
