# Determine if a fruit is ripe, overripe, or unripe based on its color. 
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input('Enter the name of the fruit ')


if fruit != 'Banana':
    print('Sorry, we do not have the info for this fruit! ')
    exit()

color = input('Enter the color of the fruit ')

if color not in ['Green','Yellow','Brown']:
    print('Invalid color')
    exit()

if fruit == 'Banana':
    if color == 'Green':
        print('Unripe')
    elif color == 'Yellow':
        print('Ripe')
    elif color == 'Brown':
        print('Overripe')
