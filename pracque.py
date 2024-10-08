# #check char is vowel or consonant
# n=input("enter the char:")
# m=['a','e','i','o','u']
# if n in m:
#     print("char")
# else:
#     print("consonant")

# #reverse a given num
# n=int(input("enter the no:"))
# rev=0
# while n>0:
#     x=n%10
#     rev=rev*10+x
#     n//=10
# print(rev)

# # find duplicates char from a string
# n='hello'
# for i in n:
#     if i.i:
#         print(i)


##factor program
##find the of a number
# def factor(num):
#     fac=[]
  
#     for i in range(1,num+1):
#         if num%i==0:
#             fac.append(i)
#     if len(fac)==2:
#         print("prime no")
#     return fac
# print(factor(9))

##number programs
##                            


"""Write a Python program that checks if a given string is a palindrome (a word that reads the same forward and backward).
Input: "madam"
Output: True """

# input="madam"
# rev=input[::-1]
# if rev==input:
#     print("palindrome")
# else:
#     print("not palindrome")


"""Write a Python program to calculate the sum of the digits of a given number.
Input: 123
Output: 6 (1 + 2 + 3)
"""

# input = 123
# sum=0
# while input>0:
#     sum+=input%10
#     input=input//10

# print(sum)


"""Count Vowels in a String
Write a Python program to count the number of vowels (a, e, i, o, u) in a given string.

Input: "hello"
Output: 2
"""
# count=0
# inp="helloi"
# vo=['a','e','i','o','u']
# for i in inp:
#     if i in vo :
#         count+=1
# print(count)


"""Write a Python program to print numbers from 1 to 10 using a for loop."""
# for i in range(1,11):
#     print(i)

"""Write a Python program to calculate the sum of the first 100 natural numbers using a for loop."""
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)

# Print the table of any given number using a for loop.
# n=int(input("enter the no:"))
# for i in range(1,11):
#   a=i*n
#   print(f"{i}x{n}={a}")

"""Write a program to print all even numbers between 1 and 100 using a for loop."""
# for i in range(1,101):
#     if i%2==0:
#         print(i)

"""Write a Python program to print numbers from 10 down to 1 using a while loop."""
# i=11
# while i>1:
#     i-=1
#     print(i)

"""Write a program to find the factorial of a given number using a while loop."""
# n=int(input("enter the number:"))

# fac=1
# inp=n
# while inp>0:
#     fac*=inp
#     inp-=1
# print(fac)

"""Write a program to reverse the digits of a number using a while loop."""
# n=int(input("enter the number:"))
# rev=0
# while n>0:
#     c=n%10
#     rev=rev*10+c
#     n//=10
# print(rev)

"""Write a Python program that continues taking input from the user until they enter 'exit'"""
# n=int(input("\n1.taking input\n2.exit \nEnter the choice"))
# while n>0:
#     if n==1:
#         b=int(input("enter the number:"))
#     elif n==2:
#         print("exiting")
#         break


"""Write a Python program to check if a number is positive, negative, or zero using if-else."""

# n=int(input("enter the number:"))
# if n>0:
#     print("its a positive number")
# elif n<0:
#       print("its a negative number")
# elif n==0:
#        print("its a zero")
# else:
#         print("its invalid number")
      

"""Write a Python program to check if a number is divisible by both 3 and 5 using if-else."""

# n=int(input("enter the number="))
# if n%3==0 and n%5==0:
#       print("it is divisible both by 3 and 5")
# else:
#       print("not divisible")

"""Write a Python program to print a multiplication table (from 1 to 10) using a nested for loop."""
# n=int(input("enter the number:"))
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{j}x{i}={i*j}")

"""list based questions"""

"""How do you append an element(example 4) to a list?
my_list = [1, 2, 3]"""

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)

""" Question: How can you remove an element from a list by value(remove 3)?
list = [1, 2, 3, 4]"""

# list = [1, 2, 3, 4]
# list.remove(3)
# print(list)

"""How do you sort a list in ascending order?
my_list = [3, 1, 4, 2]"""

# my_list = [3, 1, 4, 2]
# my_list.sort()
# print(my_list)

"""How can you find the length of a list?
my_list = [1, 2, 3, 4]"""

# my_list = [1, 2, 3, 4]
# print(len(my_list))

"""How do you access an element in a list by index?
my_list = [10, 20, 30, 40]"""

# my_list = [10, 20, 30, 40]
# print(my_list[0])

""" How can you reverse a list?
my_list = [1, 2, 3, 4]"""

# my_list = [1, 2, 3, 4]
# my_list.reverse()
# print(my_list)

