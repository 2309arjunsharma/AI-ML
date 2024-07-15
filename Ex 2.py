class Mammal:
    def walk(self):
        print(f"{Mammal}.walk")

class Dog(Mammal):
    def bark(self):
        print("Bark")
    

class Cat(Mammal):
    pass

cat1 = Dog()
cat1.walk()
cat1.bark()
        
