# How to get HCF?
n1, n2 = [int(i) for i in input('Enter any two numbers: ').split(',')]
i = 1
c_factor = 0
while i != n1+1:
    if (n1 % i == 0) and (n2 % i == 0):
        if i >= c_factor:
            c_factor = i
    i += 1
print(c_factor)
