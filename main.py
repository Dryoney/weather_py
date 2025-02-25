import os
import requests

from datetime import datetime,timedelta
from dotenv import load_dotenv



def user_input():
    print("В каком городе вы хотите узнать температуру: ")
    user_input = input()
    city=str(user_input)
    if not city.isalpha():
        print ('Неверное название города')
    return city

def params_indef(city):
    load_dotenv()
    key = os.getenv("appkey")
    url_params = {
        'appid' : key,
        'q' : city,
        'units' : 'metric'
    }
    return url_params

def now_weather(url_params):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    try:
        response = requests.get(url,params = url_params)
    except requests.ConnectionError:
        print ('<сетевая ошибка>')
    data = response.json()
    today_temp = data['main']['temp']
    today_description = data['weather'][0]['description']
    print(f'Погода на сегодня в городе {url_params['q']}: {today_temp}°C, {today_description}.')

def tomorrow_weahter(url_params):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    try:
        responseTomorrow = requests.get(url,params = url_params)
    except requests.ConnectionError:
        print ('<сетевая ошибка>')
    dataTomorrow = responseTomorrow.json()
    tomorrow_timestamp = int((datetime.now() + timedelta(days=1)).timestamp())
    for forecast in dataTomorrow['list']:
            if forecast['dt'] >= tomorrow_timestamp and forecast['dt'] < tomorrow_timestamp + 86400:
                tomorrow_temp = forecast['main']['temp']
                tomorrow_description = forecast['weather'][0]['description']
                break
    print(f'Погода на завтра в городе {url_params['q']}: {tomorrow_temp}°C, {tomorrow_description}.')
def main():
    city = user_input()
    params = params_indef(city)
    now_weather(params)
    tomorrow_weahter(params)
main()