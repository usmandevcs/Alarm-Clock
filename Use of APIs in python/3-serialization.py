# 4. Serialization - “Data ko box me pack karna”
'''
Serialization = Python object → JSON banana
Deserialization = JSON → Python object

Serialization ka matlab hai Python object ko JSON format me 
convert karna, taki usse API me bheja ja sake. Deserialization 
ka matlab hai JSON data ko Python object me convert karna, taki 
usse hum easily access aur manipulate kar sakein. APIs me data 
exchange ke liye serialization aur deserialization bahut 
important hai, kyunki APIs me data JSON format me hota hai, 
aur Python me hum usse dictionary ke roop me use karte hain.
'''
import json

data = {"name": "Ali"}
json_data = json.dumps(data)   # packing
print(json_data)  # Output: {"name": "Ali"}

# unpacking:
json.loads(json_data)

