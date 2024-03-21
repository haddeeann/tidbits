import pandas


def c_to_f(f):
    c = f * 9 / 5 + 32
    return c


data = pandas.read_csv('./weather_data.csv')
print(data)
monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_F = c_to_f(monday_temp)

scores = {
    "person": ["Janet", "matt"],
    "score": [56, 25],
    "day": ['monday', 'tuesday']
}

new_data = pandas.DataFrame(scores)
print(new_data)
new_data.to_csv('new_data.csv')
