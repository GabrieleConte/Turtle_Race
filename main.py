from turtle import *
from Turtle_model import TurtleMod

winner = ""
is_race_on = False
x = -230
y = [-80, -40, 0, 40, 80]
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "blue", "purple", "orange"]
bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ").lower()
turtles = []
for i in range(0, 5):
    turtles.append(TurtleMod(x=x, y=y[i], color=colors[i]))

if bet:
    is_race_on = True

while is_race_on:
    k = False
    for turtle in turtles:
        k = turtle.move_forwards()
        if k:
            winner = turtle.name
            is_race_on = False
            break

if winner == bet:
    print("You won!")
else:
    print("Wrong bet!")
print(f"The winner is {winner}!")
screen.exitonclick()
