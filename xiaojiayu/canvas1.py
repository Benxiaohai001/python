from tkinter import *

root = Tk()

c = Canvas(root,width = 800,height = 400)
c.pack()

def paint(event):
    x1,y1 = (event.x - 1),(event.y - 1)
    x2,y2 = (event.x + 1),(event.y + 1)
    c.create_oval(x1,y1,x2,y2,fill = 'red')

c.bind('<B1-Motion>',paint)

t = Label(root,text = 'Click left button of the mouse,then paint what you want paint.')
t.pack()
mainloop()