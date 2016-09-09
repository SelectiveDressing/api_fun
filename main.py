from sys import argv, exit
import requests

def main():
	try: 
        print(argv)
        api_key = argv[1]
    except IndexError:
        print("Please give correct API key")
        exit()

    payload = {"appid": api_key,
                "q": location,
                "units": "imperial",}

    r = requests.get(" ",params = payload)

    weather = r.json()
    print("Current Temp: {}".format(weather["main"]["temp"]))


if __name__ == '__main__':
	main()