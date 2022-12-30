# 16. Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

#Python Program

def value(n):
  x = 17 - n
  if n <= 17 :
        return x
  else:
      return x * 2
      
print(value(30))
print(value(15))
