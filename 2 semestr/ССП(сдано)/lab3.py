import tkinter as tk
import random, math
from threading import Thread

random_color = "red"

class TriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сфера")
        self.root.iconbitmap("куб.ico")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.triangle = self.canvas.create_polygon(200, 100, 300, 300, 100, 300, fill="red")

        self.color_button = tk.Button(self.root, text="Изменить цвет", command=self.change_color)
        self.color_button.pack()

        self.background_button = tk.Button(self.root, text="Изменить фон", command=self.change_background)
        self.background_button.pack()

        self.speed_slider = tk.Scale(self.root, from_=0.0, to=10.0, resolution=0.1, orient=tk.HORIZONTAL,
                                     label="Скорость вращения", command=self.set_speed)
        self.speed_slider.set(1.0)
        self.speed_slider.pack()

        self.rotation_speed = 0.0
        self.rotating = False

        self.root.bind("<KeyPress>", self.key_press_event)
        self.root.bind("<KeyRelease>", self.key_release_event)

        self.thread = Thread(target=self.rotate_triangle)
        self.thread.daemon = True
        self.thread.start()

    def rotate_triangle(self):
        global random_color
        angle = 0
        while True:
            if self.rotating:
                angle += self.rotation_speed
                if angle >= 360:
                    angle -= 360
                self.redraw_triangle(angle)
            self.root.after(5)
            self.canvas.update()

    def redraw_triangle(self, angle):
        cx, cy = 200, 200
        points = [200, 100, 300, 300, 100, 300]
        rotated_points = []
        for i in range(0, len(points), 2):
            x, y = points[i], points[i + 1]
            x_new = cx + (x - cx) * math.cos(math.radians(angle)) - (y - cy) * math.sin(math.radians(angle))
            y_new = cy + (x - cx) * math.sin(math.radians(angle)) + (y - cy) * math.cos(math.radians(angle))
            rotated_points.extend([x_new, y_new])
        self.canvas.coords(self.triangle, *rotated_points)

    def change_color(self):
        global random_color
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.canvas.itemconfig(self.triangle, fill=random_color)

    def change_background(self):
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.canvas.config(bg=random_color)

    def set_speed(self, value):
        self.rotation_speed = float(value)

    def key_press_event(self, event):
        if event.keysym == "Right":
            self.rotating = True
            self.rotation_speed = abs(self.rotation_speed)
        elif event.keysym == "Left":
            self.rotating = True
            self.rotation_speed = -abs(self.rotation_speed)

    def key_release_event(self, event):
        self.rotating = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleApp(root)
    root.mainloop()
