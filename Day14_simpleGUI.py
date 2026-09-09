# Simple GUI Application using Tkinter

import tkinter as tk 

root = tk.Tk()

root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg="lightblue")

label = tk.Label(root, text="Welcome to My GUI App", font=("Arial", 18), bg="lightblue")
label.pack(pady=20)

name_label = tk.Label(root, text="Enter your name:", font=("Arial", 14), bg="lightblue")
name_label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

greeting_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
greeting_label.pack(pady=10)

def greet_user():
    name = entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!" , fg="green")
    else:
        greeting_label.config(text="Please enter your name.", fg="red")

def reset():
    entry.delete(0, tk.END)
    greeting_label.config(text="")

button = tk.Button(root, text="Greet", command=greet_user, font=("Arial", 14), bg="white")
button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 14), bg="white")
reset_button.pack(pady=10)

root.mainloop()