# map ()
numbers = [1,2,3]
 
# def triple(a):
#     return a * 3

# doing this same but in lambda function
# triple = lambda a : a * 3

# result = map(triple, numbers)

#doing lambda function but in same line

result = map (lambda a : a * 3, numbers)
print(list(result))