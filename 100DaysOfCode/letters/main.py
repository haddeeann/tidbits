with open('./names/invited_names.txt', mode='r') as file:
    names = file.read()
    name_list = names.split('\n')

with open('./starting_letter.txt', mode='r') as file:
    letter_contents = file.read()
    print(letter_contents)

for name in name_list:
    new_letter = letter_contents.replace('[name]', name)
    print(new_letter)
    file_name = f"letter_to_{name}.txt"
    with open(f"./ready/{file_name}", mode='w') as f:
        f.write(new_letter)

