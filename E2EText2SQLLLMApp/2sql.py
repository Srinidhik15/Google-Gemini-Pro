# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('student.db') 
  
# Creating a cursor object using the  
# cursor() method --it can insert record,create table etc
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255),MARKS INT);"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''Insert Into STUDENT values('Nidhi','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Santosh','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Harsha','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Ratan','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Abhi','DEVOPS','A',35)''')
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()