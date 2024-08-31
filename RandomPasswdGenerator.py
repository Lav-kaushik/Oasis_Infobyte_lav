import tkinter as tk
import random
import string

def generate_password():
    # Get the length from the entry widget
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_var.set("Length must be greater than zero.")
            return
        
        # Characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        password_var.set("Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_var = tk.StringVar()
password_var.set("Your password will appear here.")
tk.Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, textvariable=password_var).grid(row=2, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
