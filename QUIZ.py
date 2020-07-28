import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

import player_class

class Window:
    def __init__(self, title='Main', width = 600, height=600):
        self.width = 600
        self.height = 600
        self.size = f'{width}x{height}'
        self.display = tk.Tk()
        self.display.title(title)
        self.display.geometry(self.size)
        self.display.resizable(0,0)

    def start(self):
        self.display.mainloop()

if __name__ == '__main__':
    game = Window()
    game.start()