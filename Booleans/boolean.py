done = True

print(type(done) == bool)
if done:
    print("It is working")
else:
    print("It is not working")
    
book1 = True
book2 = False
read_any_book = any([book1, book2]) # it returns true if any of the value to iterable is true
read_all_books = all([book1, book2]) # it returns true if all of the value to iterable is true
print(read_any_book)
print(read_all_books)