import tkinter as tk
from tkinter import messagebox
import csv
import os

# File For Storing Expenses
EXPENSE_FILE = "expenses.csv"

# Main Application
root = tk.Tk()
root.title("Expense Tracker App")
root.geometry("600x600")
root.configure(bg="#f0f4c3")

# Expense Data List
expenses = []

# Load Expenses from CSV
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
                expenses_listbox.insert(tk.END, f"{row[0]} - ${row[1]}")
                
# Save Expenses to CSV
def save_expenses():
    with open(EXPENSE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow(expense)
            
# Add Expense Function
def add_expense():
    category = category_entry.get().strip()
    amount = amount_entry.get().strip()
    description = description_entry.get().strip()
    
    if category and amount and description:
        try:
            amount_float = float(amount)
            expenses.append([category, amount_float, description])
            expenses_listbox.insert(tk.END, f"{category} - ${amount_float} - {description}")
            save_expenses()
            category_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the amount.")
            
# Delete Expense Function
def delete_expense():
    selected_index = expenses_listbox.curselection()
    if selected_index:
        expenses_listbox.delete(selected_index)
        del expenses[selected_index[0]]
        save_expenses()
    else:
        messagebox.showwarning("Selection Error", "Please select an expense to delete.")
        
# Clear All Inputs Function
def clear_inputs():
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    
# Calculate Total Expenses Function
def calculate_total():
    total = sum(float(expense[1]) for expense in expenses)
    messagebox.showinfo("Total Expenses", f"Total Expenses: ${total:.2f}")
    
# Clear All Expenses Function
def clear_all_expenses():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expenses.clear()
        expenses_listbox.delete(0, tk.END)
        save_expenses()
        
# GUI Layout
title_label = tk.Label(root, text="Expense Tracker App", font=("Helvetica", 16, "bold"), bg="#f0f4c3")
title_label.pack(pady=20)

# Input Fields
category_label = tk.Label(root, text="Category:", font=("Helvetica", 12), bg="#f0f4c3")
category_label.pack(pady=5)
category_entry = tk.Entry(root, font=("Helvetica", 12))
category_entry.pack(pady=5)

amount_label = tk.Label(root, text="Amount:", font=("Helvetica", 12), bg="#f0f4c3")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root, font=("Helvetica", 12))
amount_entry.pack(pady=5)
description_label = tk.Label(root, text="Description:", font=("Helvetica", 12), bg="#f0f4c3")
description_label.pack(pady=5)

description_entry = tk.Entry(root, font=("Helvetica", 12))
description_entry.pack(pady=5)

# Buttons
add_expense_button = tk.Button(root, text="Add Expense", font=("Helvetica", 12), command=add_expense)
add_expense_button.pack(pady=5)
delete_expense_button = tk.Button(root, text="Delete Expense", font=("Helvetica", 12), command=delete_expense)
delete_expense_button.pack(pady=5)
clear_inputs_button = tk.Button(root, text="Clear Inputs", font=("Helvetica", 12), command=clear_inputs)
clear_inputs_button.pack(pady=5)

calculate_total_button = tk.Button(root, text="Calculate Total", font=("Helvetica", 12), command=calculate_total)
calculate_total_button.pack(pady=5)
clear_all_expenses_button = tk.Button(root, text="Clear All Expenses", font=("Helvetica", 12), command=clear_all_expenses)
clear_all_expenses_button.pack(pady=5)

# Listbox to display expenses
expenses_listbox = tk.Listbox(root, font=("Helvetica", 12), width=50, height=15)
expenses_listbox.pack(pady=10)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
expenses_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=expenses_listbox.yview)

# Exit Function
def exit_app():
    root.destroy()
    
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=exit_app)
exit_button.pack(pady=10)

# Load existing expenses on startup
load_expenses()
# Run the application
root.mainloop()