import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Listbox Example")
root.geometry("300x200")

# Create a Listbox widget
listbox = tk.Listbox(root)
listbox.pack(pady=20)

for item in ["Apple", "Banana", "Cherry", "Grapes", "Orange"]:
    listbox.insert(tk.END, item)

root.mainloop()
