# try:
#     a=int(input("enter a first number:"))
#     b=int(input("enter a second number:"))
#     print(a/b)
# except:
#     print("zero division error")
# else:
#     print("no error")
# finally:
#     print("always executes ")
# print("stop")

#check exceptions
#index error
# try:
#     a=[1,2,3]
#     print(a[3])
# except IndexError:
#     print("index error")
# except NameError:
#     print("name error")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division error")

# except:
#     print("index error")
# else:
#     print("no error")
# finally:
#     print("always executes ")
# print("stop")

#name error
# try:
 
#     print(a)
# except IndexError:
#     print("index error")
# except NameError:
#     print("name error")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division error")

# except:
#     print("name error")
# else:
#     print("no error")
# finally:
#     print("always executes ")
# print("stop")

# #value error
# try:
    
#     a=int(input("enter the input:"))
# except IndexError:
#     print("index error")
# except NameError:
#     print("name error")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division error")

# except:
#     print("value error")
# else:
#     print("no error")
# finally:
#     print("always executes ")
# print("stop")

#key error
# try:
#     dic={'name':'ammu','age':10}
#     print(dic['place'])
# except KeyError:
#     print("key error first")
# except:
#     print("key error")

# #import error
# try:
#   from math import cube
# except ImportError:
#     print("import error first")
# except:
#     print("import error")

# #type error
# try:
#     print("10"+10)
# except TypeError:
#     print("type error first")
# except:
#     print("type error")


#keyword raise

# try:
#     age=int(input("enter your age"))
#     if age<18:
#         raise
#     else:
#         print("eligible for voting")
# except:
#     print("not eligible for voting")

# ##
# try:
#     age=int(input("enter your age"))
#     if age<18:
#         raise TypeError
#     else:
#         print("eligible for voting")
# except TypeError:
#     print("not eligible for voting")
# except:
#     print("not eligible for voting")

# #we can create a exception name
# class AgeError(Exception):
#     pass
# try:
#     age=int(input("enter your age"))
#     if age<18:
#         raise AgeError
#     else:
#         print("eligible for voting")
# except AgeError:
#     print("not eligible for voting")
# except:
#     print("not eligible for voting")

#keyword assert
try:
    a=10
    b=50
    assert a>b,"a is lessthan b"
    print("a is greater than b")
except AssertionError as msg:
    print(msg)