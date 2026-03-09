def count():
    count = 0
    
    def increment():
        nonlocal count # to access the nonlocal variable we use count
        count = count + 1
        print(count)
    increment()

count()