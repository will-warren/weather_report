# import unittests
from weather import Weather, CurrentCondition
import json
import requests


def show_weather():
    w = Weather(27573)
    return w.get_request(27573, 'conditions/')


def show_current_conditions():
    return CurrentCondition.show_current_conditions(27573, 'conditions/')


print(show_current_conditions())
# zipcode = 27573
#
# weatherundrgrnd_api_key = 'c847353b2b521fd7'
#
#
# base_url = 'http://api.wunderground.com/api/{}/'.format(weatherundrgrnd_api_key)
#
#
# # json prints to screen, go back and make it useful for project demands
# # Weather class should take a location make the requests
#
# def print_results(basic_url, zipcode):
#     features = ['conditions/', 'forecast10day/', 'astronomy/', 'alerts/', 'currenthurricane/']
#
#     url = '{}{}{}{}'.format(base_url, features[0], zipcode, ".json")
#     # print(get.json())
#
#
#     results = {}
#     for f in features:
#         get = requests.get('{}{}q/{}{}'.format(base_url, f, zipcode, ".json"))
#         results[f] = get.json()
#
#     for r, value in results.items():
#         for value, inner_value in value.items():
#             print(value, inner_value)
#
# print_results(base_url, zipcode)
