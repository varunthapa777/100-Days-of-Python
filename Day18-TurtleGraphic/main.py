import turtle as t
import random

# colors = colorgram.extract("img.jpg", 30)
# color_palet = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palet.append((r, g, b))
#
#
# print(color_palet)
colors = [(166, 169, 29), (203, 164, 94), (199, 132, 155), (223, 234, 227), (16, 106, 153), (156, 96, 39), (130, 156, 179), (192, 216, 224), (40, 135, 106), (145, 66, 105), (229, 198, 111), (227, 208, 214), (108, 166, 145), (172, 18, 11), (0, 103, 119), (94, 153, 81), (193, 78, 106), (229, 171, 189), (25, 61, 109), (171, 14, 30), (100, 129, 166), (151, 115, 109), (36, 80, 44), (64, 147, 181), (175, 202, 186), (28, 52, 94), (239, 198, 4), (169, 203, 210), (218, 180, 174)]

tim = t.Turtle()
t.colormode(255)
tim.speed(40)
tim.penup()
x_axis = -300.0
y_axis = -300.00
tim.setposition(x_axis,y_axis)
for i in range(10):
    tim.pendown()
    for _ in range(11):
        color = random.choice(colors)
        tim.color(color)
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.penup()
        tim.forward(60)
        tim.pendown()

    tim.penup()
    y_axis += 60
    tim.setposition((x_axis, y_axis))


tim.hideturtle()

screen = t.Screen()
screen.exitonclick()


