import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_list = []
nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Which word would you link to translate to NATO alphabet? ").upper()
split_word = list(user_word)

for letter in split_word:
    nato_list.append(nato_dict[letter])

print(nato_list)
