import random
from turtle import Turtle, Screen
tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for _ in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#

colors = ["medium aquamarine", "medium blue", "dark green", "deep pink", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#
# def draw_shape(num_side):
#     angle = 360 / num_side
#     print(angle)
#     tim.color(random.choice(colors))
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.left(angle)
#
#
# for i in range(3,10):
#    draw_shape(i)


# Random walk

angles = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(angles))








screen = Screen()
screen.exitonclick()
