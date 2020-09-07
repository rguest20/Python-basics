def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiu":
            if letter.isupper():
                translation = translation + "O"
            else:
                translation = translation + "o"
        else:
            translation = translation + letter
    return translation


number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for column in row:
        print(column)

phrase1 = input("Input a fun phrase: ")
print(translate(phrase1))
