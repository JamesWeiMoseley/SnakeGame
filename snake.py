import turtle
import time
import random

score = 0
high = 0
delay = 0.12
tail = []

new_window = turtle.Screen()
new_window.setup(width=600, height=600)
new_window.title("Snake Game")
new_window.bgcolor("lightblue")
new_window.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(-200,0)
snake.direction="right"

food = turtle.Turtle()
food.shape("turtle")
food.color("yellow")
food.penup()
food.goto(0,random.randint(-200, 200))

pen = turtle.Turtle()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 20, "normal"))
pen.shape("square")
pen.color("white")

def up():
    if snake.direction != "down":
        snake.direction = "up"

def down():
    if snake.direction != "up":
        snake.direction = "down"

def left():
    if snake.direction != "right":
        snake.direction = "left"

def right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        snake.sety(snake.ycor()+22)
    if snake.direction == "down":
        snake.sety(snake.ycor()-22)
    if snake.direction == "left":
        snake.setx(snake.xcor()-22)
    if snake.direction == "right":
        snake.setx(snake.xcor()+22)

def delete_tail():
    for t in tail:
        t.goto(1000,1000)
    tail.clear()

def eat_food(score, high):
    if snake.distance(food) < 20:
        food.goto(random.randint(-280,280), random.randint(-280,280))

        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("grey")
        body.penup()
        tail.append(body)

        score += 10

        update_scoreboard()


    for i in range(len(tail)-1, 0, -1):
        tail[i].goto(tail[i-1].xcor(), tail[i-1].ycor())
    if len(tail)>0:
        tail[0].goto(snake.xcor(), snake.ycor())
    score+=10
    if score > high:
        high = score
    update_scoreboard()


def update_scoreboard():
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high), align="center", font=("Arial", 20, "normal"))


def main():
    #movement commands for controlling the snake
    new_window.listen()
    new_window.onkeypress(up, "Up")
    new_window.onkeypress(down, "Down")
    new_window.onkeypress(left, "Left")
    new_window.onkeypress(right, "Right")

    while True:
        new_window.update()
        score = 10
        time.sleep(delay)

        #if the snake goes out of bounds
        if snake.ycor()>290 or snake.ycor()<-290 or snake.xcor()>290 or snake.xcor() < -290:
            time.sleep(0.2)
            snake.goto(-200,0)
            snake.direction = "right"
            delete_tail()

        eat_food(score, high)

        move()

        #if the snake hits it's tail
        for t in tail:
            if t.distance(snake) < 20:
                time.sleep(1)
                snake.goto(-100, 0)
                snake.direction = "right"
                delete_tail()



if __name__ == "__main__":
    main()
    new_window.mainloop()
