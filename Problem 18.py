#18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

#Python Program



def number(a,b,c):
    x = a + b + c
    
    if a == b == c :
        return x*3
    
print(number(11,12,13))
print(number(10,10,10))