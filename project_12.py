# How to check if a point belongs to a circle?
import math
try:
    x, y = [float(s) for s in input('Enter points: ').split(',')]
    h, k = [float(s) for s in input('Enter centre point: ').split(',')]
    r = float(input('Enter radius of circle: '))

    check = math.sqrt((x - h) ** 2 + (y - k) ** 2)
    if r == check:
        print('The point lies at circumference of a circle.')
    elif r > check:
        print('The point lies inside circle.')
    elif r < check:
        print('The point lies outside circle')
except:
    print('Input valid data only.(separate points with comma)')
