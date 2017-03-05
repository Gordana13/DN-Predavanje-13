# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox


def klik():
    km = int(input.get())
    tkMessageBox.showinfo("REZULTAT", km * 0.62137)


glavno_okno = Tkinter.Tk()
glavno_okno.title("Pretvornik kilomtrov")
glavno_okno.geometry("500x100+650+350")

glavno_okno.configure(bg="springgreen2")

skupina1 = Tkinter.Frame(glavno_okno)
skupina1.pack()

vsebina = Tkinter.Frame()
vsebina.pack()

naslov = Tkinter.Label(skupina1, text="Pretvornik km v milja", bg="springgreen2")
naslov.config(font=("Helvetica", 20, "bold"))
naslov.pack()

text_km = Tkinter.Label(vsebina, text="Vnesite kilometre: ", bg="springgreen2")
text_km.config(font=("Arial", 12))
text_km.pack(side=Tkinter.LEFT)

input = Tkinter.Entry(vsebina, width=20)
input.config(fg="darkgreen")
input.pack(side=Tkinter.LEFT)

gumb = Tkinter.Button(vsebina, text="Pretvori", command=klik)
gumb.config(bg="gray", font=("Arial", 8, "bold"))
gumb.pack(side=Tkinter.RIGHT, padx=10, pady=20)

vsebina.configure(bg="springgreen2")

glavno_okno.mainloop()