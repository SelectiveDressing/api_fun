from sys import argv, exit
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
    
    print("\nHow many days do you want a forecast for?")
    print("The default is 'current'.")
    count = int(input("\n: > "))

    payload = {"appid": api_key,
                "q": location, #city, country
                "units": "imperial",
                "cnt": count,}
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?", params = payload)

#print off ...attributes
    weather = r.json()
    print("\nCurrent Temp: {}".format(weather["main"]["temp"]))

#booty

if __name__ == '__main__':
    main()