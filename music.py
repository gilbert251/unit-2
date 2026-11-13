import os
import time
import pygame

pygame.mixer.init()

mp3_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]

if not mp3_files:
    print("No .mp3 files found in this folder! Please add some music files first.")
    exit()


print("Available songs:")
for song in mp3_files:

    print(f"- {os.path.splitext(song)[0]}")

song_input = input("\nEnter the song name: ").strip()

if not song_input.lower().endswith(".mp3"):
    filename = f"{song_input}.mp3"
else:
    filename = song_input

if os.path.exists(filename):
    try:

        pygame.mixer.music.load(filename)
        

        song_sound = pygame.mixer.Sound(filename)
        song_length = int(song_sound.get_length())

        pygame.mixer.music.play()
        print(f"\nNow playing: {filename}")
        print(f"Listening for the full song duration: {song_length} seconds...")
        

        time.sleep(song_length)
        
        print("Stopping music (Song finished).")
        pygame.mixer.music.stop()
        
    except pygame.error as e:
        print(f"Error playing file: {e}")
else:
    print(f"Error: Could not find '{filename}' in this folder.")

