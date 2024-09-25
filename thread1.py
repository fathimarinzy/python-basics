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


import time
import threading
def square(a):
    for i in a:
        time.sleep(1)
        print("square of",i,"is",i**2)
        print(threading.current_thread())
        print(t1.getName())
def cube(a):
     for i in a:
        time.sleep(1)
        print("cube of",i,"is",i**3)
        print(threading.current_thread())
        print(t2.getName())


a=[1,2,3,4,5]
t=time.time()
t1=threading.Thread(target=square,args=(a,))
t2=threading.Thread(target=cube,args=(a,))
t1.start()
t1.setName("firt thread")
print(threading.active_count())
t2.start()
t1.setName("second thread")
print(threading.active_count())
t1.join()
t2.join()


print(time.time()-t)
print(threading.active_count())