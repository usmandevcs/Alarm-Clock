# FILE HANDLING - OS I/O, buffering, text vs binary
''''
When file open hoti:
Python → OS system call → file descriptor → buffer layer.
'''
# Modes deep
'''
r → fail if not exist / read only
w → create if not exist / write only
w → truncate file
a → append pointer end
b → binary mode
t → text mode (default)
'''
# Text vs Binary

# Text:
from concurrent.futures import process


open("data.txt", "r")

# using with to open file:
'''
by using WITH statement, we can ensure that the file is properly 
closed after its suite finishes, even if an exception is raised. 
It provides a cleaner and more concise syntax for working with 
files.
'''
with open("data.txt", "r") as file:
    data = file.read()
    print(data)

# Binary:
with open("data.bin", "rb") as file:
    data = file.read()
    print(data)

# Binary me encoding nahi hoti.

# Encoding layer:
'''
When you open a file in text mode (e.g., "r" or "w"), Python uses 
an encoding layer to convert between the bytes stored in the 
file and the string representation used in your Python code. 
By default, Python uses UTF-8 encoding, but you can specify a 
different encoding if needed.
When you read from a file in text mode, the encoding layer decodes
the bytes from the file into a string. When you write to a file in
text mode, the encoding layer encodes the string into bytes before
writing it to the file.
When you open a file in binary mode (e.g., "rb" or "wb"), the
encoding layer is bypassed, and you work directly with bytes. This  
means that when you read from a file in binary mode, you get the raw 
bytes, and when you write to a file in binary mode, you need to 
provide bytes rather than strings.
'''
# Example of encoding:
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello, world! 👋")

# File pointer control
with open("data.txt", "r") as file:
    print(file.read(5))  # Read first 5 characters
    print(file.tell())   # Get current file pointer position
    file.seek(0)         # Move file pointer back to the beginning
    print(file.read())   # Read the entire file again

# Large file streaming
with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip())   # Process each line without loading 
                                # the entire file into memory.

with open("big.log") as f:
    for line in f:
        process(line)
'''
In this example, we open a large log file and process it line by 
line. This approach is memory-efficient because it doesn't load 
the entire file into memory at once, allowing us to handle files 
that are larger than the available memory.
'''

# JSON file handling:
import json
data = {"name": "Alice", "age": 30, "city": "New York"}

# Writing JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
'''The json.dump() function is used to write a Python object 
(in this case, a dictionary) to a file in JSON format. The indent 
parameter is used to specify the indentation level for 
pretty-printing the JSON data. In this example, the JSON data 
will be indented with 4 spaces for better readability.
The resulting data.json file will contain the following content:
{
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
'''

# Reading JSON from a file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
'''
The json.load() function is used to read JSON data from a file and
convert it back into a Python object (in this case, a dictionary).
When you run this code, it will read the JSON data from data.json
and print the resulting Python dictionary:
{'name': 'Alice', 'age': 30, 'city': 'New York'}
'''
