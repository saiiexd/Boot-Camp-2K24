import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Place Geometry Manager Example")
root.geometry("300x200")

# Create and place widgets
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label1.place(x=50, y=30, width=200, height=30)
label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label2.place(x=50, y=70, width=200, height=30)
label3 = tk.Label(root, text="Label 3", bg="green", fg="white")
label3.place(x=50, y=110, width=200, height=30)

root.mainloop()
