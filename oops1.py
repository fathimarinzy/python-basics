# # #create a class
# # class Bird:
# #     eyes=2
# #     beak=1
# # parrot=Bird()
# # print(parrot.eyes)
# # print(parrot.beak)

# # # mul objects with one class
# # class Bird:
# #     eyes=2
# #     beak=1
# # parrot=Bird()
# # print(parrot.eyes)
# # print(parrot.beak)

# # peacock=Bird()
# # print(peacock.eyes)
# # print(peacock.beak)

# # class Bird:
# #     eyes=2
# #     beak=1
# # parrot=Bird()
# # print(parrot.beak)
# # parrot.eyes=1
# # print(parrot.eyes,"eyes")
# # peacock=Bird()
# # print(peacock.eyes)
# # print(peacock.beak)

# # # give a method
# # class Bird:
# #     eyes=2
# #     beak=1
# #     def fly(self):
# #         print("parrot")
# # parrot=Bird()
# # print(parrot.beak)
# # parrot.eyes=1
# # print(parrot.eyes,"eyes")
# # parrot.fly()
# # peacock=Bird()
# # print(peacock.eyes)
# # print(peacock.beak)
# # peacock.fly()

# # class Bird:
# #     eyes=2
# #     beak=1
# #     def fly(self,a):
# #      print(a)
# # parrot=Bird()
# # # print(parrot.beak)
# # # parrot.eyes=1
# # # print(parrot.eyes,"eyes")
# # parrot.fly("parrot")
# # peacock=Bird()
# # print(peacock.eyes)
# # print(peacock.beak)
# # peacock.fly("peacock")

# #    #use of instance variable
# # class Bird:
# #     eyes=2
# #     beak=1
# #     def fly(self,a):
# #        self.a=a
# #        print(a)
# #     def walk(self):
# #         print(self.a)


# # parrot=Bird()

# # parrot.fly("parrot")
# # parrot.walk()
# # parrot.eyes=1
# # peacock=Bird()
# # peacock.fly("peacock")


# # #create a 3 methods

# # class Add:
# #     def num(self,a,b):
# #         self.a=a
# #         self.b=b
# #         print(b)
# #     def calc(self):
       
# #         self.c=self.a+self.b
# #     def res(self):
# #         print(self.c)
# # add=Add()
# # add.num(10,20)
# # add.calc()
# # add.res()

# # #3 methods class=rectangle calculate area and perimeter

# # class Rectangle:
# #     def val(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def area(self):
# #         self.c=self.a*self.b
# #         print(self.c)
# #     def perimeter(self):
# #         self.d=2*self.a*self.b
# #         print(self.d)
# # rec=Rectangle()
# # rec.val(2,4)
# # rec.area()
# # rec.perimeter()

# # #3 method class=book display tilte and author
# # class Book:
# #     def tit(self,a):
# #         self.a=a
# #     def aut(self,b):
# #         self.b=b
# #     def display(self):
# #         # print(self.a + self.b)
# #         print(self.a)
# #         print(self.b) 
# # boo=Book()
# # boo.tit("Adujeevitham")
# # boo.aut("Benyamin")
# # boo.display()

# # #class=bank 4 methods
# # class Bank():
         
# #     def initialamount(self,initialamount):
# #         self.balance=initialamount
      
# #     def deposit(self,deposit):
       
# #         self.balance+=deposit
# #         print("current balance",self.balance)
       
# #     def withdraw(self,withdraw):
# #         if withdraw> self.balance:
# #             print("Insufficient balance!")
# #         else:
# #             self.balance -= withdraw
# #             print("Current balance:", self.balance)
        
# #     def currentbalance(self):
# #         print("current balance=",self.balance)
# # bank=Bank()      
# # while True:
           
# #             choice=int(input("\n1.Add details\n2.Deposit\n3.Withdraw\n4.Current Balance\n5.Exit\nEnter your choice="))
# #             if choice==1:
# #                 while True:
          
# #                     name=input("enter your name:")
# #                     acc=int(input("enter your acc no:"))
# #                     amount=int(input("Enter your initial balance :"))
# #                     bank.initialamount(amount)
# #                     break 
# #             elif choice==2:
# #                 depo=int(input("Enter your deposit amount:"))
# #                 bank.deposit(depo)
                
# #             elif choice==3:
# #                 n=int(input("Enter your withdraw amount:"))
# #                 bank.withdraw(n)
# #             elif choice==4:
# #                 bank.currentbalance() 
# #             elif choice==5:
# #                 print("Exit")
# #                 break


# # #contruct
# # class student:
# #     college="abc"
# #     def __init__(self,a):
# #         print("welcome",a)
# #     def study(self):
# #         print("studying")
# # ammu=student(1000)       
# # print(ammu.college)
# # ammu.study()


# # #create class person that initialize with name and age with include a method
# # # displAY info that prints the name and age of tht person
# # class Person:
    
