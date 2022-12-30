# 16. Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

#Python Program

def value(n):
  x = 17 - n
  if x <= 17 :
        return x*2
  else:
      return x
      
print(value(20))
print(value(10))
