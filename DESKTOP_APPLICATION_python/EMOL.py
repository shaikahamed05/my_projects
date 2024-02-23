from tkinter import *
from PIL import ImageTk

emod_window=Tk()
emod_window.geometry('1366x768')
emod_window.title('intro')
bgImage=ImageTk.PhotoImage(file='Images/EMOL_LOGO_IMAGE.jpg')
emod_window.state('zoomed')

bglabel=Label(emod_window,image=bgImage)
bglabel.place(x=0,y=0)

emod_window.after(2000, emod_window.destroy)

emod_window.mainloop()

import LOGIN