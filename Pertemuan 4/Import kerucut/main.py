import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
import fungsi

def hitung_luas_Selimut():
  
     r = float( JariJari.get())
     s = float( GarisPelukis.get())

     LS = fungsi.hitung_luas_selimut(r,s)
  
     txtLuasSelimut.delete(0, END)
     txtLuasSelimut.insert(END, LS) 

def hitung_luas_Permukaan():
  
     r = float( JariJari.get())
     s = float( GarisPelukis.get())

     LP = fungsi.hitung_luas_permukaan(r,s)
  
     txtLuasPermukaan.delete(0, END)
     txtLuasPermukaan.insert(END, LP) 

def hitung_Volume():
    
     r = float( JariJari.get())
     T = float( Tinggi.get())

     V = fungsi.hitung_volume(r,T)

   
     txtVolume.delete(0, END)
     txtVolume.insert(END,V)

def hitung():
  hitung_luas_Selimut()
  hitung_luas_Permukaan()
  hitung_Volume()
   # Create tkinter object

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Volume Kerucut")

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

# Label Pelukis

Qs = Label (frame, text="Garis Pelukis: ")
Qs.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# Textbox Pelukis

GarisPelukis = Entry (frame)
GarisPelukis.grid(row=2, column=1)


# Button

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut

luasSelimut = Label (frame, text="Luas Selimut:") 
luasSelimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut

txtLuasSelimut = Entry(frame)
txtLuasSelimut.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output label Luas Permukaan

LuasPermukaan = Label (frame, text="Luas Permukaan: ") 
LuasPermukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtLuasPermukaan = Entry (frame)
txtLuasPermukaan.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output label Volume

Volume = Label (frame, text="Volume: ") 
Volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtVolume = Entry (frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)


app.mainloop()

