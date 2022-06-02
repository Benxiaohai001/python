from tkinter import *
import math as s
root = Tk()

m = Canvas(root,width = 200,height = 100,background = 'red')
m.pack()

center_x = 100
center_y = 50
r = 50
points = [
    # A：左上点
    center_x - int(r * s.sin(2 * s.pi / 5)),
    center_y - int(r * s.cos(2 * s.pi / 5)),
    # center_x - r * s.sin(s.pi/3),
    # center_y + r * s.sin(s.pi/6),
    #B: 右上点
    center_x + int(r * s.sin(2 * s.pi / 5)),
    center_y - int(r * s.cos(2 * s.pi / 5)),
    #center_x + r * s.sin(s.pi/3),
    # center_y + r * s.sin(s.pi/6),
    # C:左下点
    # center_x - r * s.sin(s.pi/3),
    center_x - r * s.sin(s.pi/5),
    center_y + r * s.cos(s.pi/5),
    # D:顶点
    center_x,
    0,
    # E:右下点
    center_x + r * s.sin(s.pi/5),
    center_y + r * s.cos(s.pi/5),
]
m.create_polygon(points,fill = 'yellow',outline = 'yellow')

mainloop()