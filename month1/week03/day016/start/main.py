import another_module
from turtle import Turtle, Screen

print(another_module.another_variable)
print(another_module.another_list)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.speed(1)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.begin_fill()
timmy.circle(100)
timmy.end_fill()



my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

