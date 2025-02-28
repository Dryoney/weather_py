import os
import requests
import sys

from datetime import datetime,timedelta
from dotenv import load_dotenv


def validate_user_input(city: str):
    if not city.isalpha():
        print ("Неверное название города")
    return city


def url_parametrs(city: str):
    key = os.getenv("appkey")
    url_params = {
        "appid" : key,
        "q" : city,
        "units" : "metric"
    }
    return url_params


def now_weather(url_params: list[str]):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    try:
        response = requests.get(url,params=url_params)
    except requests.ConnectionError:
        print ('<сетевая ошибка>')
        sys.exit(1)
    data = response.json()
    today_temp = data['main']['temp']
    today_description = data['weather'][0]['description']
    print(f'Погода на сегодня в городе {url_params['q']}: {today_temp}°C, {today_description}.')


def tommorow_weather(url_params: list[str]):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    try:
        responce_tomorrow = requests.get(url,params = url_params)
    except requests.ConnectionError:
        print ('<сетевая ошибка>')
        sys.exit(1)
    data_tomorrow = responce_tomorrow.json()
    tomorrow_timestamp = int((datetime.now() + timedelta(days=1)).timestamp())
    for forecast in data_tomorrow['list']:
            if forecast['dt'] >= tomorrow_timestamp and forecast['dt'] < tomorrow_timestamp + 86400:
                tomorrow_temp = forecast['main']['temp']
                tomorrow_description = forecast['weather'][0]['description']
                break
    print(f'Погода на завтра в городе {url_params['q']}: {tomorrow_temp}°C, {tomorrow_description}.')


def main():
    load_dotenv()
    city = str(input('Введите название города: '))
    try:
        validate_user_input(city)
    except InvalidInput:
        print('Неверное название города')
        return
    params = url_parametrs(city)
    now_weather(params)
    tommorow_weather(params)


if __name__ == "__main__":
    main()