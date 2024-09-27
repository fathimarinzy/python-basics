# import time
# def square(a):
#     for i in a:
#         time.sleep(1)
#         print("square of",i,"is",i**2)
# def cube(a):
#      for i in a:
#         time.sleep(1)
#         print("cube of",i,"is",i**3)


# a=[1,2,3,4,5]
# t1=time.time()
# square(a)
# cube(a)
# print(time.time()-t1)



# import time
# import threading
# def square(a):
#     for i in a:
#         time.sleep(1)
#         print("square of",i,"is",i**2)
# def cube(a):
#      for i in a:
#         time.sleep(1)
#         print("cube of",i,"is",i**3)


# a=[1,2,3,4,5]
# t=time.time()
# t1=threading.Thread(target=square,args=(a,))
# t2=threading.Thread(target=cube,args=(a,))
# t1.start()
# t2.start()

# t1.join()
# t2.join()


# # square(a)
# # cube(a)
# print(time.time()-t)


# import time
# import threading
# def square(a):
#     for i in a:
#         time.sleep(1)
#         print("square of",i,"is",i**2)
#         print(threading.current_thread())
#         print(t1.getName())
# def cube(a):
#      for i in a:
#         time.sleep(1)
#         print("cube of",i,"is",i**3)
#         print(threading.current_thread())
#         print(t2.getName())


# a=[1,2,3,4,5]
# t=time.time()
# t1=threading.Thread(target=square,args=(a,))
# t2=threading.Thread(target=cube,args=(a,))
# t1.start()
# t1.setName("firt thread")
# print(threading.active_count())
# t2.start()
# t1.setName("second thread")
# print(threading.active_count())
# t1.join()
# t2.join()


# print(time.time()-t)
# print(threading.active_count())

"""a text in a file read into one file and write into another file """
# import time
# def pro(file1,file2):
#     f=open(file1,"r")
#     data=f.read()
#     time.sleep(5)
#     ff=open(file2,"w")
#     ff.write(data)
# file1="source.txt"
# file2="file11.txt"
# file3="file2.txt"
# pro(file1,file2)
# pro(file1,file3)
# print("file processing completed")


"""using thead"""
# import time
# import threading
# def pro(file1,file21):
#     f=open(file1,"r")
#     data=f.read()
#     time.sleep(5)
#     ff=open(file21,"w")
#     ff.write(data)
# file1="source.txt"
# file2="file11.txt"
# file3="file2.txt"
# t1=threading.Thread(target=pro,args=(file1,file2))
# t2=threading.Thread(target=pro,args=(file1,file3))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("file processing completed")

"""write 2 times into one file"""

# from threading import *
# import threading
# import time
# def pro(source_file):
#     f=open(source_file,"a")
#     f.write("1 2 3 4 5 6 7 8 9 10 \n")
#     time.sleep(5)
#     ff=open(source_file,'a')
#     ff.write("a b c d e f g h i\n")
# source_file="source.txt"


# thread1=threading.Thread(target=pro,args=(source_file,))
# thread2=threading.Thread(target=pro,args=(source_file,))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# print("file processing completed")


"""multiple thread"""

# from threading import *
# import threading
# import time

# def pro(source_file):
#     f=open(source_file,"a")
#     f.write("1 2 3 4 5 6 7 8 9 10 \n")
#     time.sleep(5)
#     ff=open(source_file,'a')
#     ff.write("a b c d e f g h i\n")
# source_file="source.txt"


# thread1=threading.Thread(target=pro,args=(source_file,))
# thread2=threading.Thread(target=pro,args=(source_file,))
# thread3=threading.Thread(target=pro,args=(source_file,))
# thread4=threading.Thread(target=pro,args=(source_file,))
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

# print("file processing completed")

"""synchronization"""

