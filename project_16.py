# How to create a multiplication table using while loop.
x = int(input('Which number multiplication table do you want? '))
y = 0
while y <= 10:
    print(x, 'x', y, '=', x*y)
    y = y+1