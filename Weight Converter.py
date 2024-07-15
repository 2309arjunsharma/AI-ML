weight = float(input("Enter your Weight: "))
ask = input("(L)bs or (K)g: ")
ask = ask.upper()
if ask == "L":
    weight = weight*0.45
    print("Weight is",weight,"kgs")
else:
    weight = weight/0.45
    print("Weight is",weight,"lbs")


