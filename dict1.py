x={"name":"ammu","age":10,"place":"kochi"}
print(x)
print(len(x))
print(type(x))
x={"name":"ammu","age":10,"place":"kochi","name":"anu"}
print(x)
x={"name":"ammu","age":10,"place":"kochi","name":"anu","place":"kollam"}
print(x)

x={"name":"ammu","age":10,"place":"kochi"}
print(x["name"])
print(x["age"])

for i in x:
    print(i)

for i in x:
    print(x[i])

print(x.keys())
print(x.values())
print(x.items())

for i in x.keys():
    print(i)
for i in x.values():
    print(i)    
for i in x.items():
    print(i)
for i,j in x.items():
    print(i,j)

x["age"]=20
print(x)
del x["age"]
print(x)
# pgm to check if value 200 exist in following dict
dict={"A":100,"B":200,"C":300}
if 200 in dict.values():
    print("200 in dict")
else:
    print("200 not in dict")

    #methods

x={"name":"ammu","age":10,"place":"kochi"}
print(x["name"])
z=x.get("name")
print(z)
x.update({"name":"anu"})
print(x)
x.update({"course":"python"})
print(x)
y={"lang":"python"}
x.update(y)
print(x)
z=x.pop("name")
print(x)
z=x.popitem()
print(x)
x.clear()
print(x)

#print the value of key history from the below dict
d={"class":{"student":{"name":"mike","marks":{"physics":70,"history":80}}}}

print(d["class"]["student"]["marks"]["history"])

#pgm to to rename a key city to location in the dic
d={"name":"kelly","age":25,"salary":8000,"city":"newyork"}
d.popitem()
d.update({"location":"newyork"})
print(d)
#pgm to change athiras salary to 8500
d={"emp1":{"name":"john","salary":5000},
   "emp2":{"name":"anu","salary":7000},
   "emp3":{"name":"athira","salary":8000}
   }
d["emp3"]["salary"]=8500
print(d)


# from key is useful when we need to initialize a dictionary with a set of keys and common values

key=["a","b","c"]
value=10
value1=[1,2,3]
x=dict.fromkeys(key,value)
y=dict.fromkeys(key,value1)
print(x)
print(y)


'''set default'''
#setdefault method in python is used to insert a key with a specified value into a dictionary
#  if the key is not already present.if the key is present,
# it returns the value of that key this method is useful for ensuring a key is present in a
#  dictionary and assigning a default value if it isn't


my={"name":"ammu"}
my.setdefault("age",10)
print(my)
my.setdefault("age",None)
print(my)
my.setdefault("name","anu")
print(my)

#1 to 10 is keys and the values are square 

d={}
for i in range(1,11):
    d[i]=i*i
print(d)


#dictionary comprehension
# d={key:value for i in  iterable if condition}

d={i:i*i for i in range(1,11)}
print(d)

#only print even number squares

d={i:i*i for i in range(1,11) if i%2==0}
print(d)

# swap keys and values using dictionary comprehension

d={"a":1,"b":2,"c":3}

d={v:k for k,v in d.items()}
print(d)

#print dictionary which contain value(age) are even

a={"ammu":10,"anu":20,"tintu":15,"pinky":25}

a={v:i for v,i in a.items() if i%2==0}
print(a)

#print dictionary which contain value(age) are even and greater than 20

a={"ammu":15,"anu":18,"tintu":35,"pinky":30}
a={v:i for v,i in a.items() if i%2==0 and i>20}
print(a)

# print dictionary which contain value(age)   greater than 20 as "old" and less than 20 as "young"

a={"ammu":15,"anu":18,"tintu":35,"pinky":30}
a={i:"old" if j>20 else "young" for i,j in a.items()}
print(a)

# increment everyone salary by 5000

a={"ammu":15000,"anu":18000,"tintu":35000,"piny":30000}
a={i:j+5000 for i,j in a.items()}
print(a)

company={
    'E001':{'name':'alice','position':'manager','salary':85000,'department':'HR'},
    'E002':{'name':'bob','position':'developer','salary':95000,'department':'IT'},
    'E003':{'name':'Charlie','position':'designer','salary':70000,'department':'Design'},
    'E004':{'name':'Diana','position':'Developer','salary':90000,'department':'IT'},
    'E005':{'name':'Eve','position':'manager','salary':92000,'department':'Sales'}
}

# 1. get all employee in a specific department

department=input("enter the department")
for i in company.values():
    if i['department']==department:
        print(i['name'])
