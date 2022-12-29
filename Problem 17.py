#17. Write a Python program to test whether a number is within 100 or 1000 or 2000.

#Python Program

x = int(input("Enter the number: "))

if x <= 100:
    print("The number is in range 100")

elif x > 100 and x <= 1000:
    print("The number is in range 1000")
    
elif x > 1000 and x <= 2000:
    print("The number is in range 2000")

else:
    print("Invalid number, try again")