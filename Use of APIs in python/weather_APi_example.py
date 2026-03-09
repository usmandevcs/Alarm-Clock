# EXAMPLE - Weather API
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Lahore&appid=KEY"

response = requests.get(url)

data = response.json()

print(data["weather"][0]["description"])

# Output: clear sky
'''
Flow:

. GET request send

. JSON mila

. Python dict me convert

. value print
'''
