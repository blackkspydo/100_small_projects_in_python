# How to create multiplication table using for loop?
x = int(input('Which number multiplication table do you want? '))
for y in range(1,11):
    print(x, 'x', y, '=', x * y)
