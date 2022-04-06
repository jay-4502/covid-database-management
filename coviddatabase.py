import sqlite3
import datetime
connection_object= sqlite3.connect('COVID.db')
cursor_object=connection_object.cursor()
cursor_object.execute('DROP TABLE IF EXISTS COVID')

table='''CREATE TABLE COVID
        (AADHAR_No VAECHAR(20) PRIMARY KEY  NOT NULL,
        NAME  VARCHAR(20)  NOT NULL,
        AGE  INT,
        DOSES  INT
        );'''
cursor_object.execute(table)
w=input('aadhar_no: ')
x=input('name: ')
y=input('age: ')
z=input('doses: ')
cursor_object.execute ("""INSERT INTO COVID (aadhar_no,name,age,doses)VALUES(?,?,?,?)""",(w,x,y,z))
connection_object.commit()
print('data inserted into table: ')
data=cursor_object.execute('''SELECT * FROM COVID''')
a=datetime.datetime.now()
print(a)
b=input('enter aadhar_no: ')
try:
    flag=0
    for row in data:
        if row[0]==b:
            print(row)
            flag=1
        if flag==0:
            print("data not found as error occured")
except:
    connection_object.close()















































        