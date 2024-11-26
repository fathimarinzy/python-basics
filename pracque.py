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
# string = "A man a plan a canal Panama"
# string=string.lower().replace(" ","")
# print(string)
# if string ==string[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

"""regularexpression"""

# Write a regular expression to find all occurrences of the word "cat" or "dog" in a given text.
# text = "The Cat chased the dog. A small cat and a big DOG played together."
# import re
# c=re.findall(r"cat|dog",text,re.IGNORECASE)
# print(c)

# Write a regex to find all sequences of exactly 3 digits in a text. For example, in the text 
# "My number is 123 and his number is 4567", the output should be ['123'].
# text = "My number is 123 and his number is 4567"
# import re
# c=re.findall(r"\b\d{3}\b",text)
# print(c)

# Write a regex to validate an email address. The regex 
# should account for common email formats, such as username@domain.com.
# email = "user.name@example.com"
# import re
# c=r"\b\w+\.\w+@\w+\.\w+\b"
# d=re.match(c,email)
# print(d)

# Write a regular expression to extract dates in the format DD/MM/YYYY from a given text.
# Example: From the text "I have a meeting on 15/10/2023 and another one on 03/12/2024", 
# the output should be ['15/10/2023', '03/12/2024'].

# text ="I have a meeting on 15/10/2023 and another one on 03/12/2024"
# import re
# c=re.findall(r"\b\d{2}\/\d{2}\/\d{4}\b",text)
# print(c)

# Write a regex to extract all words from a sentence. 
# A word is defined as a sequence of letters and can be delimited by spaces or punctuation marks.
# sentence = "Hello, world! This is a test."
# import re
# c=re.findall(r"\b\w+\b",sentence)
# print(c)

# Write a regex to find all hashtags from a given string.
# Example: For the input "Loving this #sunset at the #beach", the output should be ['#sunset', '#beach'].
# a= "Loving this #sunset at the #beach"
# import re
# b=re.findall(r"[#]\w+",a)
# print(b)

# Write a regular expression to extract the file extension (e.g., .pdf, .txt, etc.) from file names.
# Example: "resume.pdf", "report.docx", "image.jpeg" should result in ['.pdf', '.docx', '.jpeg'].

# a=["resume.pdf", "report.docx", "image.jpeg"]
# b=" ".join(a)
# import re
# c=re.findall(r"\b\.\w+\b",b)
# print(c)

# write a regex to remove all HTML tags from a given string.
# Example: From the text "<p>Hello, World!</p>", the output should be "Hello, World!".
# text ="<p>Hello, World!</p>"
# import re
# a=re.findall(r"H.+!",text)
# print(a)

# Write a regex to validate phone numbers in the format (XXX) XXX-XXXX where X is a digit.
# Example: Valid phone number: (123) 456-7890.
# a="My phone number is (123) 456-7890 and office number is (987) 654-3210"
# import re
# c=re.findall(r"\(\d{3}\) \d{3}\-\d+",a)
# print(c)

# Write a regex to find all words of exactly 5 characters in length from a given sentence.
# Example: For the input "There are many trees in the garden", the output should be ['trees'].

# v="There are many trees in the garden"
# import re
# c=re.findall(r"\b\w{5}\b",v)
# print(c)

# Write a regex to find all repeated words in a sentence.
# Example: From the text "This is is a test test", the output should be ['is', 'test'].

# text= "This is is a test test"
# import re
# v=re.findall(r"\b(\w+)\s+\1\b",text)
# print(v)

# Write a regex to extract all URLs from a block of text.
# Example: For the input "Visit our website at https://example.com or follow us at http://twitter.com", 
# the output should be ['https://example.com', 'http://twitter.com'].

# c="Visit our website at https://example.com or follow us at http://twitter.com"
# import re
# v=re.findall(r"\b\w+\:\/\/\w+\.\w+\b",c)
# print(v)

# Write a regex to check if a password is strong. A strong password is defined as:
# At least 8 characters long
# Contains both uppercase and lowercase letters
# Has at least one digit
# Has at least one special character (e.g., @, #, $).

