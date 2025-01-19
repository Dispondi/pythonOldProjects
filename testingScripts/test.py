
import tkinter as tk
from tkinter.filedialog import askopenfilename
 
 
def open_file():
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return

root = tk.Tk()
btn = tk.Button(text='Открыть',command=open_file)
btn.pack()
root.mainloop()