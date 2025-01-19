import tkinter as tk
from tkinter import messagebox
 
window = tk.Tk()
 
entry = tk.Entry(width=50)

def check_num(text: str):
    stat = True
    for i in text:
        try:
            int(i)
        except ValueError:
            pass
        else:
            stat = False
    return stat
def result():
    text = entry.get()
    if text.lower() == 'андрей':
        return messagebox.showinfo(title=None,message=f'А хуй тебе')
    elif text != '' and check_num(text):
        return messagebox.showinfo(title=None,message=f'Пошел нахуй {text}')
    else:
        return messagebox.showinfo(title=None,message='Нормально введи блять')

button = tk.Button(text='Результат', command=lambda: result())
label = tk.Label(text='Имя введи блять')
label.pack()
entry.pack()
button.pack()

window.mainloop()