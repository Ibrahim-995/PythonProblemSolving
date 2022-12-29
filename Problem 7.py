#7. Write a Python program to accept a filename from the user and print the extension of that.

#Python Program

x = input("Enter file name:" )
y = x.split(".")
print(y[1])