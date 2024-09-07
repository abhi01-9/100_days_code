import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
m = 0
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, -100 + m)
    m += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if user_bet == turtle.pencolor():
                print(f"Congratulations you won the race with color {user_bet}")
            else:
                print(f"You lose {turtle.pencolor()} color have won")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
