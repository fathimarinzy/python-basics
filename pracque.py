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
def factor(num):
    fac=[]
  
    for i in range(1,num+1):
        if num%i==0:
            fac.append(i)
    if len(fac)==2:
        print("prime no")
    return fac
print(factor(9))