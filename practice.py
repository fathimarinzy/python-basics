#right angled triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#right angled triangle reverse and with num
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()



# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
        
#     print()    

#pyramid with num

# p=1
# n=5
# for i in range(1,6):
#     for j in range(n-i):
#         print( " ",end=" ")
#     for j in range(1,i+1):
#         print(p,end=" ")  
#         p+=1
#     print()

#reverse pyramid of num

# n=5
# for i in range(n):
#     for j in range(i):
#         print("",end=' ')
#     for j in range(1,n-i+1):
#         print(j, end=' ')
#     print()

# # n=5
# for i in range(n):
#     for j in range(n-i):
#         print(' ', end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print('', end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for i in range(n-i):
         print("*",end=" ")
    print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for i in range(n-i):
#          print("*",end=" ")
#     print()


# n=4
# for i in range(n-1):
#     for j in range(i+1):
#         print("*", end=" ")
    
    
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()



# n=4
# for i in range(n-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
    
    
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n=4
# for i in range(n-1):
#     for j in range(i+1):
#         print("*", end=" ")
    
    
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j== n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end="  ")
#     print()   



# n=5
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j== n//2:
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")
#     print()   


# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j== n-1:
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")
#     print()   

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j== n-1:
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")
#     print()   

n=5
# for i in range(n):
#     for j in range(i+1):
#         if i==n-1 or j==0 or i==j:
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")
#     print()   


# n=5
# for i in range(n):
#     for j in range(n-i):
#         if i==0 or j==0 or i+j== n-1:
#             print("*",end="  ")
#         else:
#             print(" ",end="  ")
#     print()

#    

# n=5
# for i in range(n):
#     for j in range(n-i):
#             print(" ",end=" ")
#     for j in range(i):
#           if i==n-1 or j==0:
#             print("*",end=" ")
#           else:
#                print(" ",end=" ")
#     for j in range(i+1):
#           if i==n-1 or i==j:
#                print("*",end=" ")
#           else:
#                print(" ",end=" ")
#     print()   


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(i,end=" ")
#     print()
# n=5
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()


# n=5
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1    
#     print() 



# n=5
# p=5
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p-=1    
#     print() 



# n=5
# p=0
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=2    
#     print() 

# n=5

# for i in range(n):
#     for j in range(i+1):
#         if i%2==0:
#             print("1",end=" ")
#         else:
#             print("2",end=" ")
     
#     print() 


# n=5
# p=1
# for i in range(n-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#       print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=1    
    
#     print() 
# p=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range((n-1)-i):
#       print(p,end=" ")
#     for j in range(n-i):
#         print(p,end=" ")
#     p-=1    
    
#     print() 



# n=5

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(j+1,end=" ")   
    
#     print() 


# n=5

# for i in range(n-1):
#     p=1
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(p,end=" ")
#         p+=1   
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()

# for i in range(n):
#     p=1
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range((n-1)-i):
#         print(p,end=" ")
#         p+=1   
#     for j in range(n-i):
#         print(p,end=" ")
#         p+=1
#     print()



# n=5

# for i in range(n):
#     p=1
#     for j in range(i+1):
     
#         print(p,end=" ")
#         p+=1
    
#     for j in range((n-1)-i):
#       print(" ",end=" ")
#     for j in range((n-1)-i):
#         print(" ",end=" ")
#     print() 
#     for j in range(n-i):
        
#         print(p,end=" ")
#         p+=1
#     print()

  
#     n=5
# p=1
# for i in range(n-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#       print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=1    
    
#     print() 


   

# for i in range(n):
#     p=1
#     for j in range(n-i):
#         print(p,end=" ")
#         p+=1
#     print()
    
# n=5
# for i in range(n-1):
#     p=1
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     for j in range((n-1)-i):
#         print(" ",end=" ")
#     for j in range((n-1)-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         p=1
        
#         print(j+1,end=" ")
      
#     print()
# for i in range(n):
#     p=1
#     for j in range(n-i):
#         print(p,end=" ")
#         p+=1
#     for j in range((i-1)+1):
#         print(" ",end=" ")
#     for j in range((i-1)+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         p=1
#         print(j+1,end=" ")
        
