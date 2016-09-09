from sys import argv, exit
from os import sys
import requests
from forecast import Forecast
user_forecast = Forecast()
def main():
    try:
        print(argv)
        api_key = argv[1]
    except IndexError:
        print("Please give correct API key")
        exit()

    print("\nWhat city, country?")
    print("\nUse the format: city, country")
    location = input("city, country: > ")
    
    print("0: exit")
    print("1: Daily Weather")
    print("2: 5-day Forecast")
    print("3: 10-day Forecast")

    choice = input("\n: > ")

    payload = {"appid": api_key,
                "q": location, #city, country
                "units": "imperial",}

    if choice == "1":
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?", params = payload)
        weather = r.json()
        user_forecast.daily_weather(weather)
#5-day
    elif choice == "2":
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast?", params = payload)
        weather = r.json()
        user_forecast.five_day_weather(weather)
        
#        for times in weather.items():
#            if "weather" in times:
#                print("\nCurrent Temp: {}".format(times))

#10 day
    elif choice == "3":
        payload["cnt"] = 10
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?", params = payload)   
        weather = r.json()
        user_forecast.ten_day_weather(weather)



        # emptyList = []
        # for item in weather.keys():
        #     if item == "list":
        #         emptyList.append(weather["list"])
        # #print(emptyList)
        # raw_temp = []
        # raw_humidity = []
        # raw_pressure = []
        # raw_weather = []
        # for x_list in emptyList:
        #      for dict_item in x_list:
        #         if "temp" in dict_item:
        #             raw_temp.append(dict_item["temp"])
        #             #print(raw_temp)

        #         if "humidity" in dict_item:
        #             raw_humidity.append(dict_item["humidity"])
        #             #print(raw_humidity)

        #         if "pressure" in dict_item:
        #             raw_pressure.append(dict_item["pressure"])
        #             #print(raw_pressure)

        #         if "weather" in dict_item:
        #             raw_weather.append(dict_item["weather"])
        #             #print(raw_weather)
        # print(raw_temp)
        # print("*"*10)
        # print(raw_humidity)
        # print("*"*10)
        # print(raw_pressure)
        # print("*"*10)
        # print(raw_weather)
    else:
        sys.exit()


if __name__ == '__main__':
    main()