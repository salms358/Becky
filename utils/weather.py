import requests

API_KEY = "your_openweather_api_key"  # Replace with your API key

def get_weather(city):
    """
    Fetch the current weather for a given city.
    :param city: City name
    :return: Weather description as a string
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is {weather} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't fetch the weather. Please try again later."
    except Exception as e:
        return f"An error occurred: {e}"
