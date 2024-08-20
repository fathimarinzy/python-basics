import os
# os.remove("abc.txt")
os.rmdir("txxxtis")

#to delete folder with files
import shutil
shutil.rmtree("hello")
with open("abc.txt","w") as file:
    x=file.write("worked")
    print(x)
file.close()


import math
print(math.factorial(5))
print(math.sqrt(25))
print(pow(2,5))

from math import factorial,sqrt
print(factorial(25))
print(sqrt(25))

from math import *
print(factorial(25))
print(sqrt(25))
print(ceil(1.9))
print(ceil(1.1))
print(floor(1.9))
print(floor(1.1))
print(pow(2,5))

import math
print(dir(math) )

import random
l=[1,2,3,4,5]
random.shuffle(l)
print(l)
print(random.choice(l))
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10,3))
print(random.sample(l,3))

# generate 100 lottery tickets and select two winner
import random
s=[random.randint(000000,999999) for i in range(100)]
print(random.sample(s,2))

# select 3 no btw 100 to 999 which is divisible by 5
import random
for i in range(3):
    print(random.randrange(100,999,5))

#check to find the computer guess and our guess is true
import random
com=random.randrange(0,9)
# print(com)
guess=0
while guess<3:
    n=int(input("enter the no:"))
    if com==n:
        print("you win")
        break
    else:
        print("you lose")
    guess+=1
else:
    print("game over")