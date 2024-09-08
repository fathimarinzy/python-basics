## page creation
from tkinter import *

x = Tk()
x.title("Welcome to Tkinter Window")
x.configure(bg='dark slate grey')

l1 = Label(x, text='Name',bg='light grey',fg='dark slate grey',width=10, height=3, font='Arial 10 bold')
l1.grid(row=1, column=1)
l2 = Label(x, text='Age',bg='light grey',fg='dark slate grey',width=10, height=3, font='Arial 10 bold')
l2.grid(row=2, column=1)
l3 = Label(x, text='Email',bg='light grey',fg='dark slate grey', width=10,height=3, font='Arial 10 bold')
l3.grid(row=3, column=1)

e1 = Entry(x, justify='left',bd=5,bg='white',fg='black')
e1.grid(row=1, column=2)
e2 = Entry(x, justify='left',bd=5,bg='white',fg='black')
e2.grid(row=2, column=2)
e3 = Entry(x, justify='left',bd=5, bg='white',fg='black')
e3.grid(row=3, column=2)
def click():
    l7=Label(x,text='My Details')
    l7.grid(row=5,column=1)
   
    l4 = Label(x, text='Name',bg='light grey',fg='dark slate grey',width=10, height=3, font='Arial 10 bold')
    l4.grid(row=6, column=1)
    x.configure(e1.get())
    l5 = Label(x, text='Age',bg='light grey',fg='dark slate grey',width=10, height=3, font='Arial 10 bold')
    l5.grid(row=7, column=1)
    # x.configure(e2.get())
    l6 = Label(x, text='Email',bg='light grey',fg='dark slate grey', width=10,height=3, font='Arial 10 bold')
    l6.grid(row=8, column=1)
    x.configure(e3.get())
  
def cli():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    


b1 = Button(x, text='Submit',justify='left',bg='medium sea green' ,fg='white',command=click)
b1.grid(row=4,column=1) 
b2 = Button(x, text='Delete',justify='right',bg='medium sea green', fg='white',command=cli)
b2.grid(row=4,column=2) 

print("start")
x.mainloop()
print("stop")
