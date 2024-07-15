import Calculator1



print("Choose:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponentiation")
choice = int(input("Choose (1/2/3/4/5): "))
if choice==1 or choice==2 or choice==3 or choice==4 or choice==5:
    x = float(input("Enter Number1: "))
    y = float(input("Enter Number2: "))
    if choice == 1:
        print("Answer is", Calculator1.Add(x, y))
    elif choice == 2:
        print("Answer is", Calculator1.Subtract(x, y))
    elif choice == 3:
        print("Answer is", Calculator1.Multiply(x, y))
    elif choice == 4:
        print("Answer is", Calculator1.Divide(x, y))
    else:
        print("Answer is", Calculator1.Exponent(x, y))
else:
    print("Invalid Value")


