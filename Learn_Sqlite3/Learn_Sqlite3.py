# pip install db-sqlite3

import sqlite3

# Create connection
con = sqlite3.connect("demo_dataBase.db")
print("Create connection")


# Create Table
con.execute("CREATE TABLE IF NOT EXISTS pythonjuly('name', 'email', 'ph')")
print("Create Table")

# insert records
con.execute('''INSERT INTO pythonjuly('name', 'email', 'ph') 
              VALUES('Balaji', 'balaji@gmail.com', 23145)''')
con.commit()
print("inserted records")

# read all data
data = con.execute("SELECT * FROM pythonjuly")
print(type(data))
for i in data:
    print(i)
print("reading all data")


# update the value


# close
con.close()
print("closed")