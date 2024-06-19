import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Grid Example")
root.geometry('300x200')

# Create labels and entry fields using the grid layout
tk.Label(root, text="First Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Last Name:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=1, column=1, padx=10, pady=10)
tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=2, column=1, padx=10, pady=10)
submit_button = tk.Button(root, text="Submit")
submit_button.grid(row=3, columnspan=2, pady=10)
root.mainloop()
