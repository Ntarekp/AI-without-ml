i =1
w =2
t= 3
total = i +\
    w +\
    t
print(total)
"""
Python does not recognise text in strings without being placed in an identifier or variable


# Initial variables
x, y = 10, 8

print(f"Before swapping: x = {x}, y = {y}")

# Swap the variables in a single line
x, y = y, x

print(f"After swapping: x = {x}, y = {y}")

a = b = c ="kayitare","prince"
print(a)
print(b)
print(type(c))"""

fruit = ["apple", "banana", "cherry"]
x, y,z = fruit
print(x)
print(y)
print(z)
fruts =("apple", "banana", "chery","orange","mango","avocado")

# (green,yellow,*red) = fruts
(green,*yellow,red) = fruts

print(green)
print(yellow)
print(red)

a = "apple"
b = 4
c =" kayitare"
print(a,b)
print(a+ str(b))

print(bytes(range(65, 91)).decode('utf-8'), bytes(range(97, 123)).decode('utf-8'))

# 1. Python's three numeric types
# Integer
my_int = 10
print(f"my_int: {my_int} is of type {type(my_int)}")

# Float
my_float = 20.5
print(f"my_float: {my_float} is of type {type(my_float)}")

# Complex
my_complex = 3 + 4j
print(f"my_complex: {my_complex} is of type {type(my_complex)}")

# 2. Type Conversion
# Convert an integer to a float
int_to_float = float(my_int)
print(f"Converted {my_int} to float: {int_to_float} is of type {type(int_to_float)}")

# Convert a float to an integer (truncates the decimal part)
float_to_int = int(my_float)
print(f"Converted {my_float} to int: {float_to_int} is of type {type(float_to_int)}")

# Convert a float to a complex number (the imaginary part is 0)
float_to_complex = complex(my_float)
print(f"Converted {my_float} to complex: {float_to_complex} is of type {type(float_to_complex)}")


