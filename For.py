def caesar_shift():
    input_word = input("Pick a word to encrypt: ")
    final_word = []
    for letter in input_word:
        cypher = (ord(letter) + 2)
        final_word.append(chr(cypher))
    print("Caesar shift output = " + "".join(final_word))


caesar_shift()

friends = ["Jim", "Shaun", "Guy"]
for index in range(5):
    if index == 0:
        print(str(index) + "!")
    else:
        print("not first")
