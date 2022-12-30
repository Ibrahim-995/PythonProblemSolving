#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# Python Program

x = input("Enter the string: ")
y = int(input("Enter the number of copies: "))

for i in range(y):
    print(x)
    i = i+1
