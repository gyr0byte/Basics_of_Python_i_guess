condition = True
if condition == True:
    print("The condition was True")

else:
    print("The condition was False")
    
age = int(input("Enter your age: "))
if age >= 19 and age <= 50:
    print("You are an adult")

elif age < 18 and age >= 1:
    print("You are a child")

elif age <= 0:
    print("Invalid age")

else:
    print("You are an elderly")