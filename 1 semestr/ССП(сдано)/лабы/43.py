import tkinter as tk


def change_to_circle():
    canvas.delete("shape")
    canvas.create_oval(25, 25, 75, 75, outline="black", fill="white", tags="shape")

def change_to_rectangle():
    canvas.delete("shape")
    canvas.create_rectangle(25, 25, 75, 75, outline="black", fill="white", tags="shape")

def change_to_triangle():
    canvas.delete("shape")
    canvas.create_polygon(25, 25, 50, 75, 75, 25, outline="black", fill="white", tags="shape")

root = tk.Tk()

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

circle_button = tk.Button(root, text="Круг", command=change_to_circle)
rectangle_button = tk.Button(root, text="Квадрат", command=change_to_rectangle)
triangle_button = tk.Button(root, text="Треугольник", command=change_to_triangle)

circle_button.pack()
rectangle_button.pack()
triangle_button.pack()

canvas.create_oval(25, 25, 75, 75, outline="black", fill="white", tags="shape")
root.mainloop()