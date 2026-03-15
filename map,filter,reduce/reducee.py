# reduce()
from functools import reduce
expenses = [("Dinner", 1200), ("Maintainance", 2500)]

# Long way of doing this
# sum = 0
# for expense in expenses:
#     sum += expense[1]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)
