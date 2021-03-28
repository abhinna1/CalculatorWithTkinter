import tkinter
from tkinter import *


root = Tk()#root is the window
root.geometry("250x300")#resolution of the window
root.title('Calculator')
root.resizable(0,0)

def frameDivide(): #Dividing frames i.e. rows
    frame1 = Frame(root,bg='#000000')
    frame1.pack(expand=True,fill='both')

    frame2 = Frame(root)
    frame2.pack(expand=True,fill='both')

    frame3 = Frame(root)
    frame3.pack(expand=True,fill='both')

    frame4 = Frame(root)
    frame4.pack(expand=True,fill='both')



    #button functions
    def Frame2button():
        btn1 = Button(
            frame2,
            text='1',
            font=('Roboto',22),


        )
        btn1.pack(side=LEFT,expand=True,fil='both')

        btn2 = Button(
            frame2,
            text='2',
            font=('Roboto', 22),
        )
        btn2.pack(side=LEFT, expand=True, fil='both')

        btn3 = Button(
            frame2,
            text='3',
            font=('Roboto', 22),

        )
        btn3.pack(side=LEFT, expand=True, fil='both')

        btn4 = Button(
            frame2,
            text='+',
            font=('Roboto', 22),

        )
        btn4.pack(side=LEFT, expand=True, fil='both')
    def Frame3button():
        #button 4
        btn5=Button(
            frame3,
            text='4',
            font = ('Roboto',22),
        )
        btn5.pack(side=LEFT,expand=True,fill='both')

        #button 6
        btn6 = Button(
            frame3,
            text='5',
            font=('Roboto', 22),
        )
        btn6.pack(side=LEFT, expand=True, fill='both')

        # button 7
        btn7 = Button(
            frame3,
            text='6',
            font=('Roboto', 22),
        )
        btn7.pack(side=LEFT, expand=True, fill='both')

        # button 8
        btn8 = Button(
            frame3,
            text='-',
            font=('Roboto', 22),
        )
        btn8.pack(side=LEFT, expand=True, fill='both')
    def Frame4button():
        btn9=Button(
            frame4,
            text='7',
            font=('Roboto',22),
        )
        btn9.pack(side=LEFT,expand='true',fill='both')
        btn0=Button(
            frame4,
            text='8',
            font=('Roboto',22),
        )
        btn0.pack(side=LEFT,expand=True,fill='both')

        btneit = Button(
            frame4,
            text='9',
            font=('Roboto', 22),
        )
        btneit.pack(side=LEFT, expand=True, fill='both')

        btnnin = Button(
            frame4,
            text='0',
            font=('Roboto', 22),
        )
        btnnin.pack(side=LEFT, expand=True, fill='both')
    def lable():
        lb=Label(root,frame1, text='hello',fg='#FFFFFF')
        lb.pack(expand=True,fill='both')
    #calling all buttons
    Frame4button()
    Frame3button()
    Frame2button()
    lable()
frameDivide()
root.mainloop()


