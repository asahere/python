import sqlite3
con=sqlite3.connect("data.db")
print("connection established")
#con.execute("CREATE TABLE student (name varchar(20),rollno int,place varchar(30))")
#con.execute("INSERT INTO student values('Lex',22,'Kattanam')")
x=con.execute("SELECT * FROM student")
for i in x:
    print(i)
con.commit()
con.close()