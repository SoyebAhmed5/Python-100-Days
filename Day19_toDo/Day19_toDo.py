import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#e0f7fa")

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
        
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        
# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold"), bg="#e0f7fa")
title_label.pack(pady=20)

#Entry for new task
task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack(pady=10)

# Add Task Button
add_task_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=add_task)
add_task_button.pack(pady=5)

# Delete Task Button
delete_task_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_task_button.pack(pady=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=15)
tasks_listbox.pack(pady=10) 

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Exit Function
def exit_app():
    root.destroy()
    
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=exit_app)
exit_button.pack(pady=10)

# Run the application
root.mainloop()