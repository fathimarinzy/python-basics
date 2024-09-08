from tkinter import *


x = Tk()
x.title("Welcome to Tkinter Window")
x.configure(bg='dark slate grey')


l1 = Label(x, text='Name', bg='light grey', fg='dark slate grey', width=10, height=3, font='Arial 10 bold')
l1.grid(row=1, column=1)
l2 = Label(x, text='Age', bg='light grey', fg='dark slate grey', width=10, height=3, font='Arial 10 bold')
l2.grid(row=2, column=1)
l3 = Label(x, text='Email', bg='light grey', fg='dark slate grey', width=10, height=3, font='Arial 10 bold')
l3.grid(row=3, column=1)

e1 = Entry(x, justify='left', bd=5, bg='white', fg='black')
e1.grid(row=1, column=2)
e2 = Entry(x, justify='left', bd=5, bg='white', fg='black')
e2.grid(row=2, column=2)
e3 = Entry(x, justify='left', bd=5, bg='white', fg='black')
e3.grid(row=3, column=2)

def click():
    global l4 ,l5 ,l6, l7

    l7 = Label(x, text='My Details', bg='dark slate grey', fg='white', font='Arial 12 bold')
    l7.grid(row=5, column=1, columnspan=2)

    l4 = Label(x, text=f'Name: {e1.get()}', bg='light grey', fg='dark slate grey', width=30, height=3, font='Arial 10')
    l4.grid(row=6, column=1, columnspan=2)

    l5 = Label(x, text=f'Age: {e2.get()}', bg='light grey', fg='dark slate grey', width=30, height=3, font='Arial 10')
    l5.grid(row=7, column=1, columnspan=2)

    l6 = Label(x, text=f'Email: {e3.get()}', bg='light grey', fg='dark slate grey', width=30, height=3, font='Arial 10')
    l6.grid(row=8, column=1, columnspan=2)


def cli():
    global l4 ,l5 ,l6, l7
    l4.destroy()
    l5.destroy()
    l6.destroy()
    l7.destroy()
    # e1.destroy()
    # e2.destroy()
    # e3.destroy()


b1 = Button(x, text='Submit', justify='left', bg='medium sea green', fg='white', command=click)
b1.grid(row=4, column=1)

b2 = Button(x, text='Delete', justify='right', bg='medium sea green', fg='white', command=cli)
b2.grid(row=4, column=2)

print("start")
x.mainloop()
print("stop")
