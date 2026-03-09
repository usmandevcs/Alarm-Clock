# IF __NAME__== ‘__MAIN__’ IN PYTHON  
'''
'__name__' evaluates to the name of the module in python from where 
the program is run. 
If the module is being run directly from the command line, the 
' __name__' is set to string “__main__”. Thus, this behaviour is used 
to check whether the module is run directly or imported to another file.
asan alfaz ma agr hum kisi file se code ko import kar k use karty hain
to ye humy us file ka name show kar de ga agr hum kisi file se code 
ko import nahi kar rhy to ye (__main__) print kardy ga.
'''
# EXAMPLE:

from module import func #  ye code humny import kiya 
# iska output ma name wo file hogi jaha se import iya ha


def myfunc():
    print("Hello! Usman")

myfunc()
print(__name__)

# ye humny import nahi kiya to iska name __main__ aye ga 