import sqlite3
from tkinter import messagebox                                 
from tkinter import*
con=sqlite3.connect("data.db")
#con.execute("CREATE TABLE register(username varchar(20),password varchar(20))")
def r():
    w1=Tk()
    def db():
        u=e.get()
        p=e2.get()
        con.execute("INSERT INTO register values(?,?)",(u,p))
        con.commit()
        messagebox.showinfo("register","success")
        w1.destroy()
    l1=Label(w1,text="username")
    e=Entry(w1,width=20)
    l2=Label(w1,text="password")
    e2=Entry(w1,width=20)
    l1.grid()
    e.grid()
    l2.grid()
    e2.grid()
    reg2=Button(w1,text="create",command=db)
    reg2.grid(row=3,column=1)
    mainloop()

def l():
    w2=Tk()
    def f():
        u=e.get()
        p=e2.get()
        k=con.execute("SELECT * FROM register where username=? and password=?",(u,p))
        for i in k:
            messagebox.showinfo("login","success")
            break
        else:
            messagebox.showinfo("login","invalid")
        w2.destroy()
    l1=Label(w2,text="username")
    e=Entry(w2,width=20)
    l2=Label(w2,text="password")
    e2=Entry(w2,width=20)
    l1.grid()
    e.grid()
    l2.grid()
    e2.grid()
    lg2=Button(w2,text="Login",command=f)
    lg2.grid()
    mainloop()

w=Tk()
reg=Button(w,text="Register",command=r)
lg=Button(w,text="Login",command=l)
reg.grid()
lg.grid()
mainloop()



    