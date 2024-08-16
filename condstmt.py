a=11
if a<10:
    print("a is less than 10")
else :
    print("a is greater")

a = int(input("enter the no:" ))
if a< 0:
    print("negative")
elif a>0:
    print("positive")
elif a==0:
    print("equal")
else:
    print("invalid")

a=10
b=20
c=30
if a>b and a>c:
    print("a is the largest")
elif b>a and b>c:
    print("b is the greatest")
elif c>b and c>a:
    print("c is the larest")
else:
    print("invalid")
  



a =int(input("enter the no:"))
if a%2==0:
   print("even no")
else :
    print("odd no")

a= int(input("enter the no:"))
if a>=18:
    print("person is eligible to vote")
else:
    print("not eligible to not")
  
n =int(input("enter the no:"))
if n%5==0 :
    print("hello")
else:
    print("bye")
n= int(input("enter the no:"))
if n%7==0:
    print("divisible by 7")
else:
    print("not divisible by 7")
a= int(input("enter the no:"))
n=a%10
print(n)
if n%3==0:
    print("it is divisible by 3")
else:
    print("not divisible by 3")

n=int(input("enter the no:"))
if n%2==0 and n%3==0:
    print("the no is divisible by 2 and 3")
else:
    print("not divisible by 2 and 3")

n= input("enter the character:")
a = "aeiou"
print(a)
if n in a:
    print("character is vowel")
else:
    print("not vowel")

a=int(input("enter the no:"))
if a==1:
    print("sunday")
elif a==2:
    print("monday")
elif a==3:
    print("tue")
elif a==4:
    print("wed")
elif a==5:
    print("thur")
elif a==6:
    print("fri")
elif a==7:
    print("sat")
else:
    print("enter the no")

a =int(input("enter the no:"))
if 1<=  a<=10:
    print("in range") 
else:
    print("not in range")
a=int(input("enter the no:"))
if a%2==0:
    print("divisible by 2")
    if a%5==0:
        print("divisible by 5")
    else:
        print("not divisible by 5")
else:
    print("not divisible by 2")
    if a%5==0:
        print("divisible by 5")
    else:
        print("not divisible by 5")


a=10
b=20
print(a)
print(b)
temp=a
a=b 
b=temp
print(a)
print(b)

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)