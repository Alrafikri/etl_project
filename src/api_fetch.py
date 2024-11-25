import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

# OpenWeatherMap API example
api_key = os.getenv('API_KEY')
city = 'Banyumas'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    weather_df = pd.json_normalize(data)
    weather_df.to_csv('../data/raw/weather_data.csv', index=False)
    print("Succes to fetch and save data")
else:
    print("Failed to fetch data")