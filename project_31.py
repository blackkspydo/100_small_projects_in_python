# How to get the value of fibonacci element?
element = int(input('Enter the element '))
n1, n2 = 0, 1
i = 0
if element < 0:
    print('Please enter positive integer only!')
elif element == 1:
    print(f"This Fibonacci sequence has {element} element", ":", n1)

else:
    while i != element - 1:
        n = n1 + n2
        n1 = n2
        n2 = n
        i += 1
print(f'The fibonacci value of element {element} is', n2)
