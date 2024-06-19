import tkinter as tk

# Function to be called when the button is clicked
def on_button_click():
    print("Button clicked!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Place Example")
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="This is a label", bg="lightblue", fg="black")
label.place(x=50, y=50)
entry = tk.Entry(root)
entry.place(x=50, y=100)
button = tk.Button(root, text="Click Me", command=on_button_click)
button.place(x=50, y=150)

root.mainloop()
