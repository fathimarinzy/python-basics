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