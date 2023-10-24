import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nata_alphabet = {row.letter: row.code for (index, row) in nato_data.iterrows()}

phonetic_code = []

loop = True
while loop:
    try:
        word = input("Enter a word: ").upper()
        phonetic_code = [nata_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letter in the alphabet please.")
    else:
        print(phonetic_code)
        loop = False

