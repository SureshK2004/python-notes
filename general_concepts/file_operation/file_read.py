import csv
import os.path
s=os.path.isfile('student_out.csv')
print(s)
if s:
    print('file_exists')
    with open("student_out.csv",'r',newline='')as file:#filename,filemode,newline
        reader=csv.reader(file)# in reader mode we can reader
        for a in reader:
            print(a)
else:
    print('file does not exists')