#     print()



# n=5
# p=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p+=1    
#     print()




# n=5
# p=65
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(chr(p),end=" ")   
#     p+=1
#     print()

# n=5
# p=65
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range((i-1)+1):
#         print(chr(p),end=" ")   
  
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()
    
    
# n=5
# p=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()

# n=5
# p=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p+=2
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#       if i%2==0:
#          print("A",end=" ")
#       else:
#          print("B",end=" ")
#     print()


# n=5
# p=65
# for i in range(n-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range((i-1)+1):
#         print(chr(p),end=" ")
#     for j in range(i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()
# p=69
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range((n-1)-i):
#         print(chr(p),end=" ")
#     for j in range(n-i):
#         print(chr(p),end=" ")
#     p+=1
#     print()
    

# n=5

# for i in range(n):
#     p=65
#     for j in range(i+1):
#         print(chr(p),end=" ")
#         p+=1
#     print()

# n=5
# for i in range(n):
#     p=65
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(chr(p),end=" ")
#         p+=1
#     print()

# n=5

# for i in range(n):
#     p=69
#     for j in range(i+1):
#         print(chr(p),end=" ")
#         p-=1
#     print()


n=5
k=69
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
      
        print(chr(p),end=" ")

        p-=1
    k-=1
    print()


# n=5

# for i in range(n):
#     p=65
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range((i-1)+1):
       
#         print(chr(p),end=" ")
#         p+=1
#     for j in range(i+1):
#         print(chr(p),end=" ")
#         p-=1
#     print()


# s="CODER"
# n=len(s)
# p=n-1
# for i in range(n):
#     for j in range(i+1):
#         print(s[p],end=" ")
#     p-=1
#     print()

# s="CODER"
# n=len(s)
# p=n-1
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range((i-1)+1):
#         print(s[p],end=" ")
#     for j in range(i+1):
#         print(s[p],end=' ')
#     p-=1
#     print()


# s="CODER"
# n=len(s)
# k=4
# for i in range(n):
#     p=k

#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(s[p],end=" ")
#         p-=1
#     k-=1
#     print()

# courses=['history','maths','physics','compsci']
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[-1])
# print(courses[4])
# course=['art','education']
# courses.extend(course)
# courses.remove('maths')
# courses.pop()
# num=[10,2,3,4,]
# courses.sort()
# num.sort(reverse=True)
# print(courses)
# print(num)


# sorted_courses=sorted(courses)
# print(sorted_courses)

# num=[1,2,3,4,5]
# print(min(num))
# print(max(num))
# print(sum(num))

# print(courses.index('maths'))


# for i,course in enumerate ( courses,start=1):
#     print(i,course)

# a="-".join(courses)
# print(a)
# b=a.split("-")
# print(b)


# list=[1,0,2,0,4,5,6]
# for i in list:
#     if i ==0:
#         list.remove(i)
#         list.append(i)
# print(list)
# x=[10,20,"python","java","php",True,False]
# print(x[-6:-2])

# list=[1,2,3,4,5,6]
# sum=0
# for i in list:
    
#     sum=sum+i
# print(sum)



# y=[2,4,'six',8,'ten']
# y.pop(2)

# print(y)

# l=[(2,5),(1,2),(4,4),(2,3),(2,1)]

# for i in range(len(l)):
                
# z=[]
# l=['ram','sam','mam']
# for i in l:
#   x= i.upper()
#   z.append(x)
#   print(z)


# i=25
# while i <=500:
#     print(i)
#     i+=25

# i=0
# while i<10:
#     j=0
#     while j <i:
#         print("$",end=" ")
#         j+=1
#     print()
#     i+=1

# for i in range(15,7,-1):
#     print(i)

# i=1
# while i <20 and i>0 and 1:
#     print("hello..")
#     i=2*i

# n=763
# sum=0
# while n!=0:
#   x=n%10
 
#   sum=sum+x
#   n=n//10
# print(sum)