"""How do you extend a list with another list?
my_list = [1, 2]
another_list = [3, 4]"""
# my_list = [1, 2]
# my_list.extend( [3, 4])
# print(my_list)

""" How can you count the occurrences of an element in a list(count of 2)?
my_list = [1, 2, 2, 3]"""

# my_list = [1, 2, 2, 3]
# print(my_list.count(2))

"""How can you insert an element at a specific index in a list(Insert 2 at index 1)?
my_list = [1, 3, 4]"""

# my_list = [1, 3, 4]
# my_list.insert(1,2)
# print(my_list)


# Question: How do you pop an element from a list by index(Remove element at index 2)?
# my_list = [1, 2, 3, 4]
# my_list.pop(2)
# print(my_list)

# 11.Question: How can you clear all elements from a list?
# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)


# 12.Question: How do you find the maximum element in a list(using max function also you can find maximum value from a list)?
# my_list = [5, 3, 9, 1]
# a=max(my_list)
# print(a)


# 13.Question: How can you find the minimum element in a list(using min function also you can find minimum value from a list?
# my_list = [5, 3, 9, 1]
# a=min(my_list)
# print(a)


# 14.Question: How can you slice a list to get a subset(Get elements from index 2 to 4)?
# my_list = [0, 1, 2, 3, 4, 5]
# a=my_list[2:5]
# print(a)

# 15.Question: How do you concatenate two lists?
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# d=list1+list2
# print(d)

# 16.Question: How can you check if an element exists in a list?
# my_list = [1, 2, 3, 4]
# a= 4 in my_list
# print(a)

# 17.Question: How do you find the index of the first occurrence of an element in a list?
# my_list = [1, 2, 3, 2]
# print(my_list.index(2))

# 18.Question: How can you replace an element at a specific index in a list(Replace element at index 1 by 5)?
# my_list = [1, 2, 3]
# Output: [1, 5, 3]
# my_list = [1, 2, 3]
# my_list[1]=5
# print(my_list)

# 19.Question: How do you extend a list by adding another list's elements?
# my_list = [1, 2]
# another_list = [3, 4]
# Output: [1, 2, 3, 4]
# my_list = [1, 2]
# another_list = [3, 4]
# my_list.extend(another_list)
# print(my_list)

# 20.Question: How can you remove all occurrences of an element from a list?
# my_list = [1, 2, 2, 3, 2]
# Output: [1, 3]
# my_list = [1, 2, 2, 3, 2]
# l=[]
# for i in my_list:
#     if i!=2:
        
#         l.append(i)
# print(l)

# 21.Question: How do you get a list of unique elements from a list?
# my_list = [1, 2, 2, 3, 4, 4]``
# Output: [1, 2, 3, 4]

# my_list = [1, 2, 2, 3, 4, 4]
# l=[]
# for i in my_list:
#     if i not in l:
#         l.append(i)
# print(l)

# 22.Question: How can you convert a string into a list of characters?
# my_string = "hello"
# a=list(my_string)
# print(a)


# 23.Question: How do you create a list from a string using a specified delimiter?
# my_string = "apple,banana,cherry"
# Output: ['apple', 'banana', 'cherry']
# my_string = "apple,banana,cherry"
# a=my_string.split(',')
# print(a)

# 24.Question: How can you find the sum of all elements in a list?
my_list = [1, 2, 3, 4]
# a=sum(my_list)
# print(a)

# sum=0
# for i in my_list:
#     sum+=i
# print(sum)

# 25.Question: How do you create a list of squares of numbers from 1 to 5?
# Output: [1, 4, 9, 16, 25]
my_list=[1,2,3,4,5]
# a=[i**2 for i in my_list]
# print(a)
# m=[]
# for i in my_list:
#     m.append(i*i)
# print(m)


# 26.Question: How can you find the intersection of two lists?
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# # Output: [2, 3]
# o=[]
# for i in list1:
#         if i in list2 :
#             o.append(i)
# print(o)

# 27.Question: How do you remove duplicates from a list while maintaining order?
# my_list = [1, 2, 2, 3, 4, 4]
# Output: [1, 2, 3, 4]
# my_list = [1, 2, 2, 3, 4, 4]
# o=[]
# for i in my_list:
#     if i not in o:
#         o.append(i)
#         print(o)



# 28.Question: How can you convert a list of integers to a list of strings?
# int_list = [1, 2, 3]
# str_list = []
# for i in int_list:
#     a=str(i)
#     str_list.append(a)
# print(str_list)

# 29.Question: How do you find the common elements in three lists?
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# list3 = [3, 4, 5]
# # Output: [3]

# a=[i for i in list1 if i in list2 and i in list3]
# print(a)

