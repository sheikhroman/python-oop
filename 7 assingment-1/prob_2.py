import requests, json, time

def weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather?lat=24.36&lon=88.62&appid=b8958b649044dea5e3d14279ed9fc246&units=metric"

    res = requests.get(url)
    string_r = res.content.decode('UTF-8')
    dict_r = json.loads(string_r)
    # print(dict_r)
    while(True): 
        print(f"Your Location: {dict_r['name']}")
        print(f"Your Country: {dict_r['sys']['country']}")
        print(f'Current Temperature: {dict_r["main"]["temp"]}°C')
        print(f'Feels Like: {dict_r["main"]["feels_like"]}°C')
        print(f'Minimum Temperature: {dict_r["main"]["temp_min"]}°C')
        print(f'Maximum Temperature: {dict_r["main"]["temp_max"]}°C')
        print(f'Humidity: {dict_r["main"]["humidity"]}')
        print(f'Sea Level: {dict_r["main"]["sea_level"]}')
        time.sleep(1800)

weather_data()
