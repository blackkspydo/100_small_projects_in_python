# How to find longest word in a string?
string = input('Enter any string: ')
i = 0
j = 100000
word = string.split(' ')
for elem in word:
    if i < len(elem):
        longest_string = elem
        i = len(elem)
    if j > len(elem):
        smallest_string = elem
        j = len(elem)

print('\nSmallest string:',smallest_string)
print('Longest string:',longest_string)