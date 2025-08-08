import pandas

data = pandas.read_csv(r"100-days-of-coding--Python-\contents\Day 26\nato_phonetic_alphabet.csv")

data_to_dict = {row["letter"]:row["code"] for (index, row) in data.iterrows()}

username = input("Enter a word: ").upper()

nato_list = [data_to_dict[letter] for letter in username]
print(nato_list)