import random
snumber = random.randint(1, 50)
guess1 = 0
guess2 = 7
name = input("Name: ")
print("Welcome",name,"to Arjun's guessing game! Guess number  between 1-50. You have 7 chances")
while guess1 < guess2:
    guess = int(input("Guess: "))
    if guess == snumber:
        print("You have won. Good Job!")
        break
    if snumber>40 and snumber<=50:
        print("It is between 40 and 50.")
    elif snumber>30 and snumber<=40:
        print("It is between 30 and 40.")
    elif snumber>20 and snumber<=30:
        print("It is between 20 and 30.")
    elif snumber>10 and snumber<=20:
        print("It is between 10 and 20.")
    else:
        print("It is less than 10.")
    guess1 = guess1 + 1
else:
    print("You have failed!",snumber,"was the number")