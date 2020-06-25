# How to get factorial using a while loop
number = int(input('Enter the number: '))
x = number - 1
while x != 1:
    number = number * x
    x -= 1
print('Factorial =',number)