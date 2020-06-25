# How to get even and odd numbers from array.
from random import randint
x = 20
even = []
odd = []
array = []
for i in range(x):
    array.append(randint(1, 500))
for i in array:
    if i % 2 == 0:
       even.append(i)
    else:
        odd.append(i)
print(array)
print(f'Even numbers:{len(even)} {even}')
print(f'Odd numbers:{len(odd)} {odd}')