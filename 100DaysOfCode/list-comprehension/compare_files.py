with open('./numbers1.txt', 'r') as f:
    numbers1 = f.readlines()

with open('./numbers2.txt', 'r') as f:
    numbers2 = f.readlines()

overlap = [int(n) for n in numbers1 if n in numbers2]

print(overlap)