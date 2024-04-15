#  (c * 9/5) + 32 = f
days_c = {'Monday': 10,
          'Tuesday': 15,
          'Wednesday': 30,
          'Thursday': 40,
          'Friday': 45,
          'Saturday': 50,
          'Sunday': 5}

days_f = {day:(c * 9/5) + 32 for (day, c) in days_c.items()}

print(days_f)
