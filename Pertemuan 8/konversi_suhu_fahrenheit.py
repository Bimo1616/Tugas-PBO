from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)      
        # pasang Label
        Label(mainFrame, text='Fahrenheit:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=4,column=0,sticky=W,padx=5,pady=5)
        Label(mainFrame,text="Kelvin:").grid(row=5,column=0,sticky=W,padx=5,pady=5)

        # pasang textbox
        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=1, column=1, padx=5, pady=5)  
        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=3, column=1, padx=5, pady=5)
        self.txtReamur = Entry(mainFrame)
        self.txtReamur.grid(row=4,column=1,padx=5,pady=5)
        self.txtKelvin = Entry(mainFrame)
        self.txtKelvin.grid(row=5,column=1,padx=5,pady=5)
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung konversi suhu 
    def onHitung(self):
        #konversi celcius
        F = int(self.txtFahrenheit.get())
        value = (5/9 * (F - 32))
        self.txtCelcius.delete(0,END)
        self.txtCelcius.insert(END,str(value))

        #konversi reamur
        F = int(self.txtFahrenheit.get())
        value = (4/9 * (F - 32))
        self.txtReamur.delete(0,END)
        self.txtReamur.insert(END,(str(value)))

        #konversi kelvin
        F = int(self.txtFahrenheit.get())
        value = (5/9 * (F - 32)+ 273)
        self.txtKelvin.delete(0,END)
        self.txtKelvin.insert(END,(str(value)))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmSuhu(root, "Program Konversi Suhu")
    root.mainloop() 