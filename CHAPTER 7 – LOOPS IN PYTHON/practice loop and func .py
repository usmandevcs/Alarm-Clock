def make_chai(patti,doodh):
    return f"Garam {patti} aur {doodh} wali chai is ready!"
order = make_chai("tapal", 2)
# print(order)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(int(input("Enter a number to find its factorial: "))))

#  For Loop use cases:
nums = [1,2,3]
it = iter(nums)

# print(next(it))
# print(next(it))
'''
this is manual iteration using iter() and next() functions. 
We can also use a for loop to iterate through the list:
'''
'''
enumerate
Index + value
'''
for i, v in enumerate(["a","b","c"]):
    print(i, v)


# zip - parallel iteration
'''
It allows us to iterate over multiple sequences in parallel, 
combining elements from each sequence into tuples.
'''
names = ["Ali","Sara"]
marks = [80,90]

for n, m in zip(names, marks):
    print(n, m)

# Generator – lazy loop
def count_up(n):
    for i in range(n):
        yield i
counter = count_up(10)
print(next(counter))

# While loop use cases:
'''
Infinite loop control:
While loops are often used when we want to create an infinite 
loop that continues until a certain condition is met.then we 
use break statement to exit the loop when the condition is 
satisfied.
'''
while True:
    break
