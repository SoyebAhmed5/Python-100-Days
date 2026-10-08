import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#f0f4c3")

title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

weight_label = tk.Label(root, text="Weight (kg):", font=("Arial", 14), bg="#f0f4c3")
weight_label.pack(pady=10)

weight_entry = tk.Entry(root, font=("Arial", 14), bg="#ffffff")
weight_entry.pack(pady=10)

height_label = tk.Label(root, text="Height (m):", font=("Arial", 14), bg="#f0f4c3")
height_label.pack(pady=10)

height_entry = tk.Entry(root, font=("Arial", 14), bg="#ffffff")
height_entry.pack(pady=10)

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")

calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 14), bg="#4CAF50", fg="#ffffff", command=calculate_bmi)
calculate_button.pack(pady=20)

root.mainloop()