# #     def __init__(self,name,age) :
# #         self.name=name
# #         self.age=age
# #     def display(self):
# #         print("name",self.name)
# #         print("name",self.age)
# # p=Person("rinzy",19)
# # p.display()
# # # #
# # class Rectangle:
# #     def __init__(self,length,breadth):
# #         self.length=length
# #         self.breadth=breadth
# #     def area(self):
# #         print("area=",self.length*self.breadth)
# # p=Rectangle(10,30)
# # p.area()

# # # #
# # class Student:
# #     def __init__(self,name,grade):
        
# #         self.name=name
# #         self.grade=grade
# #     def average(self):
# #        self.avg=sum(self.grade)//len(self.grade)
# #     def display(self):
# #         print("name=",self.name)
# #         print("grade=",self.grade)
# #         print("average=",self.avg)
# # p=Student("rinzy",[85,90,78,92])
# # p.average()

# # #inheritance
# ##single inheritance
# # class Father:
# #     def phone(self):
# #         print("phone is using")
# #     def walk(self):
# #         print("walking")
# # class Son(Father):
  
# #         print("studying")
# # f=Son()
# # f.phone()
# # f.walk()

# # class Father:
# #     def phone(self):
# #         print("phone is using")
# #     def walk(self):
# #         print("walking")
# # class Son(Father):
# #     def study(self):
# #         print("studying")
# # f=Son()
# # f.phone()
# # f.walk()
# # f.study()

# # #inheritance with constructor
# # class Father:
# #     def __init__(self):
# #         print("father page")
# #     def phone(self):
# #         print("phone is using")
# #     def walk(self):
# #         print("walking")
# # class Son(Father):
# #     def __init__(self):
# #         print("son page")
# #     def study(self):
# #         print("studying")
# # f=Son()
# # f.phone()
# # f.walk()
# # f.study()
# # #super method
# class Father:
#     def __init__(self,a):
#         print("father page",a)
#     def phone(self):
#         print("phone is using")
#     def walk(self):
#         print("walking")
# class Son(Father):
#     def __init__(self,s,f):
#         print("son page")
#         super().__init__(f)#another method
#         # Father.__init__(self)
#     def study(self):
#         print("studying")
# f=Son("son","father")
# f.phone()
# f.walk()



# #multilevel inheritance
# class Grandfather :
#     def phone(self):
#         print("phone is using")
# class Father(Grandfather):
#     def walk(self):
#         print("walking")
# class Son(Father):
#     def study(self):
#         print("studying")
# f=Son()
# f.study()
# f.phone()
# f.walk()

# #multiple inheritance
# class Father:
#     def phone(self):
#         print("phone is using")
# class Mother :
#     def  walk(self):
#         print("walking")
# class Son(Mother,Father):
#     def study(self):
#         print("studying")
# f=Son()
# f.study()
# f.phone()
# f.walk()
# # same method in parent 
# class Father:
#     def walk(self):
#         print("phone is using")
# class Mother :
#     def  walk(self):
#         print("walking")
# class Son(Mother,Father):
#     def study(self):
#         print("studying")
# f=Son()
# f.study()
# f.walk()

# # #hierarchial inheritance
# class Vehicle:
#     def acceleration(self):
#         print("vehicle class")
# class Car(Vehicle):
#     def four(self):
#         print("four wheeler")
# class Bike(Vehicle):
#     def two(self):
#         print("two wheeler")
# f=Car()
# f.four()
# f.acceleration()
# # f.two() #car has no method two .car and bike has no relation
# ff=Bike()
# # ff.four() #bike has no method four .car and bike has no relation
# ff.acceleration()
# ff.two()

# #hybrid inheritance
# class Grandfather :
#     def phone(self):
#         print("phone is using") #single
# class Father(Grandfather):
#     def walk(self):
#         print("walking")
# class Son(Grandfather):
#     def Study(self):
#         print("studying")
# class Grandson(Father,Son):#multiple
#     def Eat(self):
#         print("eating")
# obj=Grandson()
# obj.Eat()
# obj.Study()
# obj.walk()
# obj.phone()
# print(Grandson.__mro__)

# # constructor in multilevel
# class Grandfather:
#     def __init__(self,g):
#         print("grandfather page")
#     def phone(self):
#         print("phone is using")
# class Father(Grandfather):
#     def __init__(self,f,g):
#         print("father page")
#         super().__init__(g)
#     def walk(self):
#         print("walking")
# class Son(Father):
#     def __init__(self,s,f,g):
#         print("son page")
#         super().__init__(f,g)
#     def study(self):
#         print("studying")
# obj=Son('s','f','g')
# obj.study()

#polymorphism
# #method overloading does not support in python
# class Student:
#     def display(self,a,b):
#         print(a+b)
#     def display(self,a,b,c):
#         print(a+b+c)
# s=Student()
# s.display(10,20)

