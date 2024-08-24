#check char is vowel or consonant
n=input("enter the char:")
m=['a','e','i','o','u']
if n in m:
    print("char")
else:
    print("consonant")

#reverse a given num
n=int(input("enter the no:"))
rev=0
while n>0:
    x=n%10
    rev=rev*10+x
    n//=10
print(rev)

# find duplicates char from a string
n='hello'
for i in n:
    if i.i:
        print(i)
