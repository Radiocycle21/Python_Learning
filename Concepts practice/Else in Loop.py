# ------------------------------------------------------------------------------------------------------
#  Else in loop
# ------------------------------------------------------------------------------------------------------

# runs a block of code only if the loop finishs naturally
# lopp completed without any break

items = [1,3,4,7]

for i in items: 
    print(i)
else: 
    print("Loop is completed")

# this else runs no matter what, so why not just write it after the loop? 

for i in items: 
    print(i)
print("Loop is completed")

# you get the same result like above block as else makes no sense

# so to make else statement make sense. use else with loops only when there's a break

# ------------------------------------------------------------------------------------------------------
# Find out if there are even numbers
# ------------------------------------------------------------------------------------------------------

items = range(1, 21, 3)

for i in items: 
    if i % 2 == 0:
        print("Even Number Found", i)
        break
else: 
    print("all numbers are odd")

# else statement will run only if the loop is not interrupted


# ------------------------------------------------------------------------------------------------------
# Real world application example
# ------------------------------------------------------------------------------------------------------
 
# 1. else is use to search and validate the data 


# ------------------------------------------------------------------------------------------------------
# Python Task
# ------------------------------------------------------------------------------------------------------

# check for missing names in a list

names = ['Kumara', 'Tuba', None, 'Mounika']

for name in names: 
    if name is None: 
        print("Found a missing name")
        break
else:
    print("All names are avialbale")

# check if all files are CSV Files 

files = ['data1.csv', 'report.pdf', 'data2.txt', 'report2.csv', ]

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a CSV')
        break
else:
    print('All files are CSV')

# ------------------------------------------------------------------------------------------------------
# Python Challenge
# ------------------------------------------------------------------------------------------------------

# check wheter any filename appears more than once 

# file_list = ['report.csv','data.xlsx','summary.docx','report.csv','data.csv',]

# print "DUplicate found" if a duplicate exists, otherwise print "All files are unique"

# ------------------------------------------------------------------------------------------------------

file_list = ['report.csv','data.xlsx','summary.docx', 'data.csv', 'report.csv',]

for file in file_list:
    if file_list.count(file) > 1 :
        print("Duplicate found")
        break
else:
    print('All files are unique')

    