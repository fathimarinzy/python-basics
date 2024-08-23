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
out=[]
input=[2,7,11,15] 
for i in range(len(input)):
    for j in range(i+1,len(input)):
        if input[i]+input[j]==9:
            out=[i,j]
            print(out)
            break


# inp= l1=[a,b,c,d,e,f,g,h,i] l2=[0,1,1,0,1,2,2,0,1] otp= l3=[a,d,h,b,c,e,i,f,g]
l1= ['a','b','c','d','e','f','g','h','i']
l2=[0,1,1,0,1,2,2,0,1]
l3=[]
# for i  in range(len(l1)):
     