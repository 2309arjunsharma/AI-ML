import random

for i in range(3):
    print(random.random(),"\n")

for i in range(3):
    print(random.randint(10, 20),"\n")


members = ['Arjun', 'Yajas', 'Ambar', 'Avani', 'Raghav']
leader = random.choice(members)
print("The leader is",leader,"\n")

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

dice = Dice()
print(dice.roll(),"\n")
    
