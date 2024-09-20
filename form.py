from tkinter import *
import re
x=Tk()
x.title("tkinter")

f1=Frame(x,highlightbackground='white',highlightthickness=5)
f1.grid(row=0,column=0,ipadx=100,ipady=100,padx=40,pady=40)

l1=Label(f1,text='Name',width=10,height=3)
l1.grid(row=1,column=1)
e1=Entry(f1,justify='left')
e1.grid(row=1,column=2)


l2=Label(f1,text='Phone Number')
l2.grid(row=2,column=1)
e2=Entry(f1,justify='left')
e2.grid(row=2,column=2)


l3=Label(f1,text='Email',width=10,height=3)
l3.grid(row=3,column=1)
e3=Entry(f1,justify='left')
e3.grid(row=3,column=2)


l4=Label(f1,text='Password',width=10,height=3)
l4.grid(row=4,column=1)
e4=Entry(f1,justify='left')
e4.grid(row=4,column=2)

l5=Label(f1,text='Confirm Password')
l5.grid(row=5,column=1)
e5=Entry(f1,justify='left')
e5.grid(row=5,column=2)




def click():
  name=e1.get()
  phone=e2.get()
  email=e3.get()
  password=e4.get() 
  confirmpassword = e5.get()
  x1=re.findall(r"\b\w+\b",name)
  y=re.findall(r"\b\d{10}\b",phone)  
  z=re.findall(r"\b\w+@\w+\.\w+\b",email)
  # v=re.findall(r"\b")
  print(x1)
  print(y)
  print(z)


b1=Button(f1,text='submit',command=click)
b1.grid(row=6,column=2,columnspan=2)

x.mainloop()