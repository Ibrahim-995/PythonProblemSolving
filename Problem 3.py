#3. Write a Python program to display the current date and time.

#Pythone Code:

import datetime
x = datetime.datetime.now()
print (x.strftime("%Y-%m-%d %H:%M:%S"))