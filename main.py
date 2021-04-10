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
        self.PRIMARY_COLOR = "#DF0000"
        self.SECOND_COLOR = "#FF7676"
        self.config(bg=self.PRIMARY_COLOR)
        self.YoutubeLogo = tk.PhotoImage(file=r"assets\youtube.png").zoom(2).subsample(8)
        self.VIDEO_PATH = r"C:\Users\HP\Desktop\Projet personnel\youtube_downloader\Video"

        # Start Window
        self.components()

    # Permit to open youtube
    def OpenYoutube(self):
        webbrowser.open("https://www.youtube.com/")

    # Download the video
    def download(self):
        URL = self.getURL()
        if os.path.exists(self.VIDEO_PATH):
            try:
                y = YouTube(URL).streams.first().download(self.VIDEO_PATH)
                tkinter.messagebox.showinfo("Success", "The video has been downloaded")
            except EOFError:
                tkinter.messagebox.showerror("Error","There was an error downloading the video. Try Again... ")
                print(EOFError)
        else:
            os.mkdir(self.VIDEO_PATH)
            try:
                y = YouTube(URL).streams.first().download(self.VIDEO_PATH)
                tkinter.messagebox.showinfo(
                    "Success", "The video has been downloaded")
            except EOFError:
                tkinter.messagebox.showerror("Error","There was an error downloading the video. Try Again... ")
                print(EOFError)

    # Start all components of window
    def components(self):
        print(""" GITHUB : https://github.com/Kyrokx """)

        self.Input = tk.Entry(self, bg=self.SECOND_COLOR, font=("Helvetica", 20), fg="BLACK")
        self.Input.place(x=150, y=200)

        self.Button = tk.Button(self, text="Download", bg=self.SECOND_COLOR, font=("Helvetica", 20),fg="BLACK", command=self.download)
        self.Button.place(x=220, y=250)

        self.Imgbutton = tk.Button(self, image=self.YoutubeLogo, bg=self.PRIMARY_COLOR, bd=0, command=self.OpenYoutube)
        self.Imgbutton.pack()

        self.mainloop()

    # Get the yt link
    def getURL(self):
        link = self.Input.get()
        if link.startswith("https://youtu.be"):
            return link
        else:
            return tkinter.messagebox.showwarning("Attention", "Votre lien doit comenmcer par 'https://youtu.be' !")
            sys.exit(0)


app = Main()