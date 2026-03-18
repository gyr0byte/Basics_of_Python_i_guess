class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __gt__(self, other):
        return True if self.age > other.age else False
    
German = Dog("Shepherd", 4)
Japanese = Dog("Jo", 3)

print(German > Japanese)