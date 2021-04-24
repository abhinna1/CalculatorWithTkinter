from tkinter import *

root=Tk()
root.title('Calculator')
root.configure(bg='Grey39')#changing background of the window
root.iconbitmap('program_icon.ico')
root.resizable(0,0)#disabling resizing option for window


def take_num(num): #function to read the button clicked by the user
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(num))

def clearScreen(): #function to clear screen
    temp.set('')

def add(): #Function for addition button
    first_number = screen.get()
    global f_num
    global operation
    f_num = float(first_number)
    operation='add'
    screen.delete(0, END)

def substract(): #Function for substraction button
    first_number = screen.get()
    global f_num
    global operation
    f_num = float(first_number)
    operation='substract'
    screen.delete(0, END)

def multiply(): #Function for multiplication button
    first_number = screen.get()
    global f_num
    global operation
    f_num = float(first_number)
    operation='multiply'
    screen.delete(0, END)

def divide(): #Function for division button
    first_number = screen.get()
    global f_num
    global operation
    f_num = float(first_number)
    operation='divide'
    screen.delete(0, END)

def equal(): #Function for equal to button
    try:
        if operation=='add':
            second_number = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num + int(second_number))

        if operation=='substract':
            second_number = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num - int(second_number))

        if operation=='multiply':
            second_number = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num * int(second_number))

        if operation =='divide':
            second_number = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num / int(second_number))
    except:
        screen.insert(0, 'Error')


#Global Variables

temp=StringVar() #stores the number input by the user

screen=Entry(text=temp,width=30,borderwidth=5,bg='Misty Rose')#Entry Section to display the clicked numbers and output of operations performed
screen.grid(row=0,columnspan=4,column=0,padx=0,pady=0)

operation=''#global variable to determine the type of operation an operator button performs


#Number Buttons
btn_1 = Button(text='1',width=10,height=3,command=lambda : take_num(1),bg='gray29',fg='Orange')
btn_1.grid(row=1, column=0,padx=0,pady=0)
btn_2 = Button(text='2',width=10,height=3,command=lambda : take_num(2),bg='gray29',fg='Orange')
btn_2.grid(row=1, column=1,padx=0,pady=0)
btn_3 = Button(text='3',width=10,height=3,command=lambda : take_num(3),bg='gray29',fg='Orange')
btn_3.grid(row=1, column=2,padx=0,pady=0)

btn_4 = Button(text='4',width=10,height=3,command=lambda : take_num(4),bg='gray29',fg='Orange')
btn_4.grid(row=2, column=0,padx=0,pady=0)
btn_5 = Button(text='5',width=10,height=3,command=lambda : take_num(5),bg='gray29',fg='Orange')
btn_5.grid(row=2, column=1,padx=0,pady=0)
btn_6 = Button(text='6',width=10,height=3,command=lambda : take_num(6),bg='gray29',fg='Orange')
btn_6.grid(row=2, column=2,padx=0,pady=0)

btn_7 = Button(text='7',width=10,height=3,command=lambda : take_num(7),bg='gray29',fg='Orange')
btn_7.grid(row=3, column=0,padx=0,pady=0)
btn_8 = Button(text='8',width=10,height=3,command=lambda : take_num(8),bg='gray29',fg='Orange')
btn_8.grid(row=3, column=1,padx=0,pady=0)
btn_9 = Button(text='9',width=10,height=3,command=lambda : take_num(9),bg='gray29',fg='Orange')
btn_9.grid(row=3, column=2,padx=0,pady=0)

btn_0=Button(text='0',width=10,height=3,command=lambda : take_num(0),bg='gray29',fg='Orange')
btn_0.grid(row=4,column=0,padx=0,pady=0)

btn_point=Button(text='.',width=10,height=3,command=lambda : take_num('.'),bg='gray29',fg='Orange')
btn_point.grid(row=1,column=3,padx=0,pady=0)


#Mathematical Operation Buttons

btn_plus=Button(text='+',width=10,height=3,command=add,bg='gray29',fg='Orange')
btn_plus.grid(row=4,column=1,padx=0,pady=0)

btn_substract=Button(text='-',width=10,height=3,command=substract,bg='gray29',fg='Orange')
btn_substract.grid(row=4,column=2,padx=0,pady=0)

btn_multiply=Button(text='X',width=10,height=3,command=multiply,bg='gray29',fg='Orange')
btn_multiply.grid(row=2,column=3,padx=0,pady=0)

btn_divide=Button(text='/',width=10,height=3,command=divide,bg='gray29',fg='Orange')
btn_divide.grid(row=3,column=3,padx=0,pady=0)

btn_equal=Button(text='=',width=10,height=3,command=equal,bg='gray29',fg='Orange')
btn_equal.grid(row=4,column=3,padx=0,pady=0)

btn_cls=Button(text='Clear Screen',width=45,height=3,command=clearScreen,bg='gray89',fg='Red')
btn_cls.grid(row=5,column=0,padx=0,pady=0,columnspan=4)

root.mainloop()