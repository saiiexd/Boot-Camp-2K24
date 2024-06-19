import tkinter as tk

# Function to draw shapes
def draw_shape(event):
    x, y = event.x, event.y
    if shape_var.get() == "Rectangle":
        canvas.create_rectangle(x, y, x + 50, y + 30, fill="blue")
    elif shape_var.get() == "Circle":
        canvas.create_oval(x, y, x + 30, y + 30, fill="red")

root = tk.Tk()
root.title("Simple Drawing App")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

shape_label = tk.Label(root, text="Select Shape:")
shape_label.pack()
shape_var = tk.StringVar()
shape_dropdown = tk.OptionMenu(root, shape_var, "Rectangle", "Circle")
shape_dropdown.pack()

canvas.bind("<B1-Motion>", draw_shape)

root.mainloop()
