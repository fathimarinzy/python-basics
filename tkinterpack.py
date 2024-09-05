# from tkinter import *
# x=Tk()
# x.title("tkinter")


# l1=Label(x,text='name')
# l1.pack()
# l2=Label(x,text='name')
# l2.pack()
# l3=Label(x,text='name')
# l3.pack()
# l4=Label(x,text='name')
# l4.pack()
# l5=Label(x,text='name')
# l5.pack()
# l6=Label(x,text='name')
# l6.pack()
# l7=Label(x,text='name')
# l7.pack()
# l8=Label(x,text='name')
# l8.pack()

# print("start")
# x.mainloop()
# print("stop")


from tkinter import *
x=Tk()
x.title("tkinter")



l1=Label(x,text='First number')
l1.pack()

a=IntVar
e1 = Entry(x, justify='left',bd=5,bg='white',fg='black',textvariable=a)
e1.pack()

l2=Label(x,text='Second number')
l2.pack()
b=IntVar()
e2 = Entry(x, justify='left',bd=5,bg='white',fg='black',textvariable=b)
e2.pack()
l3=Label(x,text='Result')
l3.pack()
c=IntVar
e3 = Entry(x, justify='left',bd=5,bg='white',fg='black',textvariable=c)
e3.pack()

def click():
   
    sum=a+b
    c.get(sum)


b1 = Button(x, text='FIND SUM',justify='left',bg='medium sea green' ,fg='white',command=click)
b1.pack()
print("start")
x.mainloop()
print("stop")