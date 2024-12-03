import requests

# API Details
API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "e280f762068bef6bfba6ab1cae010129"  # Replace with your valid OpenWeatherMap API key

def get_weather_data(location, units="metric"):
    """
    Fetch weather data for a given location.

    Args:
        location (str): City name or location.
        units (str): Unit of measurement ('metric' for Celsius, 'imperial' for Fahrenheit).

    Returns:
        dict: Parsed weather data or None if there's an error.
    """
    try:
        params = {
            "q": location,
            "appid": API_KEY,
            "units": units,
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
