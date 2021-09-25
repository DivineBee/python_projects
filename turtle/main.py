from turtle import Turtle, color
from turtle import Screen
import random

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput("Make ur bet", "Choose a color: ")
print(bet)

nr_sides = 3


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Figures sides
# while nr_sides <= 10:
#     timmy.color(random.choice(colours))
#     for i in range(nr_sides):
#         angle = 360 / nr_sides
#         timmy.forward(90)
#         timmy.left(angle)
#     nr_sides += 1

# Well spirograph
# def draw_spirograph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         timmy.circle(100)
#         timmy.color(random_color())
#         timmy.setheading(timmy.heading() + size_of_gap)
#
# draw_spirograph(20)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
ad = 0

is_race_on = False

for index in range(0, 6):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[index])
    turtle.goto(-230, -90 + ad)
    ad += 30
    all_turtles.append(turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtlik in all_turtles:
        if turtlik.xcor() > 230:
            is_race_on = False
            winner = turtlik.pencolor()
            if winner == bet:
                print(f"You've won {winner} is the winner")
            else:
                print(f"You've lost {winner} is the winner")
        random_distance = random.randint(0, 10)
        turtlik.forward(random_distance)

screen.exitonclick()
