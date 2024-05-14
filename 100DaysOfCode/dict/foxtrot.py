import pandas

df = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato = {row.letter: row.code for (index, row) in df.iterrows()}


def input_cycle():
    word = input('Enter a word: ')
    try:
        word_list = [nato[letter.upper()] for letter in word]
    except KeyError as e:
        print('You may only enter letters, please try again.\n')
        input_cycle()
    else:
        print(word_list)


input_cycle()
