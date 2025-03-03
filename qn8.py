#Problem: Keep asking the user for input until they 
# enter a number between 1 and 10.

while True:
    number = int(input('Enter any number between 1 to 10: '))
    if number>=1 and number<=10:                    #if 1<= number <=10:
        print('Thank you!')
        break
    else:
        print('You have entered a wrong number. Try again')