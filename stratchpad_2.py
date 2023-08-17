from turtle import Screen, Turtle


def draw():
    turtle_rectangle.color("green")

    width, height = screen.window_width(), screen.window_height()

    turtle_rectangle.penup()
    turtle_rectangle.goto(-width/2, 0)
    turtle_rectangle.pendown()

    turtle_rectangle.begin_fill()

    for _ in range(2):
        turtle_rectangle.forward(width)
        turtle_rectangle.right(90)
        turtle_rectangle.forward(height/2)
        turtle_rectangle.right(90)

    turtle_rectangle.end_fill()

screen = Screen()

turtle_rectangle = Turtle()
turtle_rectangle.speed('fastest')  # because I have no patience

draw()

turtle_rectangle.hideturtle()
screen.exitonclick()