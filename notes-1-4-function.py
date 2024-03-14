# Function
# Lucas 
# Feb 26 2024

# Create a fuction called say_hello
# print "Hello"

def say_hello():
    print("Hello!")

# Create a fuction called say_hello_params
# print "Hello {parameter}!"
#   e.g. say_hello_params("Jim")
#       "Hello JIm!"
    
def say_hello_params(name):
    print(f"Hello {name}!")

# Create a fuction called how-big
# It takes a number as an input/param
#   It returns how big the number is
    
def how_big(num):
        if num < 0:
             return "Very small"
        if num < 10:
             return "Pretty small"
        if num < 100:
             return "Small"
        if num < 1000:
             return "Big"

# Create a fuction called addeer
#    Accepts two inputs that are numbers
#    Return the sum of the fuction
def adder(x,y):
     return x + y

say_hello()
say_hello_params("Jim")
print(how_big(999))
result = adder(6,660)
print(result) 