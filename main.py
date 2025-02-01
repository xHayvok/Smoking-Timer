#TODO V2 Features: Implement randomization feature


from turtle import Screen, done
from timer import Timer # type: ignore
from buttons import Button


window = Screen()
window.setup(400, 400)
window.bgcolor("black")
window.title("Smoking Timer")

timer = Timer()

start_button = Button()
start_button.start_button()
pause_button = Button()
pause_button.pause_button()

hit_button = Button()
hit_button.hit_set()

time_button = Button()
time_button.time_set()

window.listen()
pause_button.onclick(timer.pause_timer)
start_button.onclick(timer.timer_loop)
hit_button.onclick(timer.set_hit_count)
time_button.onclick(timer.set_timer_length)


done()