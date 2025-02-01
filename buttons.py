from turtle import Turtle


FONT = ("Arial", 16, "normal")

class Button(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)

    def start_button(self):
        self.shapesize(2, 2)
        self.goto(-40, -30)
        self.color("green")
        self.shape("triangle")

    def pause_button(self):
        self.shapesize(2, 2)
        self.goto(40, -30)
        self.color("red")
        self.shape("square")

    def hit_set(self):
        self.goto(-150, 150)
        self.color("pink")
        self.write("Set Hits", font=FONT)
        self.goto(-165, 165)
        self.color("pink")
        self.shape("circle")

    def time_set(self):
        self.goto(-150, 125)
        self.color("pink")
        self.write("Set Time", font=FONT)
        self.goto(-165, 140)
        self.color("pink")
        self.shape("circle")