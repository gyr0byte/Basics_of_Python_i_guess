# def square_number(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_number([1, 2, 3, 4, 5])
# using list comprehension
my_nums = (x * x for x in [1, 2, 3, 4, 5])

# converting generators into a list
# print(list(my_nums))
for num in my_nums:
    print(num)
