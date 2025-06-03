import requests
import json
import os

city = input("Enter the Name of the city:")
url = f"http://api.weatherapi.com/v1/current.json?key=e365061d34454e9b9b9122342251704&q={city}"
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"] ["temp_c"]

os.system(f'say \'The current weather in {city} is {w} degrees\'')