# x=[10,20,30,40,50]
# print(x)
# print(len(x))

# x=["python","java","php"]
# print(x)


# x=[True,False]
# print(x)
# x=[10,20,"python","java","php",True,False]
# print(x)

# print(type(x))

# for i in x:
#     print(i)

# for i in range(len(x)):
#     print(x[i])

# print(x[0])
# print(x[-1])
# print(x[2:6])
# print(x[-6:-2])
# print(x[::-1])
# a="hai"
# x=list(a)
# print(x)


# x=["python","java","php"]
# x.append("dotnet")
# print(x)

# x=["python","java","php"]
# x.insert(2,"dotnet")
# print(x)

# x=["python","java","php"]
# z=[10,20,30,40,50]
# x.extend(z)
# print(x)


# p="hello"
# z.extend(p)
# print(z)


# n=int(input("enter the no:"))
# a=[" ","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","forteen","fifteen","sixteen","seventeen","eighteen"]
# b=[" "," ","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety" ]
# if n<20:
#  print(a[n])
# elif a>=20 and a<=99:
#  x=n%10
#  y=n//10
#  if y==0:
#   print(b[y])
#  else:
#   print(b[y]+b[x])
 




# a=[]
# for i in range(1,11):
#   n=int(input("enter the no:"))
#   print(n)
#   a.append(n)
#   print(a)


# x=["M","na","i","ke"]
# y=["y","me","s","lly"]
# z=[]
# for i in range(len(x)):

#  z.append(x[i]+y[i])
# print(z)

# list1=["hello","hai"]
# list2=["dear","madam"]
# z=[]
# for i in range(len(list1)):
#   for j in range(len(list2)):
  
#     z.append(list1[i]+list2[j])
 
# print(z)


# z=['My','name','is','kelly','name']
# print(z.index('name'))
# print(z.count('name'))
# z.clear()
# print(z)
# z.reverse()
# print(z)
# z.sort()
# print(z)
# z.pop()
# print(z)
# x=z.pop(2)
# print(x)
# print(z)
# z.remove("My")
# print(z)
# x=z.copy()
# print(x)
# list=[1,2,3,4,5,6]
# # for i in range(len(list)):
    
# #  print(list[i])
# # for i in list:
# #     print(i)
# i=0
# while i <len(list):
#     i+=1
#     print(i)




#pgm to add item after 6000 in the following list 
# list=[10,20,[300,400,[5000,6000],500],30,40]
# print(list[2])
# print(list[2][2])
# list[2][2].append(7000)
# print(list[2][2])
# print(list)


#pgm to add sublist ["h","i","j"]

# list=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
# print(list[2][1][2])
# list[2][1][2].extend('h' 'i' 'j')
# print(list)


#remove all occurence of item 20
# list=[5,20,15,20,25,50,20] 
# for i in list:
#     if i==20:
#      list.remove(i)
# print(list)


#to find value 20 in the list ,and if it is present ,replace it with 200.only update the first occurence of an item
# list=[5,10,15,20,25,50,20]
# for i in range(len(list)):
#   if list[i]==20:
#     list[i]=200
#     break

# print(list)


#output is "day nice a have"
# a= "have a nice day"
# x=a.split()

# x.reverse()
# # print(x)
# z=" ".join(x)
# print(z)


#without duplicates
# l=[1,2,3,5,4,2,1,3,5,4]   
# z=[]
# for i in l:
#     if i not in z:
#         z.append(i)
# print(z)
   


#sum of list  items
# l=[1,2,3,5,4,2,1,3,5,4]   
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
#another method
# l=[1,2,3,5,4,2,1,3,5,4] 
# z=sum(l)
# print(z)    

#find the max and min items in list
l=[11,84,56,19,73,56]
# l.sort()
# a=min(l)
# b=max(l)
# print(a)
# print(b)
#another method
# l.sort()
# print("min:",l[0])
# print("max:",l[-1])
    


#list comprehension
# a="python"
# x=[i for i in a]
# print(x)

# x=[i*i for i in range(1,11)]
# print(x)

# s=[1,2,3,4,5,6,7,8,9,10]
# x=[i for i in s if i%2==0]
# print(x)


# s=[1,2,3,4,5,6,7,8,9,10]
# x=[i for i in s if i%2==0 if i%5==0]   #or
# x=[i for i in s if i%2==0 and i%5==0]
# print(x)


#using list comprehension check palindrome
# l=["madam","level","random","python","mom"]
# x=[i for i in l if i==i[::-1]]
# print(x)

#convert this string items to uppecase
# p=["hai","hello","welcome"]

# x=[i.upper() for i in p  ]
# print(x)


#find common elements in list
# x=[1,2,3,4,5]
# y=[2,3,5,6,8]
# x=[i for i in x  if i in y ]
# print(x) 


#convert the pos number to true and the neg no to false
# f=[-2,-1,5,1,2] 
# x=[i>0 for i in f ]
# print(x)

#remove all vowels
# s=" list comprehension is simple"

# x=[i for i in s if i not in 'aeiou']
# y=" ".join(x)
# print(y)



#print the half of the items in the list
# l=[10,20,30,40,50,31]
# x=[i/2 for i in l]
# print(x)

#matrix 2*2
# a=[[1,2],[3,4]]
# for i in a:
#     for j in i:
#         print(j,end=" ")
#     print()

# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     for j in i:
#         print(j,end=" ")
#     print()

#addition of matrix
# a=[[1,2],[3,4]]
# b=[[1,2],[3,4]]
# c=[[0,0],[0,0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         c[i][j]=a[i][j]+b[i][j]
# print(c)

#create a matrix
# a=int(input("enter the rows :"))
# b=int(input("enter the columns:"))
# mat=[]
# for i in range(a):
#     first=[]
#     for j in range(b):
#        values=int(input("enter the values:"))
#        first.append(values)
#     mat.append(first)
# print(mat)
       

#3*3 multiplication
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[1,2,3],[4,5,6],[7,8,9]]
# c=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range (len(a)):
#     for j in range(len(b)):
#         for k in range(len(c)):
#          c[i][j]+=a[i][k]*b[k][j]
        
# print(c)


#transpose of a matrix
# a=[[1,2,3]
#    [4,5,6],
#    [7,8,9]]
# b=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a)):
#         b[j][i]=a[i][j]
# for i in b:
#     print(i)


