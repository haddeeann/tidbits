import math

loop = "stringloop"

left = math.floor(len(loop) / 2)
right = left + 1

while left >= 0 or right < len(loop):
    if left >= 0:
        print(loop[left])
    if right < len(loop):
        print(loop[right])
    left -= 1
    right += 1
