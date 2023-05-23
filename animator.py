from turtle import color
from simulator import Simulator
import tkinter as tk

class Animator():
    def __init__(self, simulator:Simulator) -> None:
        self.window = tk.Tk()
        self.simulator = simulator
        
        
    def setup(self):
        self.window.title("Traffic light")
        self.window.geometry("460x470")
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        
        circle_up = self.canvas.create_oval(160, 10, 300, 150)
        circle_left = self.canvas.create_oval(10, 160, 150, 300)
        circle_right = self.canvas.create_oval(310, 160, 450, 300)
        circle_down = self.canvas.create_oval(160, 310, 300, 460)
        
        self.text_right = self.canvas.create_text(380, 230, text=str(self.simulator.cars[0]), font=("Arial", 30))
        self.text_up = self.canvas.create_text(230, 80, text=str(self.simulator.cars[1]), font=("Arial", 30))
        self.text_left = self.canvas.create_text(80, 230, text=str(self.simulator.cars[2]), font=("Arial", 30))
        self.text_down = self.canvas.create_text(230, 380, text=str(self.simulator.cars[3]), font=("Arial", 30))
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.arrow_down = self.canvas.create_line(230, 239, 230, 300, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_up = self.canvas.create_line(230, 231, 230, 160, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_left = self.canvas.create_line(226, 235, 158, 235, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_right = self.canvas.create_line(234, 235, 302, 235, arrow=tk.LAST, width=5, fill="gray")
        
        self.text_counter = self.canvas.create_text(40, 20, text="counter: " + str(self.simulator.counter), font=("Arial", 10))
    
    def update(self):
        for i in range(101):
            self.window.after(1000)
            self.window.update()
            self.simulator.update()
            current_dir = self.simulator.current_light
            self.arrow_down = self.canvas.create_line(230, 239, 230, 300, arrow=tk.LAST, width=5, fill="red")
            self.arrow_up = self.canvas.create_line(230, 231, 230, 160, arrow=tk.LAST, width=5, fill="red")
            self.arrow_left = self.canvas.create_line(226, 235, 158, 235, arrow=tk.LAST, width=5, fill="red")
            self.arrow_right = self.canvas.create_line(234, 235, 302, 235, arrow=tk.LAST, width=5, fill="red")
            if(current_dir == 0):
                self.canvas.itemconfig(self.arrow_right, fill = "green")
            if(current_dir == 1):
                self.canvas.itemconfig(self.arrow_up, fill = "green")
            if(current_dir == 2):
                self.canvas.itemconfig(self.arrow_left, fill = "green")
            if(current_dir == 3):
                self.canvas.itemconfig(self.arrow_down, fill = "green")
            self.canvas.itemconfig(self.text_right, text=str(self.simulator.cars[0]))
            self.canvas.itemconfig(self.text_up, text=str(self.simulator.cars[1]))
            self.canvas.itemconfig(self.text_left, text=str(self.simulator.cars[2]))
            self.canvas.itemconfig(self.text_down, text=str(self.simulator.cars[3]))
            self.canvas.itemconfig(self.text_counter, text="counter: " + str(self.simulator.counter))
        self.window.mainloop()
    
    def run(self):
        self.setup()
        self.update()