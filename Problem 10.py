#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Python program

x = int(input("Enter a number: "))
y = int(str(x)+str(x))
z = int(str(x)+str(y))

print(x + y + z)