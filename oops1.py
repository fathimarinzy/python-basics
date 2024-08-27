#create a class
class Bird:
    eyes=2
    beak=1
parrot=Bird()
print(parrot.eyes)
print(parrot.beak)

# mul objects with one class
class Bird:
    eyes=2
    beak=1
parrot=Bird()
print(parrot.eyes)
print(parrot.beak)

peacock=Bird()
print(peacock.eyes)
print(peacock.beak)

class Bird:
    eyes=2
    beak=1
parrot=Bird()
print(parrot.beak)
parrot.eyes=1
print(parrot.eyes,"eyes")
peacock=Bird()
print(peacock.eyes)
print(peacock.beak)

# give a method
class Bird:
    eyes=2
    beak=1
    def fly(self):
        print("parrot")
parrot=Bird()
print(parrot.beak)
parrot.eyes=1
print(parrot.eyes,"eyes")
parrot.fly()
peacock=Bird()
print(peacock.eyes)
print(peacock.beak)
peacock.fly()

class Bird:
    eyes=2
    beak=1
    def fly(self,a):
     print(a)
parrot=Bird()
# print(parrot.beak)
# parrot.eyes=1
# print(parrot.eyes,"eyes")
parrot.fly("parrot")
peacock=Bird()
print(peacock.eyes)
print(peacock.beak)
peacock.fly("peacock")

   #use of instance variable
class Bird:
    eyes=2
    beak=1
    def fly(self,a):
       self.a=a
       print(a)
    def walk(self):
        print(self.a)


parrot=Bird()

parrot.fly("parrot")
parrot.walk()
parrot.eyes=1
peacock=Bird()
peacock.fly("peacock")


#create a 3 methods

class Add:
    def num(self,a,b):
        self.a=a
        self.b=b
        print(b)
    def calc(self):
       
        self.c=self.a+self.b
    def res(self):
        print(self.c)
add=Add()
add.num(10,20)
add.calc()
add.res()

#3 methods class=rectangle calculate area and perimeter

class Rectangle:
    def val(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        self.c=self.a*self.b
        print(self.c)
    def perimeter(self):
        self.d=2*self.a*self.b
        print(self.d)
rec=Rectangle()
rec.val(2,4)
rec.area()
rec.perimeter()

#3 method class=book display tilte and author
class Book:
    def tit(self,a):
        self.a=a
    def aut(self,b):
        self.b=b
    def display(self):
        # print(self.a + self.b)
        print(self.a)
        print(self.b) 
boo=Book()
boo.tit("Adujeevitham")
boo.aut("Benyamin")
boo.display()

#class=bank 4 methods
class Bank():
         
    def initialamount(self,initialamount):
        self.balance=initialamount
      
    def deposit(self,deposit):
       
        self.balance+=deposit
        print("current balance",self.balance)
       
    def withdraw(self,withdraw):
        if withdraw> self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= withdraw
            print("Current balance:", self.balance)
        
    def currentbalance(self):
        print("current balance=",self.balance)
bank=Bank()      
while True:
           
            choice=int(input("\n1.Add details\n2.Deposit\n3.Withdraw\n4.Current Balance\n5.Exit\nEnter your choice="))
            if choice==1:
                while True:
          
                    name=input("enter your name:")
                    acc=int(input("enter your acc no:"))
                    amount=int(input("Enter your initial balance :"))
                    bank.initialamount(amount)
                    break 
            elif choice==2:
                depo=int(input("Enter your deposit amount:"))
                bank.deposit(depo)
                
            elif choice==3:
                n=int(input("Enter your withdraw amount:"))
                bank.withdraw(n)
            elif choice==4:
                bank.currentbalance() 
            elif choice==5:
                print("Exit")
                break


#contruct
class student:
    college="abc"
    def __init__(self,a):
        print("welcome",a)
    def study(self):
        print("studying")
ammu=student(1000)       
print(ammu.college)
ammu.study()


#create class person that initialize with name and age with include a method
# displAY info that prints the name and age of tht person
class Person:
    
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def display(self):
        print("name",self.name)
        print("name",self.age)
p=Person("rinzy",19)
p.display()
# #
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area=",self.length*self.breadth)
p=Rectangle(10,30)
p.area()

# #
class Student:
    def __init__(self,name,grade):
        
        self.name=name
        self.grade=grade
    def average(self):
       self.avg=sum(self.grade)//len(self.grade)
    def display(self):
        print("name=",self.name)
        print("grade=",self.grade)
        print("average=",self.avg)
p=Student("rinzy",[85,90,78,92])
p.average()

#inheritance
class Father:
    def phone(self):
        print("phone is using")
    def walk(self):
        print("walking")
class Son(Father):
  
        print("studying")
f=Son()
f.phone()
f.walk()

class Father:
    def phone(self):
        print("phone is using")
    def walk(self):
        print("walking")
class Son(Father):
    def study(self):
        print("studying")
f=Son()
f.phone()
f.walk()
f.study()

#inheritance with constructor
class Father:
    def __init__(self):
        print("father page")
    def phone(self):
        print("phone is using")
    def walk(self):
        print("walking")
class Son(Father):
    def __init__(self):
        print("son page")
    def study(self):
        print("studying")
f=Son()
f.phone()
f.walk()
f.study()
#super method
class Father:
    def __init__(self,a):
        print("father page",a)
    def phone(self):
        print("phone is using")
    def walk(self):
        print("walking")
class Son(Father):
    def __init__(self,s,f):
        print("son page")
        super.__init__(f)#another method
        # Father.__init__(self)
    def study(self):
        print("studying")
f=Son()
f.phone()
f.walk()
f.study()


