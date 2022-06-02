from tkinter import *

root = Tk()

c = Canvas(root,width = 500,height = 500)
c.pack()

l1 = c.create_line(0,250,500,250,dash = (4,4))
l2 = c.create_line(250,0,250,500,dash = (4,4))


# 1.头





mainloop()