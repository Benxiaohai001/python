import easygui as g
import sys

while 1:
    g.msgbox('Welcome to the first GUI game!!!')

    msg = 'What do you want from easyGUI?'
    title = 'Game interaction!!!'
    choices = ['Love','Programme','OOXX','Anything']

    choice = g.choicebox(msg,title,choices)

    g.msgbox('Your choice is '+str(choice))

    msg = 'Will you play again?'

    title = 'Chose please'

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit()
