snumber = 7
guessc = 0
guessl = 4
name = input("Name: ")
print("Welcome",name,"to Arjun's guessing game! Guess number  between 0-9.")
while guessc < guessl:
    guess = int(input("Guess: "))
    guessc = guessc + 1
    if guess == snumber:
        print("You have won. Good Job!")
        break
else:
    print("You have failed!")
