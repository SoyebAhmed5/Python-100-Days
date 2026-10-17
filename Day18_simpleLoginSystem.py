import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Simple Login System")
root.geometry("400x300")
root.configure(bg="#f0f4c3")

# Predefined Credentials
USER_CREDENTIALS = {
    "admin":"admin123",
    "user":"user123"
}

# Title Label
title_label = tk.Label(root, text="Login System", font=("Helvetica", 16, "bold"), bg="#f0f4c3")
title_label.pack(pady=20)

#Username Input
username_label = tk.Label(root, text="Username:", font=("Helvetica", 12), bg="#f0f4c3")
username_label.pack(pady=5)
username_entry = tk.Entry(root, font=("Helvetica", 12))
username_entry.pack(pady=5)
# Password Input
password_label = tk.Label(root, text="Password:", font=("Helvetica", 12), bg="#f0f4c3")
password_label.pack(pady=5)
password_entry = tk.Entry(root, font=("Helvetica", 12), show="*")
password_entry.pack(pady=5)

# Login Function
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Login Button
login_button = tk.Button(root, text="Login", font=("Helvetica", 12), command=login)
login_button.pack(pady=20)

# Exit Function
def exit_app():
    root.destroy() 
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=exit_app)
exit_button.pack(pady=10)

# Run the application
root.mainloop()