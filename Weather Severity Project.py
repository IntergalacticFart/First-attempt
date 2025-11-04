rain_count = 0.0
wind_count = 0.0
days = 0
sentinelValue = True

while sentinelValue:
    myInput = input()
    if myInput[0] == "-" and myInput[1:] == "1.0":
        sentinelValue = False
    else:
        myList = myInput.split()
        rain = float(myList[0])
        wind = float(myList[1])
        rain_count += rain
        wind_count += wind
        days += 1
        print("The rain is:", rain)
        print("The wind is:", wind)

    if days > 0:
        average_rain = rain_count/days
        average_wind = wind_count/days
        weather_severity = (average_rain * 10) + average_wind
        print("The average rain is:", average_rain, "inches")
        print("The average wind is:", average_wind, "mph")
        print("The weather severity for", days, "days is:", weather_severity)
    else:
        print("No data")