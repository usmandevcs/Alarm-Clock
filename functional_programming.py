# Functional Programming (FP)
'''
FP ka bunyadi maqsad yeh hai ke hum data ko badalne (mutating) 
se bachein aur sirf functions par zor dein.
'''
# FP mein do sab se aham concepts hain jin par hum baat karenge:

# 1. Pure Functions (Khaalis Functions)

# 2. Immutability (Na Badalne Wali Cheezein)

# 3. First-Class Functions (Functions ko variables ki tarah istemal karna)

# 1. Pure Functions (Khaalis Functions)
'''
khalis function woh hota hai jo sirf apne inputs par depend karta hai
Yeh asal list haie ke andar koi side effects nahi hote.
Iska matlab yeh hai ke agar aap same inputs do baar denge,
toh aapko hamesha same output milega.
'''
# Example:
original_list = [10, 20] 

def add_to_list(current_list, item):
    # Nayi list banana (Copy)
    new_list = list(current_list) 
    
    # Nayi list mein badlav karna
    new_list.append(item) 
    
    # Nayi list wapas karna
    return new_list 

list_after_add = add_to_list(original_list, 30)

# Original list nahi badli: [10, 20]
print(f"Original List: {original_list}") 

# Output hamesha predictable rahega.
print(f"New List: {list_after_add}")


# 2. Immutability (Na Badalne Wali Cheezein)
'''
Matlab: Immutability ka matlab hai woh data jo banne ke baad 
kabhi badla nahi ja sakta.

FP mein, hum hamesha Immutable data (na badalne wala data) 
istemal karne ki koshish karte hain, ya agar humein koi badlav 
karna ho, toh hum purane data ko badalne ke bajaye us se naya 
data bana lete hain.
'''
# Python mein Immutability:
'''
Python mein do tarah ke data types hote hain:

Immutable (Na Badalne Wale): String, Integers, Floats, Tuples.

Mutable (Badalne Wale): Lists, Dictionaries, Sets.
'''
# FP mein Immutability Kyun Zaroori Hai?
# Immutability Pure Functions banane mein madad karti hai.
'''
Agar function sirf Immutable data leta hai, toh yeh 100% yaqeeni 
(sure) hai ke function us data mein Side Effect nahi dega, 
kyunke woh data badal hi nahi sakta.

Is se debugging (ghaltiyan nikalna) bahut aasan ho jati hai, 
kyunke aapko hamesha pata hota hai ke data kahan aur kab badla 
gaya.
'''
# Example of Immutability:
def add_to_tuple(original_tuple, item):
    # Naya tuple banana (Original ko badalne ke bajaye)
    new_tuple = original_tuple + (item,) 
    return new_tuple
original_tuple = (1, 2, 3)
new_tuple = add_to_tuple(original_tuple, 4)
print(f"Original Tuple: {original_tuple}")  # Original Tuple: (1, 2, 3)
print(f"New Tuple: {new_tuple}")            # New Tuple: (1, 2, 3, 4)
