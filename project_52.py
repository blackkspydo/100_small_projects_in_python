# Longest ordered sequence in ascending order.
from random import random
num = 20
items = [0] * num

for i in range(num):
    items[i] = int(random() * 50)
print(items)

maxi = 1
my_length = 1
my_code = 0

for i in range(1, num):
    if items[i] > items[i - 1]:
        my_length += 1
    else:
        if my_length > maxi:
            maxi = my_length
            my_code = i
        my_length = 1
print("The maximum length = ", maxi)
print("The ordered values are = ", items[my_code - maxi: my_code])
