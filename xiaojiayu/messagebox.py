from tkinter import *
from tkinter import messagebox

# messagebox.askokcancel(title = 'Lenovo',message = 'Do you like Lenovo?')
# messagebox.askretrycancel(title = 'Lenovo',message = 'Do you like Lenovo?')
# messagebox.askyesno(title = 'Lenovo',message = 'Do you like Lenovo?')
# messagebox.showinfo(title = 'Lenovo',message = 'Do you like Lenovo?')

root = Tk()
w = Label(root,text = '我也不知道写什么？')
# messagebox.showwarning(title = 'Lenovo',message = 'Do you like Lenovo?')
messagebox.askokcancel(title = 'Lenovo',message = 'Do you like Lenovo?',default = 'cancel',icon = 'error',\
                       parent = w)

mainloop()