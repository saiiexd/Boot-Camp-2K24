import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Canvas Example")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
canvas.create_rectangle(50, 50, 200, 150, fill="blue")
canvas.create_oval(250, 50, 350, 150, fill="red")
canvas.create_line(50, 200, 350, 200, fill="green")

root.mainloop()
