fruits = ['apple', 'pear', 'blueberry']


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('pick a diff fruit')
    else:
        print(fruit + 'pie')


make_pie(21)

posts = [
    {
        'likes': 21,
        'comments': 2
    },
    {
        'comments': 1
    }
]

total_likes = 0

for post in posts:
    if 'likes' in post:
        total_likes = total_likes = post['likes']

print(total_likes)
