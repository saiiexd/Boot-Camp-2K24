#This project is a basic calculator that performs addition, subtraction, multiplication, and division operations.


import tkinter as tk
from tkinter import messagebox

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            raise ValueError

        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

#entry
entry_num1 = tk.Entry(root, width=10)
entry_num1.pack(side=tk.LEFT, padx=5)

operation_var = tk.StringVar()
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack(side=tk.LEFT, padx=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.pack(side=tk.LEFT, padx=5)

# Button for calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(side=tk.LEFT, padx=5)

# Label result
result_label = tk.Label(root, text="Result: ")
result_label.pack(side=tk.LEFT, padx=5)

root.mainloop()
