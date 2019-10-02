from tkinter import *


class VigenereCipher:
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    text = None
    keyInput = None
    mode = None
    result = None

    def encrypt(self, text, key):
        self.result = ""
        kpos = []

        # Mendapatkan nilai angka pada key
        for x in key:
            kpos.append(self.alphabets.find(x))

        # Variable i disini akan menjadi patokan key mana yang akan digunakan per karakter
        i = 0

        for x in str(text):
            # Jika karakter bukan merupakan huruf maka langsung tambahkan ke hasil
            if x.isalpha():

                # Jika value i sama dengan panjang key, maka kembalikan nilai i jadi 0
                if i == len(kpos):
                    i = 0

                pos = self.alphabets.find(x) + kpos[i]
                if pos > 25:
                    pos = pos - 26
                self.result += self.alphabets[pos].capitalize()
                i += 1
            else:
                self.result += x
        return self.result

    def decrypt(self, text, key):
        self.result = ""
        kpos = []
        for x in key:
            kpos.append(self.alphabets.find(x))
        i = 0
        for x in str(text):
            if x.isalpha():
                if i == len(kpos):
                    i = 0
                pos = self.alphabets.find(x.lower()) - kpos[i]
                if pos < 0:
                    pos = pos + 26
                self.result += self.alphabets[pos].lower()
                i += 1
            else:
                self.result += x

        return self.result


class gui:
    window = Tk()
    inputText = None
    inputKey = None
    resCipher = None
    enkrip = None
    dekrip = None
    vigenereCipher = VigenereCipher()

    def __init__(self):
        self.window.title("Vigenere Cipher")
        self.window.geometry("300x300")
        self.inputText = Entry(self.window, width=20)
        self.inputText.grid(column=0, row=0)
        self.inputKey = Entry(self.window, width=5)
        self.inputKey.grid(column=1, row=0)
        self.resCipher = Entry(self.window, width=20)
        self.resCipher.grid(column=0, row=1)

        self.enkrip = Button(self.window, text="Enrkipsi", width=10, command=self.encrypt)
        self.enkrip.grid(column=0, row=2)
        self.dekrip = Button(self.window, text="Dekripsi", width=10, command=self.decrypt)
        self.dekrip.grid(column=1, row=2)

        self.window.mainloop()

    def encrypt(self):
        text = self.inputText.get()
        key = self.inputKey.get()
        hasil = self.vigenereCipher.encrypt(text, key)
        self.resCipher.insert(0, "")
        self.resCipher.insert(0, hasil)

    def decrypt(self):
        text = self.inputText.get()
        key = self.inputKey.get()
        hasil = self.vigenereCipher.decrypt(text, key)
        self.resCipher.insert(0, "")
        self.resCipher.insert(0, hasil)


if __name__ == "__main__":
    baru = gui()
