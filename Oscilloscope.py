import tkinter as tk
import math

class Oscilloscope:
    def __init__(self, root):
        self.root = root
        self.root.title("Oscilloscope")

        self.canvas = tk.Canvas(root, width=800, height=400, bg='black')
        self.canvas.pack()

        self.frequency = 1
        self.amplitude = 100
        self.phase = 0
        self.speed = .1

        self.update_waveform()

    def draw_waveform(self):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_y = height // 2

        points = []
        for x in range(width):
            y = center_y + self.amplitude * math.sin((x * self.frequency * 0.01) + self.phase)
            points.append((x, y))

        for i in range(len(points) - 1):
            self.canvas.create_line(points[i], points[i + 1], fill='green')

    def update_waveform(self):
        self.phase += self.speed
        self.draw_waveform()
        self.root.after(50, self.update_waveform)

if __name__ == "__main__":
    root = tk.Tk()
    oscilloscope = Oscilloscope(root)
    root.mainloop()
