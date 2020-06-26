# How to selection sort elements in array?
from random import randint

x = 20
array = []

for i in range(20):
    array.append(randint(1, 20))
print(f'Unsorted:{array}')

j = x-1
while j != 0:
    k = 0
    for i in range(1,j+1):
        if array[i] > array[k]:
            k = i
    array[k], array[j] = array[j], array[k]
    j -= 1
print(f'Sorted array:{array}')