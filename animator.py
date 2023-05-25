from json import load
from turtle import color
from simulator import Simulator
import tkinter as tk
from PIL import ImageTk, Image


class Animator():
    def __init__(self, simulator:Simulator) -> None:
        self.window = tk.Tk()
        self.simulator = simulator
        
        
    def setup(self):
        self.path = "crossroad.jpg"
        self.load = Image.open(self.path)
        self.load = self.load.resize((475, 475))
        self.img  = ImageTk.PhotoImage(self.load)
        
        self.number = 0
        
        self.window.title("Traffic light")
        self.window.geometry("460x470")
        self.canvas = tk.Canvas(self.window, width=self.load.width, height=self.load.height)
        #self.canvas.create_image(0, 0, image=self.img, anchor=tk.NW)
        
        circle_up = self.canvas.create_oval(160, 10, 300, 150)
        circle_left = self.canvas.create_oval(10, 160, 150, 300)
        circle_right = self.canvas.create_oval(310, 160, 450, 300)
        circle_down = self.canvas.create_oval(160, 310, 300, 460)
        
        self.text_right = self.canvas.create_text(380, 230, text=str(self.simulator.cars[0]), font=("Arial", 30))
        self.text_up = self.canvas.create_text(230, 80, text=str(self.simulator.cars[1]), font=("Arial", 30))
        self.text_left = self.canvas.create_text(80, 230, text=str(self.simulator.cars[2]), font=("Arial", 30))
        self.text_down = self.canvas.create_text(230, 380, text=str(self.simulator.cars[3]), font=("Arial", 30))
        
        self.text_number_right = self.canvas.create_text(40, 50, text="Right: " + str(self.number), font=("Arial", 10))
        self.text_number_up = self.canvas.create_text(40, 65, text="Up: " + str(self.number), font=("Arial", 10))
        self.text_number_left = self.canvas.create_text(40, 80, text="Left: " + str(self.number), font=("Arial", 10))
        self.text_number_down = self.canvas.create_text(40, 95, text="Down: " + str(self.number), font=("Arial", 10))
        
        self.arrow_down = self.canvas.create_line(230, 239, 230, 300, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_up = self.canvas.create_line(230, 231, 230, 160, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_left = self.canvas.create_line(226, 235, 158, 235, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_right = self.canvas.create_line(234, 235, 302, 235, arrow=tk.LAST, width=5, fill="gray")
        
        self.text_counter = self.canvas.create_text(40, 35, text="counter: " + str(self.simulator.counter), font=("Arial", 10))
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
    def update(self):
        self.added_cars_ani = [0, 0, 0 , 0]
        for i in range(101):
            self.sum = 0
            self.window.after(500)
            self.window.update()
            self.simulator.update()
            self.added_cars_ani = self.simulator.numbers()
            
            current_dir = self.simulator.current_light
            self.arrow_down = self.canvas.create_line(230, 239, 230, 300, arrow=tk.LAST, width=5, fill="red")
            self.arrow_up = self.canvas.create_line(230, 231, 230, 160, arrow=tk.LAST, width=5, fill="red")
            self.arrow_left = self.canvas.create_line(226, 235, 158, 235, arrow=tk.LAST, width=5, fill="red")
            self.arrow_right = self.canvas.create_line(234, 235, 302, 235, arrow=tk.LAST, width=5, fill="red")
            
            self.canvas.itemconfig(self.text_right, text=str(self.simulator.cars[0]))
            self.canvas.itemconfig(self.text_up, text=str(self.simulator.cars[1]))
            self.canvas.itemconfig(self.text_left, text=str(self.simulator.cars[2]))
            self.canvas.itemconfig(self.text_down, text=str(self.simulator.cars[3]))
             
            if(current_dir == 0):
                self.canvas.itemconfig(self.arrow_right, fill = "green")
                if (self.simulator.cars[0] == 0):
                    self.canvas.itemconfig(self.text_number_right, text="Right: 0")
                else:
                    self.canvas.itemconfig(self.text_number_right, text="Right: " + str(self.added_cars_ani[0] - 10))
                self.canvas.itemconfig(self.text_number_up, text="Up: " + str(self.added_cars_ani[1]))
                self.canvas.itemconfig(self.text_number_left, text="Left: " + str(self.added_cars_ani[2]))
                self.canvas.itemconfig(self.text_number_down, text="Down: " + str(self.added_cars_ani[3]))
            elif(current_dir == 1):
                self.canvas.itemconfig(self.arrow_up, fill = "green")
                self.canvas.itemconfig(self.text_number_right, text="Right: " + str(self.added_cars_ani[0]))
                if (self.simulator.cars[1] == 0):
                    self.canvas.itemconfig(self.text_number_up, text="Up: 0")
                else:
                    self.canvas.itemconfig(self.text_number_up, text="Up: " + str(self.added_cars_ani[1] - 10))
                self.canvas.itemconfig(self.text_number_left, text="Left: " + str(self.added_cars_ani[2]))
                self.canvas.itemconfig(self.text_number_down, text="Down: " + str(self.added_cars_ani[3]))
            elif(current_dir == 2):
                self.canvas.itemconfig(self.arrow_left, fill = "green")
                self.canvas.itemconfig(self.text_number_right, text="Right: " + str(self.added_cars_ani[0]))
                self.canvas.itemconfig(self.text_number_up, text="Up: " + str(self.added_cars_ani[1]))
                if (self.simulator.cars[2] == 0):
                    self.canvas.itemconfig(self.text_number_left, text="Left: 0")
                else:
                    self.canvas.itemconfig(self.text_number_left, text="Left: " + str(self.added_cars_ani[2]) - 10)
                self.canvas.itemconfig(self.text_number_down, text="Down: " + str(self.added_cars_ani[3]))
            elif(current_dir == 3):
                self.canvas.itemconfig(self.arrow_down, fill = "green")
                self.canvas.itemconfig(self.text_number_right, text="Right: " + str(self.added_cars_ani[0]))
                self.canvas.itemconfig(self.text_number_up, text="Up: " + str(self.added_cars_ani[1]))
                self.canvas.itemconfig(self.text_number_left, text="Left: " + str(self.added_cars_ani[2]))
                if (self.simulator.cars[3] == 0):
                    self.canvas.itemconfig(self.text_number_down, text="Down: 0")
                else:    
                    self.canvas.itemconfig(self.text_number_down, text="Down: " + str(self.added_cars_ani[3]) - 10)
            self.canvas.itemconfig(self.text_counter, text="counter: " + str(self.simulator.counter))
            
        self.window.mainloop()

    def run(self):
        self.setup()
        self.update()