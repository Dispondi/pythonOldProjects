import tkinter as tk
window = tk.Tk()
window.resizable(False,False)
window.geometry('600x210+480+400')
window.title('Введите домашний адрес')

frm1 = tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
frm1.pack()
frm2 = tk.Frame(master=window)
frm2.pack(fill=tk.X, ipady=5)


lbls = ['Имя:','Фамилия:','Адрес 1:','Адрес 2:','Город:',
        'Регион:','Почтовый индекс:','Страна:']

ent_list = []
for i in range(len(lbls)):
    lbl = tk.Label(text=lbls[i],master=frm1)
    lbl.grid(column=0,row=i,sticky='e')
    ent = tk.Entry(master=frm1,width=250)
    ent_list.append(ent)
    ent.grid(column=1,row=i,sticky="ew")

def clearing(n):
    return ent_list[n].delete(0,tk.END)

def clear():
    for n in range(len(ent_list)):
        clearing(n)

def send():
    data = {}
    s = ''
    for n in range(len(lbls)):
        data[lbls[n]] = ent_list[n].get()
    for k,v in data.items():
        s += f'{k} {v}\n'
    with open('adresse.txt','w') as f:
        f.write(s)

btn_c = tk.Button(text='Очистить',command=clear,master=frm2,borderwidth=1)
btn_s = tk.Button(text='Отправить',command=send,master=frm2,borderwidth=1)
btn_s.pack(side=tk.RIGHT,padx=5,ipadx=10)
btn_c.pack(side=tk.RIGHT,ipadx=10)

window.mainloop()