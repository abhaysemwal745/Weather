import requests

API_KEY = "03ab0ee801c24615baf60947260102"

city = input("Enter city name: ").strip()   #.strip() removes extra spaces===========
country = input("Enter country name: ").strip()

url = "https://api.weatherapi.com/v1/current.json"

params = {              #Hey requests, take this dictionary and attach it to the URL properly.
    "key": API_KEY,
    "q": f"{city}, {country}"
}

res = requests.get(url, params=params, timeout=10).json()
'''
requests.get(...) → send GET request to server
url → where
params → what data
timeout=10 → wait max 10 seconds, then give up
json() → convert API response into Python dictionary
'''

if "error" in res:
    print("Error:", res["error"]["message"])
else:
    location = res["location"]
    current = res["current"]
    condition = current["condition"]

    print("\n========== LOCATION ==========")
    print(f"City: {location['name']}")
    print(f"Region: {location['region']}")
    print(f"Country: {location['country']}")
    print(f"Latitude: {location['lat']}, Longitude: {location['lon']}")
    print(f"Timezone: {location['tz_id']}")
    print(f"Local Time: {location['localtime']}")

    print("\n========== WEATHER ==========")
    print(f"Condition: {condition['text']}")
    print(f"Temperature: {current['temp_c']} °C")
    print(f"Feels Like: {current['feelslike_c']} °C")
    print(f"Is Day: {'Yes' if current['is_day'] else 'No'}")

    print("\n========== WIND ==========")
    print(f"Wind Speed: {current['wind_kph']} kph")
    print(f"Wind Direction: {current['wind_dir']} ({current['wind_degree']}°)")
    print(f"Gust Speed: {current['gust_kph']} kph")

    print("\n========== ATMOSPHERE ==========")
    print(f"Humidity: {current['humidity']}%")
    print(f"Pressure: {current['pressure_mb']} mb")
    print(f"Visibility: {current['vis_km']} km")
    print(f"Cloud Cover: {current['cloud']}%")

    print("\n========== RAIN & UV ==========")
    print(f"Precipitation: {current['precip_mm']} mm")
    print(f"Dew Point: {current['dewpoint_c']} °C")
    print(f"UV Index: {current['uv']}")
