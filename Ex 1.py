class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("Long John Silver")
john.talk()

bob = Person("Bob Smith")
bob.talk()
