#19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged.

# Python Program

#x ="Is there anyone?"
x = "there anyone?"
z = "Is"

if x[0]+x[1] == z :
    print(x)
else :
    print(z+' '+x)
