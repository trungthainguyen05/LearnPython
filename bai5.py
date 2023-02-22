from tkinter import *


win = Tk()
win.title('Ung dung post on FB')
# win.configure(width=500, height =600)
# win.geometry('500x600+600+100')
# win.resizable(width=False, height=True)
scrW = win.winfo_screenwidth()
scrH = win.winfo_screenheight()

win.geometry('500x600+%d+%d' %(scrW/2-250,scrH/2-300))


win.mainloop()