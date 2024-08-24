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
list=[1,0,2,0,4,6]

for i in list:
    if i==0:
      list.remove(0)
      list.append(0)
print(list)


#write a python function that takes a list and returns a new list with distinct elements
#from the list

def fun(n):
    m=[]
    # print(" list=",n)
    for i in n :
      if i not in m:
        m.append(i)
    print("new list=",m)
list=[1,2,3,3,3,3,4,5]
fun(list)


 #find the missing number
def display(l):
   n=len(l)+1
   total=n*(n+1)//2
   total_l=sum(l)
   missing=total-total_l 
   return missing
list=[1,2,4,5,6]
print(display(list))


# what is the python prgrm to find pairs of numbers from a given list such
# that the sum of their squares equala a perfect square ? a^2+b^2=c^2.
# input: a=[1,2,3,4,5,6,7,8,9,10]
# output:3,4,5,6,8,10
import math
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(a):
    for j in range(a):
        c=a[i^2]+a[j^2]
        

      

