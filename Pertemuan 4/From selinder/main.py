import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi import hitung_luas_Selimut,hitung_luas_Permukaan,hitung_Volume

def hitung():
    hasil_luas_selimut = hitung_luas_Selimut(JariJari.get(),Tinggi.get())
    hasil_luas_permukaan = hitung_luas_Permukaan(JariJari.get(),Tinggi.get())
    hasil_volume = hitung_Volume(JariJari.get(),Tinggi.get())
    txtLuasSelimut.delete(0, END)
    txtLuasSelimut.insert(END, hasil_luas_selimut)
    txtLuasPermukaan.delete(0, END)
    txtLuasPermukaan.insert(END, hasil_luas_permukaan)
    txtVolume.delete(0, END)
    txtVolume.insert(END,hasil_volume)  
   # Create tkinter object

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Volume Selinder")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label jari Jari

Qr = Label (frame, text="Jari Jari: ")
Qr.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Jari Jari

JariJari = Entry (frame)
JariJari.grid(row=0, column=1)

# Label Tinggi

QT = Label (frame, text="Tinggi: ")
QT.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox Tinggi

Tinggi = Entry (frame)
Tinggi.grid(row=1, column=1)


# Button

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut

luasSelimut = Label (frame, text="Luas Selimut:") 
luasSelimut.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut

txtLuasSelimut = Entry(frame)
txtLuasSelimut.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output label Luas Permukaan

LuasPermukaan = Label (frame, text="Luas Permukaan: ") 
LuasPermukaan.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtLuasPermukaan = Entry (frame)
txtLuasPermukaan.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output label Volume

Volume = Label (frame, text="Volume: ") 
Volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtVolume = Entry (frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)


app.mainloop()

