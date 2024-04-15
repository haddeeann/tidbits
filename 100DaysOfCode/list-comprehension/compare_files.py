with open('./numbers1.txt', 'r') as f:
    file1 = f.read().split('\n')

with open('./numbers2.txt', 'r') as f:
    file2 = f.read().split('\n')

numbers1 = [int(n) for n in file1]
numbers2 = [int(n) for n in file2]

overlap = [n for n in numbers1 if n in numbers2]

print(overlap)