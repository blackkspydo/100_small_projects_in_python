# How to find quadrant of a point?
x,y = input('Enter the point: ').split(',')
x=float(x)
y=float(y)
if x>0 and y>0:
    print('This is first quadrant.')
elif x<0 and y>0:
    print('This is second quadrant.')
elif x<0 and y<0:
    print('This is third quadrant.')
elif x>0 and y<0:
    print('This is fourth quadrant')
