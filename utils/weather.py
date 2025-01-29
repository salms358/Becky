import requests
import os

# Ensure your API key is properly set
API_KEY = os.environ.get("WEATHER_KEY")

def get_weather(city):
    """
    Fetch the current weather for a given city using OpenWeather API.
    """
    if not API_KEY:
        return "API key not found. Please set it in env.py or .env."

    try:
        city = city.replace(" ", "+")  # Normalize city names with spaces
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city.replace('+', ' ')} is {weather} with a temperature of {temperature}°C."
        elif response.status_code == 404:
            return "I couldn't find that city. Did you type it correctly?"
        else:
            return "Sorry, I couldn't fetch the weather. Please try again later."
    except Exception as e:
        return f"An error occurred: {e}"

