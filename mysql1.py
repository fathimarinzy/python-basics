import mysql.connector 
data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database2023"
)
print("connected")

cursor1=data.cursor()
# cursor1.execute('create database database2023')
# print('database created')

# cursor1.execute('create table table11(id int primary key auto_increment,name varchar(20),place varchar(20) )')
# print("table created")

"""single value inserting"""
# x='insert into table11(name,place)values("ammu","kochi")'
# cursor1.execute(x)
# data.commit()
# print("values inserted")

# """multiple value inserting"""
# x='insert into table11(name,place)values(%s,%s)'
# y=[("appu","kottyam"),("akku","malabar")]
# cursor1.executemany(x,y)
# data.commit()
# print("values inserted")

"""to show table"""
cursor1.execute('select * from table11')
print("show table")
x=cursor1.fetchall()
print(x)

# for i in x:
#     print(i)

# x=cursor1.fetchone()
# print(x)

"""update"""
# cursor1.execute('update table11 set name="anu" where id=1')
# data.commit()
# print("updated")
"""delete"""
# cursor1.execute('delete from table11  where id=1')
# data.commit()
# print("deleted")

"""drop"""
# cursor1.execute('drop table table11')
# data.commit()
# print("droped")
