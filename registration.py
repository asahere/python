import sqlite3
con=sqlite3.connect("data.db")
print("Connection Established")
con.execute("CREATE TABLE employee(id int,name varchar(20),password varchar(20))")
con.execute("INSERT INTO employee values(1,'Alice@gmail.com','Alice@123')")

for i in x:
    print(i)
con.commit()
con.close()