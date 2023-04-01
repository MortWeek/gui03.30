from tkinter import *

# langas = Tk()
# langas.geometry("350x300")
# virsutinis = Frame(langas)
# apatinis = Frame(langas)
#
# mygtukas1 =Button(virsutinis, text="1 mygtukas")
# mygtukas2 =Button(virsutinis, text="2 mygtukas")
#
# virsutinis.pack()
# apatinis.pack(side=BOTTOM)
# mygtukas1.pack(side=LEFT)
# mygtukas2.pack(side=LEFT)
# langas.mainloop()

langas = Tk()

uzrasas1 = Label(langas, text="Vardas")
laukas1 = Entry(langas)
uzrasas2 = Label(langas, text="Pavarde")
laukas2 = Entry(langas)
varnele = Checkbutton(langas, text="Pazymek varnele")

uzrasas1.grid(row=0, column=0, sticky=E)
laukas1.grid(row=0, column=1)
uzrasas2.grid(row=1, column=0, sticky=E)
laukas2.grid(row=1, column=1)
varnele.grid(row=2, columnspan=2)

langas.mainloop()