# ------------------------------------------------------------------------------------------------------
#  logical operators
# ------------------------------------------------------------------------------------------------------

# logical operators are and | or 

# used to combine multiple boolean expressions 

# and -- both the conditions must be true to get an output 
# or -- atleast one of the conditions must be true to get an output 

# ------------------------------------------------------------------------------------------------------

print(3 > 1 and 5 < 1) 
print(3 > 1 and 5 > 1)

print(3 > 1 or 5 < 1)
print(3 < 1 or 5 < 1)

# example- checks if the system is under pressure 
cpu_usage = 70
memory_useage = 95 

print(cpu_usage > 90 or memory_useage > 90)

# example2 - checking user credentials before login 

email = True 
password = False 
print (email and password)

# not operator 
# it reverses the truth. it turns True into False and False into True 

print(not 3 > 2)
print(not True)
print(not False)
print(not not False)

name = ""
print(name)
print( not name)
print(not 0)

# controling mixed conditions

# execution order- parentheses () first 
# "and" has higher priority than "or" by default.
# use parentheses () to control the order 

# parantheses is used to override the default. 
# in the order of operations whatever is in the parantheses get's executed and then other operators are excecuted

# ------------------------------------------------------------------------------------------------------
#  python task
# ------------------------------------------------------------------------------------------------------

# allow access only if the user is logged in 
# or they are guest 
# but they must not banned
# ------------------------------------------------------------------------------------------------------

is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or is_guest and not is_banned)
print((is_logged_in or is_guest) and not is_banned)

# ------------------------------------------------------------------------------------------------------
#  python challenge
# ------------------------------------------------------------------------------------------------------

# 1. Check if the user's name is not empty and the age is greater than or equal to 18 
# 2. check if the password is at least 8 charachters long and does not contain spaces 
# 3. check if a user's email is not empty, contains "@", and end with '.com'
# 4. check if a username is a string, is not none, and is longer than 5 characters 
# 5. check if the user is either an admin or a moderator, and either they're not banned or they've verified their email
# ------------------------------------------------------------------------------------------------------

# 1. Name not empty AND age >= 18
name = input(f"Please enter a name: ").strip()
age = input("please enter an age: ").strip()
print(f"The name provided is {name} and the age provided is {age}")

valid_user = (name != "") and age.isdigit() and (int(age) >= 18) 
print("valid user:", valid_user)

# 2. Password length >= 8 AND no spaces
password = input("Enter your password: ")
valid_password = (len(password) >= 8) and (" " not in password)
print("Password valid:", valid_password)


# 3. Email not empty, contains '@', ends with '.com'
email = input("Enter your email: ").strip()
valid_email = (email != "") and ("@" in email) and email.endswith(".com")
print("Email valid:", valid_email)


# 4. Username is a string, not None, and > 5 chars
username = input("Enter your username: ")
valid_username = isinstance(username, str) and (username is not None) and (len(username) > 5)
print("Username valid:", valid_username)


# 5. Role is admin or moderator AND (not banned OR verified)
role = input("Enter your role (admin/moderator/user): ").lower().strip()
banned = input("Are you banned? (yes/no): ").lower().strip() == "yes"
verified = input("Have you verified your email? (yes/no): ").lower().strip() == "yes"

access_granted = (role in ["admin", "moderator"]) and (not banned or verified)
print("Access granted:", access_granted)


