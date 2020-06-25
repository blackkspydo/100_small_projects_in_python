# How to x for leap year?
year = int(input('Enter year:'))
x = year % 4
next_year = year - x+4
if x == 0:
    print(year, 'is a leap year.')
else:
    print('No,', year, 'is not a leap year. The upcoming leap year is', next_year, '.')
