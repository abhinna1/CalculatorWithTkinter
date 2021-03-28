import tkinter
from tkinter import *

root = Tk()
root.geometry('250x300')
root.resizable(0,0)

def frames():
    frame1=Frame(root,bg='#000000')
    frame1.pack(expand=True,fill='both')

    frame2 = Frame(root)
    frame2.pack(expand=True, fill='both')
    frame3 = Frame(root)
    frame3.pack(expand=True,fill='both')
    frame4=Frame(root)
    frame4.pack(expand=True,fill='both')

    def buttons():
        button1=Button(
            frame2,
            text='1',
            font=('Roboto',22)
        )
        button2 = Button(
            frame2,
            text='2',
            font=('Roboto',22)
        )
        button3=Button(
            frame2,
            text='3',
            font=('Roboto',22)

        )
        button1.pack(side = LEFT,expand=True,fill='both')
        button2.pack(side=LEFT,expand=True,fill='both')
        button3.pack(side=LEFT,expand=True,fill='both')

        #Row 2
        button4 = Button(
            frame3,
            text='4',
            font=('Roboto', 22)
        )
        button5 = Button(
            frame3,
            text='5',
            font=('Roboto', 22)
        )
        button6 = Button(
            frame3,
            text='6',
            font=('Roboto', 22)

        )
        button4.pack(side=LEFT, expand=True, fill='both')
        button5.pack(side=LEFT, expand=True, fill='both')
        button6.pack(side=LEFT, expand=True, fill='both')

        #line 3
        button7 = Button(
            frame4,
            text='7',
            font=('Roboto', 22)
        )
        button8 = Button(
            frame4,
            text='8',
            font=('Roboto', 22)
        )
        button9 = Button(
            frame4,
            text='9',
            font=('Roboto', 22)

        )
        button7.pack(side=LEFT, expand=True, fill='both')
        button8.pack(side=LEFT, expand=True, fill='both')
        button9.pack(side=LEFT, expand=True, fill='both')

        screen = Label(frame1, text='', anchor=SE, font=('Roboto', 22))
        screen.pack(expand=True, fill='both')
    buttons()
frames()

root.mainloop()