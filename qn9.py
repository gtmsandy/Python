#prime number
#1 cannot be considered i.e. num>1 and divisible by its own number
#so we check till (num -1)
num = int(input('Enter a number: '))
is_prime = True

if num>1:
    for i in range (2, num-1):
        if(num%i == 0):
            is_prime=False
            break

print(is_prime)