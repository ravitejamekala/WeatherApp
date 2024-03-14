import requests
import json
if __name__ == '__main__':

    api = "ae605cae1d3e4b2eba9171522241303"
    city = input("Enter your city name:  ")
    weather_info = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}")
    json_data = json.loads(weather_info.text)
    print("Temperature", json_data['current']['temp_c'])
    print("Wind (km/hr)", json_data['current']['wind_kph'])
    print("Humidity", json_data['current']['humidity'])

