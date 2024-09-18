# from tkinter import messagebox,filedialog
# from tkinter import *

# root=Tk()

# def display():
#     messagebox.showinfo('information','login success')
#     messagebox.showwarning('warning','it only conssits of alphabets and space')
#     messagebox.showerror('error','login error')
#     messagebox.askokcancel('ask question','are you sure')
#     messagebox.askyesno('ask question','are you sure')
#     messagebox.askretrycancel('ask question','are you sure')
#     x=messagebox.askquestion('ask question','are you sure')
#     print(x)
#     if x=="yes":
#         print("yes clicked")
#     else:
#         print("no clicked")



# b1 = Button(root, text='clear', width=3, height=2, bg='medium sea green', fg='white', command=display)
# b1.grid(row=2, column=1)


# root.mainloop()

##que

# from tkinter import messagebox,filedialog
# from tkinter import *

# root=Tk()

# def success():
#      messagebox.showinfo('information','login success')
# def cancel():
#     messagebox.showinfo('information','login cancelled')
# def display():
#     x=messagebox.askyesno("ask question",'are you sure')
#     if x:
#         success()     
#     else:
#         cancel()
       

# b1 = Button(root, text='submit', width=3, height=2, bg='medium sea green', fg='white', command=display)
# b1.grid(row=2, column=1)

# root.mainloop()

##que
# from tkinter import messagebox,filedialog
# from tkinter import *

# root=Tk()
# l=Label(root,text='clicked 0 times')
# l.pack()
# count=0
# def click():
#     global count
#     count+=1
#     l.configure(text=f"clicked{count}times")


# b1 = Button(root, text='submit', width=3, height=2, bg='medium sea green', fg='white', command=click)
# b1.pack()
# root.mainloop()


##radiobutton
# from tkinter import *

# root=Tk()

# s=IntVar()
# r1=Radiobutton(root,text='female',variable=s,value=1)
# r1.grid(row=1,column=1)
# r2=Radiobutton(root,text='male',variable=s,value=2)
# r2.grid(row=2,column=1)
# r3=Radiobutton(root,text='others',variable=s,value=3)
# r3.grid(row=3,column=1)

# ss=IntVar()
# r4=Radiobutton(root,text='python',variable=ss,value=1)
# r4.grid(row=4,column=1)
# r5=Radiobutton(root,text='java',variable=ss,value=2)
# r5.grid(row=5,column=1)
# r6=Radiobutton(root,text='php',variable=ss,value=3)
# r6.grid(row=6,column=1)

# root.mainloop()


##checkbutton

from tkinter import *
root=Tk()


c1=Checkbutton(root,text='english').grid(row=1,column=1)
c2=Checkbutton(root,text='hindi').grid(row=2,column=1)
c3=Checkbutton(root,text='malayalm').grid(row=3,column=1)


root.mainloop()
