# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input('Enter the age of the person: '))
day = input('Enter the day: ')

price = 12 if age>=18 else 8

if day == "Wednesday":
    price = price - 2
else:
    price = price
print(f'The price is {price}')