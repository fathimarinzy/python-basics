# i=0
# while i<5:
#     print(i)
# i=0
# while i<5:
#     i+=1
#     print(i)

# i=0
# while i<10:
#     i=i+1
#     print(i)
# i=0
# i%2==0
# i=0
# while i<=10:
#     i=i%2==0
#     print(i)

# i=0
# while i<10:
#     i=i+1
#     print(i,'-',i*i)
# i=0
# a=2
# while i<10:
#     print(a)
#     a+=2
#     i+=1

# i=0
# a=1
# while i<10:
#     print(a)
#     a+=2    
#     i+=1   

# i=0
# a=10
# while i<50:
#     print(a)
#     i+=10
#     a+=10


# a=20
# while a>=2:
#     print(a )
#     a-=2


# sum=0
# number=1
# while number<=10:
#     sum+=number
#     number+=1
#     print(sum)

# n=10
# sum=n*(n+1)//2
# print("sum=",sum)

# sum=0
# n=2
# i=0
# while i<10:
   
#     sum+=n
#     n+=2
#     i+=1
# print(sum)
   
# n=10
# sum=n*(n+1)
# print(sum)

# n=int(input("enter the no:"))
# i=1
# while i<=10:
#     print(f"{i}*{n}={i*n}")
#     i+=1



# start=int(input("enter the start no:"))
# end=int(input("enter the end no:"))

# while start<=end:
#     print(start)
#     start+=2




# n=int(input("enter the no:"))
# i=2
# prime= True
# while i<n:
#     if n%i==0:
#         print("nota prime no")
#         prime= False
#         break
#     i+=1
# if prime:
#     print("prime no")


# n=str(input("enter the no:"))
# sum=0
# i=0
# while i<len(n):
#     i+=1 
#     sum+=i
# print(sum)

# n=int(input("enter the no"))
# count=0
# sum=0
# while n>0:
#     n//=10
#     count+=1
#     sum+=count
# print(sum)

# n=int(input("enter the no"))
# count=0
# while n>0:
#     n//=10
#     count+=1
#     if n=*count:
#         print()

# a=int(input("enter the no"))
# reverse=0
# while a>0:
#     x=a%10
#     reverse=reverse*10+x
#     a//=10
# print(reverse)
# a=123
# x=a%10
# print(x)

n=int((input("enter the no:")))
m=n
reverse=0
while m>0:
    x=n%10
    reverse=reverse*10+x
    n//=10
if  reverse==m :
    print("palindrome")

else:
    print("not a plaindrome")


# n=int(input("enter the no:"))

# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10

# print(sum)

# n=int(input("enter the no:"))
# m=n
# i=0
# sum=0
# product=0
# temp =n
# spi=0
# while temp!=0:
#     temp//=0
#     sum+=i
#     i+=1
# temp=n
# while temp!=0:
#     d=temp%10
#     product+=i
   
#     i+=1
# if spi==m:
#     print("spi ")
# else:
#     print("npt")

# i=0
# while i<5:
#     if i==3:
#         break
#     i+=1
#     print(i)
# else:
#     print("finished")

# i=0
# while i<5:
#     i+=1
#     if i==3:
#       continue
   
#     print(i)
# else:
#     print("finished")

#pass stmt
# i=0
# while i<5:
#     pass



#for loop

# for i in "python":
#     print(i)

# for i in range(2,5):
#     print(i)
# for i in range(5):
#     print(i)

# for i in range(1,10,2):
#     print(i)


#print 1 t0 10 no
# for i in range (1,11):
#     print(i)

#odd no btw 1 and 100

# for i in range(1,101,2):

#     print(i)

#print series
# for i in range (10,110,10):
#     print(i)

#print series 105 to 7

# for i in range(105,0,-7):
#     print(i)

#multiple of 3
# for i in range(3,31,3):
#     print(i)


#factorial of a num
# a = int(input("enter the no:"))
# fact=1
# for i in range(1,a+1):
#     fact*=i
# print(fact)

#pattern
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#square
# n=
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")

#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()    

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# n =5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("5" , end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()    

# n=6
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end=" ")



# for i in range(1,6):
#     for j in range(1,i+1):
#        if i%2==0:
#            print(2,end=" ")
#        else:
#             print(1,end=" ")    

#     print()       
# p=1
# for i in range(1,6):
#     for j in range(i):
#         print(p,end=" ")
#         p+=1
#     print()


# n=5
# for i in range(n):
#     for j in range(n):
#      if i==n//2 or j==n//2:
#         print("*",end=" ")
#      else:
#         print(" ",end=" ")

#     print()


# n=5
# for i in range(n):
#     for j in range(n):
#      if i==j or i+j==n-1:
#         print("*",end=" ")
#      else:
#         print(" ",end=" ")

#     print()

# print("hello")
# print("hai")


#reverse of string 

# n="hello"
# p=" "
# for i in n:
#    p=i+p
# print(p)
    