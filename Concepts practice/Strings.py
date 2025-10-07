
#------------------------------------------------------------------------------------------------------
#  Road map to follow for strings
# ------------------------------------------------------------------------------------------------------

# this is a list of all the different types of operations that can be done on strings 

# type            -- type(), str()
# math            -- len(), count()
# transformations -- replace(), 'H' + 'i', f{}, split(), 'ha'*2, 'cat'[0], 'cat'[1:3]
# cleaning        -- lstrip(), rstrip(), strip(), lower(), upper()
# search          -- startswith(), endswith(), find(), 'a'in'cat'
# validation      -- isalpha(), isnumeric()

# ------------------------------------------------------------------------------------------------------

# strings are always written in a single or double quotes. ('') ("")
# anything wirtten between the quotes single or double is considered as string by python
# for multiple lines string we can use tripple quotes ("""".....""")
# They are immutable, meaning once created, their content cannot be changed directly.
# Since strings are iterable, you can loop through each character using a for loop.

# ------------------------------------------------------------------------------------------------------
# type
# ------------------------------------------------------------------------------------------------------

name = "Prajwal Sai"
print(type(name))

age = 30 
print(type(age))
print("your age is :", age)
print("your age is:" + str(age)) # the age is converted to string only in the print not the actual value

print(type(age)) # checking the type to confirm if the datatype is still int

age = age + 5 #since it is still int, we can do calculations like it is a number 
print(age)
age = str(age) # here we are changing the datatype of the value itself to string 
print(type(age))
# age = age + 5 # now if we do the calculation we'll get errors since the age is now a string

# imp: python is flexible with datatypes- but watch out! you can change a value's type, but python will treat it differently
# python runs line by line, top to bottom. 

# ------------------------------------------------------------------------------------------------------
# Maths
# ------------------------------------------------------------------------------------------------------

# len()

password = "123a"
print(len(password))

# real life example 

if len(password) < 8 :
    print ("your Password is too short!")

# len() counts everything even spaces
# usecase- validate input length- prevent values that are too short or too long

# Count()

text = """ 
        python is easy to learn.
        python is powerful.
        many people love python.
    """

print(text.count("python"))

# python is case-sensetive, means uppercase and lowercase letters are treated as different

#usecase- detect quality issues- count how many unwanted charachters in my data 

# ------------------------------------------------------------------------------------------------------
# Transformations
# ------------------------------------------------------------------------------------------------------

# replace()

price = "1234,56"
print(price.replace(",","."))

phone = "9837-8943-33"
print(phone.replace("-","/"))

# replace() is not just for changing values, you can also remove unwanted parts by replacing them with an empty string ("")

print(phone.replace("-",""))

# use case- clean numeric formats- removes symbols and commas to prepare for numeric conversion 

price = "$1,299.9"
print(price.replace("$","").replace(",",""))

# chain methods are executed in order from left to right. each replace() runs on the result of the one before it. 

#------------------------------------------------------------------------------------------------------
#  Python challenge
# ------------------------------------------------------------------------------------------------------

#  convert the messy phone number into a clean number format with only digits

# "+49 (176) 123-4567"

# it should be cleaned to show- 00491761234567

# ------------------------------------------------------------------------------------------------------

ph_number = "+49 (176) 123-4567"
print(ph_number.replace("+","").replace("(","").replace(")","").replace(" ","").replace("-",""))
 
# ------------------------------------------------------------------------------------------------------

# concatanate '+'
# operator 
# output: string
# joins(concatanates) two strings into one.

first_name = 'Michael'
last_name = "Scott"
full_name = first_name + " " + last_name
print(full_name)

# use case - build file paths - build dynamic paths using folder and file variables

folder = "c:/users/Prajwal"
file = "report.csv"
full_file_path = folder + "/" + file 
print(full_file_path)

# f-string
# modern, super-easy way to format and build strings
# 'f' stands for 'Formatted'
# lets you easily put variables and expressions directy inside string value

name = "Sam"
ag = 34 
is_student = False 
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + "."  ) 
# old way, complicated, tendency to make mistakes 

print(f"my name is {name}, I am {age} years old, and student status is {is_student}.")

