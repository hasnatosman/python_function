import turtle
turtle.speed(5)
turtle.color("blue")


def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


counter = 0
while counter < 72:
    draw_square(100)
    turtle.right(5)
    counter += 1

turtle.exitonclick()
turtle.hideturtle()
