import tkinter as tk
from tkinter import messagebox
import pyperclip
from generator import generate_password

def generate():
    try:
        # Get user input
        length = int(length_entry.get())
        include_uppercase = uppercase_var.get()
        include_numbers = numbers_var.get()
        include_symbols = symbols_var.get()

        # Generate password
        password = generate_password(length, include_uppercase, include_numbers, include_symbols)

        # Display password
        result_label.config(text=password)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")

# Create the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")

# UI Elements
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).pack(anchor="w", padx=20)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor="w", padx=20)

symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350)
result_label.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Start the GUI loop
root.mainloop()
