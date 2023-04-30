from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import object_detection as od 
import imageio 
import cv2  
class window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master 
        self.pos = []
        self.line = []
        self.rect = []
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        self.counter = 0
        menu= Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Open", command=self.open_file)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        analyse= Menu(menu)
        analyse.add_command(label="Region of Interest", command=self.regionOfInterest)
        menu.add_cascade(label="analyse", menu=analyse)
        self.filename="Images/home'jpg"
        self.imgSize= Image.open(self.filename)
        self.tksize= ImageTk.PhotoImage(self.imgsize)
        self.w, self.h= (1366, 768)
        self.canvas = Canvas(master=root, width=self.w, height=self.h)
