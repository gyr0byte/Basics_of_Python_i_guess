def hello_func(greeting):
    return f"{greeting} Function."


print(hello_func("Hi"))


def student_info(*args, **kwargs):
    print(args)  # these are like tuples
    print(kwargs)  # these are like dictionaries


course = ["Math", "Art"]
info = {"name": "Gaurav", "age": 19}

student_info(*course, **info)
