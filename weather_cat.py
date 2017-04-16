# import unittests
from weather import *
import json
import requests


def show_cc(zipcode):
    cc = CurrentConditions(zipcode)
    return cc.get_conditions()


def show_10day(zipcode):
    tenday = TenDayForecast(zipcode)
    return tenday.get_10day()


def show_sun(zipcode):
    sun= SunCycle(zipcode)
    return sun.get_sunrise(), sun.get_sunset()


def get_alerts(zipcode):
    alerts = WeatherAlert(zipcode)
    return alerts.get_alerts()


def get_hurricanes(zipcode):
    hurricanes = Hurricanes(zipcode)
    return hurricanes.get_hurricanes()
