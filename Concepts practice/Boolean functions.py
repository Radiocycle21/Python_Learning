# ------------------------------------------------------------------------------------------------------
#  Boolean functions
# ------------------------------------------------------------------------------------------------------

print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

# none isn't emplty- it's missing!-- none means no value. ""Empty means the value exisits, but empty string

# any-- returns true if at least one value is true
# all-- returns true if all values are true

email = ""
phone = "0176-123456"
username =  ""

# allows registration 
#if nay field is filled 

print(any([email, phone, username]))

#allows registration 
# only of all fields is filled
print(all([email, phone, username]))

print(isinstance(123, int))
print(isinstance(True, str))

print("Hello".endswith("o"))
print("Hello".startswith("H"))