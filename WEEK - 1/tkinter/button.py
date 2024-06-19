# # Tkinter Button Widget

# The Button widget in Tkinter is used to create buttons in a Python application. These buttons can display text or images to indicate their purpose. You can assign a function or method to be executed automatically when the button is clicked.

# #Syntax:

# The syntax for creating a Button widget is as follows:

# ```python
# button = Button(master, option=value, ...)
# ```

# # Parameters:

# - master: This represents the parent window or frame.

# - options: The following options can be used as key-value pairs to configure the button's appearance and behavior.

# #example

import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "Hello, Tkinter!")
root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("300x200")
button = tk.Button(root, text="Click Me", command=on_button_click, bg="lightblue", fg="black", font=("Arial", 12), padx=10, pady=5)
button.pack(pady=20)
root.mainloop()
