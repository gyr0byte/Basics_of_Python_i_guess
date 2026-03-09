class Person:
    name = "Gaurav"
    occupation = "God"
    networth = 100
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
a.info()