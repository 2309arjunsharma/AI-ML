phone = input("Phone no.: ")
number_names = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
for p in phone:
    output = output + number_names.get(p, "!!!") + " "
print(output)
