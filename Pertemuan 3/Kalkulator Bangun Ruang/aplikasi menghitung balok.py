import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
  
     p = float(panjang.get())

     l = float(lebar.get())
      
     t = float(tinggi.get())
   
     L = round ((2 * p * l) + ( 2 * p * t ) + ( 2 * l * t) ) 
  
     txtLuas.delete(0, END)
     txtLuas.insert(END, L) 

def hitung_keliling():
    
     p = float(panjang.get())

     l = float(lebar.get())
      
     t = float(tinggi.get())

     K = round ( p * l * t)

   
     txtkeliling.delete(0, END)
     txtkeliling.insert(END,K)

def hitung():
  hitung_luas()
  hitung_keliling()
   # Create tkinter object

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Keliling balok")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label panjang

okehpanjang = Label (frame, text="panjang: ")
okehpanjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox panjang

panjang = Entry (frame)
panjang.grid(row=0, column=1)

# Label tinggi

okehtinggi = Label (frame, text="tinggi: ")
okehtinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox tinggi

tinggi = Entry (frame)
tinggi.grid(row=1, column=1)

# Label lebar

okehlebar = Label (frame, text="lebar: ")
okehlebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# Textbox lebar

lebar = Entry (frame)
lebar.grid(row=2, column=1)


# Button

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas

luas = Label (frame, text="Luas: ") 
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas

txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output label Keliling

keliling = Label (frame, text="Keliling: ") 
keliling.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Keliling

txtkeliling = Entry (frame)
txtkeliling.grid(row=5, column=1, sticky=W, padx=5, pady=5)


app.mainloop()

