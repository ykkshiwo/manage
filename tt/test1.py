from tkinter import *
root = Tk()
def printCoords(event):
    print ('event.char = ',event.char)
    print ('event.keycode = ',event.keycode)
# 创建第一个Button,并将它与BackSpace键绑定
bt1 = Button(root,text = 'Press BackSpace')
bt1.bind('<BackSpace>',printCoords)

# 创建二个Button，并将它与回车键绑定
bt2 = Button(root,text = 'Press Enter')
bt2.bind('<Return>',printCoords)

# 创建第三个Button，并将它与F5键绑定
bt3 = Button(root,text = 'F5')
bt3.bind('<F5>',printCoords)

# 创建第4个Button，并将它与左Shift键绑定，与参考上说法一致
bt4 = Button(root,text = 'Left Shift')
bt4.bind('<Shift_L>',printCoords)

# 创建第5个Button，并将它与右Shift键绑定，与参考上说法一致
bt5 = Button(root,text = 'Right Shift')
bt5.bind('<Shift_R>',printCoords)


# 将焦点设置到第1个Button上
bt2.focus_set()
bt1.grid()
bt2.grid()
bt3.grid()
bt4.grid()
bt5.grid()

root.mainloop()