print("Hi Python")
print("Hi Prajwal")
print('Hello Python')

# escape sequences -- uses it to pause a sequence

# using the \" you can use to add double quotes in the output
print("Hi \"Python\"")

print('Hi "Python"')  # another way to have double quotes and break the sequence

print("Path: C: \\users\\ Prajwal")

print("message1\n")
print("message2")  # uses \n to add a new empty line between message1 and message 2

# you can use multiple \n to get multiple line spaces
print("Message1 \n\n\nMessage2")

print("Message1 \t Message2")  # you can use \n to get a tab space

# ------------------------------------------------------------------------------------------------------
#  Python challenge
# ------------------------------------------------------------------------------------------------------

# use print() to recreate the exact output
# you are allowed to use only one print()
# your learning path:
# - python Basics
# - Data Engineering
# - AI

# ------------------------------------------------------------------------------------------------------

print("""Your learning path:
\t- python Basics
\t- Data Engineering
\t- AI""")

# ------------------------------------------------------------------------------------------------------
# Real life example of print- use case 
# ------------------------------------------------------------------------------------------------------

price_shirt = 25.00 
price_jeans = 45.50 

qty_shirt = 2 
qty_jeans = 1 

total_shirt = price_shirt * qty_shirt 
total_jeans = price_jeans * qty_jeans 
subtotal = total_shirt + total_jeans 
print("Subtotal:", subtotal)
discount = subtotal * 0.10 
print("Discount:", discount)
final_total = subtotal - discount 
print("Final Totat:", final_total)

