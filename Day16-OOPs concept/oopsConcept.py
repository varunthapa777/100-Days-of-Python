# from turtle import Turtle, Screen
#
# gojo = Turtle()
# gojo.shape("turtle")
# gojo.color("DeepPink")
# my_screen = Screen()
#
# gojo.forward(100)
#
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
