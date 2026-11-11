import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Drawing Pad")
root.geometry("800x600")
root.configure(bg="#ffffff")


current_color = "#000000"
current_width = 5

def draw(event):
    x1, y1 = (event.x - current_width), (event.y - current_width)
    x2, y2 = (event.x + current_width), (event.y + current_width)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

canvas = tk.Canvas(root, bg="#ffffff")
canvas.pack(fill="both", expand=True)
canvas.bind("<B1-Motion>", draw)

def choose_color():
    global current_color
    color = colorchooser.askcolor(title="Choose color")
    if color[1]:
        current_color = color[1]
        print(f"Color changed to: {current_color}")
        
color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(side="left", padx=10, pady=10)

def change_width(value):
    global current_width
    current_width = int(value)
    print(f"Brush width changed to: {current_width}")
    
width_slider = tk.Scale(root, from_=1, to=20, orient="horizontal", label="Brush Width", command=change_width)
width_slider.pack(side="left", padx=10, pady=10)

def clear_canvas():
    canvas.delete("all")
    print("Canvas cleared.")
    
clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack(side="left", padx=10, pady=10)

root.mainloop()