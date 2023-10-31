import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetics = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetics)

user_words = input("Enter a word: ").upper()
output = [phonetics[letter] for letter in user_words]
print(output)
