from tkinter import *
root = Tk()

# l = Label(root,text = 'I\'m the first line!!!',width = 800,height = 100,anchor = N)
# l.pack()

c = Canvas(root,width = 800,height = 400)
c.pack()

def show(event):
    g = event.widget
    x = g.canvasx(event.x)
    y = g.canvasy(event.y)
    print(event.x,event.y,x,y)


c.bind('<B1-Motion>',show)





mainloop()