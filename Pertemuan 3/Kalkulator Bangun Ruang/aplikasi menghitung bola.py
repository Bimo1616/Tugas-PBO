import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas_Bola():
  
     r = float( JariJari.get())

     LB = round (4*(22/7)*r*r) 
  
     txtLuasBola.delete(0, END)
     txtLuasBola.insert(END, LB) 


def hitung_Volume():
    
     r = float( JariJari.get())
     
     V = round (4/3*(22/7)*(r*r*r))

   
     txtVolume.delete(0, END)
     txtVolume.insert(END,V)

def hitung():
  hitung_luas_Bola()
  hitung_Volume()
   # Create tkinter object

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Volume Bola")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label jari Jari

Qr = Label (frame, text="Jari Jari: ")
Qr.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Jari Jari

JariJari = Entry (frame)
JariJari.grid(row=0, column=1)

# Button

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Bola

luasBola = Label (frame, text="Luas Selimut:") 
luasBola.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Bola

txtLuasBola = Entry(frame)
txtLuasBola.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output label Volume

Volume = Label (frame, text="Volume: ") 
Volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan

txtVolume = Entry (frame)
txtVolume.grid(row=3, column=1, sticky=W, padx=5, pady=5)


app.mainloop()

