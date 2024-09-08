from tkinter import *
x=Tk()
x.title("tkinter")
c=IntVar()
e1 = Entry(x, bd=5,justify='center',bg='white',fg='black',textvariable=c)
e1.grid(row=1,column=1,columnspan=4)

val=''
def click(a):
    # print(a)
    c.set(a)
   
    



    





b1 = Button(x, text='clear',width=3,height=2,bg='medium sea green' ,fg='white')
b1.grid(row=2,column=1)
b2 = Button(x, text=7,width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(7))
b2.grid(row=3,column=1)
b3= Button(x, text='4',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(4))
b3.grid(row=4,column=1)
b4 = Button(x, text='1',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(1))
b4.grid(row=5,column=1)
b5 = Button(x, text='+/-',width=3,height=2,bg='medium sea green' ,fg='white')
b5.grid(row=6,column=1)

b6 = Button(x, text='<',width=3,height=2,bg='medium sea green' ,fg='white')
b6.grid(row=2,column=2)
b7= Button(x, text='8',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(8))
b7.grid(row=3,column=2)
b8 = Button(x, text='5',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(5))
b8.grid(row=4,column=2)
b9 = Button(x, text='2',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(2))
b9.grid(row=5,column=2)
b10 = Button(x, text='0',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(0))
b10.grid(row=6,column=2)

b11 = Button(x, text='%',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click('%'))
b11.grid(row=2,column=3)
b12 = Button(x, text='9',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(9))
b12.grid(row=3,column=3)
b13 = Button(x, text='6',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(6))
b13.grid(row=4,column=3)
b14 = Button(x, text='3',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click(3))
b14.grid(row=5,column=3)
b15 = Button(x, text='.',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click('.'))
b15.grid(row=6,column=3)

b16 = Button(x, text='/',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click('/'))
b16.grid(row=2,column=4)
b17 = Button(x, text='*',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click('*'))
b17.grid(row=3,column=4)
b18 = Button(x, text='-',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click("-"))
b18.grid(row=4,column=4)
b19 = Button(x, text='+',width=3,height=2,bg='medium sea green' ,fg='white',command=lambda:click("+"))
b19.grid(row=5,column=4)
b20 = Button(x, text='=',width=3,height=2,bg='medium sea green' ,fg='white')
b20.grid(row=6,column=4)





print("start")
x.mainloop()
print("stop")