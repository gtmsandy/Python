# 1. write a function to calculate and return the square of a number

# def square(number): #number is a parameter not argument (they are placeholder)
#     return number**2
# print(square(18))




# 2. Create a function that takes two numbers as parameters and returns their sum

# def sum(a,b):
#     return a+b
# print(sum(3,99))




# 3. Write a function multiply that multiplies two numbers
        # but can also accept and multiply strings.
# def mult(a,b):
#         return a*b
# print (mult(7,'a'))



# 4. Create a function that returns both the area 
# and circumference of a circle given its radius.

# import math

# def circle_stat(radius):
#         area = math.pi * radius**2
#         circumference = 2 * math.pi * radius
#         return area,circumference

# a,c=circle_stat(5)
# print(f'Area is {a:.2f} and circumference is {c:.2f}')




# 5. Write a function that greets a user. 
# If no narne is provided, it should greet with a default name.

# def greet(name="User"):
#         return "Hello, " + name + "!"

# print(greet("Sandy"))
# print(greet())




#  6. a lambda function to compute the cube of a number.

# cube = lambda x: x**3
# print(cube(3))



# 7. Write a function that takes variable nurnber of arguments 
# and returns their sum using 'args' function

# def sum_all(*args):
#         print(*args)
#         print(args)
#         return sum(args)

# print(sum_all(1,2,3,4,5))



# 8. Create function that accepts number of keyword arguments 
# and prints them in the format [Function with **kwargs]


# def print_kwargs(**kwargs):
#         for key, value in kwargs.items():
#                 print(f"{key}: {value}")

# print_kwargs(name="shaktiman", power="laser")
# print_kwargs(name="shaktiman")
# print_kwargs(name="shaktiman", power="laser", enemy="XYZ")



#  9. Problem: Write a generator function that yields even numbers 
# up to a specified limit. (generator function with yield)

# def even_gen(limit):
#         for i in range(2,limit+1,2):
#                 yield i

# for num in even_gen(10):
#         print (num)







# 10. Create a recursive function to calculate the factorial of a number.
# recursive function

def factorial(n):
        if n==0:
                return 1
        else:
                return n*factorial(n-1)

print(factorial(0))