from turtle import color

from matplotlib.pyplot import arrow
from simulator import Simulator
import tkinter as tk
from PIL import ImageTk, Image


class Animator():
    def __init__(self, simulator:Simulator) -> None:
        self.window = tk.Tk()
        self.simulator = simulator
        
        
    def setup(self):
        
        self.path = "D:\Theory\Reinforcement-Learning-Traffic-Light\crossroad.jpg"
        self.load = Image.open(self.path)
        self.load = self.load.resize((475, 475))
        self.img  = ImageTk.PhotoImage(self.load)
        
        self.number = 0
        
        self.window.title("Traffic light")
        self.window.geometry("460x470")
        self.canvas = tk.Canvas(self.window, width=self.load.width, height=self.load.height)
        self.canvas.create_image(0, 0, image=self.img, anchor=tk.NW)
        
        #Creating Circles & texts
        self.circle = []
        self.text = []
        x , m = 0, 0
        for i in range(2):
            self.circle.append(self.canvas.create_oval(310 - x, 160 - x, 450 - x, 300 - x))
            self.circle.append(self.canvas.create_oval(10 + x, 160 + x, 150 + x, 300 + x))
            self.text.append(self.canvas.create_text(380 - x, 230 - x,text = str(self.simulator.cars[m]), font=("Arial", 30)))
            self.text.append(self.canvas.create_text(80 + x, 230 + x, text = str(self.simulator.cars[m+2]), font=("Arial", 30)))
            x = 150
            m = 1
            
        self.direction= ["Right: ", "Up: ", "Left: ", "Down: "]
        self.text_number = []
        ini = 50
        for f in range(4):
            self.text_number.append(self.canvas.create_text(40, ini ,text = self.direction[f], font=("Arial", 10)))
            ini += 15
        self.text_counter = self.canvas.create_text(40, 35, text="counter: " + str(self.simulator.counter), font=("Arial", 10))
    
        self.arrow_right = self.canvas.create_line(234, 235, 302, 235, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_up = self.canvas.create_line(230, 231, 230, 160, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_left = self.canvas.create_line(226, 235, 158, 235, arrow=tk.LAST, width=5, fill="gray")
        self.arrow_down = self.canvas.create_line(230, 239, 230, 300, arrow=tk.LAST, width=5, fill="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
    def update(self):
        self.added_cars_ani = [0, 0, 0 , 0]
        for i in range(101):
            self.window.after(1000)
            self.window.update()
            self.simulator.update()
            self.added_cars_ani = self.simulator.numbers()
            
            current_dir = self.simulator.current_light
            self.arrow_right = self.canvas.create_line(234, 235, 302, 235, arrow=tk.LAST, width=5, fill="red")
            self.arrow_up = self.canvas.create_line(230, 231, 230, 160, arrow=tk.LAST, width=5, fill="red")
            self.arrow_left = self.canvas.create_line(226, 235, 158, 235, arrow=tk.LAST, width=5, fill="red")
            self.arrow_down = self.canvas.create_line(230, 239, 230, 300, arrow=tk.LAST, width=5, fill="red")
            
            for e in range(4):
                self.canvas.itemconfig(self.text[e], text=str(self.simulator.cars[e]))
             
            if(current_dir == 0):
                self.arrow_right = self.canvas.itemconfig(self.arrow_right, fill="green")
                self.canvas.itemconfig(self.text_number[0], text="\tRight: " + str(self.added_cars_ani[0]) + " decrese: 10")
                for q in range(1, 4):
                    self.canvas.itemconfig(self.text_number[q], text=self.direction[q] + str(self.added_cars_ani[q]))
            elif(current_dir == 1):
                self.canvas.itemconfig(self.arrow_up, fill = "green")
                self.canvas.itemconfig(self.text_number[0], text="Right: " + str(self.added_cars_ani[0]))
                self.canvas.itemconfig(self.text_number[1], text="\tUp: " + str(self.added_cars_ani[1]) + " decrese: 10")
                self.canvas.itemconfig(self.text_number[2], text="Left: " + str(self.added_cars_ani[2]))
                self.canvas.itemconfig(self.text_number[3], text="Down: " + str(self.added_cars_ani[3]))
            elif(current_dir == 2):
                self.canvas.itemconfig(self.arrow_left, fill = "green")
                self.canvas.itemconfig(self.text_number[0], text="Right: " + str(self.added_cars_ani[0]))
                self.canvas.itemconfig(self.text_number[1], text="Up: " + str(self.added_cars_ani[1]))
                self.canvas.itemconfig(self.text_number[2], text="\tLeft: " + str(self.added_cars_ani[2]) + " decrese: 10")
                self.canvas.itemconfig(self.text_number[3], text="Down: " + str(self.added_cars_ani[3]))
            elif(current_dir == 3):
                self.canvas.itemconfig(self.arrow_down, fill = "green")
                self.canvas.itemconfig(self.text_number[0], text="Right: " + str(self.added_cars_ani[0]))
                self.canvas.itemconfig(self.text_number[1], text="Up: " + str(self.added_cars_ani[1]))
                self.canvas.itemconfig(self.text_number[2], text="Left: " + str(self.added_cars_ani[2]))
                self.canvas.itemconfig(self.text_number[3], text="\tDown: " + str(self.added_cars_ani[3]) + " decrese: 10")
            self.canvas.itemconfig(self.text_counter, text="counter: " + str(self.simulator.counter))
            
        self.window.mainloop()

    def run(self):
        self.setup()
        self.update()