# ------------------------------------------------------------------------------------------------------
#  advanced for Loops in python
# ------------------------------------------------------------------------------------------------------
#  Break, Continue and Pass
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
#  Break statement in python
# ------------------------------------------------------------------------------------------------------

# break statement is used to stop the loop immediatetly 
# it jumps out and ends the loop right away

names = ['john', 'maria', '', 'kumar']

for name in names :
    if name == '': 
        print ('Empty value detected!')
        break
    print(f"Name = {name}")

# ------------------------------------------------------------------------------------------------------
#  Continue statement in python
# ------------------------------------------------------------------------------------------------------

# it skips one loop cycle without stopping the loop 
# skip this one and go to next 

names = ['john', 'maria', '', 'kumar']

for name in names :
    if name == '': 
        print ('Empty value detected!')
        continue
    print(f"Name = {name}")

# use continue to skip bad or empty data without stopping the whole loop 

# ------------------------------------------------------------------------------------------------------
#  Pass statement in python
# ------------------------------------------------------------------------------------------------------

# it is a placeholder where nothing happens 
# for now, just keep going, do nothing 

names = ['john', 'maria', '', 'kumar']

for name in names :
    if name == '': 
        pass #todo: handle empty value
    print(f"Name = {name}")

# it is a placeholder that can be replaced. 

names = ['john', 'maria', '', 'kumar']

for name in names :
    if name == '': 
        name = name.replace('', 'unknown')
    print(f"Name = {name}")

# ------------------------------------------------------------------------------------------------------
# Break vs continue real- world application
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Python task
# ------------------------------------------------------------------------------------------------------

# loop through a list of days and print only the working days, skipping the weekends

days = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun']

for day in days: 
    if day in weekends:
        continue
    print(f'workday : {day}')

# avoid hardcoding values inside for or if instead, define them as variables

# ------------------------------------------------------------------------------------------------------
# Python task
# ------------------------------------------------------------------------------------------------------

# scan emails to block unsafe data from entering your system 

emails = [
    'data@gmail.com',
    'prajwal@outlook.in',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection: hacker Attack')
        break
    print(f"processing email: {email}")

# ------------------------------------------------------------------------------------------------------
# Comparison: Break vs Continue vs Pass
# ------------------------------------------------------------------------------------------------------

# Break: critical risk, high emergency- exists immediatly 
# Continue: medium risk - skip 1 iteration 
# Pass: low risk- Do nothing 