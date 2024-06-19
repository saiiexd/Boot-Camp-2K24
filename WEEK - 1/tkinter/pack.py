import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Pack Example")
root.geometry('300x200')

# Create three label widgets
label1 = tk.Label(root, text="Label 1", bg="lightblue", fg="black")
label2 = tk.Label(root, text="Label 2", bg="lightgreen", fg="black")
label3 = tk.Label(root, text="Label 3", bg="lightyellow", fg="black")
label1.pack(side="top", fill="both", expand=True, padx=10, pady=5)
label2.pack(side="left", fill="both", expand=True, padx=10, pady=5)
label3.pack(side="right", fill="both", expand=True, padx=10, pady=5)

root.mainloop()
