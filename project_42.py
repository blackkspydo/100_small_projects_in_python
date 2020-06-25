# How to generate random numbers using arrays.
from random import randint
x = 100
array = []
for i in range(x):
    array.append(randint(1, 500))
for i in array:
    print(i, end=' ')
