def hello(name):
    if not name:
        return "There is no name"
    return f"Hello {name}"

print(hello(""))
print(hello("Gaurav"))