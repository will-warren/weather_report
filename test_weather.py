# import unittests
from weather import Weather, CurrentCondition
import json
import requests


def show_weather():
    w = Weather(27573)
    return w.get_request(27573, 'conditions/')


def show_current_conditions():
    return CurrentCondition.show_current_conditions(27573, 'conditions/')
