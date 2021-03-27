from tkinter import *

root = Tk()
root.geometry('1920x1080')

frame1=Frame(root)
frame1.pack(expand = True, fill='both')

frame2=Frame(root,bg='#000000')
frame2.pack(expand = True, fill='both')

frame3=Frame(root)
frame3.pack(expand = True, fill='both')

button = Button(
    frame2,
    text = 'DownToFuck?',
    font=('Roboto',22),
)
button.pack(side = TOP, expand = True, fill='both')

root.mainloop()