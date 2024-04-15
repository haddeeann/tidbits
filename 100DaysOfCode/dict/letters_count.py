sentence = input()

words = sentence.split(' ')

count = {word:len(word) for word in words}

print(count)