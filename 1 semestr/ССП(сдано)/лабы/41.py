import tkinter as tk


def turn_on_red():
    canvas.itemconfig(red_light, fill="red")
    canvas.itemconfig(yellow_light, fill="gray")
    canvas.itemconfig(green_light, fill="gray")

def turn_on_yellow():
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(yellow_light, fill="yellow")
    canvas.itemconfig(green_light, fill="gray")

def turn_on_green():
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(yellow_light, fill="gray")
    canvas.itemconfig(green_light, fill="green")

root = tk.Tk()

canvas = tk.Canvas(root, width=100, height=300)
canvas.pack()

red_light = canvas.create_oval(25, 50, 75, 100, fill="gray")
yellow_light = canvas.create_oval(25, 125, 75, 175, fill="gray")
green_light = canvas.create_oval(25, 200, 75, 250, fill="gray")

red_button = tk.Button(root, text="Красный", command=turn_on_red)
yellow_button = tk.Button(root, text="Желтый", command=turn_on_yellow)
green_button = tk.Button(root, text="Зеленый", command=turn_on_green)

red_button.pack()
yellow_button.pack()
green_button.pack()

canvas.itemconfig(red_light, fill="red")
root.mainloop()