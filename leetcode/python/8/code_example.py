import re
txt = "1234a"
x = re.search('[a-z]', txt)
target_string = "Abraham Lincoln was born on February 12, 1809,"
# \d to match digits
res = re.search(r'\d{4}', target_string)
# match value
print(res.group())
# Output 1809

# start and end position
print(res.span())
# Output (41, 45)

# start position
print(res.start())
# Output 41

# end position
print(res.end())
# Output 45