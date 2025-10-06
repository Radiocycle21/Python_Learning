# Data types 

a = 10        #int- integer
b = 3.14      #float- Float
c = "Hello"   #str- string
d = 'Hi'      #str- string
e = "1234"    #str- string
f = True      #bool- Boolean 
g = False     #bool- Boolean
h = None      #NoneType
i = ""        #str- blank- a string without value inside
j = " "       #str-empty- whiteSpace- a string with one or more blank spaces inside


text = 'Hi'
number = 10 

print(text)
print(number)

print(type(text))
print(type(number))

print(len(text))
#print(len(number)) # will get an error that there is no len() for int

print(text.upper())
# print(number.upper()) # will get an error

print(number.bit_length())

#------------------------------------------------------------------------------------------------------
#  Python challenge
# ------------------------------------------------------------------------------------------------------

# create 5 variables - each with a diffrerent data types:

#  1. your age 
#  2. your height(with decimals)
#  3. your name 
#  4. Are you a student?
#  5. Something with no value yet

#  then print the values, data types, lenghts of all variables

# ------------------------------------------------------------------------------------------------------
 
Age = 30 
height = 5.10
name = "Prajwal Sai N."
Student = False
job = None

print(Age)
print(height)
print(name)
print(Student)
print(job)

print(type(Age))
print(type(height))
print(type(name))
print(type(Student))
print(type(job))

# print(len(Age)) - int datatype so no result
# print(len(height)) - float datatype so no result
print(len(name))
# print(len(Student)) - bool datatype so no result
# print(len(job)) - nonetype datatype so no result

