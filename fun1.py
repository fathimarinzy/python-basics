# def function_name(n):
#     print("success",n)
# function_name(10)

# def function_name(n,m):
#     print("success",n,m)
# function_name(10,20)


# # addition using fun
# def add(a,b):
#     print("sum=",a+b)
# add(10,20)

# def add(a,b):
#     print(a+b)
# x=int(input("enter 1 no:"))
# y=int(input("enter 2 no:"))
# add(x,y)


# #return stmt
# def add(a,b):
#    return a+b
# x=int(input("enter 1 no:"))
# y=int(input("enter 2 no:"))
# print(add(x,y))

# # #cannot use return and print stmt
# def add(a,b):
#     return a+b
#     # print a+b
# x=int(input("enter 1 no:"))
# y=int(input("enter 2 no:"))
# print(add(x,y))


# def fun(n):
#     print("success",n)
#     for i in n:
#         print(i)
# a=[10,20,30]
# fun(a)


# # #pass the list and finsd the sum
# def fun(n):
#     print("sum=",sum(a))
# a=[10,20,30]
# fun(a)

# #pass the string and check palindrome

# def fun(n):
#     if n == n[::-1]:
#         print("palindrome",n)
#     else:
#         print(" palindrome",n)
# a = "malayalam"
# fun(a)

# # calculator

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x // y

# def calculator():
#     print(" Calculator")
   
#     while True:
#       choice = input("\n1.add\n2.sub\n3.multiply\n4.div\n5.exit\nEnter your choice : ")

#       if choice == "1":
#         a = int(input("Enter first number: "))
#         b= int(input("Enter second number: "))
#         print( add(a,b))
#       elif choice == "2":
#         a = int(input("Enter first number: "))
#         b= int(input("Enter second number: "))
#         print( subtract (a,b))
#       elif choice == "3":
#         a = int(input("Enter first number: "))
#         b= int(input("Enter second number: "))
#         print( multiply(a,b))
#       elif choice == "4":
#         a = int(input("Enter first number: "))
#         b= int(input("Enter second number: "))
#         print(divide(a,b))
#       else:
#         print("exit")
#         break

# calculator()


# register and login
dic={}
def reg():
    username=int(input("enter the username:"))
    password=int(input("enter the password:"))
    dict[username]=password
    print("register successfull ")

def log():
    username=int(input("enter the username:"))
    password=int(input("enter the password:"))
    if username in dict and   dict[username]==password:
        print("login successfull ")
    else:
        print("invalid ")

while True:
      choice = int(input("\n1.register\n2.login\n3.exit\nEnter your choice : "))

      if choice == 1:
        reg()
      elif choice==2:
        log()
      elif choice==3:
        print("exit")
        break


def fun(name,age=30):
    print("sucess",name,age)
fun("ammu")
fun("anu",20)


#global variable , in local variable print stmt does not print outside the code
b=200
def fun():
    global a
    a=100
    print(a)
    print(b)
    print("success")
fun()
print(a)


# #arbitrary arguments
def display(*a):
    print(a)
display(10,20,30)


def display(a,b,c):
    print(a,b,c)
display(a=10,b=20,c=30)

#keyword arguments
def display(**a):
    print(a)
display(a=10,b=20,c=30)

# recursion
def display(n):
    if n==0:
        return n
    else:
        return n+display(n-1)
print(display(5))


# factorial of a num using recursion
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    
print(fact(5))

# sum of digits using  recursion
def sum(n):
   
    if n==0:
        return n
    else:
        return n%10+sum(n//10)

print(sum(1234))


# reverse a string using recursive fn
def rev(n):
    if len(n)==0:
        return n
    else:
     return n[-1]+ rev(n[:-1])

print(rev("hello"))


# #calculate x raised to power of n
def pow(a,b):
    if b==1:
      return a
    else:
       return a*pow(a,b-1)
print(pow(2,3))