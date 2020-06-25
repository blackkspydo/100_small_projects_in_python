# Simple intersection:
list1 = ['3', '4', '5', '6', '7', 's', 'g', 'h', 'j', 'k', 'l']
list2 = ['3', '5', '7', '8', 'f', 'u', 'r', 'h', 's', 'h', 'k']
list3 = list((set(list1) & set(list2)))
print(list3)