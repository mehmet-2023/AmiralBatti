import random
import time
from tkinter import *
from tkinter import ttk

#Değişkenler...
global ships
ships = []

global enabled2
enabled2 = False

#Gemi Koyma Fonksiyonu
#3X1 Boyutlu Gemileri Sıra Halinde Koyma Eksik
def cell_click(event):
    global enabled
    global ships
    global rakip_gemi
    global enabled1
    global enabled2
    global enabled3
    if enabled == "Gemi1":
        widget = event.widget
        col = widget.grid_info()['column']
        row = widget.grid_info()['row']
        ships.append(str({row})+","+str({col}))
        widget.configure(bg='black', fg='white')
        enabled=False
        info.config(text="3x1 Boyutundaki Gemiyi Koy")
        enabled1=True
        enabled2=True
        enabled3=True
        enabled = "Gemi2"
    elif enabled == "Gemi2":
        if enabled1 == True:
            widget = event.widget
            current_color = widget.cget("bg")
            if current_color == "black":
                info.config(text="Geminin Üstüne Gemi Konulmaz.")
            else:
                col = widget.grid_info()['column']
                row = widget.grid_info()['row']
                ships.append(str({row})+","+str({col}))
                widget.configure(bg='black', fg='white')
                enabled1 = False
        elif enabled1 == False and enabled2 == True:
            widget = event.widget
            current_color = widget.cget("bg")
            if current_color == "black":
                info.config(text="Geminin Üstüne Gemi Konulmaz.")
            else:
                col = widget.grid_info()['column']
                row = widget.grid_info()['row']
                ships.append(str({row})+","+str({col}))
                widget.configure(bg='black', fg='white')
                enabled2 = False
        elif enabled2 == False and enabled3 == True:
            widget = event.widget
            current_color = widget.cget("bg")
            if current_color == "black":
                info.config(text="Geminin Üstüne Gemi Konulmaz.")
            else:
                col = widget.grid_info()['column']
                row = widget.grid_info()['row']
                ships.append(str({row})+","+str({col}))
                widget.configure(bg='black', fg='white')
                info.config(text="3x1 Boyutundaki Diğer Gemiyi Koy")
                enabled = "Gemi3"
                enabled1 = True
                enabled2 = True
                enabled3 = True
    elif enabled == "Gemi3":
        if enabled1 == True:
            widget = event.widget
            current_color = widget.cget("bg")
            if current_color == "black":
                info.config(text="Geminin Üstüne Gemi Konulmaz.")
            else:
                col = widget.grid_info()['column']
                row = widget.grid_info()['row']
                ships.append(str({row})+","+str({col}))
                widget.configure(bg='black', fg='white')
                enabled1 = False
        elif enabled1 == False and enabled2 == True:
            widget = event.widget
            current_color = widget.cget("bg")
            if current_color == "black":
                info.config(text="Geminin Üstüne Gemi Konulmaz.")
            else:
                col = widget.grid_info()['column']
                row = widget.grid_info()['row']
                ships.append(str({row})+","+str({col}))
                widget.configure(bg='black', fg='white')
                enabled2 = False
        elif enabled2 == False and enabled3 == True:
            widget = event.widget
            current_color = widget.cget("bg")
            if current_color == "black":
                info.config(text="Geminin Üstüne Gemi Konulmaz.")
            else:
                col = widget.grid_info()['column']
                row = widget.grid_info()['row']
                ships.append(str({row})+","+str({col}))
                widget.configure(bg='black', fg='white')
                info.config(text="Bu kadardı. Şimdi Rakibi Bekle")
                gemi1_int = random.randint(1,4)
                gemi11_int=random.randint(1,7)
                gemi2_int = random.randint(1,4)
                gemi22_int = random.randint(1,4)
                rakip_gemi = [[random.randint(1,7),random.randint(1,7)],[gemi1_int,gemi11_int],[(gemi1_int+1),gemi11_int],[(gemi1_int+2),gemi11_int],[gemi22_int,gemi2_int],[gemi22_int,(gemi2_int+1)],[gemi22_int,(gemi2_int+2)]]
                info.config(text="Rakibe Atış Yap")
                enabled = False
                enabled2 = True
#Değişkenler..
global atilan
atilan = []
global rakip_cnt
global cnt
rakip_cnt = 0
cnt = 0

