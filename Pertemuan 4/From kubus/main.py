import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi import hitung_luas, hitung_keliling

def hitung():
    hasil_luas = hitung_luas(txtrusuk.get())
    hasil_keliling = hitung_keliling(txtrusuk.get())
    txtLuas.delete(0, END)
    txtLuas.insert(END, hasil_luas)
    txtkeliling.delete(0, END)
    txtkeliling.insert(END,hasil_keliling)

  # Create tkinter object

app = tk. Tk()

# Tambahkan judul

app.title("Kalkulator Luas dan Keliling kubus")

# Windows

frame = Frame (app)
frame.pack(padx=20, pady=20)

# Label Rusuk

rusuk = Label (frame, text="rusuk: ")
rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Rusuk

txtrusuk = Entry (frame)
txtrusuk.grid(row=0, column=1)


# Button

hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas

luas = Label (frame, text="Luas: ") 
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas

txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output label Keliling

keliling = Label (frame, text="Keliling: ") 
keliling.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Keliling

txtkeliling = Entry (frame)
txtkeliling.grid(row=4, column=1, sticky=W, padx=5, pady=5)


app.mainloop()

  