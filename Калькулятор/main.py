from tkinter import *


def calculate(operation):
    if operation == 'C':
        ent.delete(0,END)
    elif operation == '=':
        try:
            eval(ent.get())
        except SyntaxError:
            text = 'SyntaxError'
        else:
            text = str(eval(ent.get()))
        ent.delete(0,END)
        ent.insert(0,text)
    else:
        text = ent.get() + operation
        ent.delete(0,END)
        ent.insert(0,text)

root = Tk()

root.title('Калькулятор')
root.resizable(False,False)

ent=Entry(foreground='lightgreen',justify='right',font = "Helvetica 34 bold",background='black')
ent.grid(column=0,row=0,columnspan=4,sticky='ew',ipady=10)

btns=[
            'C','(',')','/','`',
            '7','8','9','*','`',
            '4','5','6','-','`',
            '1','2','3','+','`',
            '0',',','='
        ]

row=1
column = 0
for btn in btns:
    comm = lambda x=btn : calculate(x)

    if btn == '`':
        row += 1
        column = 0
    elif btn == '=':
        butn = Button(text=f'{btn}',font = "Helvetica 14",command=comm)
        butn.grid(column=column,row=row,ipady=10,ipadx=10,columnspan=2,sticky='ew')
    else:
        butn = Button(text=f'{btn}',font = "Helvetica 14",command=comm)
        butn.grid(column=column,row=row,ipady=10,ipadx=10,sticky='ew')
        column += 1

root.mainloop()