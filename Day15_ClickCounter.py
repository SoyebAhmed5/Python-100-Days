# CLICK COUNTER APP

import tkinter as tk

root = tk.Tk()
root.title("Click Counter")
root.geometry("300x200")

click_count = 0

def increment_click():
    global click_count
    click_count += 1
    label.config(text=f"Clicks: {click_count}")

label = tk.Label(root, text="Clicks: 0", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Click Me!", font=("Arial", 16), command=increment_click)
button.pack(pady=20)

root.mainloop()
