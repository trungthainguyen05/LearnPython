from tkinter import *

def up():
    print("up")
def left():
    print("left")
def right():
    print("right")
def down():
    if (downBtn['bg']=='green'):
        downBtn['bg'] ='red'
    else:
        downBtn['bg'] ='green'
    print("down")    

win = Tk()

fram1 = Frame(win)
fram1.pack()
fram2 = Frame(win)
fram2.pack()
fram3 = Frame(win)
fram3.pack()

upBtn = Button(fram1, text="up", command = up, bg="red", fg="white")
upBtn.pack()

leftBtn = Button(fram2, text="left", command = left)
leftBtn.pack(side=LEFT)
rightBtn = Button(fram2, text="right", command = right)
rightBtn.pack(side=RIGHT)

downBtn = Button(fram3, text="down", command = down)
downBtn.pack()

win.mainloop()