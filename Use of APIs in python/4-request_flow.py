# FULL REQUEST FLOW – “Order ka safar”
'''
Jab hum API call karte:

1. DNS → website ka address find:
mtlb jab hum kisi website ka URL type karte hain, toh pehle DNS 
(Domain Name System) server se us website ka IP address find 
kiya jata hai. Ye bilkul waise hi hai jaise hum kisi ka phone 
number dhundte hain apne contact list me.

2. TCP connection → connection banata:
TCP (Transmission Control Protocol) connection establish karna 
hota hai client aur server ke beech. Ye connection ensure karta 
hai ki data packets sahi tarah se transfer ho rahe hain, aur 
agar koi packet lost ho jata hai toh usse dobara bheja jata hai. 


3. TLS → secure lock 🔒:
TLS (Transport Layer Security) ek protocol hai jo internet par 
data ko encrypt karta hai, taki wo secure rahe. Jab hum HTTPS 
website par visit karte hain, toh TLS use hota hai data ko 
encrypt karne ke liye, taki hackers us data ko easily access na 
kar sakein. TLS ek secure lock ki tarah kaam karta hai, jo 
ensure karta hai ki humari information safe rahe jab hum online 
transactions karte hain ya sensitive data share karte hain.

4. HTTP request send:
HTTP (Hypertext Transfer Protocol) request send karna hota hai 
client se server ko. HTTP request me method 
(GET, POST, PUT, DELETE), 
URL (jo resource hum access karna chahte hain), 
headers (jo additional information provide karte hain), 
aur body (jo data bheja jata hai, agar required ho) hota hai. 
Jab hum API call karte hain, toh hum ek HTTP request send karte 
hain server ko, taki wo hume required data ya service provide 
kar sake.

5. Server process:
Server HTTP request receive karta hai, usse process karta hai, 
aur phir ek HTTP response generate karta hai. Server request 
ke method, URL, headers, aur body ko analyze karta hai, aur 
uske basis par appropriate action leta hai. Jaise agar request 
GET method ka hai, toh server requested resource ko retrieve 
karke client ko bhejta hai. Agar request POST method ka hai, 
toh server client se data receive karke usse process karta hai, 
aur phir response me result bhejta hai.

6. Response back:
Server HTTP response send karta hai client ko. HTTP response me 
status code (jo indicate karta hai ki request successful thi ya nahi), 
headers (jo additional information provide karte hain),
aur body (jo actual data ya message hota hai) hota hai. 
Jaise agar request successful thi, toh server 200 OK status 
code ke sath response bhejta hai, aur body me requested data 
provide karta hai. Agar request me koi error hota hai, toh 
server appropriate error status code (jaise 404 Not Found, 
500 Internal Server Error) ke sath response bhejta hai, 
aur body me error message provide karta hai.

Ye sab milliseconds me hota.
'''
# PAGINATION - “Data bohot zyada hai”
'''
Server bolta:
“Ek page me 10 toys milenge”
mtlb agar hum 100 toys chahte hain, toh hume 10 pages ke 
liye request karni padegi. Har page ke liye alag request bhejni 
padegi, taki humara server overload na ho jaye aur hum 
efficiently data receive kar sakein. 
'''
'''
To handle pagination, we can use a loop to send multiple 
requests for each page until we have retrieved all the data 
we need.
''' 
# For example:
import requests
page = 1
while True:
    r = requests.get(f"url?page={page}")
    data = r.json()
    if not data:
        break
    page += 1

# RATE LIMIT  “Zyada order mat karo”
'''
Server bolta:
“1 minute me 10 request hi”

Solution:

. delay

. retry
'''
# Response object ke important parts
'''
response.status_code   # number (200,404...)
response.text          # simple text
response.json()        # JSON ko dict bana deta
response.headers       # extra info
response.url           # final URL
'''