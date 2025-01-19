import tkinter as tk
from random import randint as rand
from random import choice


def name(n_n: int,gl_n: int):
    gl= 'aeiouy'
    other = 'bcdfghjklmnpqrstvwxz'
    name_ = ''

    l_pos = []
    
    while gl_n != 0:
        randn = rand(0,n_n -1)
        if randn not in l_pos:
            l_pos.append(randn)
            gl_n -= 1

    for i in range(n_n):
        if i in l_pos:
            letter = choice(gl)
            name_ += letter
        else:
            letter = choice(other)
            name_ += letter
    return name_
    
        

def randName():
    gl= 'aeiouy'
    n_name = int(ent_n_n.get())
    gl_name = int(ent_gn_n.get())

    n_sname = int(ent_n_sn.get())
    gl_sname = int(ent_gn_sn.get())
    

    if n_name >= gl_name and n_sname >= gl_sname:
        name_f = name(n_name,gl_name)
        sname_f = name(n_sname,gl_sname)
    else:
        name_f = 'пошелнахуй'
        sname_f = 'пошелнахуй'
    
    full_name = name_f.capitalize() + ' ' + sname_f.capitalize()
    
    counting = 0
    for i in full_name:
        if i in gl:
            counting += 1
    
    if counting < (gl_name + gl_sname):
        randName()
    else:
        lbl_result2['text'] = full_name

def randName_check():
    try:
        randName()
    except RecursionError:
        lbl_result2['text'] = 'Пиздец случился'

window = tk.Tk()
window.resizable(False,False)
window.columnconfigure([0,1],weight=1)
window.rowconfigure([0,1],weight=1,minsize=50)
window.rowconfigure(2,weight=1,minsize=60)

frm1 = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
frm2 = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
frm3 = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
frm4 = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
frm1.grid(column=0,row=0)
frm2.grid(column=1,row=0)
frm3.grid(column=0,row=1)
frm4.grid(column=1,row=1)
lbl_n_n = tk.Label(master=frm1,text='Кол-во букв в имени:')
ent_n_n = tk.Entry(master=frm1,width=5)
lbl_n_n.pack(padx=10,ipadx=10,ipady=5)
ent_n_n.pack()
lbl_n_sn = tk.Label(master=frm2,text='Кол-во букв в фамилии:')
ent_n_sn = tk.Entry(master=frm2,width=5)
lbl_n_sn.pack(padx=10,ipadx=10,ipady=5)
ent_n_sn.pack()
lbl_gn_n = tk.Label(master=frm3,text='Кол-во гласных в имени:')
ent_gn_n = tk.Entry(master=frm3,width=5)
lbl_gn_n.pack(ipadx=10,ipady=5)
ent_gn_n.pack()
lbl_gn_sn = tk.Label(master=frm4,text='Кол-во гласных в фамилии:')
ent_gn_sn = tk.Entry(master=frm4,width=5)
lbl_gn_sn.pack(ipadx=10,ipady=5)
ent_gn_sn.pack()

ent_n_n.insert(0,0)
ent_gn_n.insert(0,0)
ent_n_sn.insert(0,0)
ent_gn_sn.insert(0,0)

button_result = tk.Button(text='Генерировать',font=["Segoe UI",10],command=randName_check)
button_result.grid(column=1,row=2,sticky=tk.N)
lbl_result = tk.Label(text='Результат:',font=["Segoe UI", 14])
lbl_result.grid(column=0,row=2,sticky=tk.NW)
lbl_result2 = tk.Label(text='',font=["Segoe UI", 15])
lbl_result2.grid(column=0,row=2,sticky=tk.SW)

window.mainloop()