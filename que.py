# "write a python program that takes a list of words and groups words with the sameletters into sublists.store all these
# sublists in a main list and print the result . for eg,if the input is ['eat','tea','ten','bat','ate','net'],
# the program should group anagrams and print the result as a list of lists."

# inp=['eat','tea','ate','ten','net','bat']
# out={}
# for i in inp:
#     sor=''.join(sorted(i))
#     # print(sor)
#     if sor in out:
#         out[sor].append(i)
#     else:
#         out[sor]=[i]
# res=list(out.values())
# print(res)

#input=[2,7,11,15] target=9 output=[0,1]
# out=[]
# input=[2,7,11,15] 
# for i in range(len(input)):
#     for j in range(i+1,len(input)):
#         if input[i]+input[j]==9:
#             out=[i,j]
#             print(out)
            #   break


# inp= l1=[a,b,c,d,e,f,g,h,i] l2=[0,1,1,0,1,2,2,0,1] otp= l3=[a,d,h,b,c,e,i,f,g]
# l1= ['a','b','c','d','e','f','g','h','i']
# l2=[0,1,1,0,1,2,2,0,1]
# l3=[]
# for i  in range(len(l1)):


#from a list of nubers remove zero to the end of the list
# list=[1,0,2,0,4,6]

# for i in list:
#     if i==0:
#       list.remove(0)
#       list.append(0)
# print(list)


# #write a python function that takes a list and returns a new list with distinct elements
# #from the list

# def fun(n):
#     m=[]
#     # print(" list=",n)
#     for i in n :
#       if i not in m:
#         m.append(i)
#     print("new list=",m)
# list=[1,2,3,3,3,3,4,5]
# fun(list)


#  #find the missing number
# def display(l):
#    n=len(l)+1
#    total=n*(n+1)//2
#    total_l=sum(l)
#    missing=total-total_l 
#    return missing
# list=[1,2,4,5,6]
# print(display(list))


# what is the python prgrm to find pairs of numbers from a given list such
# that the sum of their squares equala a perfect square ? a^2+b^2=c^2.
# input: a=[1,2,3,4,5,6,7,8,9,10]
# output:3,4,5,6,8,10
# import math

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         c = a[i]**2 + a[j]**2
#         d = int(c**0.5)
#         if d**2 == c:
#             b.extend([a[i], a[j]])
# b = sorted(set(b))
# print(b)


#if a upper diagonal element is lower than lower diagonal
#  element,thrn replace lower diagonal element with 1 else replace upper diagonal elemnt with 0

# matrix = [
#     [5, 8, 3],
#     [4, 7, 6],
#     [1, 2, 9]
# ]
# n = len(matrix)
# for i in range(n):
#     for j in range(i+1, n):
#         if matrix[i][j] < matrix[j][i]:
#             matrix[j][i] = 1
#         else:
#             matrix[i][j] = 0
# for row in matrix:
    # print(row)



#  find the employee with highest salary
#  promote an employee (eg:E002) by increasing salary and updating position

#given a sorted array of distinct integers and a target value,return the index if the target 
#is found.if not ,return the index where it would be if it were inserted in order.


# class Solution:
#     def found(self,nums,target):
#         if target in nums:
#             print(nums.index(target))  
#         else:
           
#             nums.append(target)
#             nums.sort()
#             print(nums.index(target))  
# s = Solution()
# s.found([1,3,5,6], 5)  
# s.found([1,3,5,6], 2)  
# s.found([1,3,5,6], 7) 


#create a class student with class variables school.
#a.create a paramatrized constructor with id,name,and age
#b.create instance of the class with id=1,name=sara,age=10 and id=2,nam='jose',age=20
#c.access value of attributes of an instances using built in function
#d.change the name attributes from jose to kris of defined instances
# e.check if class student has place attribute.if class student has no place place attribute
#  then create it using the built in method


# class Student:
#     school='abc'
#     def __init__(self,id,name,age):
#         self.id=id
#         self.name=name
#         self.age=age
        
