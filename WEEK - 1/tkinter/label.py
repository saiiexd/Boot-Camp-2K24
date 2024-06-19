import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Label Example")
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16), bg="lightyellow", fg="blue")
label.pack(pady=20)
root.mainloop()
