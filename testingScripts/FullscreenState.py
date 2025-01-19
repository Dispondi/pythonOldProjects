import tkinter as tk


 
window = tk.Tk()
window.geometry("300x100+810+440")
window.resizable(True, True)
window.minsize(300,100)
window.attributes("-alpha", 1)
window.attributes("-toolwindow", True)
state = True

def set_fs():
    global state
    if state == False:
        window.attributes("-fullscreen", False)
        state = True
    else:
        window.attributes("-fullscreen", True)
        state = False


label = tk.Label(text='Текст')
button = tk.Button(text='Фулскрин',command=lambda: set_fs())
button2 = tk.Button(text='Закрыть окно',command=lambda: window.destroy())



label.pack(anchor='n')
button.pack(anchor="center", side=tk.LEFT, expand=True)
button2.pack(anchor="center",side=tk.RIGHT,expand=True)

window.mainloop()