#import os
# import os
# from datetime import datetime
# # print(os.getcwd())
# # # os.chdir()
# # print(os.listdir())
# # for dirpath,dirnames,filenames in  os.walk('Users\Lenovo\OneDrive\Desktop\python basics'):
# #     print("current path:",dirpath)
# #     print("directories:",dirnames)
# #     print("files:",filenames)
# #     print()
# # print(os.environ.get('HOME'))
# # 'test.txt'
# # filepath=os.path.join(os.environ.get('HOME'),'test.txt')
# # print(filepath)

# # print(os.path.basename('/tmp/test.txt'))
# # print(os.path.dirname('/tmp/test.txt'))
# # print(os.path.split('/tmp/test.txt'))
# # print(os.path.exists('/tmp/test.txt'))
# # print(os.path.isdir('/tmp/test.txt'))
# # print(os.path.isfile('/tmp/test.txt'))
# # print(os.path.splitext('/tmp/test.txt'))
# # print(dir(os.path))

# # import module we have written 
# import modules1


# # standard libraries
# import random
# course=['history','math','physics','compsci']
# random=random.choice(course)
# print(random)

# import math
# rad=math.radians(90)
# print(rad)
# print(math.sin(rad))


# import calendar
# print(calendar.isleap(2020))


# import os
# print(os.__file__)

# # comic
# import antigravity


# functions
# def hello():
#     pass
# hello()

# def hello():
#     print("hello")
# hello()


# def hello():
#     print("hello")
# hello()
# hello()
# hello()
# hello()

# def hello():
#     return "hello"
# print(hello())

# def hello():
#     return "hello"
# print(len(hello()))
# def hello():
#     return "hello"
# print(hello().upper())

# def hello(greet,hi):
#     return '{},{} Function.'.format(greet,hi)
# print(hello('greet','you'))

# #positional keyword arguments
# def stuinfo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# stuinfo('math','art',name='john',age=22)

# def stuinfo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# list=['math', 'art']
# dict={'name': 'john', 'age': 22}
# stuinfo(list,dict)#it will give the list and dict together

# #to get output seperately
# def stuinfo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# list=['math', 'art']
# dict={'name': 'john', 'age': 22}
# stuinfo(*list,**dict)


#dict comp
# f={'new york':32,'boston':75,'los angeles':100,'chicago':50}
# c={key: round((value-32)*(5/9)) for(key,value)in f.items()}
# print(c)

# weather={'new york':'snowing','boston':'sunny','los angeles':'sunny','chicago':'cloud'}
# sunny={key:value for(key,value) in weather.items() if value=="sunny" }
# print(sunny)

# f={'new york':32,'boston':75,'los angeles':100,'chicago':50}
# desc={key:("warm" if value>=40 else "cold")for (key,value)in f.items()}
# print(desc)

# def temp(value):
#     if value >=70:
#         return "HOT"
#     elif 69>= value>=40:
#         return "warm"
#     else:
#         return "cold"
# f={'new york':32,'boston':75,'los angeles':100,'chicago':50}
# desc={key:temp(value)for (key,value)in f.items()}
# print(desc)

#oops
# class Employee:
#     pass

# emp1=Employee()
# emp2=Employee()
# # print(emp1)
# # print(emp2)

# emp1.first='corey'
# emp2.last='User'
# print(emp1.first)
# print(emp2.last)

# class Employee:
#     def __init__(self,first,last,pay):
#         self.fname=first
#         self.lname=last
#         self.pay=pay

# emp=Employee('corey','user','500000')
# print(emp)
# class Employee:
#     def __init__(self,first,last,pay):
#         self.fname=first
#         self.lname=last
#         self.pay=pay
#     def fullname(self):
#         return '{} {}'.format(self.fname,self.lname)
    

# emp1=Employee('corey','user',500000)
# print(emp1.fullname())

# class Employee:
#     noofemplo =0
#     def __init__(self,first,last,pay):
#         self.fname=first
#         self.lname=last
#         self.pay=pay
#         Employee.noofemplo +=1
#     def fullname(self):
#         return '{} {}'.format(self.fname,self.lname)

# emp1=Employee('corey','user',500000)
# emp2=Employee('laila','user',500000)
# # print(emp1.fullname())
    
# print(Employee.noofemplo)


###tkinter
import tkinter as tk
# tk._test() 
root=tk.Tk()
root.title("Simple App")



root.mainloop()