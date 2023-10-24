import turtle as t
import random

is_game_on = False

screen = t.Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_axis = -230
y_axis = -100
turtles = []
for i in range(6):
    turtle_obj = t.Turtle(shape="turtle")
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.goto(x_axis, y_axis)
    turtle_obj.pendown()
    y_axis += 40
    turtle_obj.speed(1)
    turtles.append(turtle_obj)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color?: ")

if user_bet:
    is_game_on = True

while is_game_on:
    for racer in turtles:
        if racer.xcor() > 230:
            is_game_on = False
            winner_color = racer.pencolor()
            t.penup()
            t.sety(racer.ycor())
            turtles.clear()
            style = ("arial", 15, 'bold')
            t.color(winner_color)
            if user_bet == winner_color:
                print(f"You've Won! The {winner_color} turtle is the winner!")
                t.write(f"You've Won! The {winner_color} turtle is the winner!", move=False, align="center", font=style)
            else:
                print(f"You've Lose! The {winner_color} turtle is the winner!")
                t.write(f"You've Lose! The {winner_color} turtle is the winner!", move=False, align="center", font=style)
            t.hideturtle()
        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)


screen.exitonclick()
