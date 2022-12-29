#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_st_date = (11, 12, 2014)

exam_st_date = (11, 12, 2014)
x = list(exam_st_date)

y = str(x)

print(y[1]+y[2]+"/"+y[5]+y[6]+"/"+y[9]+y[10]+y[11]+y[12])

