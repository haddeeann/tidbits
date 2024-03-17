import pandas
data = pandas.read_csv('./squirrel_data.csv')

gray = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')

