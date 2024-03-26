import tkinter as tk
from tkinter import messagebox

balloon_popped = False

def inflate_oval():
    global top_y, bottom_y, balloon_popped
    if not balloon_popped:
        canvas.delete("oval")
        top_y -= 1
        canvas.create_oval(center_x - radius, top_y, center_x + radius, bottom_y, fill="red", tags="oval")
        if top_y > 10:
            root.after(100, inflate_oval)
        else:
            pop_balloon()

def pop_balloon():
    global balloon_popped
    balloon_popped = True
    messagebox.showerror("БУМ", "Шарик сделал бум 😢 , возьмём новый?")
    restart_animation()

def restart_animation():
    global top_y, bottom_y, balloon_popped
    balloon_popped = False
    top_y = canvas.winfo_reqheight() / 2
    bottom_y = (top_y + 2 * radius) + 50
    canvas.delete("oval")
    canvas.create_oval(center_x - radius, top_y, center_x + radius, bottom_y, fill="red", tags="oval")
    root.after(1000, inflate_oval)

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

radius = 20
center_x = canvas.winfo_reqwidth() / 2 
top_y = (canvas.winfo_reqheight() / 2) 
bottom_y = (top_y + 2 * radius) + 50 

canvas.create_oval(center_x - radius, top_y, center_x + radius, bottom_y, fill="red", tags="oval")
root.after(500, inflate_oval) 

root.mainloop()