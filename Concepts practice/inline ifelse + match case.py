# ------------------------------------------------------------------------------------------------------
#  inline if statments or Ternaary operator
# ------------------------------------------------------------------------------------------------------

# syntax: 

# <value_if_true> if <condition> else <value_if_false>

# It’s a shorter and cleaner way to assign a value or return something based on a condition, instead of using a full multi-line if-elif-else block.
# The condition is evaluated first:
# If it’s True, the expression before if is returned.
# If it’s False, the expression after else is returned.
# Must always include else; cannot omit it.
# Can be used in assignments, print, or function returns.
# Nesting allowed but keep it readable; single-line only.
# output of the inline if is stored in a variable 
# there is no elif in this inline if statements

# ------------------------------------------------------------------------------------------------------

score = input("Please enter your score: ")

# Regular method


if int(score) >= 90 :
    print ("A")
else: 
    print("F")

# inline method 

print("A" if int(score) >= 90 else "F")

grade = "A" if int(score) >= 90 else "F"
print(grade)

# adding multiple conditions without using elif in inline method

if int(score) >= 90 :
    print ("A")
elif int(score) >= 80 :
    print("B")
else: 
    print("F")

# inline method 

grade = "A" if int(score) >= 90 else "B" if int(score) >= 80 else "F"
print (grade)

# ------------------------------------------------------------------------------------------------------
#  Case-Match
# ------------------------------------------------------------------------------------------------------

# evaluate a value agaisnt mulitple values. Runs the code of the first match
# this can be used only for matching values


# ------------------------------------------------------------------------------------------------------
#  Python task
# ------------------------------------------------------------------------------------------------------

# Convert the full country names into 2-letter abbrevations 

country = input("Enter the country names from this list ['India', 'United States', 'Egypt', 'Germany'] : ")

# regular method

if country == "United States" :
    print("US")
elif country == "India" :
    print("IN")
elif country == "Egypt" :
    print("EG")
elif country == "Germany" :
    print("DE")
else: 
    print("Unknown Country")

# using case-match 

match country:
    case "United Sates" | "USA" :
        print("US")
    case "India" :
        print("IN")
    case "Egypt" :
        print("EG")
    case "Germany" :
        print("DE")
    case _ :
        print("Unknown Country")




