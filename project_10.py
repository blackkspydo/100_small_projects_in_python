# How to determine if triangle exists.
a,b,c= input('Enter three sides of a triangle: ').split(',')
a=float(a)
b=float(b)
c=float(c)
if (b+c > a) and (a+c > b) and (b+a > c):
    print('The triangle exists.')
else:
    print("The triangle doesnot exists.")
