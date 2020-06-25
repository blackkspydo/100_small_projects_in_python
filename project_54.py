# How to bubble sort elements in array?
from random import randint

x = 20
array = []

for i in range(x):
    array.append(randint(1, 20))
print(f'Unsorted:{array}')

for i in range(x):
    for j in range(x - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(f'Sorted:{array}')
