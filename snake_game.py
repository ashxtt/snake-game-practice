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
head.direction = "stop"

# * function to move my head up
def go_up():
    head.direction = "up"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"
def go_down():
    head.direction = "down"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

# * Keyword bindings
# * Connects a keypress with a puticular function
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_down, "s")

# * This loop updates the screen
while True:
    wn.update()
    move()
    time.sleep(delay)

wn.mainloop()