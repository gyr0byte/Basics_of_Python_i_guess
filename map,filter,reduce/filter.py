# filter()

numbers = [1, 2, 3, 4]

# def isEven(n):
#     return n % 2 == 0

# result = filter(isEven, numbers)
result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))