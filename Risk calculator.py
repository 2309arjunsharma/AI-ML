try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print("Age is",age,", Income is",income,", Risk is",risk)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value")
