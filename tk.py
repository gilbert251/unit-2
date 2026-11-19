import tkinter as tk

window = tk.Tk()
window.title("Sign Up")
window.configure(bg="#e8eef7")
window.geometry("320x260")

# --- pack() is used for the window's own widgets ---
title = tk.Label(
    window, text="Join the Club",
    font=("Arial", 18, "bold"), fg="#1a365d", bg="#e8eef7",
)
title.pack(pady=(15, 5))

card = tk.Frame(window, bg="white", relief="groove", bd=2)
card.pack(padx=20, pady=10, fill="x")

# --- grid() is used inside the card (a different container) ---
tk.Label(card, text="Name:", bg="white").grid(row=0, column=0, sticky="e", padx=8, pady=8)
name_entry = tk.Entry(card, width=22)
name_entry.grid(row=0, column=1, padx=8, pady=8)

tk.Label(card, text="Email:", bg="white").grid(row=1, column=0, sticky="e", padx=8, pady=8)
email_entry = tk.Entry(card, width=22)
email_entry.grid(row=1, column=1, padx=8, pady=8)

submit = tk.Button(
    window, text="Submit",
    font=("Arial", 12, "bold"),
    bg="#2b6cb0", fg="white",
    activebackground="#1a4a80", activeforeground="white",
    cursor="hand2", padx=20, pady=4,
)
submit.pack(pady=10)

window.mainloop()
