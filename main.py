from sys import argv, exit
from os import sys
import requests

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
        print(weather)
#5-day
    elif choice == "2":
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast?", params = payload)
        weather = r.json()
        
#        for times in weather.items():
#            if "weather" in times:
#                print("\nCurrent Temp: {}".format(times))

#10 day
    elif choice == "3":
        payload["cnt"] = 10
        r = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?", params = payload)   
        weather = r.json()

        emptyList = []
        for item in weather:
            emptyList.append(filter(lambda x: x["temp"], item))
        print(emptyList)

    else:
        sys.exit()


if __name__ == '__main__':
    main()