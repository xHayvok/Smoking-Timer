from turtle import Turtle, numinput
import time
from playsound import playsound # type: ignore

DEFAULT_TIME = 1
DEFAULT_HITS = 3
FONT = ("Arial", 16, "normal")
TIMER_FONT = ("Arial", 32, "normal")
TIME_END_SOUND = "_internal/timer_end.wav"

class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.set_length = DEFAULT_TIME * 60
        self.length = self.set_length
        self.set_hits = DEFAULT_HITS
        self.hits = self.set_hits
        self.timer_running = False
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color("pink")
        self.update_time()

    def set_hit_count(self, x, y):
        self.set_hits = int(numinput(title="Hit Counter", prompt="How many hits would you like to take?", default=DEFAULT_HITS))
        self.hits = self.set_hits
        self.update_time()

    def set_timer_length(self, x, y):
        self.set_length = int(numinput(title="Timer Set", prompt="How long between hits? (in minutes)", default=DEFAULT_TIME) * 60)
        self.length = self.set_length
        self.update_time()

    def update_hits(self):
        self.goto(0, 50)
        self.write(f"Hits remaining: {self.hits}", align="center", font=FONT)
        self.goto(0, 0)

    def update_time(self):
        self.seconds = self.length % 60
        self.minutes = int((self.length - self.seconds) / 60)
        #print("Updating time")
        self.clear()
        self.update_hits()
        self.write(f"{self.minutes:02}:{self.seconds:02}", align="center", font=TIMER_FONT)

    def decrease_time(self):
        self.length -= 1
        #print("Decreasing time")
        self.update_time()

    def pause_timer(self, x, y):
        #print("Pause timer toggle")
        if self.timer_running == False:
            self.restart_timer()
        else:
            self.timer_running = False

    def restart_timer(self):
        #print("Timer Restarting")
        self.timer_running = False
        self.clear()
        #self.pause_timer()
        self.hits = self.set_hits
        self.length = self.set_length
        self.update_time()

    def timer_loop(self, x, y):
        if self.timer_running == False and self.length > 0:
            self.timer_running = True
            self.update_time()
            time.sleep(1)
            while self.timer_running:
                self.decrease_time()
                if self.length == 0:
                    if self.hits == 1:
                        self.timer_running = False
                        self.goto(0, -85)
                        self.write("Its time to take the last hit!", align="center", font=FONT)
                        self.goto(0, -105)
                        self.write("The game is over", align="center", font=FONT)
                        self.goto(0, 0)
                        playsound(TIME_END_SOUND)
                    elif self.hits > 1:
                        self.hits -= 1
                        self.length = self.set_length
                        self.pause_timer(x=0, y=0)
                        self.goto(0, -85)
                        self.write("Its time to take a hit!", align="center", font=FONT)
                        self.goto(0, 0)
                        playsound(TIME_END_SOUND)
                time.sleep(1)
                #print(f"Running a loop time:{self.length}")