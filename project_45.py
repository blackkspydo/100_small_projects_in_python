# How to get positive number out of negative number.
from random import randint
x = 20
pos = []
neg = []
array = []
for i in range(x):
    array.append(randint(-500, 500))
for i in array:
    if i > 0:
        pos.append(i)
    if i < 0:
        neg.append(i)
print(array)
print(f'Positive elements({len(pos)}): {pos}')
print(f'Negative element({len(neg)}): {neg}')
