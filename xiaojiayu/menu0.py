from tkinter import *

root = Tk()
# Create a top level menu
menu = Menu(root)

def callback():
    print('I\'m called!!!')

# 创建一个下拉文件，然后将它添加到顶级菜单中
filemenu = Menu(menu)
filemenu.add_command(label = 'Open',command = callback)
filemenu.add_command(label = 'Save',command = callback)
filemenu.add_separator()
filemenu.add_command(label = 'Quit',command = root.quit)
menu.add_cascade(label = 'File',menu = filemenu)


# 创建另一个下拉文件，然后将其添加到顶级菜单中
editmenu = Menu(menu,tearoff = False)
editmenu.add_command(label = 'Copy',command = callback)
editmenu.add_command(label = 'Cut',command = callback)
editmenu.add_command(label = 'Paste',command = callback)
menu.add_cascade(label = 'Edit',menu = editmenu)

# Display Menu
root.config(menu = menu,)


mainloop()