import tkinter as tk
import tkinter.messagebox
from pytube import YouTube
import os
import sys
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
        self.YTimg = tk.PhotoImage(file=r"assets\youtube.png").zoom(2).subsample(8)
        self.PATH = r" PUT THE PATH OF DIRECTORY THAT VIDEO WILL BE REGISTERED "

        # Start Window
        self.components()

    # Open YouTube
    def openYoutube(self):
        webbrowser.open("https://www.youtube.com/")

    # Download the video
    def download(self):
        url = self.getURL()

        try:
            if os.path.exists(self.PATH):
                os.mkdir(self.PATH)
            y = YouTube(url).streams.first().download(self.PATH)
            tkinter.messagebox.showinfo("Success", "The video has been successfully downloaded.")
        except EOFError:
            tkinter.messagebox.showerror("ERROR", "An error happened during the download of the video. Please retry...")
            print(EOFError)

    # Launch window's components
    def components(self):
        print("""\n\n GITHUB : https://github.com/Kyrokx \n\n""")
        self.Input = tk.Entry(self, bg=self.__INPUT_MAIN_COLOR___, font=("Helvetica", 20), fg="BLACK")
        self.Input.place(x=150, y=200)

        self.Button = tk.Button(
            self,
            text="Download",
            bg=self.__INPUT_MAIN_COLOR___,
            font=("Helvetica", 20),
            fg="BLACK",
            command=self.download
        )
        self.Button.place(x=220, y=250)

        self.Imgbutton = tk.Button(
            self,
            image=self.YTimg,
            bg=self.__MAIN_COLOR___,
            bd=0,
            command=self.openYoutube
        )
        self.Imgbutton.pack()

        self.mainloop()

    # Get the link
    def getURL(self):
        x = self.Input.get()
        if x.startswith("https://youtu.be"):
            return x
        else:
            return tkinter.messagebox.showwarning("Warning", "Your link must begin with 'https://youtu.be'!")
            sys.exit(0)


app = Main()