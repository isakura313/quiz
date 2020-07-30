import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

import player_class

class Window:
    """
    Главное окно
    """
    def __init__(self, title='Главное', width = 600, height=600):
        self.width = 600
        self.height = 600
        self.size = f'{width}x{height}'
        self.display = tk.Tk()
        self.display.title(title)
        self.display.geometry(self.size)
        self.display.resizable(0,0)

    def start(self):
        self.display.mainloop()

class Frame:
    """ Класс, в котором сменяются картинки"""
    def __init__(self, window, title, background_image = None):
        self.window = window
        self.frame = ttk.Frame(window.display, width = window.width, height = window.height )
        self.title = title
        self.change_title()

        self.style = ttk.Style()
        self.style.configure('TLabel', font = ("Calibri", 16))
        self.set_background_image(background_image)
        self.frame.grid(row = 0, column = 0, sticky = 'nsew')

    def activate(self):
        self.frame.tkraise()

    def change_title(self):
        self.frame.title(self.title)

    def set_background_image(self, background_image):
        if background_image:
            image = ImageTk.PhotoImage(
                Image.open(background_image).resize((self.window.width, self.window.height), Image.ANTIALIAS)
            )
            background_label = ttk.Label(self.frame, image = image)
            background_label.image = image
            background_label.place(x=0, y = 0, relwidth = 1, relheight = 1)

if __name__ == '__main__':
    game = Window()
    game.start()