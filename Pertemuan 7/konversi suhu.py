import tkinter as tk

def konversi_suhu():
    try:
        suhu_input = float(entry_suhu.get())
        jenis_suhu_input = jenis_suhu.get()

        if jenis_suhu_input == 'Celsius':
            suhu_celsius = suhu_input
            suhu_fahrenheit = (suhu_celsius * 9/5) + 32
            suhu_kelvin = suhu_celsius + 273.15
        elif jenis_suhu_input == 'Fahrenheit':
            suhu_fahrenheit = suhu_input
            suhu_celsius = (suhu_fahrenheit - 32) * 5/9
            suhu_kelvin = (suhu_fahrenheit - 32) * 5/9 + 273.15
        elif jenis_suhu_input == 'Kelvin':
            suhu_kelvin = suhu_input
            suhu_celsius = suhu_kelvin - 273.15
            suhu_fahrenheit = (suhu_kelvin - 273.15) * 9/5 + 32

        label_hasil.config(text=f"Hasil konversi: {suhu_celsius:.2f} Celsius, {suhu_fahrenheit:.2f} Fahrenheit, {suhu_kelvin:.2f} Kelvin")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid untuk suhu.")

# Membuat instance dari tkinter
root = tk.Tk()
root.title("Konversi Suhu")

# Membuat label
label_suhu = tk.Label(root, text="Masukkan suhu:")
label_suhu.grid(row=0, column=0, padx=10, pady=10)

# Membuat entry (input) untuk suhu
entry_suhu = tk.Entry(root)
entry_suhu.grid(row=0, column=1, padx=10, pady=10)

# Membuat opsi pilihan untuk jenis suhu
jenis_suhu = tk.StringVar()
jenis_suhu.set('Celsius')  # Default jenis suhu

dropdown_jenis_suhu = tk.OptionMenu(root, jenis_suhu, 'Celsius', 'Fahrenheit', 'Kelvin')
dropdown_jenis_suhu.grid(row=0, column=2, padx=10, pady=10)

# Membuat tombol konversi
tombol_konversi = tk.Button(root, text="Konversi", command=konversi_suhu)
tombol_konversi.grid(row=1, column=0, columnspan=3, pady=10)

# Membuat label hasil konversi
label_hasil = tk.Label(root, text="Hasil konversi: ")
label_hasil.grid(row=2, column=0, columnspan=3, pady=10)

# Menjalankan loop utama tkinter
root.mainloop()
