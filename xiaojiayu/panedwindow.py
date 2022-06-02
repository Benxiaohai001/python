from tkinter import *


m1 = PanedWindow()
m1.pack(fill = BOTH,expand = 1)

left = Label(m1,text = 'left pane',background = 'red')
m1.add(left)

m2 = PanedWindow(orient = VERTICAL,background = 'blue')
m1.add(m2)

top = Label(m2,text = 'top pane',foreground = 'yellow')
m2.add(top)

bottom = Label(m2,text = 'bottom pane',foreground = 'green')
m2.add(bottom)

mainloop()