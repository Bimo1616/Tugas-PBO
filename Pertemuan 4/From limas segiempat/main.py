import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from fungsi import hitung_luas, hitung_volume

def hitung():
    hasil_luas = hitung_luas(txtluas_sisi1.get(),txtluas_sisi2.get(),txtluas_sisi3.get(),txtluas_sisi4.get(),txtluas_sisi5.get())
    hasil_volume = hitung_volume(txtluas_alas.get(),txttinggi.get())
    txtluas.delete(0,END)
    txtluas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)


    
# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Limas Segiempat")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Luas Sisi 1
luas_sisi1 = Label(frame, text="Luas Sisi 1:")
luas_sisi1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 1
txtluas_sisi1 = Entry(frame)
txtluas_sisi1.grid(row=0, column=1)

# Label Luas Sisi 2
luas_sisi2 = Label(frame, text="Luas Sisi 2:")
luas_sisi2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 2
txtluas_sisi2 = Entry(frame)
txtluas_sisi2.grid(row=1, column=1)

# Label Luas Sisi 3
luas_sisi3 = Label(frame, text="Luas Sisi 3:")
luas_sisi3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 3
txtluas_sisi3 = Entry(frame)
txtluas_sisi3.grid(row=2, column=1)

# Label Luas Sisi 4
luas_sisi4 = Label(frame, text="Luas Sisi 4:")
luas_sisi4.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 4
txtluas_sisi4 = Entry(frame)
txtluas_sisi4.grid(row=3, column=1)

# Label Luas Sisi 5
luas_sisi5 = Label(frame, text="Luas Sisi 5:")
luas_sisi5.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Sisi 5
txtluas_sisi5 = Entry(frame)
txtluas_sisi5.grid(row=4, column=1)

# Label Luas Alas
luas_alas = Label(frame, text="Luas Alas:")
luas_alas.grid(row=5, column=0, sticky=W, padx=5, pady= 5)
# Textbox Luas Alas
txtluas_alas = Entry(frame)
txtluas_alas.grid(row=5, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=6, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=6, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Luas
luas = Label(frame, text="Luas:")
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=8, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)
# Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=9, column=1)

app.mainloop()