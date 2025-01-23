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

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for i in range(n-i):
#          print("*",end=" ")
#     print()


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


# n=5
# k=69
# for i in range(n):
#     p=k
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
      
#         print(chr(p),end=" ")

#         p-=1
#     k-=1
#     print()


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
# import tkinter as tk
# # tk._test() 
# root=tk.Tk()
# root.title("Simple App")



# root.mainloop()

# n=13
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=" ")
#         i += n - j-1
#     print()



# # hollow pattern
# n = 10
# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print("*", end=" ")
#     for k in range(1, 2 * i):
#         if k == 1 or k == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(1, n - i + 1):
#         print("*", end=" ")
#     print()  
# for i in range(n, 0, -1):
#     for j in range(1, n - i + 1):
#         print("*", end=" ")
#     for k in range(1, 2 * i):
#         if k == 1 or k == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(1, n - i + 1):
#         print("*", end=" ")
#     print()


# # a="TRAVIDUX"
# # b="VRIDAUTX"
# # a="CAT"
# # b="CATASTROPHIC"
# # a="HELLO"
# # b="HELO"
# a = "NOON"
# b = "OLONSEIGHCET"
# for i in a:
#     if a.count(i) > b.count(i):  
#         print("not present")
#         break
# else:
#     print("present")

    
    

# #heart
# n = 10
# # Top half of the heart
# for i in range(n // 2, n, 2):
#     for j in range(1, n - i, 2):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     for j in range(1, n - i + 1):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# # Bottom half of the heart
# for i in range(n, 0, -1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(1, i * 2):
#         print("*", end=" ")
#     print()




# #cross
# n = 5  

# # Top half of the pattern
# for i in range(1, n + 1):
#     for j in range(i - 1):
#         print(" ", end=" ")
#     print(i, end=" ")
#     for j in range((n - i) * 2 - 1): 
#         print(" ", end=" ")
#     if i != n:
#         print(i)
#     else:
#         print()

# # Bottom half of the pattern
# for i in range(n - 1, 0, -1):
#     for j in range(i - 1):
#         print(" ", end=" ")
#     print(i, end=" ")
#     for j in range((n - i) * 2 - 1):  
#         print(" ", end=" ")
#     # Print right number
#     print(i)


#1.write a program to print numbers from 1 to 15.skip numbers divisible by 3.

# i=1
# while i < 16:
#     if i %3 !=0:
#         print(i)
#     i+=1


#2.write a program to print numbers starting from 1.stop the loop if the number is greater than 10

# i=1
# while i<=10:
#     print(i)
#     i+=1

#3.write a program to print numbers from 1 to 20.stop the loop when the number is 15, and
# skip numbers divisible by 5.
# i=1
# while i <=20:
#     if i==15:
#         break
#     if i %5==0:
#         i+=1
#         continue
#     print(i) 
#     i+=1

        
#4.write a program to find the first number between 1 and 50 that is divisible by both 4 and 6.
# n=[]
# i=1
# while i<=50:
#     if i%4==0 and i%6==0:
#         n.append(i)
#         print(n[0])
#         break
#     i+=1

#5.write a program that asks the user to input a number.if the number is 0,do nothing , but
# continue the loop to ask for another input.stop the loop when the user enters a negative number.


# while True:
#     n=int(input("enter the num="))
#     if n==0:
#         continue
#     if n<0:
#         break

    

# # # #1.write a program to check if a number is positive .if positive,determine if its a single
# # # #  digit number.

# n=int(input("enter the num="))
# if n<0:
#     print('not a positive number')
# elif n>0:
#     if 1<=n<=9:
#         print("positive and single digit")
#     else:
#         print("positive not a single digit")


# # # #2.write a program to check if a number is divisible by 2.if it is,further check if it is
# # # #  also divisible by 4.
# n=int(input("enter the num:"))
# if n%2==0:
#     if n%4==0:
#         print("divisibe by 4 and 6")
# else:
#     print("not divisibe by 4 and 6")


# # # #3.write a program to check if a person is eligible to vote.if eligible ,check if they are
# # # #  eligible to run for  president(age>=35)

# n=int(input("enter the age to vote="))
# if n>=18:
#     if n>=35:
#         print("eligible to vote and  eligible to run for  president ")
#     else:
#         print("eligible to vote and not eligible to run for  president ")
# else:
#     print("not eligible to vote and not eligible to run for  president ")


# # # #4.write a program to determine if a student passed or failed.if theypassed,check if their 
# # # # score is a distinction(>=75)

