#Modul 8 (GUI)
#Modul 1 (variabel dan tipe data)
from tkinter import *  
from tkinter import messagebox 
from tkinter import ttk


def next () : #Function
        if stringnama.get () == 0 :
                msgn = messagebox.showerror(message="Semua identitas Harap Diisi")  
        elif stringnama.get () == " "  :
                msgn2 = messagebox.showerror(message="Semua identitas Harap Diisi")  
        elif stringcontact.get () == 0 :
                msgk = messagebox.showerror(message="Semua identitas Harap Diisi")
        elif stringcontact.get () == " "  :
                msgk = messagebox.showerror(message="Semua identitas Harap Diisi")
        elif strpekerjaan.get () == 0 :
                msgp = messagebox.showerror(message="Semua identitas Harap Diisi")  
        elif radio.get () == 0 :
                msgr = messagebox.showerror(message="Semua identitas Harap Diisi")
        else :
                global nw
                nw = Frame (root, bg='deep sky blue', width=800, height=400)
                nw.pack ()
                root.geometry("400x250")
                root.title("Hasil")
                #input
                nama = stringnama.get () #Modul 6 (Getter)
                kontak = stringcontact.get ()
                lblk = Label(nw, text=kontak, bg='deep sky blue', fg='white', font=("times", "18", "bold")).place(x=10, y=130)
                #jk 
                gender = " " 
                if radio.get () == 1 : #Modul 2 (IF ELSE)
                        gender = "Mr. "
                else :
                        gender = "Mrs. "
                lbljk=Label(nw, text= gender+nama, bg='deep sky blue', fg='white', font=("times", "18", "bold")).place(x=10, y=70)
                #Job
                job = strpekerjaan.get ()
                lblj = Label (nw, text=job, bg='deep sky blue', fg='white', font=("times", "18", "bold")).place(x=10, y=160)
                lblb1= Label(nw, text=" ", bg="red", width=100, fg="white", font=("times", "20", "bold")).place(x=0, y=0)
                lblb2= Label(nw, text=" ", bg="white", width=100, fg="white", font=("times", "20", "bold")).place(x=0, y=35)
                quit1 = Button(nw, text="Quit", command=root.destroy, width=10, bg="red", fg="white", font=("times", "14", "bold")).place(x=210, y=200)
                re = Button (nw, text="Buat Lagi", command= redo, width=10, bg="red", fg="white", font=("times", "14", "bold")).place(x=80, y=200)
                #ttl
                lablttl = Label(nw, text=day.get()+"-"+month.get ()+"-"+year.get (), bg='deep sky blue', fg='white', font=("times", "18", "bold")).place(x=10, y=100)
def snk () :
    syarat = ["1. Semua data harus diisi\n", "2. Mohon data diisi dengan benar\n", "3. Semua data yang dicantumkan harus bisa \tdipertanggungjawabkan\n", 
                "4. Harap gunakan nomor telepon Indonesia"]     
    for x in syarat :#Modul 3 (Perulangan For)
            msg = messagebox.showinfo(message="".join(syarat))
            x =+ 1
            break
def redo () :
    nw.destroy ()
    root.geometry("800x400")
    root.title(" Program Pembuatan Kartu Nama")



root = Tk ()
root.geometry("800x400")
root.title(" Program Pembuatan Kartu Nama")
foto=PhotoImage(file="garuda_1-removebg-preview (1).png")
foto1=Label(root, image=foto, bg="black").place(x=550, y=70)
root['bg'] = "black"




#Modul 5 (Class) 
class hal1 :
        #Modul 4 (Method)
        def __init__(self) : 
                self.tulisan = self.label ()
                self.entry = self.input ()
                self.tombol = self.button ()
                self.jk = self.radio ()
                self.cb = self.combo ()
        #Function
        
        def button (self) :     
                #Button
                slsi = Button(root, text="Submit", command=next, width=20, bg="red", fg="white", font=("times", "14", "bold")).place(x=280, y=340)
                quit = Button(root, text="Quit", command=root.destroy, width=20, bg="red", fg="white", font=("times", "14", "bold")).place(x=550, y=340)
                btnsnk = Button(root, text="Syarat dan Ketentuan", command=snk, width=20, bg="red", fg="white", font=("times", "14", "bold")).place(x=10, y=340) 
        def label (self) :
                #Label
                lblb1= Label(root, text=" ", bg="red", width=100, fg="white", font=("times", "20", "bold")).place(x=0, y=0)
                lblb2= Label(root, text=" ", bg="white", width=100, fg="white", font=("times", "20", "bold")).place(x=0, y=35)
                nama = Label(root, text="Masukkan Nama Anda : ", bg="red", fg="white",).place(x= 10, y= 80)
                umur = Label(root, text="Masukkan Tanggal Lahir Anda : ", bg="blue", fg="white").place(x= 10, y= 105)
                gender = Label(root, text="Pilih Jenis Kelamin !", bg="green", fg="white").place(x= 10, y= 130)
                pekerjaan = Label(root, text="Masukkan Profesi Anda : ", bg="red", fg="white").place(x= 10, y= 205)
                contact = Label(root, text="Masukkan Nomor yang dapat dihubungi : ", bg="green", fg="white").place(x= 10, y= 260)
                te=Label(root, text=" ", bg="red", width=100, fg="white", font=("times", "20", "bold")).place(x=0, y=290)
                
                
        def input (self) :
                #Entry
                global stringnama 
                global stringcontact
                stringnama = StringVar ()
                stringcontact = StringVar ()
                innama = Entry (root, width=40, textvariable=stringnama).place(x= 150, y= 80)
                incontact = Entry (root, width=40, textvariable=stringcontact).place(x= 250, y= 260)
        def radio (self) :
                #Radio
                global radio 
                radio = IntVar()
                R1 = Radiobutton(root, text="Pria      ", variable=radio, value=1).place(x=10, y=155)  
                R2 = Radiobutton(root, text="Wanita", variable=radio, value=2).place(x=10, y=175)  
        def combo (self) :
                #Combobox pekerjaan
                global strpekerjaan
                strpekerjaan = StringVar(value='Pilih Pekerjaan Anda') 
                Cb1 = ttk.Combobox(root, width = 20, textvariable = strpekerjaan, state="readonly")
                Cb1.place(x=10, y=230
                )
                Cb1['values']=('PNS', 
                                'SWASTA', 
                                'BUMN', 
                                'DOKTER', 
                                'PILOT', 
                                'TNI', 
                                'POLRI',
                                'PELAJAR/MAHASISWA')
                #Combobox TTL
                global day
                global month
                global year
                ttld = IntVar(value="Tanggal")
                ttlm = StringVar(value="Bulan")
                ttly = StringVar(value="Tahun")
                day = ttk.Combobox (root, width = 10, textvariable = ttld, state="readonly")
                day.place(x=190, y=105)
                garing = Label (root, text="   /", bg="black", fg='white').place(x=270, y=105)
                month = ttk.Combobox (root, width = 10, textvariable = ttlm, state="readonly")
                month.place(x=300, y=105)
                garing2 = Label(root, text="  /", bg="black", fg='white').place (x=380, y=105)
                year = ttk.Combobox (root, width = 10, textvariable = ttly, state="readonly")
                year.place(x=400, y=105)
                day ['values'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                month ['values'] = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
                year ['values']  =[1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

page = hal1 ()
root.mainloop()
    