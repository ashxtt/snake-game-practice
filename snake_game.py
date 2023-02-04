import turtle 
import time

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game by @lilgreyya")
wn.bgcolor("black")
wn.setup(width=600, height=600)
# * turns off screen updates
wn.tracer(0)

head = turtle.Turtle()
# *animation speed of the turtle
head.speed(0)
head.shape("square")
head.color("red")
# * pen up (not drawing)
head.penup()
head.goto(0,0)
head.direction = "up"

# * function to move my head up
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

# * This loop updates the screen
while True:
    wn.update()
    move()
    time.sleep(delay)

wn.mainloop()