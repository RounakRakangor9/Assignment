import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = '593e489a8dc8452a4fecdbc948dc5156'
CITY = 'Toronto'
UNITS = 'metric'

url = BASE_URL + '&appid=' + API_KEY + '&q=' + CITY + '&units=' + UNITS

# 1. Print the current temperature of the city Toronto in Celsius
response = requests.get(url)
response_in_json = response.json()
temp_celcius = response_in_json['main']['temp']
print("1. Current temperature of the city Toronto in Celcius is:", int(temp_celcius), "Degree Celcius")

# 2. Print the status 200 from a successful API response.
print("2. Status code from an API response is:", response.status_code)
