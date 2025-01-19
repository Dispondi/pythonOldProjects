import tkinter as tk
from random import randint

window = tk.Tk()
window.title('tk')

def luck():
    lbl['text'] = str(randint(1,6))


lbl = tk.Label(text='',height=2,relief=tk.SUNKEN,borderwidth=3)
btn = tk.Button(text='Бросить',command=luck,master=window,width=5,height=2, relief=tk.RIDGE,borderwidth=3)
btn.pack(fill=tk.BOTH)
lbl.pack(fill=tk.BOTH)

window.mainloop()