#Rakibin Stratejisi
def rakip_hamle(atis):
    global enabled2
    global atis2
    global atisf
    global rakip_cnt
    cellvar = 0
    if atis[0] != 7 and atis[1] != 7:
        if atis[0]!=1 and atis[1] != 1:
            atis2 = [atis[0], atis[1]+1]
            cell = cells[(atis[0],atis[1]+1)]
            if cell.cget("bg") in ["red","green"]:
                atis2 = [atis[0]+1, atis[1]]
                cell = cells[(atis[0]+1,atis[1])]
                if cell.cget("bg") in ["red","green"]:
                    atis2 = [atis[0]-1, atis[1]]
                    cell=cells[(atis[0]-1,atis[1])]
                    if cell.cget("bg") in ["red", "green"]:
                        atis2 = [atis[0],atis[1]-1]
                        cell = cells[(atis[0],atis[1]-1)]
                        if cell.cget("bg") in ["red","green"]:
                            while True:
                                atis2 = [random.randint(1, 7), random.randint(1, 7)]
                                cell = cells[(atis2[0], atis2[1])]
                                if cell.cget("bg") not in ["green", "red"]:
                                    cellvar = 1
                                    break
                        else:
                            cellvar=1
                    else:
                        cellvar=1
                else:
                    cellvar=1
            else:
                cellvar=1
        else:
            #Karmaşayı önlemek için strateji köşedeki atışlarda geçerli değil.
            while True:
                atis2 = [random.randint(1, 7), random.randint(1, 7)]
                cell = cells[(atis2[0],atis2[1])]
                if cell.cget("bg") not in ["green", "red"]:
                    cellvar = 1
                    break
    else:
        while True:
            atis2 = [random.randint(1, 7), random.randint(1, 7)]
            cell = cells[(atis2[0], atis2[1])]
            if cell.cget("bg") not in ["green", "red"]:
                cellvar = 1
                break
    if cellvar == 1:
        if cell.cget("bg") == "black":
            info.config(text="Rakip isabetli atış yaptı")
            cell.config(bg="green")
            rakip_cnt += 1
            if rakip_cnt == 7:
                info.config(text="Oyunu Rakip Kazandı!")
                enabled2 = False
            else:
                rakip_hamle(atis2)
        else:
            info.config(text="Rakip ıskaladı.")
            cell.config(bg="red")
            enabled2 = True

global risabet
risabet = False
#Atış Fonksiyonu
def cell_click2(event):
    global risabet
    global atis2
    global enabled2
    global rakip_gemi
    global rakip_cnt
    global cnt
    global cells
    global atis
    global atilan
    if enabled2:
        widget = event.widget
        row = widget.grid_info()['row']
        col = widget.grid_info()['column']
        current_color = widget.cget("bg")
        isabet = False
        if current_color not in ["green", "red"]:
            for i in rakip_gemi:
                if i[0] == (row - 11) and i[1] == col:
                    isabet = True
            if isabet:
                info.config(text="İsabetli!")
                widget.config(bg="green")
                cnt += 1
                if cnt == 7:
                    info.config(text="Oyunu Kazandın!")
                    enabled2 = False
            else:
                widget.config(bg="red")
                info.config(text="Iska. Sıra rakipte")
                enabled2 = False
                win = True
                if not risabet:
                    while True:
                        atis = [random.randint(1, 7), random.randint(1, 7)]
                        atisf = atis
                        cell = cells[(atis[0], atis[1])]
                        if cell.cget("bg") not in ["green", "red"]:
                            break
                    atilan.append(atis)
                    if cell.cget("bg") == "black":
                        cell.configure(bg='green', fg='white')
                        info.config(text="Rakip İsabetli Atış Yaptı")
                        rakip_cnt += 1
                        if rakip_cnt == 7:
                            info.config(text="Oyunu Rakip Kazandı!")
                            enabled2 = False
                        else:
                            rakip_hamle(atisf)
                            risabet = True
                            enabled2 = True
                    else:
                        win = False
                        info.config(text="Rakip Iskaladı. Sıra Sende")
                        cell.configure(bg='red', fg='white')
                        enabled2 = True
                else:
                    rakip_hamle(atis)
        else:
            info.config(text="Geçersiz Atış!")

#Pencere Tasarımı
root = Tk()
root.title("Amiral Battı")
global cells
cells = {}
for i in range(1, 8):
    for j in range(1, 8):
        cell = Label(root, text="", width=5, height=2, relief=SOLID, borderwidth=1)
        cell.grid(row=i, column=j, padx=2, pady=2)
        cell.bind('<Button-1>', cell_click)
        cells[(i, j)] = cell

#1x1 gemi
info = Label(root,text="1X1 Boyutundaki Gemiyi Koy",font=8)
global enabled
blank = Label(root,text="")
rakip = Label(root,text="Rakibin Tahtası",font=6)
enabled = "Gemi1"
info.grid(row=9,columnspan=7,column=0)
blank.grid(row=10,columnspan=7,column=0)
rakip.grid(row=11,columnspan=7,column=0)

cellse = {}
for i in range(1, 8):
    for je in range(1, 8):
        celle = Label(root, text="", width=5, height=2, relief=SOLID, borderwidth=1)
        celle.grid(row=i+11, column=je, padx=2, pady=2)
        celle.bind('<Button-1>', cell_click2)
        cellse[(i, je)] = celle

root.resizable(False,False)
root.mainloop()