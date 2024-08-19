#open(filename,mode)


#to open file
f=open("abc.txt")
f.close()


#to read
f=open("abc.txt","r")
print(f.read())
f.close()
#it gives error if the file is not created
f=open("abd.txt","r")
print(f.read())
f.close()

f=open("abc.txt")
print(f.read(9))
f.close()

f=open("abc.txt")
print(f.readline())
print(f.readline())
f.close()

f=open("abc.txt")
print(f.readlines())
f.close()

# #to write
f=open("abc.txt","w")
print(f.write("hello"))
f.close()

f=open("abcd.txt","w")
print(f.write("hello"))
f.close()
#append
f=open("abc.txt","a")
print(f.write("hai"))
f.close()

f=open("ab.txt","a")
f.write("hai")
f.close()
#in write it will create new file if the file is not
f=open("abd.txt","x")
f.close()


# que
f=open("efg.txt","w")
print(f.write("50\n"))
print(f.write("90\n"))
print(f.write("80\n"))
f.close()
f1=open("efg.txt","r")
print(f1)
v=max(f1)
print("max:",v)
f1.close

# correct ans 
f=open("kgf.txt","w")
print(f.write("50\n"))
print(f.write("90\n"))
print(f.write("80\n"))

f1=open("kgf.txt","r")
p=f1.readlines()
g=[int(i) for i in p]
print(g)
u=max(g)
print(u)


f=open("efg.txt","w")
print(f.write("hai"))

f.close()
f=open("efg.txt","r")
p=f.readlines()
print(p)
a="".join(p)
g=len(a) 
print(g)

# seek and tell
f=open("abc.txt","r")
a=f.seek(5)
print(a)
x=f.read(5)
print(x)
f.close()

f=open("abc.txt","r")
a=f.tell()
print(a)
x=f.read(5)
print(x)
a=f.tell()
print(a)
f.close()

# r is uesd to ignore \n
f=open(r"C:\Users\Lenovo\Downloads\index.html.txt","a")

f.close()


import os
# os.remove("abc.txt")
os.rmdir("txxxtis")

#to delete folder with files
import shutil
shutil.rmtree("hello")

with open("abc.txt","w") as file:
    x=file.write("worked")
    print(x)
file.close()


#que
a=[2,7,11,15]
x=[a.index(i) for i in a if i+i==9]
print(x)
