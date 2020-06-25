# How to get maximum and minimum element from array.
from random import randint
x = 20
maximum = 0
minimum = 0
array = []
for i in range(x):
    array.append(randint(1, 500))
for i in array:
    if minimum > i:
        minimum = i
    if maximum < i:
        maximum = i
print(array)
print(f'Minimum element: {minimum}')
print(f'Maximum element: {maximum}')
