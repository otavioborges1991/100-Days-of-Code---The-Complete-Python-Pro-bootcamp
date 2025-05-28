from turtle import Screen, Turtle
from random import choice, randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.speed(1)
timmy.pencolor("blue")

def random_color():
    Turtle.colormode(255)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def dashed_line(turtle, length=10, dash_length=10):
    for _ in range(length):
        turtle.forward(dash_length)
        turtle.penup()
        turtle.forward(dash_length)
        turtle.pendown()

def draw_pentagon(turtle):
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)

def draw_triangle(turtle):
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

def draw_random_walk(turtle, steps=5):
    directions = [0, 90, 180, 270]
    turtle.pensize(15)
    for _ in range(steps):
        turtle.pencolor(random_color())
        turtle.setheading(choice(directions))
        turtle.forward(30)

def draw_random_shape(timmy):
    shape = choice(['square', 'pentagon', 'triangle', 'random_walk'])
    if shape == 'square':
        draw_square(timmy)
    elif shape == 'pentagon':
        draw_pentagon(timmy)
    elif shape == 'triangle':
        draw_triangle(timmy)
    else:
        draw_random_walk(timmy)

def draw_spirograph(turtle, size_of_gap=10):
    turtle.speed(0)
    turtle.pensize(1)
    for angle in range(0, 360, size_of_gap):
        turtle.pencolor(random_color())
        turtle.setheading(angle)
        turtle.circle(100)


screen = Screen()
screen.title("Turtle Drawing")
draw_spirograph(timmy, size_of_gap=5)

screen.exitonclick()


