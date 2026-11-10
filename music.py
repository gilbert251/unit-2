#run "python3 -m pip install pygame" in your terminal before running this code to install the pygame library.
import pygame
import time
pygame.mixer.init()

try:
    pygame.mixer.music.load('Despacito.mp3')
    pygame.mixer.music.play()

    print("Listening for 228 seconds...")
    time.sleep(228)

    print("Stopping music.")
    pygame.mixer.music.stop()

except pygame.error as e:
    print(f"Error loading file: {e}")
    print("Make sure you put an audio file in this folder and updated the file name!")
