from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def clear_drawing():
    tim.clear()
    tim.home()
    tim.penup()
    tim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_drawing)
screen.exitonclick()
