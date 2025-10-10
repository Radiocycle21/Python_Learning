# ------------------------------------------------------------------------------------------------------
#  Conditional Statements
# ------------------------------------------------------------------------------------------------------

# checkpoint that checks a condition
# - true? Runs the code 
# - False? skip it

# Conditional statements control the flow of execution based on whether a condition is True or False.
# The if statement checks the first condition — if it’s True, the indented block runs.
# The elif (else-if) clause checks additional conditions when the previous ones are False.
# The else block runs only when all previous conditions are False.
# Conditions usually use comparison (==, !=, >, <, >=, <=) and logical (and, or, not) operators.
# Indentation (usually 4 spaces) is mandatory — it defines which code belongs to which block.
# Only one block of the if-elif-else chain runs, even if multiple conditions are True.

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# if Statements
# ------------------------------------------------------------------------------------------------------

# defines the first condition- "if this is true, do this; otherwise, do nothing" 

# ------------------------------------------------------------------------------------------------------

# if rules 

# 1. only one if per chain
# 2. starts with if 
# 3. mandatorily required 
# 4. it can be a stand alone condition

# ------------------------------------------------------------------------------------------------------

score = input("Please input the score: ")
if int(score) >= 90 :
    print("A") # Indentation is part of syntax of python.

# adding spaces at the begining of a line to show that the line belongs to a code block
 
# ------------------------------------------------------------------------------------------------------
# If-ELse statment. two-way Decision 
# ------------------------------------------------------------------------------------------------------

# else statement 
# Runs only if all previous conditions are flase- "if nothing was true do this instead"
# only one path runs! or only one decision is made at the end!

# ------------------------------------------------------------------------------------------------------

# else Rules 

# 1. comes at the end 
# 2. No conditions 
# 3. optional 
# 4. cannot standalone 
# 5. only one else
 
# ------------------------------------------------------------------------------------------------------

score = input("Please input the score: ")
if int(score) >= 90:
    print("A")
else:
    print("F")

# ------------------------------------------------------------------------------------------------------
# if-elif-else statements.  multiple condtions 
# ------------------------------------------------------------------------------------------------------

# elif statement asks a follow-up question. only runs if previous conditions were false
# "if the first wasn't true, thy this one"

# ------------------------------------------------------------------------------------------------------

# we can ask multiple conditions in four differnt places 
# if the condition is false                                                     - we can use the elif
# if the condition is true                                                      - we can use just the if - nested if statements
# if we want to add two conditions together                                     - we can use and / or 
# if we want to add a condition after the first condition cycle is completed    - we can add if statment at the end - independent if statement

# ------------------------------------------------------------------------------------------------------

# elif rules 

# 1. comes after if statment
# 2. multiple elif can be used
# 3. Needs condition
# 4. optional 
# 5. cannot standalone 

# ------------------------------------------------------------------------------------------------------

score = input("Please input the score: ")
if int(score) >= 90:
    print("A")
elif int(score) >= 80:
    print("B")
else:
    print("F")

# ------------------------------------------------------------------------------------------------------
# Branching: if-elif-elif-else
# ------------------------------------------------------------------------------------------------------

score = input("Please input the score: ")
if int(score) >= 90:
    print("A")
elif int(score) >= 80:
    print("B")
elif int(score) >= 70:
    print("C")
else:
    print("F")

score = input("Please input the score: ")
if int(score) >= 90:
    print("A")
elif int(score) >= 80:
    print("B")
elif int(score) >= 70:
    print("C")
elif int(score) >= 60:
    print("D")
else:
    print("F")

# ------------------------------------------------------------------------------------------------------
# nested if
# ------------------------------------------------------------------------------------------------------

# if statement inside another if 
# "if the first is true, then check the second"

# each 'if' can be followed by it's own 'else' 

score = input("Please input the score: ")
Submitted_project = input("Is Project submitted? True/False : ").strip().lower() == "true"
if int(score) >= 90:
    if Submitted_project:
        print("A+")
    else :
        print("A")
elif int(score) >= 80:
    print("B")
elif int(score) >= 70:
    print("C")
