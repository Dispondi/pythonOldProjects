from tkinter import *
from tkinter import messagebox

cell_counter = 0
def f_game(i):
    global cell_counter

    cells_field = []

    if lbl_now['text'] == 'КРЕСТИКИ' and i['image'] == 'pyimage3':
        i['image'] = tic
        lbl_now['text'] = 'НОЛИКИ'
        cell_counter += 1
    elif lbl_now['text'] == 'НОЛИКИ' and i['image'] == 'pyimage3':
        i['image'] = tac
        lbl_now['text'] = 'КРЕСТИКИ'
        cell_counter += 1
    
    if cell_counter == len(lbls):
        return f_game_end(who='')
        
    for j in range(len(lbls)): # не for i, а for j, тк i используется в аргументах функции
        if lbls[j]['image'] == 'pyimage1':
            cells_field += ['x']
        elif lbls[j]['image'] == 'pyimage2':
            cells_field += ['o']
        else:
            cells_field += ['_']
    
    if f_win(cells_field) == 'x':
        f_game_end('x')
    elif f_win(cells_field) == 'o':
        f_game_end('o')

def f_win(c_field: list):

    #вертикальные комбинации
    for i in range(3):
        combination = ''
        for j in range(3):
            if c_field[(j * 3) + i] == 'x':
                combination += 'x'
            elif c_field[(j * 3) + i] == 'o':
                combination += 'o'
        if combination == 'xxx':
            return 'x'
        elif combination == 'ooo':
            return 'o'

    #горизонтальные комбинации
    for i in range(3):
        combination = ''
        for j in range(3):
            if c_field[j + (i * 3)] == 'x':
                combination += 'x'
            elif c_field[j + (i * 3)] == 'o':
                combination += 'o'
        if combination == 'xxx':
            return 'x'
        elif combination == 'ooo':
            return 'o'
    
    # по диагонали
    for i in range(2):
        combination = ''
        if i == 0:
            for j in c_field[::4] :
                if j == 'x':
                    combination += 'x'
                elif j == 'o':
                    combination += 'o'
            if combination == 'xxx':
                return 'x'
            elif combination == 'ooo':
                return 'o'
        else:
            for j in c_field[2:7:2] :
                if j == 'x':
                    combination += 'x'
                elif j == 'o':
                    combination += 'o'
            if combination == 'xxx':
                return 'x'
            elif combination == 'ooo':
                return 'o'

def f_game_end(who: str):

    if who == 'x':
        lbl_now['text'] = 'ПОБЕДИЛИ КРЕСТИКИ'
        messagebox.showinfo(message='ПОБЕДИЛИ КРЕСТИКИ',title='ПОБЕДИЛИ КРЕСТИКИ')
        root.destroy()
    elif who == 'o':
        lbl_now['text'] = 'ПОБЕДИЛИ НОЛИКИ'
        messagebox.showinfo(message='ПОБЕДИЛИ НОЛИКИ',title='ПОБЕДИЛИ НОЛИКИ')
        root.destroy()
    else:
        lbl_now['text'] = 'НИЧЬЯ'
        messagebox.showinfo(message='НИЧЬЯ',title='НИЧЬЯ')
        root.destroy()

root = Tk()
root.title('GAME')
root.resizable(False, False)
lbl_now = Label(text='КРЕСТИКИ',font=('SIGUI',20))
lbl_now.grid(row=0,column=0,columnspan=3)

tic = PhotoImage(file="./images/tic.png")
tac = PhotoImage(file="./images/tac.png")
toe = PhotoImage(file="./images/toe.png")

lbls = []
for i in range(3):
    for j in range(3):
        lbl = Label(text='',image=toe, master=root,relief='sunken',borderwidth=1)
        lbl.grid(row=i+1, column=j)
        lbls.append(lbl)

for i in lbls:
        i.bind('<ButtonPress-1>', lambda event, i=i : f_game(i))


root.mainloop()
