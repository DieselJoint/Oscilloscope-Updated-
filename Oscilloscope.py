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
        self.speed = 0.1

        self.create_controls()
        self.update_waveform()

    def create_controls(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        tk.Label(control_frame, text="Frequency:").grid(row=0, column=0)
        self.freq_label = tk.Label(control_frame, text=str(self.frequency))
        self.freq_label.grid(row=0, column=1)
        tk.Button(control_frame, text="+", command=self.increase_frequency).grid(row=0, column=2)
        tk.Button(control_frame, text="-", command=self.decrease_frequency).grid(row=0, column=3)

        tk.Label(control_frame, text="Amplitude:").grid(row=1, column=0)
        self.amp_label = tk.Label(control_frame, text=str(self.amplitude))
        self.amp_label.grid(row=1, column=1)
        tk.Button(control_frame, text="+", command=self.increase_amplitude).grid(row=1, column=2)
        tk.Button(control_frame, text="-", command=self.decrease_amplitude).grid(row=1, column=3)

        tk.Label(control_frame, text="Phase:").grid(row=2, column=0)
        self.phase_label = tk.Label(control_frame, text=str(self.phase))
        self.phase_label.grid(row=2, column=1)
        tk.Button(control_frame, text="+", command=self.increase_phase).grid(row=2, column=2)
        tk.Button(control_frame, text="-", command=self.decrease_phase).grid(row=2, column=3)

        tk.Label(control_frame, text="Speed:").grid(row=3, column=0)
        self.speed_label = tk.Label(control_frame, text=str(self.speed))
        self.speed_label.grid(row=3, column=1)
        tk.Button(control_frame, text="+", command=self.increase_speed).grid(row=3, column=2)
        tk.Button(control_frame, text="-", command=self.decrease_speed).grid(row=3, column=3)

    def draw_waveform(self):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_y = height // 2

        # Draw grid lines
        for x in range(0, width, 50):
            self.canvas.create_line(x, 0, x, height, fill='gray')
        for y in range(0, height, 50):
            self.canvas.create_line(0, y, width, y, fill='gray')

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

    def increase_frequency(self):
        self.frequency += 0.1
        self.freq_label.config(text=str(self.frequency))

    def decrease_frequency(self):
        self.frequency -= 0.1
        self.freq_label.config(text=str(self.frequency))

    def increase_amplitude(self):
        self.amplitude += 10
        self.amp_label.config(text=str(self.amplitude))

    def decrease_amplitude(self):
        self.amplitude -= 10
        self.amp_label.config(text=str(self.amplitude))

    def increase_phase(self):
        self.phase += 0.1
        self.phase_label.config(text=str(self.phase))

    def decrease_phase(self):
        self.phase -= 0.1
        self.phase_label.config(text=str(self.phase))

    def increase_speed(self):
        self.speed += 0.01
        self.speed_label.config(text=str(self.speed))

    def decrease_speed(self):
        self.speed -= 0.01
        self.speed_label.config(text=str(self.speed))

if __name__ == "__main__":
    root = tk.Tk()
    oscilloscope = Oscilloscope(root)
    root.mainloop()
