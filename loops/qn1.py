# Calculate the sum of even numbers up to a given number n.

n=int(input('Enter the number of numbers: '))
sum=0

for i in range(n):                          #i lai 1 to n samma input lina dine
    num=int(input(f'Enter {i+1} number: ')) #harek input paxi arko input magxa user sanga
    if num%2==0:                            #if remainder = 0 it is divisible by 2
        sum=num+sum                         #sum=0 ma add gardai jane in loop in num is an even number
print(f'The sum of even numbers is {sum}')