# import re
# v=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$]).{8,}$"
# d="MyPassword@99"
# c=re.match(v,d)
# print(c)

# Write a regular expression to validate IPv4 addresses (e.g., 192.168.1.1).
# Example: The input "The IPs are 192.168.1.1 and 256.256.256.256" should return ['192.168.1.1'] as valid.

# c="The IPs are 192.168.1.1 and 256.256.256.256"
# import re
# v=re.findall(r"\b\d{3}\.\d{3}\.\d{1}\.\d{1}\b",c)
# print(v)

# Write a regular expression to find all palindrome words (words that read the same backward as forward) in a sentence.
# Example: From the input "Anna and Bob went to the civic center", the output should be ['Anna', 'Bob', 'civic'].

# a="Anna and Bob went to the civic center"
# import re
# v=re.findall(r"\b\w+\b",a)
# print(v)
# for i in v:
#     if i.lower()==i[::-1].lower():
#         print( "palindrome=",i)


"""file"""
# Write a Python program that performs the following operations on a text file named efg.txt:
# Write: Open the file in write mode and write the string "hai" to it.
# Read: Close the file and then reopen it in read mode. Read the contents of the file.
# Display: Print the contents of the file as a list of lines.
# Join: Join the lines into a single string and calculate the length of this string.
# Output: Print the length of the string.

# f=open("fgh.txt","w")
# f.write("hai")
# f.close()
# f=open("fgh.txt","r")
# # print(f.read())
# i=f.readlines()
# print(i)
# a=" ".join(i)
# print(len(a),a)
# f.close()


"""function"""
# Write a function sum_of_two(a, b) that takes 
# two numbers as input and returns their sum.

# def tue(a,b):
#     return a+b
# print(tue(10,30) )


# Write a function is_even(n) that returns True if the 
# number is even and False if it is odd.
# def display(a):
#     if a%2==0:
#          print("True")
#     else:
#         print("False")
# display(4)

# Write a function factorial(n) that calculates the factorial 
# of a given number n.
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#        return n*factorial(n-1)
      
# v=factorial(5)
# print(v)

# def factorial(n):
#     r=1
#     for i in range(2,n+1):
#         r*=i
#     return r

# print(factorial(5))

# Write a function is_palindrome(s) that checks 
# if a given string is a palindrome

# def palindrome(n):
#     if n==n[::-1]:
#         print("palindrome")
#     else:
#         print("not")

# palindrome("malayalam")
# palindrome("hello")

# Write a function count_vowels(s) that counts how many 
# vowels are in a given string

# def count(v):
#     a=['a','e','i','o','u']
#     b=[]
#     for i in v:
#         if i in a:
#             b.append(i)
#     return len(b)

# print(count("hello"))


# Write a function fibonacci(n) that generates the first n numbers 
# of the Fibonacci sequence.
# def fibnocci(n):
#     a=[]
#     for i in range(n):
#         if i==0:
#             a.append(0)
#         elif i==1:
#             a.append(1)
#         else:
#             b=a[i-1]+a[i-2]
#             a.append(b)
#     return a
# print(fibnocci(5))

# Write a function find_max(lst) that takes a list of numbers 
# and returns the maximum value.
# def maz(n):
#    return max(n)
# print(maz([3,4,5,6]))

# Greatest Common Divisor (GCD)
# Write a recursive function to find the greatest common divisor (GCD) of two numbers.


# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(10,30))

# Write a recursive function to find the sum of all elements in an array.
# def find(a):
#     if len(a)==0:
#         return 0
#     else:
#         return a[0]+find(a[1:])
# print(find([1,3,4,5]))

# Write a recursive function to check if a given array is sorted.
# def fun(a):
#     if len(a)<=1:
#         return True
#     elif a[0]>a[1]:
#         return False
#     else:
#         return fun(a[1:])
# print(fun([1,2,3,4,5]))

'''lambda'''

# #find the positive numbers
# p=[1,-1,2,-2,3,-3]
# x=list(filter(lambda a:a>0,p))
# print(x)

#find the strings which are palindrome
# k=['mom','level','bat','cat']
# c=list(filter(lambda a:a==a[::-1],k))
# print(c)

