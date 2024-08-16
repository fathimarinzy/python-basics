# a='heelo'
# print(a)

# a="heelo"
# print(a)

# a=int(input("enter the NAME:"))
# print(a)
# print(type(a))


# s="hello world"
# print(len(s))

# p="hello"
# # print(p[0])
# # print(p[1])
# # print(p[5])

# print(p[-1])
# print(p[-2])


# a="helloworld"
# # print(a[2:6])
# # 
# # print(a[-5:-1])
# # print(a[::-1])
# # print(a[::-2])

# # print(a[1:5])
# print(a[-1:-5:-1])

# a="hello"
# b="world"
# # print(a,b)
# # print(a+b)
# # print(a+" "+b)

# a="hello world"
# print(dir(a))
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.count("l"))
# print(a.index("o"))
# print(a.find("m"))
# print(a.rindex("l"))
# print(a.rfind("l"))
# print(a.title())
# print(a.capitalize())
# print(a.istitle())
# print(a.isupper())
# print(a.islower())


# a="helloworld123"
# print(a.isalpha())


# a="1234"
# print(a.isalnum())


# a="allla 11"
# print(a.isalnum())


# a="&&&&"
# print(a.isalnum())


# a="hekkoworld"
# x=a.replace("o","&")
# print(x)

# a="ẞ"
# print(a.lower())
# print(a.casefold())

# a="123"
# print(a.isdigit())
# print(a.isnumeric())
# print(a.isdecimal())

# a="¾"
# print(a.isdigit())
# print(a.isnumeric())
# print(a.isdecimal())

# a="8^2"
# print(a.isdigit())
# print(a.isnumeric())
# print(a.isdecimal())



#to count the num of lowercase and uppercase caharcter in as tring accepted from string

# n=str(input("enter the string:"))
# lower=0
# upper=0
# for i in n:
#     if i.islower():
#       lower+=1

#     elif i.isupper:
#        upper+=1
# print("lower=",lower)
# print("upper=",upper)



#pgm to accept accept a string and count number of vowels
# n=str(input("enter the string="))
# s=0
# p=['a','e','i','o','u']
# for i in n:
#    if i in p:
#     s+=1
# print(s)  
  

#pgm to accept string and display total no of alphabets

# n=str(input("enter the string="))
# alpha=0
# for i in n:
#     if i.isalpha():
#         alpha+=1

# print("total no alphabets=",alpha)

#pgm to count the length of string without using inbuilt function
# n=str(input("enter the string="))
# count=0
# for i in n:
#     count+=1
# print(count) 

#pgm to count the uppercase and lowercase without using inbuilt function
# n="helloHELLO"
# lower=0
# upper=0
# P=['h','e','l','l','o']
# q=['H','E','L','L','O']
# for i in n:
#     if i in P:
#         lower+=1
#     elif i in q:
#         upper+=1
# print("no of lower=",lower)
# print("no of upper=",upper)

# print num  in a string 
# n="alpha1234"
# count=0
# for i in n:
#     if i.isdecimal():
#         count+=1
# print(count)



#find the sum of num in string
# n="alpha1234"
# sum=0
# for i in n:
#     if i.isdecimal():
#         sum+=int(i)
# print("sum:",sum)


# n="ending"
# if len(n)<2:
#     print(n)
# elif  n.endswith("ing"):
#     x=n[:-3]
#     print(x+"ly")
# elif len(n)>3:
#    print(n+"ing")
# print()    

    
# a="restart"
# a=a[::-1].replace("r","$",1)[::-1]
# print(a)

# a="hello world"
# print(a.startswith("h"))
# print(a.startswith("e"))
# print(a.startswith("hello"))
# print(a.endswith("d"))
# print(a.endswith("world"))
# print(a.endswith("hello"))

# a="qai hello.hello hai"
# print(a.startswith("ello",5,8))
# print(a.endswith("a",0,2))
# print(a.endswith("i",0,3))
# print(a.endswith("e",0,6))


# #convert string to list
# a="hello,hai,hello"
# x=a.split(",")
# print(x)

# #convert list to string