# new way, all the data type connversion is done automatically by python using the f-string. 
# f-strings are shorter, cleaner, easier to read!! 

print(f"2 + 3 = {2+3}") # even expressions can be used inside the f-string

print(f"{{This is me}}") # to get the curly brackets in the output just put another curly brackets. 

#basic rule. after using the f in the print statement anything that is written in the curly brackets are done automatically by python

# split
# str method
# output: list of strings
# breaks a string into smaller parts

stamp = "2026-09-20 14:30"
print(stamp.split(" ")) 

# in the above example break a date into year, month and day parts

dates = "2026-09-20"
print(dates.split("-"))

csv_file = "1233,Max,USA,`970-10-05,M"
print(csv_file.split(","))

#string 
#operator
#output: String
#repats the string multiple times 

print("ha" * 3)

#use case- Style your logs- use repeated characters to create clear sections in output 

print("="*40)

# ------------------------------------------------------------------------------------------------------
# Transformations- Data extractions
# ------------------------------------------------------------------------------------------------------

# Each charachter has a position number- it's called as index
# there are two types of indexes- positive index and negative index
# positive index-- starts from left starting with 0 
# negative index -- starts from right starting with -1 instead of 0 and so on
# to mention/announce the position needed in the string we use the posistion number with in square brackets [0]
# this is called indexing
# using indexing method we can extract only one charachter at a time. 
# if you want to extract a group of charachters you need to put the same square brackets and mention the start and end charachters [start : end] [3:5]
# this is called as slicing 
# in slicing the starting position will be included and the end position mentioned will not be included 
# example "Hello" using slicing to get "ll" we give the slicing index as [2:4] 
# open-ended slicing- if you want the starting position and everything after that, you do not mention the end index and let python fetch everything [1 : ]
# skipped slicing-- if you want python to skip induvidual charachters and give the results you need to mention the step after the end position [start : end : step] [1 : 6: 2]
# example: "Hello" [0:4:2] in this python will skip every second value and give us the charachters. result: "Hl"
# by default the step will always be 1
# if no number is written then python defaults to 1 as the step.

# ------------------------------------------------------------------------------------------------------

# indexing
# 'string'[index] 
# operator 
# output: string

text = "Python"

#extract the first charachter 
print(text[0])
print(text[-6])

#extract the last charachter 
print(text[5])
print(text[-1])

#extract h 
print(text[3])

# slicing
# operator 
# output: string
# slicing: extracts a part of the string

date = "2026-09-20"

#extract the year 
print(date[0:4])

#open-ended slicing- if you leave the start index empty, python starts from index 0 
print(date[ : 4])

# exract the month 
print(date[5:7])

# extract the day 
print(date[8: ])

# use postive indexes- if you want to extract part from the left side(start) of a string use positive index
# use negative indexes- if you want to extract part from the right side(end) of a stirng use negative index 

print (date [-2:])

# when extracting middle. check if the middle values are closer to left or right, if it is left use postitvie, if right use negative

# ------------------------------------------------------------------------------------------------------
# Cleaning
# ------------------------------------------------------------------------------------------------------

# lstrip() 
# str method 
# removes spaces from the left side of a string 

# rstrip() 
# str method 
# removes spaces from the right side of a string 

# strip() 
# str method 
# removes spaces from both the sides of a string 


text = " Engineering "

print(len(text))

print(len(text.lstrip()))
print(len(text.rstrip()))
print(len(text.strip()))

#best practice- trim spaces from user input. You never know where users might add spaces use .strip() to remove all extra spaces from both the ends

text2 = "Data engineering" 

print(len(text2.lstrip()))
print(len(text2.rstrip()))
print(len(text2.strip()))

# strip will only remove the spaces at the start and/or end, not in the middle

# if no value is passed to the strip brackets by default python removes the spaces. 
# if any value is passed that is removed from the ends of the string and not in the middle

text3 = "####ABC####"

print(text3)
print(text3.strip("#"))


text4 = "##AB#C###"
print(text4)
print(text4.strip("#")) # does not remove the # in the middle. only the ones in the ends

# use case - detect extra spaces- check the length before and after strip() to find unwanted spaces 

text5 = "    Engineering        "

