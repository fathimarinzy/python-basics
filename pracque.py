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
n=int(input("\n1.taking input\n2.exit \nEnter the choice"))
while n>0:
    if n==1:
        b=int(input("enter the number:"))
    elif n==2:
        print("exiting")
        break