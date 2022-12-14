import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from functools import partial

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.id = controller.id

        self.loaded_photos = []
        self.photos_directory = 'Images/'
        self.photos = ['01p.jpg', '02p.jpg', '03p.jpg', '04p.jpg', '05p.jfif',
                       '09p.jpg', '10p.jpg', '10p.jpg', '10p.jpg',
                       '11p.jfif', '13p.jfif', '50d.png']
        self.load_photos()

        self.descriptions = ['clear sky', 'few clouds', 'scattered clouds', 'broken clouds', 'overcast clouds',
                             'shower rain', 'rain', 'light rain', 'moderate rain',
                             'thunderstorm', 'snow', 'mist']

        self.create_widget()

    def load_photos(self):
        for p in self.photos:
            image = Image.open(self.photos_directory + p)
            image = image.resize((900, 100))
            self.loaded_photos.append(ImageTk.PhotoImage(image))

    def create_widget(self):

        for index, value in enumerate(self.controller.citiesdata.keys()):

            meteodata = self.controller.citiesdata[value]

            i = self.descriptions.index(meteodata.description)

            c_button = tk.Button(master=self,
                             cursor="hand2",
                             command=partial(self.controller.up_frame, value),
                             border=0,
                             text=value,
                             font= ('Helvetica 15 bold'),
                             compound=CENTER
                            )
            c_button.config(image=self.loaded_photos[i])
            c_button.grid(row=index, column=0)


