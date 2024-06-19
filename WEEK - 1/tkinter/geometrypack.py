import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Pack Geometry Manager Example")
root.geometry("300x200")

# Create and pack widgets
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label1.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label2.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
label3 = tk.Label(root, text="Label 3", bg="green", fg="white")
label3.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

root.mainloop()
