import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height <= 0:
            messagebox.showerror("Input Error", "Height must be greater than zero.")
            return
        if weight <= 0:
            messagebox.showerror("Input Error", "Weight must be greater than zero.")
            return
        bmi = weight / (height ** 2)
        bmi_result_var.set(f"{bmi:.2f}")

        # Interpret BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        bmi_category_var.set(category)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

bmi_result_var = tk.StringVar()
bmi_result_var.set("Your BMI will appear here.")
tk.Label(root, text="Your BMI:").grid(row=3, column=0, padx=10, pady=10)
tk.Label(root, textvariable=bmi_result_var).grid(row=3, column=1, padx=10, pady=10)

bmi_category_var = tk.StringVar()
bmi_category_var.set("BMI Category will appear here.")
tk.Label(root, text="BMI Category:").grid(row=4, column=0, padx=10, pady=10)
tk.Label(root, textvariable=bmi_category_var).grid(row=4, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