elif int(score) >= 60:
    print("D")
else:
    print("F")


# python evaluates Boolean conditions directly. avoid explicit comparisson == True or == False

# ------------------------------------------------------------------------------------------------------
# Connecting conditions: Logical operators
# ------------------------------------------------------------------------------------------------------

# and - Returns True only if both the conditions are true! 
# or - Returns True only if atleast one of the conditions is true! 

score = input("Please input the score: ")
Submitted_project = input("Is Project submitted? True/False : ").strip().lower() == "true"
if int(score) >= 90 and Submitted_project:
    print("A+")
elif int(score) >= 90:
        print("A")
elif int(score) >= 80:
    print("B")
elif int(score) >= 70:
    print("C")
elif int(score) >= 60:
    print("D")
else:
    print("F")

score = input("Please input the score: ")
Submitted_project = input("Is Project submitted? True/False : ").strip().lower() == "true"
if int(score) >= 90 and Submitted_project:
    print("A+")
elif int(score) >= 90:
        print("A")
elif int(score) >= 80:
    print("B")
elif int(score) >= 70:
    print("C")
elif int(score) >= 60 or Submitted_project:
    print("D")
else:
    print("F")

# ------------------------------------------------------------------------------------------------------
#  independent: if-else
# ------------------------------------------------------------------------------------------------------

# Each if is checked seperately 
# "ALl conditiona are tested- even if one is already true"

score = 90 
Submitted_project = False 

if score > 90:
    print("High Score")
else: 
    print("Low Score")

if Submitted_project:
    print("Project is submitted")
else :
    print("Project is not submitted")

# ------------------------------------------------------------------------------------------------------
#  python challenge 1
# ------------------------------------------------------------------------------------------------------

# Validate the quality and correctness of Email Values 

# - Must not be empty
# - Must contain '.' and '@'
# - Must contain exactly one '@' symbol 
# - Must end with '.com', '.org', or '.net'
# - Must not be longer than 254 characters
# - Must start and end with a letter or digit
# ------------------------------------------------------------------------------------------------------


email = input("Enter the Email: ").strip().lower()

if email == "":
    print("Email cannot be empty.")
elif not("." in email and '@' in email):
    print("Email must contian . and @")
elif email.count('@') != 1:
    print("Email must contain exactly one @")
elif not email.endswith(('.com', '.org', '.net')):
    print("Email must end with '.com', '.org', '.net' ")
elif len(email) > 254: 
    print("Email must not be longer than 254 charachters")
elif not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else: 
    print("Email is valid.")


# isalnum() - checks if the string contains only letters and digits 
# if you want to see full report of all the errors in the email instead of stopping after the first error found, use independent if statments

email = input("Enter the Email: ").strip().lower()

if email == "":
    print("Email cannot be empty.")
if not("." in email and '@' in email):
    print("Email must contian . and @")
if email.count('@') != 1:
    print("Email must contain exactly one @")
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with '.com', '.org', '.net' ")
if len(email) > 254: 
    print("Email must not be longer than 254 charachters")
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")

# ------------------------------------------------------------------------------------------------------
#  python challenge 2
# ------------------------------------------------------------------------------------------------------

# Validate the quality and correctness of Passwords

# - Must not be empty
# - Must be at least 8 Characters
# - Must include at least 1 uppercase
# - Must include at least 1 lowercase
# - Must not be same as the email
# - Must not contail any spaces
# - Must start and end with a letter or digit
# ------------------------------------------------------------------------------------------------------

email = input("Enter your email: ")
password = input("Enter the password: ")

if password == "" :
    print("Password must not be empty")
elif len(password) < 8 :
    print ("Your Password cannot be shorter than 8 characters")
elif password == password.upper() :
    print("Password should contain atleast one lowercase")
elif password == password.lower() :
    print("Password should contian atleast one uppercase")
elif password == email :
    print("Password cannot be same as email")
elif " " in password: 
    print("Password cannot have spaces")
elif not(password[0].isalnum() and password[-1].isalnum()):
    print("password must start and end with a letter or digit")
else: 
    print("password is valid.")

