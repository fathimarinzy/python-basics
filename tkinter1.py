from tkinter import *
x=Tk()
x.title("welcome to tkinter window ")
# x.geometry("400*400")
x.resizable(True,False)
x.resizable(True,True)
x.resizable(False,True)
# x.resizable(False,False)
# x.attributes("-alpha",0.5)
x.attributes("-topmost",1)

print("start")
x.mainloop()
print("stop")