class Animal:
    def walk(self):
        print("Walking...")


class Dog(Animal):  # dog class is inherting from the animal class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"Woof!")


roger = Dog("Roger", 8)
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()