print(len(text5))
print(len(text5.lstrip())) 
print(len(text5)- len(text5.lstrip())) # counts the number of spaces before the word "engineering"
print(len(text5.rstrip()))
print(len(text5)- len(text5.rstrip())) # counts the number of spaces after the word "engineering"
print(len(text5.strip()))
print(len(text5)- len(text5.strip())) # counts the number of spaces before and after the word "engineering"

# real life application

nr_of_spaces = len(text5.strip())
is_clean = len(text5) == len(text5.strip())
print("Nr of spaces: ", nr_of_spaces)
print("Is my data clean?", is_clean)

# case conversions 

# converts all the characters in a string to lower case, useful for data cleaning

text6 = "Python PROGRAMMING"

# use case- standardize text case - make sure text is always in lower case

# .lower() 
# str method 
# output: string 
# makes all letters lowercase

print(text6.lower())

# .upper() 
# str method 
# output: string 
# makes all letters UPPERCASE

print(text6.upper())

# use case- clean data for matching - lowercase all text to prevent case- based mismatches during search or comparison

search = "Email"
data = "email"

print(search == data)

search2 = "Email".lower()
data2 = "emAil".lower()

print (search2 == data2)

# best practice - clean before search - always trimm spaces and lowercase your data and search term before matching 

search3 = " Email"
data3 = "emAil   "

print(search3.strip().lower())
print(data3.strip().lower())
print(search3.strip().lower() == data3.strip().lower())

#------------------------------------------------------------------------------------------------------
#  Advanced Python challenge
# ------------------------------------------------------------------------------------------------------

# turn the messy string into a single clean summary with name, role and age 

#   "968-Maria, (. D@t@ Engineer);; 27y   "       -- messy string
#   Name: maria | role: data engineer | age: 27   -- clean final result 

# ------------------------------------------------------------------------------------------------------

maintext =  "968-Maria, (. D@t@ Engineer);; 27y   "

formatedtext = maintext.lstrip("968-").replace(",","").replace("(. ", "").replace("@","a").replace(");;","").rstrip("y").strip()

print(formatedtext)

name = formatedtext[0:5].lower().strip()
print(name)

role = formatedtext[6:19].lower().strip()
print(role)

age = formatedtext[-3:].strip()
print(age)

print(f"Name: {name} | role: {role} | age: {age}")

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Searching
# ------------------------------------------------------------------------------------------------------

phone = "+49-176-12345"

# is the phone code german? check the country code (+49)

# startswith(substring)
# str method 
# output: Boolean
# checks if the string begins with a specific word

print(phone.startswith("+49"))

email = "prajwal@gmail.com"

# is the email from Gmail? check the domain(gmail.com)

# endswith(substring)
# str method 
# output: Boolean
# checks if the string begins with a specific word

print(email.endswith("gmail.com"))

file = "data_backup.csv"

# is the file a csv? check the extension (.csv)

print(file.endswith(".csv"))

# is this a valid email? check for '@'

# 'substring' in 'string'
# operator 
# output: int 
# checks if a word exists in the string

print("@" in email)

url = "https: //api.company.com/v1/data"
print("/api" in url)

# find() is great when combined with other methods to add dynamics

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

#extract only phone number wihtout country code

print(phone1[4:])
print(phone2[3:])

# hardcoding the start position doesn't work when the country code length changes 

# find(substring) 
# str method
#output: number
#retuns the strating position of a word in the string

print(phone1.find("-"))

print(phone1[phone1.find("-")+1:])
print(phone2[phone1.find("-")+1:])
print(phone3[phone3.find("-")+1:])

# ------------------------------------------------------------------------------------------------------
# Validation
# ------------------------------------------------------------------------------------------------------

# we can use these to check if the string is a string or integer

# isalpha()
# str meathod
# output: boolean
# checks if the string has only letters

country = "India"
print(country.isalpha())

country = "India1"
print(country.isalpha())

country = "India#"
print(country.isalpha())

# isnumeric()
# str meathod
# output: boolean
# checks if the string has only numbers

country = "India"
print(country.isnumeric())

phone = "0176123456589"
print(phone.isnumeric())

number = "42"
print(phone.isnumeric())

phone = "01761-23456589"
print(phone.isnumeric())

number2 = "3.1456"
print(number2.isnumeric())




