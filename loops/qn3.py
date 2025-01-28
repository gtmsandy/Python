# Reverse a string using a loop.
word = input('Enter a word: ')
rev_string = ""  #reverse string lai empty rakheko

for char in word:               #scanning each character in the word
    rev_string=char+rev_string  #harek character lai rev_string ma rakhdai jane

print(f'The reversed string is {rev_string}')