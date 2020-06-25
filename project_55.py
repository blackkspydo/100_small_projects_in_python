# How to bubble sort elements in array?
from random import randint
def minimum(array):
    minimum = 0
    for i in array:
        if minimum > i:
            minimum = i
    return minimum

x = 10
array = []
for i in range(x):
    array.append(randint(1,20))
print(f'Unsorted:{array}')

for i in range(x):
    for j in range(x-i):
        m = minimum(array[i:])
        k = array[j]
        array[j] = array[i]
        array[i] = k
print(array)
