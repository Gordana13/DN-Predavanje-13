# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
import random

def klik_gumba():
    loto = []
    izpis = int(vnos.get())
    loto = random.sample(xrange(1, 30+1), izpis)
    tkMessageBox.showinfo("IZPIS ŠTEVIL", loto)

window = Tkinter.Tk()
window.title("Generator loto števil")
window.geometry("700x250+600+350")
window.configure(bg="white")

pozdrav = Tkinter.Label(text="Welcome to the Lottery numbers generator.")
pozdrav.config(font=("Perpetua", 25, "bold", "underline"))
pozdrav.configure(bg="white")
pozdrav.pack(pady=5)

vsebina = Tkinter.Frame()
vsebina.configure(bg="white")
vsebina.pack()

besedilo = Tkinter.Label(vsebina, text="Please enter how many random numbers would you like to have: ")
besedilo.config(font=("Perpetua", 17))
besedilo.configure(bg="white")
besedilo.pack(padx=10, pady=10, side=Tkinter.LEFT)

vnos = Tkinter.Entry(vsebina, width=5, justify="center")
vnos.config(font=("Arial", 11))
vnos.pack(ipady=6, side=Tkinter.LEFT, padx=10)

gumb = Tkinter.Button(text="IZPIŠI", height=2, width=15, command=klik_gumba, bg="firebrick1")
gumb.config(font=("Arial", 9))
gumb.pack(pady=5)


window.mainloop()
