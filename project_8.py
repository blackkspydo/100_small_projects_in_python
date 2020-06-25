# How to calculate mass, density and volume?
quantity = input('What do you wanna calculate?(mass,volume.density)   ')

if quantity.lower() == 'mass':
    volume = float(input('Enter volume: '))
    density = float(input('Enter density: '))
    mass = round(density*volume, 2)
    print('Mass is', mass, 'kg')

elif quantity.lower() == 'volume':
    mass = float(input("Enter mass: "))
    density = float(input('Enter density: '))
    volume = round(mass/density, 2)
    print('Volume is', volume, 'cubic meter')

elif quantity.lower() == 'density':
    mass = float(input("Enter mass: "))
    volume = float(input('Enter volume: '))
    density = round(mass / volume, 2)
    print('Density is', density, 'kg/m^3')
