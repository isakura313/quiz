import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import json
import random
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
        self.display.resizable(0, 0)

        self.frames = {'create_player':
                       CreatorPlayerFrame(self, 'Создать нового игрока', 'images/background1.png')}
        self.activate_frame('create_player')

    def start(self):
        self.display.mainloop()

    # функция создания главного кадра
    def create_main_frame(self, player):
        self.frames['main'] = MainFrame(self, "Main", player, 'question_ids', 'images/background2.png')


    def activate_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.activate()
        frame.change_title()

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
        self.frame.master.title(self.title)

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

        photo_label = ttk.Label(self.frame, text='Player photo:')
        photo_label.place(relx=0.4, rely=0.01, anchor=tk.NW)

        self.path_to_photo = 'images/no_photo.png'
        photo = ImageTk.PhotoImage(Image.open(self.path_to_photo).resize((350, 350), Image.ANTIALIAS))
        self.photo = ttk.Label(self.frame, image=photo, borderwidth=2, relief=tk.RAISED)
        self.photo.image = photo
        self.photo.place(relx=0.4, rely=0.05, anchor=tk.NW)

        photo_button = ttk.Button(self.frame, text='Choose player photo', command=self.choose_player_picture)
        photo_button.place(relx=0.4, rely=0.65, anchor=tk.NW)

        # Создание кнопки для создание игрока.
        create_button = ttk.Button(self.frame, text='Создать игрока', command=self.create_player)
        create_button.place(relx=0.8, rely=0.95, anchor=tk.NW)

    def choose_player_picture(self):
        self.path_to_photo = filedialog.askopenfilename(
            master=self.frame, title='Select player photo', filetypes=(('Image files', '*.png *.jpg *.jpeg *.gif'),)
        )
        photo = ImageTk.PhotoImage(Image.open(self.path_to_photo).resize((350, 350), Image.ANTIALIAS))
        self.photo.configure(image=photo)
        self.photo.image = photo


    def choose_player_picture(self):
        self.path_to_photo = filedialog.askopenfilename(
            master = self.frame, title = "Выберете авку игрока", defaultextension=(('Image files', '*.png *.jpg *.jpeg *.gif'),)
        )
        photo = ImageTk.PhotoImage(Image.open(self.path_to_photo).resize((350, 350), Image.ANTIALIAS))
        self.photo.configure(image= photo)
        self.photo.image = photo

    def create_player(self):
        player = player_class.Player(
            self.name_field.get(), int(self.age_field.get()), self.gender_field.get(), self.path_to_photo)
        self.window.create_main_frame(player)
        self.window.activate_frame('main')

class MainFrame(Frame):
    def __init__(self, window,  title, player, question_ids, background_image = None):
        super().__init__(window, title, background_image)

        question_ids = ['Cупергерои', ' Minecraft', 'CS GO', 'Кибербезопасность']

        photo = ImageTk.PhotoImage(Image.open(player.path_to_image).resize((300), Image.ANTIALIAS))
        player_photo = ttk.Label(self.frame, image = photo, borderwidth = 2, relief = tk.RAISED)
        player_photo.image = photo
        player_photo.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
        player_name = ttk.Label(self.frame, text = f"Имя: {player.name}", width = 40)
        player_name.place(relx =0.5, rely = 0.65, anchor = tk.CENTER)
        player_age = ttk.Label(self.frame, text = f"Возраст: {player.age}", width = 40)
        player_age.place(relx =0.5, rely = 0.7, anchor = tk.CENTER)

        player_gender = ttk.Label(self.frame, text = f"Пол: {player.gender}", width = 40)
        player_gender.place(relx =0.5, rely = 0.75, anchor = tk.CENTER)

        self.buttons = {}
        button_positions = [
            (0.2, 0.85), (0.5, 0.85), (0.8, 0.85),
            (0.2, 0.9), (0.5, 0.9), (0.8, 0.9),
            (0.2, 0.95), (0.5, 0.95), (0.8, 0.95),
        ]
        for i, question_id in enumerate(question_ids):
            position = button_positions[i]
            rel_x, rel_y = position
            button = ttk.Button(self.frame, text = f"Question #{question_id}", width = 15)
            button.id = question_id
            button.bind('<Button-1>', self.show_question)
            button.place(relx = rel_x, rely = rel_y, anchor = tk.CENTER)
            self.buttons[question_id] = button


    def show_question(self, event):
        button = event.widget
        question_id = button.id
        self.window.activate_frame(question_id)

class QuestionFrame(Frame):
    def __init__(self, window, question_id, question,
                 answers, path_to_image, background_image = None):
        title = f'Question #{question_id}'
        super().__init__(window, title, background_image)
        back_button = ttk.Button(self.frame, text = 'Назад', command = self.go_back)
        back_button.place(relx = 0.5, rely = 0.95, anchor = tk.CENTER)

    def go_back(self):
        self.activate_main_frame()

if __name__ == '__main__':
    game = Window()
    game.start()