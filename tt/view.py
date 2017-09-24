from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import sqlite3


c = 0 #此为全局变量
conn = 1
createtablename = 2
selecttablename = 3

class DatabaseFrame(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.database_name = StringVar()
		self.database = ""
		self.createPage()

	def createPage(self):
		Label(self).grid(row=0, stick=W, pady=10)
		#Label(self, text='连接数据库').pack()
		Label(self, text = '连接数据库：').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.database_name).grid(row=1, column=1, stick=E)
		Button(self,text="选择",command=self.select).grid(row=1,column=2)
		bt = Button(self, text='连接',command=self.conn).grid(row=3, column=1, stick=E, pady=10)
		bt.bind('<Return>',self.conn)
		bt.focus_set()
		bt.grid(row=3, column=1, stick=E, pady=10)
		
	def select(self):
		self.database = askopenfilename()
		self.database_name.set(self.database)
		print("connect to " + self.database)
	
	def conn(self):
		#dn = self.database_name.get()
		#tn = self.table_name.get()
		#global table
		#table = self.table_name.get()
		global conn
		conn=sqlite3.connect(self.database_name.get())
		#print(self.database+"is conecting now...")
		global c
		c = conn.cursor()
		if self.database_name.get() == "":
			showinfo(title="连接提示",message="请选择正确的数据库!")
		else:
			showinfo(title="连接提示",message="您已成功连接数据库!")
		
class createtableFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.createtable_name = StringVar()
		self.createPage()

	def createPage(self):
		#Label(self, text='').pack()
		Label(self, text = '创建表名：').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.createtable_name).grid(row=1, column=1, stick=E)
		Button(self,text="确定",command=self.createtable).grid(row=2,column=2)
		
	def createtable(self):
		global createtablename
		createtablename = self.createtable_name.get()
		#print(createtablename)
		global c
		c.execute("create table " + createtablename + "(name char(50) NOT NULL,start char(50) NOT NULL, validity char(50) not null);")
		
		
		
class selecttableFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.selecttable_name = StringVar()
		self.createPage()

	def createPage(self):
		#Label(self, text='').pack()
		Label(self, text = '选择表名：').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.selecttable_name).grid(row=1, column=1, stick=E)
		bt = Button(self,text="确定",command=self.selecttable).grid(row=2,column=2)
		bt.bind('<Return>',self.selecttable)
		bt.focus_set()
		bt.grid(row=3, column=1, stick=E, pady=10)
		
	def selecttable(self):
		global selecttablename
		selecttablename = self.selecttable_name.get()
		#print(selecttablename)
		
		
class InputFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.name = StringVar()
		self.start = StringVar()
		self.finish = StringVar()	
		self.createPage()

	def createPage(self):
		Label(self).grid(row=0, stick=W, pady=10)
		Label(self, text = '证件名称：').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.name).grid(row=2, column=1, stick=E)
		Label(self, text = '发证时间：').grid(row=3, stick=W, pady=10)
		Entry(self, textvariable=self.start).grid(row=3, column=1, stick=E)
		Label(self, text = '有效时间：').grid(row=4, stick=W, pady=10)
		Entry(self, textvariable=self.finish).grid(row=4, column=1, stick=E)
		#Label(self, text = '优惠 /元: ').grid(row=4, stick=W, pady=10)
		#Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)
		bt = Button(self, text='录入',command=self.insert)
		bt.bind('<Return>',self.insert)
		bt.focus_set()
		bt.grid(row=6, column=1, stick=E, pady=10)
		
	def insert(self):
		global conn
		name = self.name.get()
		start = self.start.get()
		finish = self.finish.get()
		c.execute("INSERT INTO " + selecttablename +" (name,start,validity) VALUES ('"+ name +"', '"+ start +"','"+ finish +"')")
		conn.commit()
		print("insert success")
		self.name.set("")
		self.start.set("")
		self.finish.set("")
						
class QueryFrame(Frame): #继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.table_name = StringVar()
		self.days = StringVar()
		self.createPage()

	def createPage(self):
		Label(self).grid(row=0, stick=W, pady=10)
		Label(self, text = '过期天数：').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.days).grid(row=2, column=1, stick=E)
		Button(self, text='查询',command=self.find).grid(row=3, column=1, stick=E, pady=10)
	def find(self):
		for i in c.execute("select * from "+ selecttablename +";"):
			print(i)

class CountFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.createPage()

	def createPage(self):
		Label(self, text='统计界面').pack()


class AboutFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.createPage()

	def createPage(self):
		Label(self, text='关于界面').pack()
