import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
  
     Ls1 = float( LuasSisi1.get())
     Ls2 = float( LuasSisi2.get())
     Ls3 = float( LuasSisi3.get())
     Ls4 = float( LuasSisi4.get())
    

     L = round (Ls1+Ls2+Ls3+Ls4) 
  
     txtLuas.delete(0, END)
     txtLuas.insert(END, L) 

def hitung_keliling():
    
     La = float(LuasAlas.get())
     t  = float(Tinggi.get())

     K = round ( 1/6*La*t)

   
     txtkeliling.delete(0, END)
     txtkeliling.insert(END,K)

def hitung():
  hitung_luas()
  hitung_keliling()
   # Create tkinter object

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Keliling Limas Segi 4")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label Ls1

QLs1 = Label (frame, text="Luas Sisi 1: ")
QLs1.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Ls1

LuasSisi1 = Entry (frame)
LuasSisi1.grid(row=0, column=1)

# Label Ls2

QLs2 = Label (frame, text="Luas Sisi 2: ")
QLs2.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Textbox Ls2

LuasSisi2 = Entry (frame)
LuasSisi2.grid(row=1, column=1)

# Label Ls3

QLs3 = Label (frame, text="Luas Sisi 3: ")
QLs3.grid(row=2, column=0, sticky=W, padx=5, pady=5)


# Textbox lebar

LuasSisi3 = Entry (frame)
LuasSisi3.grid(row=2, column=1)

# Label Ls4

QLs4 = Label (frame, text="Luas Sisi 4: ")
QLs4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Ls4

LuasSisi4 = Entry (frame)
LuasSisi4.grid(row=3, column=1)


# Label La

QLa = Label (frame, text="Luas Alas: ")
QLa.grid(row=5, column=0, sticky=W, padx=5, pady=5)


# Textbox La

LuasAlas = Entry (frame)
LuasAlas.grid(row=5, column=1)

# Label Tinggi

QTinggi = Label (frame, text="Tinggi: ")
QTinggi.grid(row=6, column=0, sticky=W, padx=5, pady=5)


# Textbox Tinggi

Tinggi = Entry (frame)
Tinggi.grid(row=6, column=1)


# Button

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas

luas = Label (frame, text="Luas:") 
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas

txtLuas = Entry(frame)
txtLuas.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# Output label Keliling

keliling = Label (frame, text="Keliling: ") 
keliling.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Keliling

txtkeliling = Entry (frame)
txtkeliling.grid(row=9, column=1, sticky=W, padx=5, pady=5)


app.mainloop()

