# ui file for weather report
# get user's zip and return weather
# later add regex to accept zips and city names
import os
from weather_cat import *

def main():
    # greeting
    os.system("clear")
    print("WEATHER CAT\n")
    print("weather on the meows\n\n")

    #get info and set up choice menu
    zipcode = input("Enter your zipcode: ")
    options = ["View All", 'Current Conditions', "10 Day Forecast", "Sunrise/Sunset", "Weather Alerts", "Active Hurricanes", "Quit"]
    options = zip(range(len(options)), options)

    # load weather according to choice and zip
    while True:
        for opt in options:
            print("{}:\t{}".format(opt[0], opt[1]))
        choice = int(input("Enter Number of Choice: "))
        if choice == 0:
            print(show_cc(zipcode))
            forecast = show_10day(zipcode)
            for fc in forecast:
                print("{}: {}\n".format(fc[0], fc[1]))
            print(show_sun(zipcode))
            print(get_alerts(zipcode))
            print(get_hurricanes(zipcode))
        elif choice == 1:
            print(show_cc(zipcode))
        elif choice == 2:
            forecast = show_10day(zipcode)
            for fc in forecast:
                print("{}: {}\n".format(fc[0], fc[1]))
        elif choice == 3:
            print(show_sun(zipcode))
        elif choice == 4:
            print(get_alerts(zipcode))
        elif choice == 5:
            print(get_hurricanes(zipcode))
        elif choice == 6:
            exit()
        else:
            print("Sorry that wasn't a valid choice, try again")




if __name__ == '__main__':
    main()