# 30.Question: How do you remove all elements from a list using a while loop?
my_list = [1, 2, 3, 4]
# i=1
# while i!=0:
#     my_list.clear()
#     i+=1
#     print(my_list)
#     break




# 31.Question: How can you multiply all the elements in a list?
my_list = [1, 2, 3, 4]
# Output: 24
# mul=1
# for i in my_list:
#     mul*=i
# print(mul)


# 32.Question: How can you find the difference between two lists (elements in the first list but not in the second)?
# list1 = [1, 2, 3, 4]
# list2 = [2, 4]
# # Output: [1, 3]
# b=[]
# for i in list1:
#     if i not in list2:
#         b.append(i)
# print(b)



# 33.Question: How can you check if a list is a palindrome (reads the same forward and backward)?
# my_list = [1, 2, 3, 2, 1]
# if my_list==my_list[::-1]:
#     print("palindrome")
# else:
#     print("not")

# 34.Question: How do you find the second largest element in a list?
# my_list = [10, 20, 4, 45, 99]
# my_list.sort()
# print(my_list)
# a=max(my_list)
# print(a)
# my_list.remove(a)
# print(my_list)
# b=max(my_list)
# print(b)

# 35.Question: How can you check if all elements in a list are the same?
# my_list = [2, 2, 2, 2]

# if all(i == 2 for i in my_list):
#         print("same")
    

           
# 36.Question: How can you find the length of each element in a list of strings?

# string_list = ["apple", "banana", "cherry"]
# # Output: [5, 6, 6]
# a=[]
# for i in string_list:
#         a.append(len(i))
# print(a)
# 37.Question: How can you split a list into two lists: one with even numbers and one with odd numbers?
my_list = [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]
# Output: [1, 3, 5]
# odd=[]
# even=[]
# for i in my_list:
#     if i%2==0:
#         even.append(i)
        
#     elif i%2!=0:
#         odd.append(i)
# print(even)
# print(odd)


# 38.Question: How do you remove elements at even indices from a list?
my_list = [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]
# m=[]
# for i in my_list:
#     if i%2!=0:
#         m.append(my_list[i])
# print(m)

# 39.Question: How can you remove all negative numbers from a list?
# my_list = [1, -2, 3, -4, 5]
# # Output: [1, 3, 5]
# l=[]
# for i in my_list:
#     if i>0:
#         l.append(i)
# print(l)

# # 40.Question: How do you find the minimum and maximum elements in a list?
# my_list = [10, 20, 30, 40, 50]

# a=min(my_list)
# b=max(my_list)
# print("max value:",b)
# print("min value:",a)


"""string based questions"""


# 1. Count the frequency of each character in a string.
# # input
# string = "hello world"
# output
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# dic={}
# string = "hello world"
# for i in string:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)


# 2.Remove all vowels from a given string.
# input
# string = "This is a test string"
# Output: "Ths s  tst strng"

# string = "This is a test string"

# vo=['a','e','i','o','u']
# b=list(string)
# for i in string:
#     if i in vo:
#         b.remove(i)
# c=" ".join(b)       
# print(c)
        


# 3. Capitalize the first letter of each word in a string.
# input
# string = "hello world"
# Output: "Hello World"
# string = "hello world"
# a=string.title()
# print(a)

# 4.Check if a substring exists within a given string.
# input
# main_string = "Python programming is fun"
# sub_string = "programming"
# Output: True

# main_string = "Python programming is fun"
# a = "programming"
# if a in  main_string:
#     print("True")
# else:
#     print("false")

# 5.Replace all occurrences of a substring in a string.
# input
# string = "Python is awesome. Python is dynamic." 
# Output: "Java is awesome. Java is dynamic."

# string = "Python is awesome. Python is dynamic." 
# a=string.replace("Python","Java")
# print(a)

# 6.Remove duplicate characters from a string.
# string = "programming"
# Output: "progamin"

# string = "programming"
# a=""
# for i in string:
#     if i not in a:
#         a+=i
# print(a)



# 7.Find the longest word in a sentence.
# string = "I love programming in Python"
# a=string.split()
# b=max(a)
# print(b)


# 8.8.Reverse the words in a given string.
# string = "Hello World"
# a=string.split()
# a.reverse()
# b=" ".join(a)
# print(b)


# 9.Check if two strings are anagrams.
# string1 = "listen"
# string2 = "silent"
# a = sorted("listen")
# b = sorted("silent")
# print(a)
# print(b)
# if a==b:
#     print("true")
# else:
#     print("false")


# 10. Check if a given string is a palindrome.
string = "A man a plan a canal Panama"
string=string.lower().replace(" ","")
print(string)
if string ==string[::-1]:
    print("palindrome")
else:
    print("not palindrome")