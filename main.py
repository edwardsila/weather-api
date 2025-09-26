import os
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Weather API Wrapper")

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("API Key Loaded:", API_KEY)

@app.get("/weather/{city}")
def get_weather(city: str):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")

    data = response.json()
    formatted = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "weather": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return formatted