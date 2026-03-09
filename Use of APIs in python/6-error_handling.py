# ERROR HANDLING - “Agar food gir gaya”
'''
Hum error ko hanle karny k liye "try, except" block ka use 
karty hain ta k hamara program crash na ho aur user ko ek acha 
message de sakay. 
'''
# Example:
'''
try:
    r = requests.get(url)
    r.raise_for_status()
except:
    print("Error aya")
'''
# 2nd Example:
try:
    # Code that may raise an error
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")