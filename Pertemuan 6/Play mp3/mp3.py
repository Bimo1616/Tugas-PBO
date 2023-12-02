import tkinter as tk
from tkinter import filedialog
import pygame.mixer

# Function to play mp3 file
def play_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("mp3 Files", "*.mp3")])
    if file_path:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Function to pause the mp3 file
def pause_mp3():
    pygame.mixer.music.pause()

# Function to resume the mp3 file
def resume_mp3():
    pygame.mixer.music.unpause()

# Function to stop the mp3 file and quit the program
def stop_mp3():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    root.quit()

# Create tkinter window
root = tk.Tk()
root.title("MP3 Player")
root.minsize(width=400, height=300)

# Create play button
play_button = tk.Button(root, text="Play MP3", command=play_mp3)
play_button.pack(pady=20)

# Create pause button
pause_button = tk.Button(root, text="Pause MP3", command=pause_mp3)
pause_button.pack(pady=20)

# Create resume button
resume_button = tk.Button(root, text="Resume MP3", command=resume_mp3)
resume_button.pack(pady=20)

# Create exit button
exit_button = tk.Button(root, text="Exit", command=stop_mp3)
exit_button.pack(pady=20)

# Start tkinter loop
root.mainloop()