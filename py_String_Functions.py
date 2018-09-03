# play more with the python library
phrase = "Frank Fang"

# change all letters to lower case
print(phrase.lower())

# change all letters to upper case
print(phrase.upper())

# check is all letters in upper or lower case
print("Is all letters in upper case: " + phrase.isupper().__str__())
print("Is all letters in lower case: " + phrase.islower().__str__())

# play more function
print("Is all letters in upper case: " + phrase.upper().isupper().__str__())

# get the length of the string
print(len(phrase))

# get the #th letter, string index start from 0
print(phrase[3])

# get the position of wanted letter in the string
print(phrase.index("g"))

# replace substring in a string
print(phrase.replace("Frank", "Zhang"))

