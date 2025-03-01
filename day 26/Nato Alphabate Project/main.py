import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
#  {"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = (input("Enter a word : ")).upper()

nato_list = [phonetic_dict[letter] for letter in word]
print(nato_list)
