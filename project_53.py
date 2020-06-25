# How to get frequently occurring element from a list?
from random import random
list_1 = [int(random()*5) for i in range(20)]
print(list_1)

set_list = set(list_1)

highest = None
frequent = 0
for item in set_list:
    freq = list_1.count(item)
    if freq > frequent:
        frequent = freq
        highest = item

print(highest)
