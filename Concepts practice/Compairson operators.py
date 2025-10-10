# ------------------------------------------------------------------------------------------------------
#  Comparison operators
# ------------------------------------------------------------------------------------------------------

# it compares two values and returns True or False based on the result 

#   ==    Equal to 
#   !=    not equal 
#   <     less than 
#   <=    less than or equal
#   >     Greater than 
#   >=    Greater than or equal

# ------------------------------------------------------------------------------------------------------

# is 10 equal to 10? 

print(10==10)
print(10 != 10)

# is 7 greater than 3?

print(7>3)

# is 7 greater than or equal to 7?

print(7>=7)

# is 7 greater than or equal to 3?

print(7>=3)

# is 3 less than 7?

print (3 < 7)

# is 3 less than or equal to 7

print (3 <= 7)

# strings can be compared too! - you can compare strings too alphabetically, not just numbers

print("a" == 'b')

# python is case-sensitive 
# so "a" and "A" are treated as different values 

print("a" == "A")

# **important** 
#  = assings  == compares 

# chained comparison - check mulitiple conditions in one line, just like in maths 
 
print(1 < 4 < 6)

# chained comparison - it evaluates it from left to right, checking each condition one by one
# chained comparison - works like SQL's BETWEEN they check if a value is between two boundries

# is age betwen 18 and 30? 

age = 20 
print(18 <= age <= 30)




