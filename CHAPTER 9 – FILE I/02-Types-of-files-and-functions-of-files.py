# TYPE OF FILES. 
# There are 2 types of files: 

# 1. Text files 
        # (.txt, .c, etc)
'''
wo files jo hum vs code ma open kar skty hain ye jo .py ha 
its also a text file.
'''

# 2. Binary files 
        # (.jpg, .dat, etc) 

'''Python has a lot of functions for reading, updating, and 
deleting files.''' 

# 1st Function is Read file 

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        return "File not found."

# 2nd funtion is Update File (Append or Overwrite)

def append_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')

# 3rd Function is Delete File

import os

def delete_file(filename):
    try:
        os.remove(filename)
        return "File deleted."
    except FileNotFoundError:
        return "File not found."

# Usage Example:
'''
# Write new data
overwrite_file('data.txt', 'Initial content.')

# Add more data
append_file('data.txt', 'Another line.')

# Read file
print(read_file('data.txt'))

# Delete file
print(delete_file('data.txt'))
'''

