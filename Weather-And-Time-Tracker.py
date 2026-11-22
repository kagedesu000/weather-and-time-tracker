from datetime import datetime
from zoneinfo import ZoneInfo
import requests

# Simple lookup for Open-Meteo WMO weather codes
WEATHER_CODES = {
    0: "Sunny / Clear",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Cloudy",
    61: "Rainy",
    71: "Snowy",
    95: "Stormy",
}

def get_weather(city: str):
    
    # Convert city name to coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_response = requests.get(geo_url, params = {"name": city, "count": 1}, timeout = 10)
    geo_response.raise_for_status()  # Raises an error if the request failed
    geo_data = geo_response.json()

    # Error detection
    if "results" not in geo_data:
        print(f"Could not find '{city}'. Please check for typos.")
        return

    # Finds longitude and latitude of the chosen city
    location = geo_data["results"][0]
    lat, lon = location["latitude"], location["longitude"]

    # Fetch current weather & timezone
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "weather_code"],
        "timezone": "auto",
    }

    # Weather data retrieval
    weather_response = requests.get(weather_url, params = weather_params, timeout = 10)
    weather_response.raise_for_status()
    weather_data = weather_response.json()

    # Extract the fields you want
    current = weather_data["current"]
    temp = current["temperature_2m"]
    code = current["weather_code"]
    condition = WEATHER_CODES.get(code, f"Other (Code {code})")

    # Calculate the city's current local time
    city_time = datetime.now(ZoneInfo(weather_data["timezone"])).strftime("%H:%M")

    # Display city data
    print(f"City: {location['name']}, {location.get('country', '')}")
    print(f"Local Time: {city_time}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {condition}")

    return temp, code

def get_vibe_message(temp: float, weather_code: int) -> str:
    # Check severe/wet weather first
    if weather_code in (95, 96, 99):
        return "\nThunderstorm warning! Stay indoors and chill!"
    if weather_code in (61, 63, 65, 80, 81, 82):
        return "\nRainy out there... Grab a waterproof jacket."
    if weather_code in (71, 73, 75, 85, 86):
        return "\nSnow day! Layer up properly."

    # Otherwise base the message on temperature (°C)
    if temp < 5:
        return "\nFreezing! Heavy coat and warm layers needed."
    elif temp < 14:
        return "\nChilly! Hoodie or long-sleeve weather."
    elif temp < 22:
        return "\nMild and comfy! Perfect streetwear weather."
    else:
        return "\nWarm out... Keep it light and stay hydrated!"


# Main loop
run = True
quit_loop = ""

# Creates a line in the console for aesthetic purposes
print("-------------------\n")

while run == True:

    # Asks for city name in order to search the API and retrieve results
    selected_city = input("Enter city name here please: ")
    result = get_weather(selected_city)

    if result is not None:
        temp, weather_code = result
        print(get_vibe_message(temp, weather_code))

    # Checks if the loop should be closed or not
    quit_loop = input("\nEnter [Q] if to end the program. Else enter any other key and continue: ")
    if quit_loop.lower() in ("quit", "q"):
        run = False
    else:
        run = True

    # Creates a line to separate previous requests in the console
    print("\n--------------------\n")