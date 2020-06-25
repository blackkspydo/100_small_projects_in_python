# How to check if the number is prime.
import numpy as np
num = int(input('Enter any number: '))

if num < 0:
    print(f'{num} is negative number.')
    quit()


def prime(n):
    i = 1
    j = 0
    while i != n + 1:
        if n % i == 0:
            j += 1
        i += 1
    if j == 2:
        print(f'{int(n)} is prime number.')
    else:
        print(f'{int(n)} is not a prime number.')


prime(num)

