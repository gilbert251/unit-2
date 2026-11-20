import tkinter as tk

window = tk.Tk()
window.title("Sign Up")
window.configure(bg="#e8eef7")
window.geometry("320x260")

def play_music():
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

# --- pack() is used for the window's own widgets ---
title = tk.Label(
    window, text="music player",
    font=("Arial", 18, "bold"), fg="#1a365d", bg="#e8eef7",
)
title.pack(pady=(15, 5))

card = tk.Frame(window, bg="white", relief="groove", bd=2)
card.pack(padx=20, pady=10, fill="x")

# --- grid() is used inside the card (a different container) ---
tk.Label(card, text="songs:", bg="white").grid(row=0, column=0, sticky="e", padx=8, pady=8)
name_entry = tk.Entry(card, width=22)
name_entry.grid(row=0, column=1, padx=8, pady=8)


play = tk.Button(
    window, text="play",
    font=("Arial", 12, "bold"),
    bg="#2b6cb0", fg="white",
    activebackground="#1a4a80", activeforeground="white",
    cursor="hand2", padx=20, pady=4, command=play_music
)
play.pack(pady=10)

window.mainloop()
