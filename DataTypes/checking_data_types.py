name = "Gaurav"
# print(type(name) == str) # first way to check if a variable is string or not
print(isinstance(name, str)) # another way of checking if data type is string or not ( this can check other data types too)

age = 19
print(isinstance(age, float)) # should print false

days = float(321)
print(isinstance(days, float)) # initially not a float but shall print true due to conversion

number = int("12")
print(isinstance(number, int)) # another example like line no. 8