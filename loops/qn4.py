# Given a string, find the first non-repeated character.

new = input('Enter a string: ')

#loop lagaune in new
for char in new:
    print(char)
    if new.count(char) == 1:
        print(f'The non repeated character is {char}')
    