# n=int(input("enter the score="))
# if n>=50:
#     if n>=75:
#         print("passed with distinction")
#     else:
#         print("passed")
# else:
#     print("failed")


# # # #5.write a program to determine if a product is on sale.if on sale,check if the discount is 
# # # # greater than 20 %

# n=input("product is on sale or not=").lower()
# if n=="yes" :
#     m=int(input("enter the discount="))
#     if m>20:
#         print("product is on sale discount greater than 20")
#     else:
#         print("product is on sale discount is not greater than 20")
# else :
#     print("product is not on sale")



# # # #6.write a program to check whether a number is positive,negative or zero.if positive,check
# # # # if it is greater than 100

# n=int(input("enter the no:"))
# if n>0:
#     if n>100:
#         print("positive and greater than 100")
#     else:
#         print("positive no")
# elif n==0:
#         print("zero")
# elif n<0:
#         print("negative no")



# # # #7.write a program to determine if a number is a multiple of both 3 and 5.if not ,check if it 
# # # # is a multiple of either 3 or 5
# n=int(input("enter the no:"))
# if n%3==0 and n%5==0:
#     print(" multiple of both 3 and 5")
# elif n%3==0 or n%5==0:
#     print(" multiple of either 3 or 5")
# else:
#     print("not multiple of both 3 and 5")
     


# # # #8.write a program to check if a person is eligible for a job based on age and experience.the 
# # # # person must be at least 21 years old and if under 30,they must have 3+ years of experience.

# n=int(input("enter the age="))
# if n>=21:
#     if n <30:
#         m=int(input('enter the exp='))
#         if m>=3:
#             print(f"eligible for job and {m} years of ex" )
#     else:
#         print("eligible for job")


# 9.print numbers from 1 to 10
# for i in range(1,11):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=1

# # #10.find the sum of numbers from 1 to 10 using a while loop
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)


# # #11.print the multiplication table of a given number using a while loop
# n=int(input('enter the no: '))
# i=1
# while i<=10:
#     print(f'{i}x{n}={i*n}')
#     i+=1


# # #12.find the factorial of a given number using a while loop

# n=int(input("enter the no="))
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact,end=" ")
    

# # #13.print all even numbers from 1 to 20 using a while loop
# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1


# # #14.count the number of digits in a given number using a while loop

# n=int(input("enter the no="))
# count=0
# while n>0:
#     n//=10
#     count+=1
# print(count)

# # # #15.calculate the sum of digits of a given number using a while loop
# n=int(input("enter the no="))
# count=0
# sum=0
# while n>0:
#     m=n%10
#     sum+=m
#     n//=10
# print(sum)

# # # #16.reverse of a given number
# n=int(input("enter the num="))
# rev=0
# while n>0:
#     m=n%10
#     rev=rev*10+m
#     n//=10
# print(rev)
 
# # # #17.check the given number is palindrome or not
# n=int(input("enter the num="))
# o=n
# rev=0
# while n>0:
#     m=n%10
#     rev=rev*10+m
#     n//=10
# print(rev)
# if o==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

# # # #18.count how many times a digit appears in a given number.

# n=int(input("enter the num="))
# digit=int(input("enter the digit="))

# ns=str(n)
# ds=str(digit)
# count=ns.count(ds)
# print(count)

# # # # 19 armstrong 

# n=int(input("Enter a number to check if it is an Armstrong number: "))
# digits = [int(d) for d in str(n)]
# power = len(digits)
# armstrong_sum = sum(d ** power for d in digits)
# if n == armstrong_sum:
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")


#20Using while
# # # *
# # # * *
# # # * * *
# # # * * * *
# # # * * * * *

# n=5
# i=0
# while i<=n:
#     print("* " * i)
#     i+=1


# 21.write a program to keep adding numbers input by the user until the total sum exceeds 50.
# # # print the sum
sum=0
while sum<=50:
    n=int(input("enter the num="))
    sum+=n





# # #22.find the power of a number using a while loop
# # #23.print numbers divisible by 3 and 5 within the range 1 to 50
# # #24.find the largest digit in a number
# # #25.niven number or not
# # # 156 -->1+5+6=12
# # # number divisible by the sum of digits.
# # #26.series 105,98,91,.....7
# # #27.write a program to print first 10 natural number in reverse order 
# # # using while loop



# # #28,write a program to check if a given number is prime using a while loop
#29,Write a Python program to print numbers starting from 1. Stop the loop if the number is greater than 10.
#30Write a Python program to print numbers from 1 to 15. Skip numbers divisible by 3.