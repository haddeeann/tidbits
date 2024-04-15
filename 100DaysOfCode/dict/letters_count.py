sentence = input()

count = {word:len(word) for word in sentence.split(' ')}

print(count)