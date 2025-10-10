# ------------------------------------------------------------------------------------------------------
#  membership operators
# ------------------------------------------------------------------------------------------------------

# checks if a value inside another value like a string, list, tuple or other sequence
# 'in' operator gives a boolean result. 
# it checks if the value exits in a sequence or not
# 'not' operator just negates the operator

# ------------------------------------------------------------------------------------------------------

print ("o" in "python")
print("f" in "python")
print("f" not in "Python")
print(3 not in [1,2,3])

# ------------------------------------------------------------------------------------------------------
#  Python task
# ------------------------------------------------------------------------------------------------------

# validate that the domain is not on the banned list

# ------------------------------------------------------------------------------------------------------

# security check: ensure the domain is not banned


domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)

# ------------------------------------------------------------------------------------------------------

# identitiy operators (is - is not)

# checks if two variables refer to the smae object in memory 

# in 'is' operator we are not comparing the values, we are chekcing if two variables are the pointing to the same object in the memory 
# we are not is comparing the values, we are checking the place in the memeory of two variables. 
# output is a boolean

# ------------------------------------------------------------------------------------------------------

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)
print(x is y)


x = 10
y = 10

print(x == y)
print(x is y)

x = ['a', 'b', 'c']
y = x

print(x == y)
print(x is y)

# = between two variables- assigns one variable to the same object that another variable is referring to.

# ------------------------------------------------------------------------------------------------------
#  Python task
# ------------------------------------------------------------------------------------------------------

# validate the email address, it must be filled in and not empty
# ------------------------------------------------------------------------------------------------------

# make sure the email exsits, and it's not empty.

email = input("Enter your email here: ")
print(email != "" )

# none - means no value at all, it is unknown 
# "" - means an empty but it is known, it is string

email = input("Enter your email here: ")
print(email is None and email != "" )

email = input("Enter your email here: ")
print(email is not None and email != "" )

# use is instead of == when checking for None
# always use is when checking for None or null
# just like in SQL, we use is to filter for null 




