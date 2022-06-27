import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_list = []
nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}

user_word = input("Which word would you link to translate to NATO alphabet? ").upper()
split_word = list(user_word)

for letter in split_word:
    nato_list.append(nato_dict[letter])

print(nato_list)
