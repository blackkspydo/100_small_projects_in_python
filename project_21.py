# How to get sum and product of digits?
d_sum = 0
d_product = 1
number = int(input('Enter digits: '))
while number != 0:
    digit = number % 10
    d_sum += digit
    d_product *= digit
    number = number//10
print('d_sum:', d_sum, '\nd_product:', d_product)