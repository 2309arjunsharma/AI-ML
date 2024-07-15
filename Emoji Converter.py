message = input(">")
words = message.split(' ')
emojis = {":)": "😃",
    ":(": "😒"}
ou = ""
for word in words:
    ou = ou + emojis.get(word, word) + " "
print(ou)
