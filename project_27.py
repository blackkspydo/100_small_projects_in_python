# How to create Fibonacci sequence?
lim = int(input('Enter the limit: '))
seq = []
n1, n2 = 0, 1
i = 0
if lim < 0:
    print('Please enter positive integer only!')
elif lim == 1:
    print(f"This Fibonacci sequence has {lim} element", ":", n1)

else:
    seq.append(n2)
    while i != lim - 1:

        n = n1 + n2
        n1 = n2
        n2 = n

        seq.append(n)
        i += 1
print(f'The fibonacci sequence of limit {lim} :', seq)
