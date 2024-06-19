import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Message Box Example")

# Function to show a message box
def show_message_box():
    messagebox.showinfo("Info", "This is an information message box.")

button = tk.Button(root, text="Show Message Box", command=show_message_box)
button.pack(padx=20, pady=10)

root.mainloop()
