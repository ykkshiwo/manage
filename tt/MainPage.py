from tkinter import *
from view import *  #菜单栏对应的各个子页面

class MainPage(object):
	def __init__(self, master=None):
		self.root = master #定义内部变量root
		self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小
		self.c = 0 #
		self.createPage()

	def createPage(self):
		self.databasePage = DatabaseFrame(self.root)
		self.createtablePage = createtableFrame(self.root)
		self.selecttablePage = selecttableFrame(self.root)
		self.inputPage = InputFrame(self.root) # 创建不同Frame
		self.queryPage = QueryFrame(self.root)
		self.countPage = CountFrame(self.root)
		self.aboutPage = AboutFrame(self.root)
		self.databasePage.pack() #默认界面
		menubar = Menu(self.root)
		menubar.add_command(label='连接数据库', command = self.database)
		menubar.add_command(label='创建表名', command = self.createtable)
		menubar.add_command(label='选择表名', command = self.selecttable)
		menubar.add_command(label='数据录入', command = self.inputData)
		menubar.add_command(label='查询', command = self.queryData)
		menubar.add_command(label='统计', command = self.countData)
		menubar.add_command(label='关于', command = self.aboutDisp)
		self.root['menu'] = menubar  # 设置菜单栏
		
	def database(self):
		self.databasePage.pack()
		self.createtablePage.pack_forget()
		self.selecttablePage.pack_forget()
		self.inputPage.pack_forget()
		self.queryPage.pack_forget()
		self.countPage.pack_forget()
		self.aboutPage.pack_forget()
		
	def createtable(self):
		self.databasePage.pack_forget()
		self.createtablePage.pack()
		self.selecttablePage.pack_forget()
		self.inputPage.pack_forget()
		self.queryPage.pack_forget()
		self.countPage.pack_forget()
		self.aboutPage.pack_forget()
		
	def selecttable(self):
		self.databasePage.pack_forget()
		self.createtablePage.pack_forget()
		self.selecttablePage.pack_forget()
		self.createtablePage.pack_forget()
		self.selecttablePage.pack()
		self.inputPage.pack_forget()
		self.queryPage.pack_forget()
		self.countPage
	
	def inputData(self):
		self.databasePage.pack_forget()
		self.createtablePage.pack_forget()
		self.selecttablePage.pack_forget()
		self.inputPage.pack()
		self.queryPage.pack_forget()
		self.countPage.pack_forget()
		self.aboutPage.pack_forget()

	def queryData(self):
		self.databasePage.pack_forget()
		self.createtablePage.pack_forget()
		self.selecttablePage.pack_forget()
		self.inputPage.pack_forget()
		self.queryPage.pack()
		self.countPage.pack_forget()
		self.aboutPage.pack_forget()

	def countData(self):
		self.databasePage.pack_forget()
		self.createtablePage.pack_forget()
		self.selecttablePage.pack_forget()
		self.inputPage.pack_forget()
		self.queryPage.pack_forget()
		self.countPage.pack()
		self.aboutPage.pack_forget()

	def aboutDisp(self):
		self.databasePage.pack_forget()
		self.createtablePage.pack_forget()
		self.selecttablePage.pack_forget()
		self.inputPage.pack_forget()
		self.queryPage.pack_forget()
		self.countPage.pack_forget()
		self.aboutPage.pack()