#------------------------------------------------------------------------------------------------------
#  Road map to follow for numbers
# ------------------------------------------------------------------------------------------------------

# this is a list of all the different types of operations that can be done on numbers 

# types             - type(), int(), float(), complex()
# math operators    - +, -, *, /, //, %, ** 
# rounding          - abs(), round(), ceil(), floor(), trunc() 
# Advanced math     - squrt(), sin(), cos(), log()
# Random            - random(), randint() 
# validation        - is_integer(), isinstance() 

# these are built-in functions, operators, import functions/modules.

# ------------------------------------------------------------------------------------------------------

# Numbers in Python are immutable data types used to represent and perform mathematical operations on numeric values.
# Python supports three main numeric types — int (integers), float (decimal numbers), and complex (real + imaginary parts).
# Numeric data can be manipulated using arithmetic operators like +, -, *, /, //, %, and **.
# Python allows automatic type conversion between numeric types during calculations (for example, integer + float → float).
# The math module provides advanced mathematical functions for calculations like square roots, logarithms, and trigonometric operations.

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# types
# ------------------------------------------------------------------------------------------------------

x = 5 
y = 5.7 
z = 2+3j 

print(type(x))
print(type(y))
print(type(z))

a = "24"
print(type(a)) # the type is considerd as string as it is in within quotes

a1 = int(a) # converting the type to int
print(type(a1))

# int(value) 
# built-in function
# output: int 
# converts compatible value into int value 

print(a * 3) # considers it as string
print(a1 * 3) #considers it as number

b = 3.14 
print(int(b)) # gives the result as int

# float(value) 
# built- in function 
# output: flaot 
# converts compatible value into float value

b1 = 3
print(float(b1)) # gives the result as float

b2 = "3.14"
print(float(b2)) # gives the result as float

c = 3 #real
d = 4 #imaginary 
print(complex(c,d)) # converts the values into complex number 

# ------------------------------------------------------------------------------------------------------
# Maths operators
# ------------------------------------------------------------------------------------------------------

print(2+3)      #addtion operator 
print(5-3)      # subraction operator 
print(4 * 2)    # multiplication operator 
print(7 / 2)    # division operator 
print (7 // 2)  # // floor division-- output: int - it dividies two numbers and rounds down 
print(7 % 2)    # % remainder -- output: 0 or 1 -- the leftover part after divisionn - used to check if a number is even or odd
print(2 ** 3)   # ** exponential -- it raises a number to the power of another number

# <operator>= 
# shorthand assignment
# apply an operator and reassign the result in one step

u = 2 
# u = u + 3 
u += 3
print(u)

u -= 1
print(u)

u *=2
print(u)

# ------------------------------------------------------------------------------------------------------
# Rounding
# ------------------------------------------------------------------------------------------------------

# abs()
# measure distance 

print(2-10) 

# abs(value) 
# built-in function 
# output: int 
# retuns the absolute(non-negative) value of a number

print (abs(2-10))

# useful for measuring distance or size, regardless of direction 

# rounding numbers 
# round()

price= 35.549738423
price1 = 35.349738423


print(round(price))
print(round(price1))


# math.floor(x)
#rounds a number down to the floor

# math.ceil(x)
# rounds a number up to the ceiling 

# math.round(x)
# round a number to the nearest whole number up or down depending on what's closer

# bankers rounding 
# ties (like .5) go to the nearest even number 

# print(floor(price))

# floor() is not a built-in function 
# floor() belongs to the man module - import it before using

import math

print(math.floor(price))

print(math.ceil(price))

# round(number, ndigits)
# rounds the number to the specified number of decimal places 

print(round(price, 2))
print(round(price, 1))

# math.trunc(x)

# math.trunc(x)- cuts off the decimal part and keeps the whole number (no rounding) 

print(math.trunc(price))

print(int(price)) # if you want to remove the decimal and have no other tasks then use int to remove the int 

# if you're not using math already, just use int() it's simple and built-in.
# if you've already imported math use trunc() it makes your intent clearer. 

# round() - handy in data analysis to clean up numbers for reports or save space 
# ceil() - perfect for data engineering- like splitting data into pages or batches

import random 

print(random.random())

# random() 
# random function 
# output: float 
# returns a random float between 0.0 and 1.0 


# randint(start, end) 
# random function 
# output: int 
# gets a random whole number from start to end(both included) 

print(random.randint(0,21))

# use it to generate test data (dummy) for like age, ID or prices 
# random sampling- picking a smaller, random part of a huge dataset 

# ------------------------------------------------------------------------------------------------------
# Validation
# ------------------------------------------------------------------------------------------------------

v = 7.0 

# is_integet() 
# float class meathod 
# output: bool 
# checks if a float has no decimal part(is a whole number)

print(v.is_integer())

w = 7.21
print(w.is_integer())

# check if numbers are truly whole 
# floats with .0 might just be from file exports

# ininstance(value, type)
# built-in function 
# output: boolean
# checks if a value belongs to a certain data type

p = 70 
print(isinstance(p, int))

p1 = 70.34
print(isinstance(p1, int))

#------------------------------------------------------------------------------------------------------
#  Python challenge
# ------------------------------------------------------------------------------------------------------

#  Generate a random integer between 1 and 100 and check if the result is an even number 

# ------------------------------------------------------------------------------------------------------

number = random.randint(1,100)
print(f"Random number generated is: {number}")
print(f"If remainder is 0 then even, if 1 then odd. Is the number even or odd?: {number % 2}")

# ------------------------------------------------------------------------------------------------------

# using if statement (trying things out personally, not in numbers course module)

number = random.randint(1, 100)
print(f"Random number generated is: {number}")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
