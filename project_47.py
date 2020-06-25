# How to replace list items witn -1, 0, -1.
from random import randint
x = 20
array = []
for i in range(x):
    array.append(randint(-20, 20))
print(array)
for i in range(len(array)):
    if array[i] > 0:
        array[i] = 1
    elif array[i] < 0:
        array[i] = -1
    else:
        array[i] = 0
print(array)
