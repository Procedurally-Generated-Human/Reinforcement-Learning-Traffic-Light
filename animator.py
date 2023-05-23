import tkinter
from simulator import Simulator
import tkinter as tk

class Animator():
    def __init__(self, simulator:Simulator) -> None:
        self.window = tk.Tk()
        self.simulator = simulator
        
    def setup(self):
        self.window.title("Traffic light")
        self.window.geometry("460x470")
        canvas = tk.Canvas(self.window, width=400, height=400)
        circle_up = canvas.create_oval(160, 10, 300, 150)
        circle_left = canvas.create_oval(10, 160, 150, 300)
        circle_right = canvas.create_oval(310, 160, 450, 300)
        circle_down = canvas.create_oval(160, 310, 300, 460)
        canvas.pack(fill=tk.BOTH, expand=True)
        self.window.mainloop()
        
    
    #def update()
    
    #def run()
    