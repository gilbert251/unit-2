import pygame
import time
pygame.mixer.init()

try:
    pygame.mixer.music.load('Despacito.mp3')
    pygame.mixer.music.play()

    print("Listening for 10 seconds...")
    time.sleep(10)

    print("Stopping music.")
    pygame.mixer.music.stop()

except pygame.error as e:
    print(f"Error loading file: {e}")
    print("Make sure you put an audio file in this folder and updated the file name!")
