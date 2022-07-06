import requests
#method to check the weather of a city - input by user
def check_weather():
    API_KEY = "c4ffa2ebfcd4dc0fe70f5d2f20b7fb42"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    city = input("Enter city: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] - 273.15, 2)
        print("Weather: ", weather)
        print("Temperature: ", temperature, "celsius")
    else:
        print("Error")


check_weather()