import tkinter as tk
from tkinter import messagebox

# Function to check the anime name
def check_anime_name():
    if entry_var.get().strip().lower() == "new anime":
        messagebox.showinfo("Result", "Yes, it's correct!")
    else:
        messagebox.showwarning("Result", "No, try again!")

# Create the main application window
root = tk.Tk()
root.title("Anime Name Guessing Game")
root.geometry('350x550')

anime_cover = tk.PhotoImage(file="path/to/your/image.png")
anime_label = tk.Label(root, image=anime_cover)
anime_label.pack(pady=10)

question_label = tk.Label(root, text="Do you know this anime?\nIf yes, what is its name?", font=("Helvetica", 14))
question_label.pack(pady=10)

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, bd=3, bg="skyblue", fg="black", font=("Georgia", 14), width=20, relief="sunken")
entry.pack(pady=20)

submit_button = tk.Button(root, text="Submit", command=check_anime_name, font=("Georgia", 14), relief='raised', bg='seagreen3')
submit_button.pack(pady=10)

root.mainloop()
