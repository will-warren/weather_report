import requests

# class for weather api homework
# makes api requests and gets desired information
weatherundrgrnd_api_key = 'c847353b2b521fd7'


base_url = 'http://api.wunderground.com/api/{}/'.format(weatherundrgrnd_api_key)

features = ['conditions/', 'forecast10day/', 'astronomy/', 'alerts/', 'currenthurricane/']


class Weather:
    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get_request(self):
        feature = features[0]
        return requests.get('{}{}{}{}'.format(base_url, feature, self.zipcode, ".json"))

    # self.url.format(self.zipcode)


class CurrentCondition(Weather):
    pass


class TenDayForecast(Weather):
    pass


class SunCycle(Weather):
    pass


class WeatherAlert(Weather):
    pass


class ActiveHurricane(Weather):
    pass
