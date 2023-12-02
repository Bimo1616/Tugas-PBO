import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hitung_bmi():
    tinggi = float(tinggi_entry.get()) / 100
    berat = float(berat_entry.get())
    umur = int(umur_entry.get())
    jenis_kelamin = jenis_kelamin_var.get()

    bmi = berat / (tinggi ** 2)
    bmi_label.config(text=f'BMI: {bmi:.2f}')

    if jenis_kelamin == "Laki-laki":
        if umur < 18:
            status_label.config(text='Status: Terlalu Muda untuk Penilaian')
        else:
            if bmi < 17:
                status_label.config(text='Status: Kurus')
            elif 17 <= bmi < 23:
                status_label.config(text='Status: Normal')
            elif 23 <= bmi < 27:
                status_label.config(text='Status: Kelebihan Berat')
            else:
                status_label.config(text='Status: Obesitas')
    elif jenis_kelamin == "Perempuan":
        if umur < 18:
            status_label.config(text='Status: Terlalu Muda untuk Penilaian')
        else:
            if bmi < 16:
                status_label.config(text='Status: Kurus')
            elif 16 <= bmi < 22:
                status_label.config(text='Status: Normal')
            elif 22 <= bmi < 27:
                status_label.config(text='Status: Kelebihan Berat')
            else:
                status_label.config(text='Status: Obesitas')

    # Menambahkan data ke grafik
    data = {'Laki-laki': [17, 23, 27],
            'Perempuan': [16, 22, 27]}
    bmi_range = data[jenis_kelamin]

    ax.clear()
    ax.bar(['Kurus', 'Normal', 'Kelebihan Berat', 'Obesitas'],
           [bmi_range[0], bmi_range[1] - bmi_range[0], bmi_range[2] - bmi_range[1], 40 - bmi_range[2]],
           color=['red', 'green', 'yellow', 'red'])
    ax.set_ylabel('Rentang BMI')
    ax.set_title(f'Rentang BMI {jenis_kelamin}')
    canvas.draw()

app = tk.Tk()
app.title('Kalkulator BMI')

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

tinggi_label = tk.Label(frame, text='Tinggi (cm):')
tinggi_label.grid(row=0, column=0)

tinggi_entry = tk.Entry(frame)
tinggi_entry.grid(row=0, column=1)

berat_label = tk.Label(frame, text='Berat (kg):')
berat_label.grid(row=1, column=0)

berat_entry = tk.Entry(frame)
berat_entry.grid(row=1, column=1)

umur_label = tk.Label(frame, text='Umur:')
umur_label.grid(row=2, column=0)

umur_entry = tk.Entry(frame)
umur_entry.grid(row=2, column=1)

jenis_kelamin_label = tk.Label(frame, text='Jenis Kelamin:')
jenis_kelamin_label.grid(row=3, column=0)

jenis_kelamin_var = tk.StringVar()
jenis_kelamin_var.set("Laki-laki")

jenis_kelamin_option = tk.OptionMenu(frame, jenis_kelamin_var, "Laki-laki", "Perempuan")
jenis_kelamin_option.grid(row=3, column=1)

hitung_button = tk.Button(frame, text='Hitung BMI', command=hitung_bmi)
hitung_button.grid(row=4, columnspan=2)

bmi_label = tk.Label(frame, text='BMI: ')
bmi_label.grid(row=5, columnspan=2)

status_label = tk.Label(frame, text='Status: ')
status_label.grid(row=6, columnspan=2)

# Menambahkan grafik
figure = Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, master=app)
canvas.get_tk_widget().pack()

app.mainloop()