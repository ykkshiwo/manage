from tkinter import *
from tkinter.messagebox import *
from MainPage import *

class LoginPage(object):
	def __init__(self, master=None):
		self.root = master #定义内部变量root
		self.root.geometry('%dx%d' % (300, 180)) #设置窗口大小
		#self.root.resizeable(width=False,height=False)
		self.username = StringVar()
		self.password = StringVar()
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root) #创建Frame
		self.page.pack()
		#Label(self.page).grid(row=0, stick=W)
		Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10)
		en = Entry(self.page, textvariable=self.username)
		en.grid(row=1, column=1, stick=E)
		Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10)
		Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
		bt = Button(self.page, text='登陆', command=self.loginCheck)
		bt.bind("<Return>",self.loginCheck_bind)
		bt.focus_set()
		bt.grid(row=3, stick=W, pady=10)
		Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

	def loginCheck(self):
		name = self.username.get()
		secret = self.password.get()
		if name == '' and secret == '':
			self.page.destroy()
			MainPage(self.root)
		else:
			showinfo(title='错误', message='账号或密码错误！')
	
	def loginCheck_bind(self,event):
		name = self.username.get()
		secret = self.password.get()
		if name == '' and secret == '':
			self.page.destroy()
			MainPage(self.root)
		else:
			showinfo(title='错误', message='账号或密码错误！')