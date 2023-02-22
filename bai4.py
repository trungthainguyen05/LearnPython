from tkinter import *


win = Tk()

# Label(win, text = 'Doan van 1', font = 'Times 20', bg = 'red').grid(row=0,column=0, sticky=E)
# Label(win, text = 'Doan van A', font = 'Times 25', bg = 'green').grid(row=0,column=1, sticky=W)
# Label(win, text = 'Doan van 2', font = 'Times 30', bg = 'blue').grid(row=1,column=0)
# Label(win, text = 'Doan van B', font = 'Times 35', bg = 'yellow').grid(row=1,column=1)
# Label(win, text = 'Doan van 3', font = 'Times 40', bg = 'purple').grid(row=2,columnspan=2)

Label(win, text = 'Doan van', bg='red',font='Times 30').place(relwidth=.5, relheight=.5, relx=50, rely=50)


win.mainloop()