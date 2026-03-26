#1. OPENING A FILE 
'''Python has an open() function for opening files. It takes 
2 parameters:  filename and mode. '''
# open("filename", "mode of opening(read mode by default)") 
# open("this.txt", "r") 

#2. READING A FILE IN PYTHON 
# Open the file in read mode 
        # f = open("this.txt", "r") 
# Read its contents 
        #  text = f.read() 
# Print its contents 
        # print(text)
# Close the file 
        # f.close() 

# OTHER METHODS TO READ THE FILE. 
'''We can also use f.readline() function to read one full line 
at a time.'''

# f.readline() # Read one line from the file. 

# MODES OF OPENING A FILE 
'''
r - open for reading 
w - open for writing  
a - open for appending 
+ - open for updating. 
'rb' will open for read in binary mode. 
'rt' will open for read in text mode.
'''
# WRITE FILES IN PYTHON 
'''In order to write to a file, we first open it in write or append 
mode after which, we use the python's f.write() method to write 
to the file!''' 
# Open the file in write mode 
        # f = open("this.txt", "w") 
# Write a string to the file 
        # f.write("this is nice") 
# Close the file 
        # f.close() 