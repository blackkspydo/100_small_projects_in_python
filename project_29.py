# How to reverse number?
num = int(input('Enter any number:'))
rev = ''
while num != 0:
    rem = num % 10
    num = num // 10
    rev += str(rem)
print(rev)
