# How to find intersection of two lists.
list1 = ['3', '4', '5', '6', '7', 's', 'g', 'h', 'j', 'k', 'l']
list2 = ['3', '5', '7', '8', 'f', 'u', 'r', 'h', 's', 'h', 'k']
list3 = []

for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
            break
print(f'List 1:{list1}\nList 2: {list2}\nList of intersection :{list3}')

