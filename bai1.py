from tkinter import *
from tkinter import ttk
import threading

win = Tk()
label1=Label(win, text="label cua toi left")
label1.pack(side=LEFT)

label2=Label(win, text="label cua toi right")
label2.pack(side=RIGHT)

def setText():
    while(True):    
        content = input()
        label1.config(text = content)
setTextThr = threading.Thread(target=setText)
setTextThr.start()

win.mainloop()