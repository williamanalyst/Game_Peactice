# In[]: Tested Sname Game
#
import random
import turtle # 
import time
# import os
#
window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('green')
window.setup(width = 600, height = 500)
window.tracer(0) # by setting the value to 0, the animation is turned off
# Create the snake head
head = turtle.Turtle()
head.speed(0) # animation speed of 
head.shape('square')
head.color('black')
head.penup() # default turtle will leave a trace, keeping 'penup' empty removes the trace
head.goto(0, 0)
head.direction = 'stop' # initial direction of the snake head
# Create snake food
food = turtle.Turtle()
food.speed(0) # animation speed of 
food.shape('circle')
food.color('red')
food.penup() # default turtle will leave a trace, keeping 'penup' empty removes the trace
food.goto(0, 100)
#
delay = 0.2 # a time of 0.15 seconds
score = 0
high_score = 0
#
#
segments = [] # 
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write('Score: 0 High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))
#
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
# define actions for later keyboard bindings
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def pause():
    head.direction = 'stop'
## keyboard bindings
window.listen() 
window.onkeypress(go_up, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a')
window.onkeypress(go_right, 'd')
window.onkeypress(pause, 'space')
#
while True:
    window.update()  # main game loop
    # check for collision with border
    if head.xcor() > 290 or head.xcor() <- 290 or head.ycor() > 240 or head.ycor() < - 240:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments list
        segments.clear()
        #
        score = 0
        pen.clear()
        pen.write('Score: {} High Score: {}'.format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))
    # check for collision with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290) # move the food to a random location
        y = random.randint(-240, 240)
        food.goto(x, y)
        # create a new segment after collision
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)
        score += 10 # add score
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('Score: {} High Score: {}'.format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))
    # move the end segment first
    for index in range(len(segments) -1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)
    # move the end segment to where the location of the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    # check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
    time.sleep(delay) # allow a delay between each movement
#
window.mainloop()
#
# In[]:
#
#
