# How to calculate the sum of N elements of series?
# 1 + x^2/2 + x^3/3 + … x^n/n
x = int(input('Enter the value of x: '))
t = int(input('Enter the term number: '))
sum1 = 0
for i in range(1, t+1):  # because we start from first term
    sum1 = sum1 + ((x**i)/i)
print('Sum of series up to', t, 'term is', round(sum1, 2))