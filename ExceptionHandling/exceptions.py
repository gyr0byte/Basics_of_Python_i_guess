try:
    result = 2 / 0
    
except ZeroDivisionError:
    print("Cannot divide by Zero")

finally:
    result = 1

print(result)

try:
    raise Exception("An Error!")

except Exception as error:
    print(error)