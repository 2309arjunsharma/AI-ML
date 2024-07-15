import random
class Dice():
    def roll(self):
        first = random.randint(1,6)
        return first

dice = Dice()
print(dice.roll())