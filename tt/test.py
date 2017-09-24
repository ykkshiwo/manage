from tkinter import *

root = Tk()
v=StringVar()

def test():
	print(v.get())
	v.set("")

Entry(root,textvariable=v).grid(row=1,column=1)
Button(root,text="test",command=test).grid(row=1,column=2)

root.mainloop()