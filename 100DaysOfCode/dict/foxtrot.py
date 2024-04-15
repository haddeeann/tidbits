import pandas

df = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato = {row.letter:row.code for (index, row) in df.iterrows()}

word = input()
word_list = [nato[letter.upper()] for letter in word]
print(word_list)