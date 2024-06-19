import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Grid Geometry Manager Example")
root.geometry("300x200")

# Create and grid widgets
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label1.grid(row=0, column=0, padx=10, pady=5)
label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label2.grid(row=0, column=1, padx=10, pady=5)
label3 = tk.Label(root, text="Label 3", bg="green", fg="white")
label3.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
