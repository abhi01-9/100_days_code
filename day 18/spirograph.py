import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 155)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
heading = 0


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_color())
        tim.circle(100)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
