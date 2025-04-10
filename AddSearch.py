import tkinter as tk
from pytube import YouTube
from pydub import AudioSegment
import os

class Cancion:
    def __init__(self, titulo, ruta):
        self.titulo = titulo  # Titulo de la canción
        self.ant = None #Canción anterior
        self.sig = None  # Canción siguiente

class SongLibrary:
    def __init__(self):
        self.head = None  # Points to the first Cancion (song) in the list

    def add_song(self, titulo, ruta):
        new_Cancion = Cancion(titulo, ruta)  # Create a new Cancion
        if self.head is None:  # If the library is empty, make this the first Cancion
            self.head = new_Cancion
        else:
            # Traverse to the end of the list and add the new Cancion
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Cancion

    def get_all_songs(self):
        songs = []
        current = self.head
        while current:
            songs.append(current.data)  # Collect song data from each Cancion
            current = current.next
        return songs

# Tkinter Integration
class SongLibraryApp:
    def __init__(self, root, library):
        self.root = root
        self.library = library

        # Window settings
        self.root.title("Librería")
        self.root.geometry("300x400")

        # Label for the library
        label = tk.Label(root, text="Librería", font=("Arial", 14))
        label.pack(pady=10)

        # Listbox to display songs
        self.listbox = tk.Listbox(root, width=40, height=15)
        self.listbox.pack(pady=10)

        # Add songs to the Listbox
        for song in self.library.get_all_songs():
            self.listbox.insert(tk.END, song)

        # Play Button
        play_button = tk.Button(root, text="Play Song", command=self.play_song)
        play_button.pack(pady=10)

    def play_song(self):
        selected_song = self.listbox.get(tk.ACTIVE)
        if selected_song:
            print(f"Playing: {selected_song}")
        else:
            print("No song selected!")

# Create the song library and add songs
library = SongLibrary()


def download_youtube_as_mp3(url, output_path, filename):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Filter for audio-only streams
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download the audio stream as a .mp4 file
        temp_file = audio_stream.download(output_path=output_path, filename=f"{filename}.mp4")
        
        # Convert the .mp4 file to .mp3 using pydub
        mp3_file = os.path.join(output_path, f"{filename}.mp3")
        audio = AudioSegment.from_file(temp_file)
        audio.export(mp3_file, format="mp3")
        
        # Remove the temporary .mp4 file
        os.remove(temp_file)
        
        print(f"MP3 downloaded successfully at: {mp3_file}")
        library.add_song(yt.title,output_path)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = "https://youtu.be/J9snXJGnAsw?si=lDtpyEtI6XwXCzZG"  # Replace with the actual video URL
output_directory = "C:\\Users\\Angie\\Downloads"  # Replace with your desired directory
file_name = "gasolina"  # Replace with your desired file name

download_youtube_as_mp3(video_url, output_directory, file_name)

# Tkinter application
root = tk.Tk()
app = SongLibraryApp(root, library)
root.mainloop()