# # constructor overloading does not in python
# class Student:
#     def __init__(self,a,b):
#         print(a+b)
#     def __init__(self,a,b,c):
#         print(a+b+c)
# s=Student(10,20)
# # operator overloading 
# # using magic methods
# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#         print(self.a+other.a)
# s=Student(10)
# ss=Student(20)
# s+ss
# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __sub__(self,other):
#         print(self.a-other.a)
# s=Student(20)
# ss=Student(10)
# s-ss

# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __mul__(self,other):
#         print(self.a*other.a)
# s=Student(20)
# ss=Student(10)
# s*ss
# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __pow__(self,other):
#         print(self.a**other.a)
# s=Student(20)
# ss=Student(10)
# s**ss
# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __truediv__(self,other):
#         print(self.a/other.a)
# s=Student(20)
# ss=Student(10)
# s/ss

# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __floordiv__(self,other):
#         print(self.a//other.a)
# s=Student(20)
# ss=Student(10)
# s//ss

# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __mod__(self,other):
#         print(self.a%other.a)
# s=Student(20)
# ss=Student(10)
# s%ss

# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __gt__(self,other):
#         print(self.a>other.a)
# s=Student(20)
# ss=Student(10)
# s>ss

# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __lt__(self,other):
#         print(self.a<other.a)
# s=Student(20)
# ss=Student(10)
# s<ss

# class Student:
#     def __init__(self,a):
#         self.a=a
#     def __ge__(self,other):
#         print(self.a>=other.a)
# s=Student(20)
# ss=Student(10)
# s>=ss

# # overriding
# #method overriding
# class Father:
#     def phone(self):
#         print("father can only call")
# class Son(Father):
#     def phone(self):
#         print("son can call,video call,masg,take img")
#         super().phone() 
# s=Son()
# s.phone()

# #constructor overriding
# class father:
#     def __init__(self):
#         print("father")
# class Son(Father):
#     def __init__(self):
#         print("son")
#         super().__init__()
# a=Son()

# #encapsulation
# #private
# class Father:
#     __name='abc'
#     def __init__(self):
#         print("working")
#         print(self.__name)
#         self.__phone()
#     def __phone(self):
       
#         print("father can only call")
# s=Father()

# ##protected
# class Father:
#     _name="abc"
#     def __init__(self):
#         print("working")
#     def _phone(self):
#         print("father can only call")
        
# class Son(Father):
#     def __init__(self):
#         print("son")
#         print(self._name)
#         self._phone()
# s=Son()

# ##some methods
# class A:
#     def show1(self):
#         print("a")
# class B(A):
#     def show2(self):
#         print("b")
# class C:
#     def show3(self):
#         print("c")
# class D(C):
#     def show4(self):
#         print("d")

# b1=B()
# d1=D()
# print(issubclass(B,A))
# print(issubclass(C,A))
# print(isinstance(b1,B))
# print(isinstance(b1,A))
# print(isinstance(d1,B))
# print(isinstance(d1,C))


# ##attribute methods
# #hasattr#setattre#getattr
# class Student:
#     name="ammu"
#     age=10
#     course="python"
# s=Student()
# print(s.name)
# print(hasattr(s,"name"))
# print(hasattr(s,"mark"))
# print(getattr(s,"name"))
# setattr(s,"name","anu")
# print(s.name)
# setattr(s,"mark",100)
# print(s.mark)
# delattr(Student,"age")
# print(s.age)

##docstring
class A:
    """this is a class of A"""
    def show1(self):
        print("a")
class B(A):
    """this is a class of B"""
    def show2(self):
        print("b")
class C:
    def show3(self):
        print("c")
class D(C):
    def show4(self):
        print("d")

b1=B()
d1=D()
print(A.__doc__)
print(B.__doc__)


print("""hello  hai   
      hello
      helllo""")


#decorators
#instance method
class Student:
    class_variable=0
    def __init__(self,name):
        self.name=name
    def modify(self,newname):
        self.name=newname
        self.__class__.class_variable+=1
        #__class__ is a special attribute that allows an instance of a class to access its class
s=Student("ammu")
print(s.name)
print(Student.class_variable)
s.modify("anu")
print(s.name)
print(Student.class_variable,"pppppp")

#class method
class Student:
    class_variable=0
    def __init__(self,name):
        self.name=name
    @classmethod
    def modify(cls):
        cls.class_variable+=1
          
s=Student("ammu")
print(s.name)
print(Student.class_variable)
# s.modify("anu")
# print(s.name)
Student.modify("anu")
print(s.name)
print(Student.class_variable,"pppppp")


#static method
class Student:
    class_variable=0
    def __init__(self,name):
        self.name=name
    @staticmethod
    def modify(a,b):
        print(a+b)
s=Student("ammu")
print(s.name)
print(Student.class_variable)
Student.modify(10,20)
print(s.name)
print(Student.class_variable,"pppppp")


##destructor
class Student:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor","first")
    def hello(self):
        print("working")
s=Student()
del s
#without del s
class Student:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor","first")
    def hello(self):
        print("working")
s=Student()
