# How to extract integers used in a string?
string = input('Enter any string:')
integers = [int(i) for i in string.split() if i.isdigit()]
print('Integers:', integers)
