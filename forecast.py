class Forecast():
    def daily_weather(self,weather):
        raw_main = []
        raw_wind = []
        for item in weather.keys():
            if "main" in item:
                raw_main.append(weather["main"])
            if "wind" in item:
                raw_wind.append(weather["wind"])
        print(raw_main)
        print("*"*10)
        print(raw_wind)

    def five_day_weather(self,weather):
        pass
    def ten_day_weather(self,weather):
        emptyList = []
        for item in weather.keys():
            if item == "list":
                emptyList.append(weather["list"])
        #print(emptyList)
        raw_temp = []
        raw_humidity = []
        raw_pressure = []
        raw_weather = []
        for x_list in emptyList:
             for dict_item in x_list:
                if "temp" in dict_item:
                    raw_temp.append(dict_item["temp"])
                    #print(raw_temp)

                if "humidity" in dict_item:
                    raw_humidity.append(dict_item["humidity"])
                    #print(raw_humidity)

                if "pressure" in dict_item:
                    raw_pressure.append(dict_item["pressure"])
                    #print(raw_pressure)

                if "weather" in dict_item:
                    raw_weather.append(dict_item["weather"])
                    #print(raw_weather)
        print(raw_temp)
        print("*"*10)
        print(raw_humidity)
        print("*"*10)
        print(raw_pressure)
        print("*"*10)
        print(raw_weather)