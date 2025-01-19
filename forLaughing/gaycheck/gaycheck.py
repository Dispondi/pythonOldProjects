from random import randint as rand
import tkinter as tk
from tkinter import messagebox
import pathlib
from pathlib import Path


def changepos(event):
    x = rand(0,215)
    y = rand(0,120)
    
    btn_n.place(x=x,y=y)
    
def yes():
    message = messagebox.showinfo(message='Я так и знал, пупсик)',title='ПИДАРАС')
    window.destroy()
    return message

#path = Path(pathlib.Path.cwd(), 'billy.ico')


window = tk.Tk()
#window.iconbitmap(path)
window.geometry('250x150')
window.resizable(False,False)
window.title('Пидор?')

lbl = tk.Label(text='Ты гей?',font=['Segoe UI',20])
lbl.place(x=80,y=10)

btn_n = tk.Button(text='Нет',font=['Segoe UI',10],width=4,command=changepos)
btn_n.place(x=70,y=70)
btn_y = tk.Button(text='Да',font=['Segoe UI',10],width=4,command=yes)
btn_y.place(x=155,y=70)

btn_n.bind('<Enter>',changepos)
window.mainloop()
