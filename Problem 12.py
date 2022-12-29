#12. Write a Python program to print the calendar of a given month and year.

#Python Program

import calendar
   
yy = int(input("Enter the year like '2014': "))
mm = int(input("Enter the number of month like 3 or 4: "))
   

print(calendar.month(yy, mm))