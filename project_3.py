# How to check for greatest of three number.
print('Separate numbers with a comma')
a,b,c = input('Enter any three numbers: ').split(',')
num_list = [int(a),int(b),int(c)]
print(num_list)
greatest_number = max(num_list)
print('The greatest number is',greatest_number)


