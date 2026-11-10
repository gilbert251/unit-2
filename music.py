import os
import time
import pygame

pygame.mixer.init()


song_name = input("Enter the song name (e.g., Despacito): ").strip()


if not song_name.lower().endswith(".mp3"):
    filename = f"{song_name}.mp3"
else:
    filename = song_name


if os.path.exists(filename):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        print(f"Now playing: {filename}")
        print("Listening for 228 seconds...")
        time.sleep(228)
        
        print("Stopping music.")
        pygame.mixer.music.stop()

    except pygame.error as e:
        print(f"Error playing file: {e}")
else:
    print(f"Error: Could not find '{filename}' in this folder.")
    print("Make sure the file is in the same directory as this script and spelled correctly.")
