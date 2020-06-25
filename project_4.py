# How to check for divisibility of a number?
quotient = int(input("Enter quotient: "))
divisor = int(input("Enter divisor: "))
if quotient % divisor == 0:
    print('The number is perfectly divisible.')
else:
    print('The number is not perfectly divisible.')