# from threading import *
# import threading
# import time
# l=threading.Lock()
# def pro(source_file):
#     l.acquire()
#     f=open(source_file,"a")
#     f.write("1 2 3 4 5 6 7 8 9 10 \n")
#     time.sleep(5)
#     ff=open(source_file,'a')
#     ff.write("a b c d e f g h i\n")
#     l.release()
# source_file="source.txt"


# thread1=threading.Thread(target=pro,args=(source_file,))
# thread2=threading.Thread(target=pro,args=(source_file,))
# thread3=threading.Thread(target=pro,args=(source_file,))
# thread4=threading.Thread(target=pro,args=(source_file,))
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

# print("file processing completed")


"""custom the thread name by inherit the Thread"""
# from threading import *
# class Mythread(Thread):
#     def cube(self,a):
#         for i in a:
#             print("cube",i*i*i)
#     def square(self,a):
#         for i in a:
#             print("square",i*i)
#     def run(self):
#             a=[1,2,3,4,5]
#             self.cube(a)
#             self.square(a)
       
# my=Mythread()     
# my.start()



"""quetions"""
# import threading
# x=0
# def increment():
#     global x
#     for i in range(10):
#         x+=1
#         print(x)
# increment()    

# import threading

# def increment():
#     x=0
#     for i in range(10):
#         x+=1
#         print(x)
# increment()     
# increment()   


# import threading
# x=0
# def increment():
#     global x
#     for i in range(10):
#         x+=1
#         print(x)
# increment()     
# increment()   

# import threading
# x=0
# def increment():
#     global x
#     for i in range(10):
#         x+=1
#         print(x)
# def main():
#     global x
#     t1=threading.Thread(target=increment)
#     t2=threading.Thread(target=increment)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# main()
# main()

# import threading
# from threading import *
# x=0
# l=threading.Lock()
# def increment():
#     global x
#     l.acquire()
#     for i in range(10000000):
#         x+=1
#         # print(x)
#     l.release()
       
# def main():
#     global x
#     x=0
#     t1=threading.Thread(target=increment)
#     t2=threading.Thread(target=increment)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
  
# for i in range(10):
#     main()
#     print("iteration{0}:x={1}".format(i,x))


# from threading import *
# class Mythread(Thread):
#     def __init__(self,a):
#          super().__init__()
#          self.a=a
#     def cube(self):
#         for i in self.a:
#             print("cube",i*i*i)
#     def square(self):
#         for i in self.a:
#             print("square",i*i)
#     def run(self):
 
#         t1=Thread(target=self.cube)
#         t2=Thread(target=self.square)
#         t1.start()
#         t2.start()
# a=[1,2,3,4,5]       
# my=Mythread(a)     
# my.start()
# my.join()

####lock

# from threading import *
# class Mythread(Thread):
#     def __init__(self,a,lock):
#          super().__init__()
#          self.a=a
#          self.lock=lock
#     def cube(self):
#         self.lock.acquire()
#         for i in self.a:
#             print("cube",i*i*i)
#         self.lock.release()
#     def square(self):
        
#         self.lock.acquire()
#         for i in self.a:
#             print("square",i*i)
#         self.lock.release()
#     def run(self):
 
#         t1=Thread(target=self.cube)
#         t2=Thread(target=self.square)
#         t1.start()
#         t2.start()
# lock=Lock()
# a=[1,2,3,4,5]       
# my=Mythread(a,lock)     
# my.start()
# my.join()



# from threading import *
# class Mythread(Thread):
#     def __init__(self,a,lock):
#          super().__init__()
#          self.a=a
#          self.lock=lock
#     def cube(self):
       
#         for i in self.a:
#             print("cube",i*i*i)
        
#     def square(self):
 
#         for i in self.a:
#             print("square",i*i)
      
#     def run(self):
#         self.lock.acquire()
 
#         t1=Thread(target=self.cube)
#         t2=Thread(target=self.square)
#         t1.start()
#         t2.start()
#         self.lock.release()
# lock=Lock()
# a=[1,2,3,4,5]       
# my=Mythread(a,lock)     
# my.start()
# my.join()