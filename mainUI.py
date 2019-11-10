import os
import binascii
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from Decoders.uniCodeStego import removeNonAscii
from Decoders.phaseDecode import phraseDecode
from Decoders.quickStego import quickStego
from Decoders.unicode2 import uniCode2
from Decoders.LSBStego import DecodeLSB
from Decoders.steganoDecode import steganoRevealLSB
from Decoders.wavFileDecode import decodingWav
from Decoders.LSB_8bit_mk5 import decodeLSB
from Decoders.spectrology import decodeSpec

root = tk.Tk()
nb = tk.Frame(root)
openFile =NONE
asciiText = NONE


class page1(tk.Frame):
    def __init__(self, parent):
        self.bfLength = StringVar()
        self.dfCon = None
        self.dfGov = None

        tk.Frame.__init__(self, parent)
        nb = ttk.Notebook(root)

        self.tab1 = tk.Frame(nb)
        self.tab1 = tk.Frame(nb)
        nb.add(self.tab1, text='Steganography')

        nb.pack(expand=1, fill="both")

        # labels/placements for GUI
        l1 = tk.Label(self.tab1, text="Upload files")
        l1.pack()
        l1.place(x=10, y=10)

        # Upload File
        l2 = tk.Label(self.tab1, text="Upload File")
        l2.pack()
        l2.place(x=70, y=30)
        # Successfully upload
        self.l2_2 = tk.Label(self.tab1, fg="dark green")
        self.l2_2.pack()
        self.l2_2.place(x=200, y=30)

        # buttons/placements for GUI
        # tab1
        b1 = tk.Button(self.tab1, text="Browse", command=self.uploadFile)
        b1.pack()
        b1.place(x=10, y=30)

        self.labelframe = LabelFrame(self.tab1, text="%s" % "Input")
        self.labelframe.place(x=10, y=70, height=600, width=500)
        # labelframe.pack(side=BOTTOM,fill="both", expand="no")

        self.labelframe2 = LabelFrame(self.tab1, text="%s" % "Output")
        self.labelframe2.place(x=520, y=70, height=600, width=500)
        # labelframe2.pack(side=BOTTOM,fill="both", expand="no")

        # input
        self.T = Text(self.labelframe, width=50)
        self.scroll = Scrollbar(self.labelframe, command=self.T.yview)
        self.T.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)

        # output
        self.T2 = Text(self.labelframe2, width=50)
        self.scroll2 = Scrollbar(self.labelframe2, command=self.T2.yview)
        self.T2.configure(yscrollcommand=self.scroll2.set)
        self.scroll2.pack(side=RIGHT, fill=Y)

        # label for dropdown
        # Upload File
        l3 = tk.Label(self.tab1, text="Steganography Algorithms")
        l3.pack()
        l3.place(x=550, y=10)
        l4 = tk.Label(self.tab1, text="Length For Brute Force")
        l4.pack()
        l4.place(x=850, y=10)
        # steganography algo dropdown
        variable = StringVar(self.tab1)
        listFunc = ["UnicodeStego","PhaseStego","QuickStego","LSBStego","WavStego2","LSBImage","SpectrologyDecode","SteganoLSB","UnicodeStego2",
                    "OpenStego"]
        variable.set("Please select stegonagraphy algo: ")  # default value
        dropdown = OptionMenu(self.tab1, variable, *listFunc, command=self.basicFunctions)
        dropdown.pack()
        dropdown.place(x=550, y=30, width=250)
        self.T3 = tk.Entry(self.tab1, width=10,textvariable=self.bfLength)
        self.T3.pack()
        self.T3.place(x=850,y=30)

    def close_window(self):
        root.destroy()

    def uploadFile(self):
        try:
            global openFile
            global asciiText
            openFile = filedialog.askopenfilename(filetypes=(("", ".txt"),("",".wav"),("",".bmp"), ("",".png"),("All files", "*.*")))
            # self.T.delete('0',END)
            with open(openFile,"rb") as file:
                #text=file.read().replace('\n', '')
                text = binascii.hexlify(file.read())
                asciiText= binascii.unhexlify(text)
                self.inputText = asciiText
                self.T.configure(state='normal')
                self.T.delete(1.0, END)
                self.T.insert(END, self.inputText)
                self.T.configure(state='disabled')
                self.T.pack(side=LEFT, fill="both", expand="yes")
            self.l2_2.configure(text=str(os.path.basename(openFile)) + " successfully uploaded!")
        except:
            messagebox.showinfo("Error", "Failed to upload file")

    def basicFunctions(self, x):
        if(openFile==NONE):
            messagebox.showinfo("Error", "Select a File first")
            return
        try:
            if x == "To Hex":
                decoded = " ".join("{:02x}".format(ord(c)) for c in self.inputText)
            elif x== "UnicodeStego":
                decoded =removeNonAscii(openFile)
            elif x== "QuickStego":
                decoded = quickStego(openFile)
            elif x== "UnicodeStego2":
                decoded = uniCode2(openFile)
            elif x== "LSBStego":
                decoded = DecodeLSB(openFile)
            elif x== "PhaseStego":
                length= int(self.bfLength.get())
                if(length!=NONE):
                    decoded=phraseDecode(openFile,length)
                else:
                    messagebox .showinfo("Error", "Enter a length for brute force")
            elif x== "SteganoLSB":
                decoded=steganoRevealLSB(openFile)
            elif x== "wavStego2":
                decoded = decodingWav(openFile)
            elif x== "LSBImage":
                decoded = decodeLSB(openFile)
            elif x== "SpectrologyDecode":
                decoded = decodeSpec()

            self.T2.configure(state='normal')
            self.T2.delete(1.0, END)
            self.T2.insert(END, decoded)
            self.T2.configure(state='disabled')
            self.T2.pack(side=RIGHT, fill="both", expand="yes")
        except:
            messagebox.showinfo("Error", "Unable to decode any text!")

    def FromHex(self):
        try:
            asciiText = self.inputText.decode("hex")
            self.T2.configure(state='normal')
            self.T2.delete(1.0, END)
            self.T2.insert(END, asciiText)
            self.T2.configure(state='disabled')
            self.T2.pack(side=RIGHT, fill="both", expand="yes")
        except:
            messagebox.showinfo("Error", "Wrong input format! Hex characters only")

    def ToHex(self):
        try:
            print (asciiText)
            hexText = binascii.hexlify(asciiText)
            self.T2.configure(state='normal')
            self.T2.delete(1.0, END)
            self.T2.insert(END, hexText)
            self.T2.configure(state='disabled')
            self.T2.pack(side=RIGHT, fill="both", expand="yes")
        except:
            messagebox.showinfo("Error", "Wrong input format! ASCII characters only")


def main():
    page1(root)

    root.title("Digital Forensics, Basil and Co")
    root.geometry("1025x700")

    root.mainloop()


if __name__ == "__main__":
    main()