# s=Student(1,'sara',10)
# s1=Student(2,'jose',20)
# print(getattr(s,'id'))
# print(getattr(s,"name"))
# print(getattr(s,"age"))
# print(getattr(s1,'id'))
# print(getattr(s1,"name"))
# print(getattr(s1,"age"))
# setattr(s1,'name','kris')
# print(s1.name)
# if hasattr(s1,'place'):
#     print(getattr(s1,'place'))
# else:
#     setattr(s,'place','kollam')
#     setattr(s1,'place','kochi')
#     print(s.place)
#     print(s1.place)


# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal 
# substring
#  consisting of non-space characters only.

####regular expression

#text="Hello,my name is john. i have two cats,mia and max."

# import re
# text="Hello,my name is john. i have two cats,mia and max."
# x=re.findall(r"\b\w{3}\b",text)
# print(x)

#text="contact info@example.com or support@example.com"
# import re
# text="contact info@example.com or support@example.com"
# x=re.findall(r"\b\w+@\w+\.\w+\b",text)
# print(x)


# text="important dates:2022-01-01,2023-05-15,and 2023-12-31"

# import re
# text="important dates:2022-01-01,2023-05-15,and 2023-12-31"
# x=re.findall(r"\b\d{4}\-\d{2}\-\d{2}\b",text)
# print(x)

###que
"""write a pgm which accept 2 strings as input and create a new string by 
 combining speecific character from each input strings based on certain criteria."""

# a="hello"
# b="world"
# c=""
# for i in range(len(a)):
#     if i%2==0:
#         c+=a[i]
#         c+=b[i]
# print(c)
#another method
# a="hello"
# b="world"
# c=a[len(a)//2]
# d=b[len(b)//2]
# re=a[0]+b[0]+c+d+a[-1]+b[-1]
# print(re)

"""write a program to remove the characters which have a odd index values of given string"""
# a="rinzy"
# l=[]
# for i in range(len(a)):
#     if i%2==0:
#         l.append(a[i])
# print(l)

# """write a python program to seperate positive and negative number from a list"""
# l=[1,4,5,-6,-7,-8]
# p=[]
# n=[]
# for i in l:
#     if i>0:
#         p.append(i)
#     else:
#         n.append(i)
# print(p)
# print(n)

"""write a program to change the position of every nth value to the (n+1)th  in a list"""
# inp=[0,1,2,3,4,5]
# # o=[1,0,3,2,5,4]

# for i in range(0,len(inp),2):
#     inp[i],inp[i+1]=inp[i+1],inp[i]
    
# print(inp)

"""prgrm to calculate the product of elements of a list excluding its duplicates"""
# l=[1,4,3,5,3,6,6]
# n=[]
# pro=1
# for i in l:
#     if i not in n:
#         n.append(i)
#         pro=pro*i
# print("product of elements:",pro)

"""convert tuple to string"""

# tu=('a','b','c','d','e','f')
# y=list(tu)
# print(y)
# z="".join(y)
# print(z)

"""prgrm that counts the number of string that have a length greater than 2 and start and end
 with the same charcter"""

# a=['ammu','mom','dad','car','is']
# b=[]
# for i in a:
#     if  len(i)>2:
#         if i[0]==i[-1]:
#             b.append(i)
# print(b)
# print(len(b))


"""prgrm to print length of unique character in a string """

# a="helloworld"
# b=""
# for i in a:
#     if i not in b:
#         b+=i
# print(b)
# print(len(b))

"""given list of words .write a python prgrm  to count how many anagram exist for each unique grouping of letters.
two words are considered anagrams if they contain the same charcters in a different order"""

# inp=['eat','tea','ten','bat','ate','net','dub','bud']
# out={}
# for i in inp:
#     z=" ".join(sorted(i))
#     if z in out:
#         out[z]+=1
#     else:
#         out[z]=1
# print(out)
    