import cv2
import tkinter as tk
from tkinter import filedialog
import pygame
import moviepy.editor as mp
from threading import Thread

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        self.video_path = None
        self.cap = None
        self.sound = None
        self.mute = False
        self.playing = False  # Menambahkan status playing

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.btn_open = tk.Button(root, text="Open Video", command=self.open_video)
        self.btn_open.pack(pady=10)

        self.btn_play = tk.Button(root, text="Play", command=self.toggle_play, state=tk.DISABLED)
        self.btn_play.pack(pady=5)

        self.btn_pause = tk.Button(root, text="Pause", command=self.toggle_pause, state=tk.DISABLED)
        self.btn_pause.pack(pady=5)

        self.btn_stop = tk.Button(root, text="Stop", command=self.stop_video, state=tk.DISABLED)
        self.btn_stop.pack(pady=5)

        self.btn_toggle_mute = tk.Button(root, text="Toggle Mute", command=self.toggle_mute)
        self.btn_toggle_mute.pack(pady=5)

        pygame.init()
        pygame.mixer.init()

    def open_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])

        if self.video_path:
            video = mp.VideoFileClip(self.video_path)
            audio = video.audio
            audio.write_audiofile("temp_audio.wav", codec='pcm_s16le')

            self.cap = cv2.VideoCapture(self.video_path)
            self.sound = pygame.mixer.Sound("temp_audio.wav")  # Load audio from the video
            self.btn_play["state"] = tk.NORMAL
            self.btn_stop["state"] = tk.NORMAL

    def toggle_play(self):
        if not self.playing:
            self.play_video()
        else:
            self.pause_video()

    def play_video(self):
        if self.cap.isOpened():
            self.playing = True
            self.btn_play["text"] = "Pause"
            self.btn_pause["state"] = tk.NORMAL

            # Get video properties
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Set the window size to match the video aspect ratio
            self.root.geometry(f"{width}x{height}")

            # Play Audio
            pygame.mixer.Channel(0).play(self.sound, loops=-1)

            # Create a separate thread to continuously display video frames
            thread = Thread(target=self.display_frames)
            thread.start()

    def display_frames(self):
        while self.playing:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Check if the video has a different color space
            if self.cap.get(cv2.CAP_PROP_CONVERT_RGB) == 0:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display video frames using OpenCV
            cv2.imshow("Video Player", frame)
            if cv2.waitKey(28) & 0xFF == ord("q"):
                break

        # Release the video capture object
        self.cap.release()
        # Destroy the OpenCV window
        cv2.destroyAllWindows()

        # Update GUI after video finishes
        self.btn_play["state"] = tk.NORMAL
        self.btn_pause["state"] = tk.DISABLED
        self.btn_play["text"] = "Play"
        self.playing = False

    def toggle_pause(self):
        if self.playing:
            pygame.mixer.Channel(0).pause()
            self.btn_play["text"] = "Play"

    def stop_video(self):
        if self.playing:
            self.playing = False
            pygame.mixer.Channel(0).stop()
            cv2.destroyAllWindows()  # Menutup jendela OpenCV
            self.cap.release()
            self.btn_play["state"] = tk.NORMAL
            self.btn_pause["state"] = tk.DISABLED
            self.btn_stop["state"] = tk.DISABLED
            self.btn_play["text"] = "Play"

    def toggle_mute(self):
        self.mute = not self.mute
        if self.mute:
            pygame.mixer.Channel(0).set_volume(0.0)  # Mute
        else:
            pygame.mixer.Channel(0).set_volume(1.0)  # Unmute

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
