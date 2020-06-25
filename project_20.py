# Number of digits in an Integers.
count = 0
num = int(input('Enter any number: '))
while num > 0:
    num = num // 10
    count += 1
print('Number of digits:', count)