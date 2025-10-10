# ------------------------------------------------------------------------------------------------------
#  Loops in python
# ------------------------------------------------------------------------------------------------------

# Loops control the flow of the code. 
# repeat a block of code over and over until a condition is met
# Loops is basically autopilot for the code, python automatically runs the same peice of code till a condition is met
# Commonly used for data processing, aggregation, filtering, and iteration over files or collections.
# Loops are used to execute a block of code repeatedly until a specified condition is met.
# They help automate repetitive tasks and reduce code duplication.
# Each iteration runs the same code but can work with changing data values.
# Loops continue until the condition becomes False or a control statement (break, return, etc.) stops it.
# Python mainly supports two types of loops — for (iterates over sequences) and while (runs based on a condition).

# ------------------------------------------------------------------------------------------------------
# For Loop 
# ------------------------------------------------------------------------------------------------------

# go through a group of items one by one to do something for each item
#  syntax structure: 
# for [Loop Variable] in [sequence] :
#           print([loop Variable])
# Python Iterator: an object that lets you go throguh items one by one in a sequence. 
# iterator remembers what's done. knows what's next. 
# keeps track what is done and what needs to be done. 

# ------------------------------------------------------------------------------------------------------

print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

# in the above code, we are repeating the thing over and over till we get all the results. 
# so, instead we can use a for loop to do the same

for i in (1,2,3,4,5) : 
    print("Round: 1") #Python just runs the for for 5 times and gives the same result 5 times

for i in (1,2,3,4,5) : 
    print(f"Round: {i} \n")

# use the same word 
# variable --> singualr 
# sequence --> plural 

items = (1,2,3,4,5)

for item in items : 
    print(f"Round: {item}")

#  for loop needs to have a sequence 
# seuqences can be lists, tuples, sets and dictionaries, arrays. strings, range, file

items = [1,2,3,4,5, "Hi"]

for item in items : 
    print(f"Round: {item}")

# using strings to loop 

items = "Analytics"

for item in items : 
    print(f"Round: {item}")

# using built-in function called range 

# range(stop)
# example- range(5)
# the stop range will not be included in the range in loop, the numbers start from 0 

items = range(8)

for item in items : 
    print(f"Round: {item}")

# if you want to give a specific number to start from, you can use the start value as well in the range syntax 
# start will be inside the sequence, while stop will be outside the sequence. 

items = range(1, 11)

for item in items : 
    print(f"Round: {item}")

# we can even skip the number using steps. 
# range(start, stop, step)
# by default the step will always be 1 
# by default the range is always range(stop) 

items = range(1,11,2) # odd number generation

for item in items : 
    print(f"Round: {item}")

items = range(0,11,2) # even number generation

for item in items : 
    print(f"Round: {item}")

# ------------------------------------------------------------------------------------------------------
# For Loop- Real world application
# ------------------------------------------------------------------------------------------------------

# 1. moving files from source to target
# 2. data prepartion / data cleaning 
# 3. etc.

# we can use for loops to go through values and aggregate data like summing, counting or averaging 

scores = [80,50,60,75]
total = 0 

for score in scores:  # creates a running total
    total += score
    print("currrent total:", total)
print("final total:", total)


# we use for loops to transform data like cleaning data before processing 

files = ['Report.csv ', ' DATA.csv', ' final.TXT']

# inconsistant casing & unnecessary spaces 

for file in files: 
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")

# general rule: clean first, transform second-- always in that order. 

# ------------------------------------------------------------------------------------------------------
#  python challenge 1
# ------------------------------------------------------------------------------------------------------

# Print the 7-times table from 1 to 10 using a for loop

# ------------------------------------------------------------------------------------------------------

tables = range(1,11)

for table in tables :
    result = 7 * table
    print(f" 7 X {table} = {result}")

# ------------------------------------------------------------------------------------------------------
#  python challenge 2
# ------------------------------------------------------------------------------------------------------

# Print a left- aligned pyramid of stars with 6 rows using a for loop

# ------------------------------------------------------------------------------------------------------

for i in range(1, 7) :
    print("*" * i)