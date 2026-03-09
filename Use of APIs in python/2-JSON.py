# 3. JSON - “Data ka lunch box”

# JSON = dictionary jaisa format.
'''
JSON (JavaScript Object Notation) ek lightweight 
data-interchange format hai jo human-readable aur 
machine-readable dono hota hai. JSON ka use APIs me data 
exchange ke liye hota hai. JSON me data key-value pairs ke 
form me hota hai, jise Python me dictionary ke roop me 
represent kiya ja sakta hai. JSON me data ko easily parse aur 
generate kiya ja sakta hai, isliye APIs me JSON ka use bahut 
common hai. Jab hum API se data receive karte hain, to wo JSON 
format me hota hai.
'''
# Example of JSON data
from urllib import response


json_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# In Python:
response.json()  # This will convert JSON response to a Python dictionary
# Example of converting Python dictionary to JSON string
import json
python_dict = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}
json_string = json.dumps(python_dict)  # This will convert Python dictionary to JSON string
print(json_string)
'''
ye dumb() function Python dictionary ko JSON string me convert karta hai.
JSON string ko API me bhejne ke liye use kiya jata hai, jabki
response.json() function JSON response ko Python dictionary me 
convert karta hai, jise hum easily access kar sakte hain.
'''
# Example of converting JSON string to Python dictionary
json_string = '{"name": "Charlie", "age": 35, "city": "Chicago"}'
python_dict = json.loads(json_string)  # This will convert JSON string to Python dictionary
print(python_dict)
'''ye loads() function JSON string ko Python dictionary me 
convert karta hai.
JSON string ko API se receive karne ke baad use Python 
dictionary me convert karna hota hai, taki hum us data ko 
easily access aur manipulate kar sakein.
'''

