import requests

# class for weather api homework
# makes api requests and gets desired information
weatherundrgrnd_api_key = 'c847353b2b521fd7'


base_url = 'http://api.wunderground.com/api/{}/'.format(weatherundrgrnd_api_key)

features = ['conditions/', 'forecast10day/', 'astronomy/', 'alerts/', 'currenthurricane/']


class Weather:
    def __init__(self, zipcode):
        self.zipcode = zipcode

    def __repr__(self):
        return "Weather({})".format(self.zipcode)

    def __str__(self):
        return self.__repr__()

    def get_request(self, zipcode, feature):
        all_results = []
        for feature in features:
            get = requests.get('{}{}q/{}{}'.format(base_url, feature, zipcode, ".json"))
            all_results.append(get.json())

        return all_results

    # self.url.format(self.zipcode)


class CurrentCondition(Weather):
    def show_current_conditions(self, feature):
        return Weather.get_request(27573, feature)


class TenDayForecast(Weather):
    pass


class SunCycle(Weather):
    pass


class WeatherAlert(Weather):
    pass


class ActiveHurricane(Weather):
    pass
