from tkinter import *

# Pertama kita harus membuat window terlebih dahulu
# Window ini yang akan menjad 'canvas' untuk menaruh semua komponen
# Geometry untuk mengatur besarnya window
window = Tk()
window.title("Simple Get Set")
window.geometry("600x500")

# Cara untuk mendeklarasikan Label atau TextLabel pada java
# grid untuk menentukan letak dan lokasinya
ket = Label(window, text="Tolong massukan data anda")
ket.grid(column=0, row=0)

nDepan = Label(window, text="Nama Depan")
nDepan.grid(column=0, row=1)
nBelakang = Label(window, text="Nama Belakang")
nBelakang.grid(column=1, row=1)
umur = Label(window, text="Umur")
umur.grid(column=2, row=1)

# Entry untuk dapat menerima inputan dari user, equivalent dengan EditText java
iDepan = Entry(window, width=20)
iDepan.grid(column=0, row=2)
iBelakang = Entry(window, width=20)
iBelakang.grid(column=1, row=2)
iUmur = Entry(window, width=20)
iUmur.grid(column=2, row=2)

rDepan = Label(window, text="")
rBelakang = Label(window, text="")
rUmur = Label(window, text="")

def event():
    rDepan.configure(text=iDepan.get())
    rBelakang.configure(text=iBelakang.get())
    rUmur.configure(text=iUmur.get())

# Cara untuk mendeklarasikan button
enter = Button(window, text="Klik jika sudah", command=event)
enter.grid(column=1, row=3)

rDepan.grid(column=0, row=4)
rBelakang.grid(column=1, row=4)
rUmur.grid(column=2, row=4)

window.mainloop()