# x=(1,2,3,4,5)
# print(type(x))
# print(len(x))
# y=("python","java","php")
# print(y)
# z=("hai",4,5,"hello",True)
# print(z)
# s=("welcome","python")
# print(type(s))
# s=(10,)
# print(type(s))
# p=(True,False)
# print(type(p))
# z=("hai",4,5,"hello",True,4,5)
# print(z[0])
# print(z[-1])
# print(z[1:4])
# print(z[-4:-1])
# print(z[::-1])
# print(dir(z))
# print(z.index(4))
# print(z.count(4))


z=("hai",4,5,"hello",True,4,5)
# for i in z:
#     print(i)
# for i in range(len(z)):
#     print(z[i])
# for i in range(len(z)):
#     print(i)

# i=0
# while i<len(z):
#     print(z[i])
#     i+=1



# x=("python","php","java","dotnet")
# y=list(x)
# print(y)
# y[0]="Apple"
# print(y)
# del y[2]
# print(y)
# z=tuple(y)
# print(z)


# #reverse of a tuple
# a=(10,20,30,50)
# print(a[::-1])

# #find the value 20 from the tuple
# b=("orange",[10,20,30],(5,15,25))
# c=b[1][1]
# print(c)

# #create a tuple with single item 50
# a=(50,)
# print(type(a))

# #modify the tuple

# d=(11,[22,33],44,55)
# d[1][0]=222
# print(d)

# #check if all the items in tuple are same
# f=(45,45,45,45)

# a=0
# for i in f:
#     if i==45:
#        a+=1
#     else:
#         print("not same")
# if a==len(f):
#     print("all are same")    
    
# #another method
# print(f.count(f[0])==len(f))


# #count the no of occurence of item of 50 from a tuple
# tup=(50,10,60,70,50)
# print(tup.count(50))

# t1=(10,20,30,40,50)
# t2=(100,200,300,400,500,10)
# print(t1+t2)
# x=t1+t2
# print(x)
# t1+=t2
# print(t1)
# print(t1*3)
# print(100 in t2)


# #packing and unpacking
# course=("python","java","php","dotnet")
# # (a,b,c,d)=course
# # print(a)
# # print(b)
# # print(c)
# # print(d)


# (a,b,*c)=course
# print(a)
# print(b)
# print(c)


