# 1. HTTP PROTOCOL - “Rules of talking”
'''
HTTP (HyperText Transfer Protocol) is a protocol used for 
communication between clients and servers on the web. It 
defines how messages are formatted and transmitted, and how web 
servers and browsers should respond to various commands. HTTP 
is a stateless protocol, meaning that each request from a 
client to a server is treated as an independent transaction. 
The server does not retain any information about previous 
requests. HTTP operates on a request-response model, where the 
client sends a request to the server, and the server processes 
the request and sends back a response. The request and response 
messages consist of headers and a body. The headers contain 
metadata about the request or response, while the body contains 
the actual data being transmitted.

HTTP = internet ki language.

Jaise school me baat karne ke rules hote:

.haath uthao

.permission lo

.answer do

Waise hi computer baat karte HTTP se.

HTTP Request kya hota hai?

Request = tumhara order.

Isme 4 cheeze hoti:

1. URL → “kis shop pe jana hai” / address of shop
URL: https://api.weather.com/city

2. Method → “kya order karna hai”
GET → data mangna hai
POST → data bhejna hai
PUT → data update karna hai
DELETE → data delete karna hai
e.g;
GET https://api.weather.com/city
POST https://api.weather.com/city
PUT https://api.weather.com/city/123
DELETE https://api.weather.com/city/123

3. Headers → “kya cheeze chahiye”
Content-Type: application/json
Authorization: Bearer token
Jaise:
“Spicy mat banana”
“Token check karo”
code example:
headers = {"Authorization": "Bearer TOKEN"}
example:
import requests
url = "https://api.weather.com/city"
headers = {"Authorization": "Bearer TOKEN"}
response = requests.get(url, headers=headers)


4. Body → “kya data bhejna hai”
data = {
    "name": "John",
    "age": 30
}
example:
import requests
url = "https://api.weather.com/city"
data = {
    "name": "John",
    "age": 30
}
response = requests.post(url, json=data)

'''

# 2. HTTP RESPONSE - “Waiter ka answer”
'''
HTTP Response = waiter ka answer.
HTTP response me 3 cheeze hoti:

1. Status Code → “waiter ka mood”
200 → sab theek hai
404 → cheeze nahi mil rahi
500 → restaurant me problem hai

2. Headers → “waiter ki baatein”
Content-Type: application/json
Server: Apache

3. Body → “waiter ka jawab”
{
    "message": "Order received",
    "order_id": 12345
}
'''
# example:
import requests
url = "https://api.weather.com/city"
response = requests.get(url)
print(response.status_code)  # Output: 200
print(response.headers)      # Output: {'Content-Type': 'application/json', 'Server':