# Conditionals
# Lucas Zhang
# Feb 15 2024

# Implement the flowchart from notes
x = 100_0000
y = -100

# If x is less than y, say so
# If x is greater than y, say so
# If x is equal to y, say so

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

foo = input("Enter a number") # string
if int(foo) < -1 or int(foo) == 0:
    print("foo is less than one")
    print("or it's equal to zero.")

# foo = int(input("Enter a number"))  # other way to code
# if foo < -1 or foo == 0:
#     print("foo is less than one")
#     print("or it's equal to zero.")
    
# Check if foo is inside a range
# Greater then one and less than 1000
if foo > 1 and foo < 1000:
    print("foo is in the range 2 - 999")
else:
    print("Foo is outside the range 2 - 999")