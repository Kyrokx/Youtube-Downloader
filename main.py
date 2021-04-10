import tkinter as tk
import tkinter.messagebox
from pytube import YouTube
import os
import sys
import time
import webbrowser

"""
By Kyrokx - 24/03/2021
Discord = Kyrokx( " ゴールド開発者 " )#7573
Youtube downloader
Please add star "⭐" for me 🥺
"""


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Window
        self.title("Youtube Video downloader")
        self.iconbitmap("assets/youtube.ico")
        self.resizable(False, False)
        self.minsize(600, 400)
        # Config
        self.__MAIN_COLOR___ = "#DF0000"
        self.__INPUT_MAIN_COLOR___ = "#FF7676"
        self.config(bg=self.__MAIN_COLOR___)
        self.YTimg = tk.PhotoImage(
            file=r"assets\youtube.png").zoom(2).subsample(8)
        self.PATH = r" PUT THE PATH OF DIRECTORY THAT VIDEO WILL BE REGISTERED "

        # Start Window
        self.components()

    # Permet d'ouvrir youtube

    def OpenYoutube(self):
        webbrowser.open("https://www.youtube.com/")

    # Télécharger le vidéo
    def download(self):
        URL = self.getURL()
        if os.path.exists(self.PATH):
            try:
                y = YouTube(URL).streams.first().download(self.PATH)
                tkinter.messagebox.showinfo(
                    "Succès", "La video a bien été télécharger...")
            except EOFError:
                tkinter.messagebox.showerror("ERREUR",
                                             "Il y a eu un erreur avec le téléchargement de le vidéo. Veuillez réessayer... ")
                print(EOFError)
        else:
            os.mkdir(self.PATH)
            try:
                y = YouTube(URL).streams.first().download(self.PATH)
                tkinter.messagebox.showinfo(
                    "Succès", "La video a bien été télécharger...")
            except EOFError:
                tkinter.messagebox.showerror("ERREUR",
                                             "Il y a eu un erreur avec le téléchargement de le vidéo. Veuillez réessayer... ")
                print(EOFError)

    # Démarrer les composent de la fêntre
    def components(self):
        print("""

        GITHUB : https://github.com/Kyrokx
        """)
        self.Input = tk.Entry(self, bg=self.__INPUT_MAIN_COLOR___, font=(
            "Helvetica", 20), fg="BLACK")
        self.Input.place(x=150, y=200)

        self.Button = tk.Button(self, text="Download", bg=self.__INPUT_MAIN_COLOR___, font=("Helvetica", 20),
                                fg="BLACK", command=self.download)
        self.Button.place(x=220, y=250)

        self.Imgbutton = tk.Button(
            self, image=self.YTimg, bg=self.__MAIN_COLOR___, bd=0, command=self.OpenYoutube)
        self.Imgbutton.pack()

        self.mainloop()

    # Recupére le lien
    def getURL(self):
        x = self.Input.get()
        if x.startswith("https://youtu.be"):
            return x
        else:
            return tkinter.messagebox.showwarning("Attention", "Votre lien doit comenmcer par 'https://youtu.be' !")
            sys.exit(0)


app = Main()