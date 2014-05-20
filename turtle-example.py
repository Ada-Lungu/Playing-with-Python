
import turtle

the_turtle = turtle.Turtle()
screen = turtle.Screen()

def draw_spiral(my_turtle, line_lenght):
    if line_lenght > 0:
        my_turtle.forward(line_lenght)
        my_turtle.right(45)
        draw_spiral(my_turtle, line_lenght-5)

draw_spiral(the_turtle, 80)
screen.exitonclick()
