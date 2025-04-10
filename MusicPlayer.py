import tkinter as tk
from pytube import YouTube
from tkinter import *
import os
from playsound import playsound

#Nodos
class Cancion:
    def __init__(self, titulo, ruta):
        self.titulo = titulo  # Titulo de la canción
        self.ant = None #Canción anterior
        self.sig = None  # Canción siguiente

class SongLibrary:
    def __init__(self):
        self.head = None  # Points to the first song in the list

    def add_song(self, titulo, ruta):
        new_song = Cancion(titulo, ruta)
        if self.head is None:  # If the library is empty, make this the first song
            self.head = new_song
        else:
            # Traverse to the end of the list and add the new song
            current = self.head
            while current.sig:
                current = current.sig
            current.sig = new_song
            new_song.ant = current

    def get_all_songs(self):
        songs = []
        current = self.head
        while current:
            songs.append(current.titulo)  # Collect song titles
            current = current.sig
        return songs
    
class MusicPlayerApp:
#Crear ventana de reproducción
     def __init__(self, window):
        self.window = window
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        self.window.title("Player")
        self.pause_state = False
        self.library = SongLibrary()
        
        # Añadir imagenes
        self.Img = {}
        self.add_Img(1, os.path.join("assets", "bg_400_300.png")) # Cargar imagen para background
        self.add_Img(2, os.path.join("assets", "music_124.png"))  # Cargar Imagen con su tamaño real
        self.add_Img(3, os.path.join("assets", "prev_64.png")) #Cargar anterior
        self.add_Img(4, os.path.join("assets", "next_64.png")) #Cargar siguiente
        self.add_Img(5, os.path.join("assets", "pause_64.png")) #Cargar pausa
        self.add_Img(6, os.path.join("assets", "play_64.png")) #Cargar play

        self.setup_main_window()

# Método Imagen
     def add_Img(self, index, ruta):
        try:
            self.Img[index] = tk.PhotoImage(file=ruta)
        except Exception as e:
            print(f"Failed to load image at {ruta}: {e}")
    

     def setup_main_window(self):
        # Colocar fondo
        bg = Label(self.window, image = self.Img[1]) #Bg es un label para mostrarlo de fondo porque no hay forma de hacerlo directamente con window
        bg.place(x = 0, y = 0)
        #Poner botón de la nota
        self.button = tk.Canvas(self.window, width=124, height=124, highlightthickness=0, cursor = "hand2")
        self.button.create_image(62, 62, image=self.Img[2] )
        self.button.bind("<Button-1>", self.buttonNota)
        self.button.place(x = 136, y = 36)

        #Poner botón anterior
        self.btn_anterior = tk.Canvas(self.window, width=64, height=64, highlightthickness=0, cursor = "hand2")
        self.btn_anterior.create_image(32, 32, image=self.Img[3] )
        self.btn_anterior.bind("<Button-1>", self.anterior)
        self.btn_anterior.place(x = 76, y = 200)

        #Poner botón siguiente
        self.btn_siguiente = tk.Canvas(self.window, width=64, height=64, highlightthickness=0,  cursor = "hand2")
        self.btn_siguiente.create_image(32, 32, image=self.Img[4] )
        self.btn_siguiente.bind("<Button-1>", self.siguiente)
        self.btn_siguiente.place(x = 256, y = 200)

        #Poner botón de pausa, inicia por defecto pausado
        self.btn_pausa = tk.Canvas(self.window, width=64, height=64, highlightthickness=0,  cursor = "hand2")
        self.btn_pausa.create_image(32, 32, image=self.Img[6] )
        self.btn_pausa.bind("<Button-1>", self.pausa)
        self.btn_pausa.place(x = 166, y = 200)




            # Añadir funcionalidad a los botones
     def buttonNota(self, event):
        print("¡Botón presionado!")

     def anterior(self,event):
        print("Anterior")

     def siguiente(self,event):
        print("Siguiente")

     def pausa(self,event):
     
        if self.pause_state:
            self.btn_pausa.delete("all")  # Elimina al boton de pausa actual
            self.btn_pausa.create_image(32, 32, image=self.Img[6])  # Cambia la imagen
            print("pausado debe mostrar un triangulo")
        else:
            self.btn_pausa.delete("all")  # Elimina al boton de pausa actual
            self.btn_pausa.create_image(32, 32, image=self.Img[5])  # Cambia la imagen
            print("Desausado, muestra 2 lineas")
        self.pause_state = not self.pause_state




#Run 
if __name__ == "__main__":
    window = tk.Tk()
    app = MusicPlayerApp(window)
    #app.add_song_to_library("Song 1", "path/to/song1.mp3")
    #app.add_song_to_library("Song 2", "path/to/song2.mp3")
    #app.add_song_to_library("Song 3", "path/to/song3.mp3")
    window.mainloop()