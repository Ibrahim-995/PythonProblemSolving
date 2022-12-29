# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

# Python Program

x = input("Enter the numbers with coma:" )

y = x.split(",")

print(y) 

z = tuple(y)

print(z)