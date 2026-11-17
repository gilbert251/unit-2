import os
import time
import pygame

pygame.mixer.init()

mp3_files = [f for f in os.listdir('.') if f.lower().endswith('.mp3')]#finds that file ends with .mp3

if not mp3_files:
    print("No .mp3 files found in this folder! Please add some music files first.")
    exit()

print("Available songs:")
for song in mp3_files:
    print(f"- {os.path.splitext(song)[0]}")#prints song title

song_input = input("\nEnter the song name (you can copy and paste from the list): ").strip()

if not song_input.lower().endswith('.mp3'):
    filename = f"{song_input}.mp3"
else:
    filename = song_input

if os.path.exists(filename):#confirms files exist
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        print(f"\nNow playing: {filename}")
        print("Listening until the song finishes...")
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)
            
        print("Stopping music (Song finished).")
        pygame.mixer.music.stop()
        
    except pygame.error as e:
        print(f"Error playing file: {e}")#displays errors
else:
    print(f"Error: Could not find '{filename}' in this folder.")

