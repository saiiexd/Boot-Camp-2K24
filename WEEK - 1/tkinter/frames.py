import tkinter as tk

# Function to be called when buttons are clicked
def on_top_button_click():
    print("Top button clicked!")

def on_bottom_button_click():
    print("Bottom button clicked!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Frames Example")
root.geometry("300x200")

top_frame = tk.Frame(root, bg="lightblue", width=300, height=100, pady=10)
top_frame.pack(side="top", fill="both", expand=True)

bottom_frame = tk.Frame(root, bg="lightgreen", width=300, height=100, pady=10)
bottom_frame.pack(side="bottom", fill="both", expand=True)

top_label = tk.Label(top_frame, text="This is the top frame", bg="lightblue", font=("Arial", 14))
top_label.pack(pady=10)
top_button = tk.Button(top_frame, text="Top Button", command=on_top_button_click, bg="blue", fg="white")
top_button.pack(pady=10)

bottom_label = tk.Label(bottom_frame, text="This is the bottom frame", bg="lightgreen", font=("Arial", 14))
bottom_label.pack(pady=10)
bottom_button = tk.Button(bottom_frame, text="Bottom Button", command=on_bottom_button_click, bg="green", fg="white")
bottom_button.pack(pady=10)

root.mainloop()
