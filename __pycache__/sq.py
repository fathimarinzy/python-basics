# import sqlite3
# mydb=sqlite3.connect('abcd.db')
# print("database created ")

# cursor1=mydb.cursor()
# cursor1.execute('create table sept(id int primary key not null,name text not null,age int not null,address char(50),salary real)')
# print("table created")

# cursor1.execute("insert into sept(id,name,age,address,salary) values(1,'ammu',20,'ammu villa',20000)")
# mydb.commit()
# print("data inserted")

# a=cursor1.execute("select id,name,age,address,salary from sept")
# print(a)

# for r in a:
#     print(r)
#     print(type(r))
#     print("id=",r[0])
#     print("name =",r[1])
#     print("age=",r[2])
#     print("address =",r[3])
#     print("salary =",r[4])


# x="insert into sept(id,name,age,address,salary)values(?,?,?,?,?)"
# val=[(2,"hansu",13,"kochi",9000),(3,"achu",15,"kottyam",8000)]
# cursor1.executemany(x,val)
# mydb.commit()
# print("data inserted")

"""to show table"""
# cursor1.execute('select * from sept')
# print("show table")
# x=cursor1.fetchall()
# print(x)

"""update"""
# cursor1.execute('update sept set name="anu" where id=1')
# mydb.commit()
# print("updated")
"""delete"""
# cursor1.execute('delete from sept  where id=1')
# mydb.commit()
# print("deleted")

"""drop"""
# cursor1.execute('drop table table11')
# mydb.commit()
# print("droped")
