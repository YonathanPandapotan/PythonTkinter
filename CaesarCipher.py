from tkinter import *


class CaesarCipher:
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    text = None
    keyInput = None
    mode = None
    result = None

    def encrypt(self, text, key):
        self.result = ""

        for x in str(text):
            # Jika karakter bukan merupakan huruf maka langsung tambahkan ke hasil
            if x.isalpha():
                pos = self.alphabets.find(x) + key
                if pos > 25:
                    pos = pos - 26
                self.result += self.alphabets[pos].capitalize()
            else:
                self.result += x
        return self.result

    def decrypt(self, text, key):
        self.result = ""

        for x in str(text):
            if x.isalpha():
                pos = self.alphabets.find(x.lower()) - key
                if pos < 0:
                    pos = pos + 26
                self.result += self.alphabets[pos].lower()
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
    caesarCipher = CaesarCipher()

    def __init__(self):
        self.window.title("Caesar Cipher")
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
        hasil = self.caesarCipher.encrypt(text, int(key))
        self.resCipher.insert(0, hasil)

    def decrypt(self):
        text = self.inputText.get()
        key = self.inputKey.get()
        hasil = self.caesarCipher.decrypt(text, int(key))
        self.resCipher.insert(0, hasil)


if __name__ == "__main__":
    baru = gui()
