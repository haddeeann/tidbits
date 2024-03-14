import pandas


def c_to_f(f):
    c = f * 9 / 5 + 32
    return c


data = pandas.read_csv('./weather_data.csv')
monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_F = c_to_f(monday_temp)
print(monday_temp_F)
