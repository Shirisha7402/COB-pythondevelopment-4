import tkinter as tk
import requests

API_KEY = '07857869b1159af707ff2f32ce75467f'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data

def update_weather():
    city = city_entry.get()
    weather_data = fetch_weather(city)

    if weather_data['cod'] == 200:
        city_label.config(text=f'City: {city}')
        temperature_label.config(text=f'Temperature: {weather_data["main"]["temp"]}°C')
        description_label.config(text=f'Description: {weather_data["weather"][0]["description"].capitalize()}')
    else:
        city_label.config(text='City not found')
        temperature_label.config(text='')
        description_label.config(text='')
app = tk.Tk()
app.title('Weather App')
city_label = tk.Label(app, text='Enter City:')
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

fetch_button = tk.Button(app, text='Fetch Weather', command=update_weather)
fetch_button.pack()

temperature_label = tk.Label(app, text='')
temperature_label.pack()

description_label = tk.Label(app, text='')
description_label.pack()

app.mainloop()
