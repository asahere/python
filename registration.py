import sqlite3
from tkinter import messagebox                                 
from tkinter import*
con=sqlite3.connect("data.db")
def check_user():
    user=name.get()
    passwd=passwd.get()
    print(user,passwrd)
    cursor.execute(
        "Select * from login where username? and password?",(user,passwd)
    )
    res=cursor.fetchone()
    if res:
        messagebox.showinfo("Success", "Login Success")
    else:
        messagebox.showerror("Error","Login Failed but you are now registered as a new user")
        cursor.execute(
            "insert into login values(?,?)",(user,passwd)
        )
window=Tk()
window.title("Login")
window.minsize(200,200)
name=StringVar()
passwd=StringVar()
lb1=Label(window,Text="Username",fg="red").grid(row=0,coloumn=1)
en=Entry(window,highlightcolor="Orange",highlightthickness=20,textvariable=name).grid(row=1,column=2)

button=Button(
    window,
    text="Register"
    bg="pink"
    fg="black"
    activebackground="purple",
    command=check_user,
).grid(row=2,column=1)
button=Button(
    window,
    text="login",
    bg="pink",
    fg="black",
    activebackground="purple",
    command=check_user,
).grid(row=2,column=2)
con.commit()
window.mainloop()