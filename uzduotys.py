
from tkinter import *

#1 uzduotis
langas = Tk()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)


def spausdinti():
    ivesta = laukas1.get()
    atsakymo_laukas.config(text="Labas, " + ivesta + "!")
    sukurta.config(text="Sukurta")

def spausdinti1(event):
    ivesta = laukas1.get()
    atsakymo_laukas.config(text="Labas, " + ivesta + "!")
    sukurta.config(text="Sukurta")


uzrasas1 = Label(langas, text="Iveskite varda")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
atsakymo_laukas = Label(langas, text="")
sukurta = Label(langas, text="")


uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
atsakymo_laukas.grid(row=1, columnspan=3)
sukurta.grid(row=2, columnspan=1)

langas.bind("<Return>", spausdinti1)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Isvalyti")
submeniu.add_command(label="Atkurti paskutini")
submeniu.add_separator()
submeniu.add_command(label="Iseiti")

langas.mainloop()

# 3 uzduotis

