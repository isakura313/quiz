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


class CreatorPlayerFrame(Frame):
    def __init__(self, window, title, background_image = None):
        super().__init__(window, title, background_image)

        #Создание подписи для поля ввода имени
        name_label = ttk.Label(self.frame, text="Имя игрока: ")
        name_label.place(relx = 0.01, rely = 0.01, anchor = tk.NW)

        self.name_field = ttk.Entry(self.frame)
        self.name_field.place(relx = 0.01, rely = 0.05, anchor = tk.NW)
        #подпись для ввода возраста игрока
        age_label = ttk.Label(self.frame, text = "Возраст игрока")
        age_label.place(relx = 0.01, rely = 0.1, anchor = tk.NW)

        self.age_field = ttk.Entry(self.frame)
        self.age_field.place(relx = 0.01, rely = 0.15, anchor = tk.NW)

        #создание подписи для списка выбора пола игрока
        gender_label = ttk.Label(self.frame, text = "Пол игрока..")
        gender_label.place(relx = 0.01, rely = 0.2, anchor = tk.NW)
        #Создание списка выбора пола
        self.gender_field = ttk.Combobox(self.frame, value = ['Мужской', 'Женский'])
        self.gender_field.place(relx = 0.01, rely = 0.25, anchor = tk.NW)

    def choose_player_picture(self):
        self.path_to_photo = filedialog.askopenfilename(
            master = self.frame, title = "Выберете авку игрока", filetype=(('Image files', '*.png *.jpg *.jpeg *.gif'),)
        )
        photo = ImageTk.PhotoImage(Image.open(self.path_to_photo).resize((350, 350), Image.ANTIALIAS))
        self.photo.configure(image= photo)
        self.photo.image = photo

    def create_player(self):
        player = player_class.Player(
            self.name_field.get(), int(self.age_field.get()), self.gender_field.get(), self.path_to_photo
        )

if __name__ == '__main__':
    game = Window()
    game.start()