import requests
import json

# class for weather api homework
# makes api requests and gets desired information
weatherundrgrnd_api_key = 'c847353b2b521fd7'
base_url = 'http://api.wunderground.com/api/{}/'.format(weatherundrgrnd_api_key)




class CurrentConditions:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = ('{}{}q/{}{}'.format(base_url, 'conditions/', self.zipcode, ".json"))

    def __repr__(self):
        return "CurrentConditions for {}".format(self.zipcode)

    def __str__(self):
        return self.__repr__()

    def get_conditions(self):
        results = requests.get(self.url).json()
        curr_conditions = "Location: {}\nTemp: {}F\nWind: {}\nWeather: {}\nPercip: {}\nTime:".format(results["current_observation"]
                    ["display_location"]["full"],
                    results["current_observation"]["temperature_string"],
                    results["current_observation"]["wind_string"],
                    results["current_observation"]["weather"],
                    results["current_observation"]
                    ["precip_1hr_string"],
                    results['current_observation']['local_time_rfc822'])
        return curr_conditions


class TenDayForecast:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = ('{}{}q/{}{}'.format(base_url, 'forecast10day/', self.zipcode, ".json"))

    def __repr__(self):
        return "TenDayForecast({})".format(self.zipcode)

    def __str__(self):
        return self.__repr__()

    def get_10day(self):
        days_list = []
        results = requests.get(self.url).json()
        for r in results["forecast"]["txt_forecast"]["forecastday"]:
            day = (r["title"], r["fcttext"])
            days_list.append(day)
        return days_list


class SunCycle:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = ('{}{}q/{}{}'.format(base_url, 'astronomy/', self.zipcode, ".json"))

    def __repr__(self):
        return "Sun: {}".format(self.zipcode)

    def __str__(self):
        return self.__repr__()

    def get_sunrise(self):
        results = requests.get(self.url).json()
        sunrise = results['moon_phase']['sunrise']
        # beautify
        return "Sunrise: {}:{}".format(sunrise['hour'], sunrise['minute'])

    def get_sunset(self):
        results = requests.get(self.url).json()
        sunset = results['moon_phase']['sunset']
        # beautify
        return "Sunset: {}:{}".format(sunset['hour'], sunset['minute'])


class WeatherAlert:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = ('{}{}q/{}{}'.format(base_url, 'alerts/', self.zipcode, ".json"))

    def __repr__(self):
        return "Alerts near {}".format(self.zipcode)

    def __str__(self):
        return self.__repr__()

    def get_alerts(self):
        results = requests.get(self.url).json()
        alerts = results['alerts']
        if len(alerts) == 0:
            return "There are no alerts in your area"
        else:
            return "{}".format(alerts)


class Hurricanes:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = ('{}{}q/{}{}'.format(base_url, 'currenthurricane/', self.zipcode, ".json"))

    def __repr__(self):
        return "Hurricanes near {}".format(self.zipcode)

    def __str__(self):
        return self.__repr__()

    def get_hurricanes(self):
        results = requests.get(self.url).json()
        beautify = "Name:\t{}\nLat Long:\t{} {}\nCategory:\t{}\nWind:\t{}\n".format(results['currenthurricane'][0]['stormInfo']['stormName_Nice'], results['currenthurricane'][0]['Current']['lat'], results['currenthurricane'][0]['Current']['lon'], results['currenthurricane'][0]['Current']['Category'], results['currenthurricane'][0]['Current']['WindSpeed']['Mph'])
        # return beautify
        return beautify
