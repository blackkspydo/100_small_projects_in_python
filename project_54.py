# How to bubble sort elements in array?
from random import  randint
x = 20
y = []

for i in range(x):
    y.append(randint(1,20))
print(f'Unsorted:{y}')

for i in range(x):
    for j in range(x-i-1):    # double loop to compare 1 element to all
        if y[j] > y[j+1]:
            z = y[j]    # y[j] is assigned in z to use this in latter step
            y[j] = y[j+1]
            y[j+1] = z

print(f'Sorted:{y}')