# #convert each string to capital letters
# t=['hello','python','hai','java']
# c=list(map(lambda a:a.upper(),t))
# print(c)

# #calculate length of each string
# y=['apple','banana','pineapple','mango']

# c=list(map(lambda a:len(a),y))
# print(c)


# find the maximum value
# e=[3,5,6,8,1]
# from functools import reduce
# c=reduce(lambda a,b:max(a,b),e)
# print(c)

 #concatenate them into a single string
# h=['hello','python','programming','language']
# from functools import reduce
# c=reduce(lambda a,b:a+b,h)
# print(c)

 #write a lambda fun to add 10 to a given number

# c=lambda a:a+10
# print(c(10))

# #reverse a string using reversed
# a="hello"
# b="".join(reversed(a))
# print(b)

"""pattern"""
# Square of stars pattern for n=5:
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()         

# Right-angle triangle of stars for n=5:
# n=6
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# Inverted right-angle triangle of stars for n=5:
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# Right-aligned triangle of stars for n=5:
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
    
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# Inverted right-aligned triangle of stars for n=5
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
# Repeating 5 pattern for n=5:
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("5",end=" ")
#     print()


# Repeating row number pattern for n=5:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()


# Increasing sequence of numbers pattern for n=6:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

# n=6
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# Alternating rows of 1 and 2 for n=5:

# 1
# 2 2
# 1 1 1
# 2 2 2 2
# 1 1 1 1 1

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if i%2==0:
#             print("1",end=" ")
#         else:
#             print("2",end=' ')
#     print()

# Continuous sequence pattern for n=5:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# p=1
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()

# Cross pattern with center row and column filled for n=5:

#   *    
# * * *
# * * * * *
# * * *
#   *

# n=5
# for i in range(n-1):
#     for j in range(n-i):
#         print(" ",end=" ")

#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()
 

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n=5
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print("*",end=" ") 
#         else:
#             print(" ",end=" ")


# k = 4  
# n = 5  
# for i in range(n):
#     p=k
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(n - i):
#         print(p, end=" ")
#         p -= 1  
#     k-=1
#     print() 

# define a class student that inherits from the person class . add an additional attribute 
#  student_id and a method to print students details , including the student ID

class Person :
    def details(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def details (self,name,age,id):
        self.id=id
        super().details(name,age)
    def print(self):
        print(f"name={self.name},age={self.age},id={self.id}")
a=Student()
a.details("anu",20,1)
a.print()


class Person :
    def details(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name={self.name},age={self.age}")
class Student(Person):
    def details (self,name,age,id):
        self.id=id
        super().details(name,age)
    def print(self):
        print(f"id={self.id}")
        super().display()
a=Student()
a.details("anu",20,1)
a.display()



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a=list(zip(l1,l2))
        b=[]
        for i,j in a:
            b.append(i+j)
        print(b)
       
s=Solution()
s.addTwoNumbers([2,4,3],[5,6,4])



# 1.write a function to find strings in a given list,starting with given prefix,no inbuilt function
# input prefix:ca
# [car,cat,fear,centre]
# output:[cat,car]


# a=['car','cat','fear','centre']
# b=[]
# for i in a:
#     if i[0]=="c" and i[1]=="a":
#         b=b+[i]       
# print(b)


# 2.a="have a nice day"
# output d="day nice a have"

# a="have a nice day"
# d=a.split( )
# print(d)
# e=d[::-1]
# print(e)
# f=" ".join(e)
# print(f)


# 3.s="malayalam"
# count each charac in string

# s="malayalam"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


# 4.
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print(i+1,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
        
# 1.Find the Maximum: Write a function to find the 
# largest number in a list without using built-in functions like max().

l=[15,22,34,2,3,5]
m=l[0]
for i in l:
    if i>m:
        m=i
print(m)


# given an array for random num given a task is to push all zeros to th given array to the end of the array
# first line contains an int value n denoting size of array next line contains elements of the array constarinsts
# 1<n<=50,1<=arr[i]<=100
# 5 1 0 0 3 0 out=1 3 0 0

