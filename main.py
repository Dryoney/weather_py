import requests
from datetime import datetime, timedelta

print("В каком городе вы хотите узнать температуру: ")
user_input = input ()
city=str(user_input)

appid = 'ffc82bea7fa6bc2bb4d0ec70cf02f7a5'
today_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric'

tomorrow_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={appid}&units=metric"

response1 = requests.get(today_url)
data1 = response1.json()
today_temp = data1['main']['temp']
today_description = data1['weather'][0]['description']
print(f'Погода на сегодня в городе {city}: {today_temp}°C, {today_description}.')

response2 = requests.get(tomorrow_url)
data2 = response2.json()
tomorrow_timestamp = int((datetime.now() + timedelta(days=1)).timestamp())
for forecast in data2['list']:
        if forecast['dt'] >= tomorrow_timestamp and forecast['dt'] < tomorrow_timestamp + 86400:
            tomorrow_temp = forecast['main']['temp']
            tomorrow_description = forecast['weather'][0]['description']
print(f'Погода на завтра в городе {city}: {tomorrow_temp}°C, {tomorrow_description}.')