# a=['hello','hai','hello']
# z=" ".join(a)
# print(z)

# a="hello"
# x=a.zfill(20)
# print(x)
# a="hello"
# x=a.zfill(5)
# print(x)
# a="hello"
# x=a.zfill(2)
# print(x)

# a="hello"
# x=a.center(20)
# print(x)
# a="hello"
# x=a.center(20,"$")
# print(x)

# a="hello"
# x=a.ljust(20,"&")
# print(x)
# a="hello"
# x=a.ljust(20)
# print(x)
# a="hello"
# x=a.rjust(20)
# print(x)



# a=" "
# print(a.isspace())


# a="hello world"
# x=a.removeprefix("hello")
# print(x)
# x=a.removesuffix("world")
# print(x)


# a="abc"
# print(a.isidentifier())
# A="ABC"
# print(A.isidentifier())

# a="1abc"
# print(a.isidentifier())
# a="a$%bc"
# print(a.isidentifier())
# a="_abc"
# print(a.isidentifier())
# a="abc23"
# print(a.isidentifier())

# a="wel\ncome"
# print(a)
# a="wel\tcome"
# print(a)
# a="wel\bcome"
# print(a)


# print("/\\/\\/\\")

# a="hai how are you \\"
# a="its raining outside"
# a="you are studying\"python programming\"language"
# print(a)

# a="hello,hai,hello,hai,hello,hai"
# x=a.split(",",2)
# print(x)

# a="hello,hai,hello,hai,hello,hai"
# x=a.rsplit(",",2)
# print(x)


# a="abc"
# print(a.isprintable())

# a="abc34555"
# print(a.isprintable())


# a="abc77##55"
# print(a.isprintable())

# a="abc       "
# print(a.isprintable())


# a="ab\nc"
# print(a.isprintable())

# a="@@@@@@@@@@welcome@@@@@@@@"
# print(a.strip("@"))
# print(a.rstrip("@"))
# print(a.lstrip("@"))


# print("my name is {} my age is {} my hobby is{}".format("ammu",10,"playing"))
# print("my name is {1} my age is {2} my hobby is{0}".format("ammu",10,"playing"))
# print("my name is {a} my age is {b} my hobby is{c}".format(a="ammu",b=10,c="playing"))


# a="ammu"
# b=10
# c=10.25
# print("my name is %s"%a)
# print("my name is %d"%b)
# print("my name is %f"%c)

# a="ammu"
# print(f"my name is{a}")

# a="hello\nhai\nhello"
# # a=a.split()
# # print(a)
# a=a.splitlines(True)
# print(a)

# a="hello world"
# result=a.maketrans("hello","12345")
# y=a.translate(result)
# print(y)

# a={"name":"ammu","age":10,"course":"python"}
# s={'"NAME":{name},"AGE":{age}'.format_map(a)}
# print(s)


# a="hello welcome hai"
# print(a.partition("welcome"))


# a="hello welcome hai"
# print(a.rpartition("welcome"))


# a="hello welcome hai"
# print(a.partition("hello"))


# a="hello welcome hai"
# print(a.rpartition("hello"))


# a="hello welcome hai"
# print(a.rpartition("abc"))

# a="hello welcome hai"
# print(a.partition("abc"))


# a="wel\tcome"
# # print(a)
# print(a.expandtabs())
# print(a.expandtabs(1))
# print(a.expandtabs(2))
# print(a.expandtabs(3))
# print(a.expandtabs(4))
# print(a.expandtabs(5))
# print(a.expandtabs(6))
# print(a.expandtabs(7))
# print(a.expandtabs(8))
# print(a.expandtabs(9))
# print(a.expandtabs(10))



# a="abc"
# print(a.isascii())

# a="abHHHHc"
# print(a.isascii())

# a="ab55765c"
# print(a.isascii())


# a=" "
# print(a.isascii())


# a="ab%$$c"
# print(a.isascii())

# a="\n"
# print(a.isascii())

# a=65
# print(chr(a))

# print(ord(65))

# text="string"
# a=text.encode("ascii")
# print(a)  