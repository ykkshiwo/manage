#author: yang kangkai
from dateutil.parser import parse
import datetime
import sqlite3

#create = input("do you want to create database?(y/n) ")
#if create == "y":
def select(name):
	row = c.execute("select * from "+ name +";")
	today=datetime.datetime.today()
	for i in row:
		finish = parse(i[2])
		interval = today - finish
		d = interval.days
		if d > 0:
			yield i[0],i[1],i[2],d

			
db = input("what database do you want to go: ")
db = db + ".db"
db_go = db
print(db_go)
conn=sqlite3.connect(db_go)
print("open successfully")
c = conn.cursor()
first_or_not = input("what will you do(1: create, 2: find,): ")

if first_or_not == "1":
	nameoftable = input("what is the name of table: ")
	c.execute("CREATE TABLE "+ nameoftable +" (name char(50) NOT NULL,start char(50) NOT NULL, validity char(50) not null);")
	v = "ykk"
	while v:
		n = input("the name of certificate: ")
		s = input("please input the start date: ")
		v = input("please input the finish date:  ")
		if v:
			date = parse(v)
			print(date)
			today = datetime.datetime.today()
			interval = today - date
			day = interval.days
			print(day)
			c.execute("INSERT INTO " + nameoftable +" (name,start,validity) VALUES ('"+ n +"', '"+ s +"','"+ v +"')")
			print("~~~~~~~~~~")
		else:
			print("finish")
	conn.commit()
elif first_or_not == "2":
	print("you select 2.")
	nameoftable = input("what is the of table do you want to find: ")
	#day = input("how long ")
	yd = select(nameoftable)
	print("ok")
	for i in yd:
		print(i)
else:
	print("please input 1 or 2.")
		
  
c.close()
conn.close()

'''
v = "ykk"
while v:
	n = input("the name of certificate: ")
	s = input("please input the start date: ")
	v = input("please input the finish date:  ")
	if v:
		date=parse(v)
		print(date)
		today=datetime.datetime.today()
		interval = today - date
		day=interval.days
		print(day)
		c.execute("INSERT INTO project (name,start,validity) VALUES ('"+ n +"', '"+ s +"','"+ v +"')")
		print("~~~~~~~~~~")
	else:
		conn.commit()
		print("finish")
'''
	

