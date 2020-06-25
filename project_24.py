# How to calculate number of odd and even digits in a number.
number = int(input('Enter any number: '))
even = 0
odd = 0
while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number // 10

print('Even digits =',even,'\nodd digits =',odd)
