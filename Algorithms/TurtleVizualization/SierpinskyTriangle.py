
import turtle
# each Triangle has: 3 points A,B,C , 3 laturi, 3 middle points of the laturi
# each Point has 2 coordonates x,y


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self,a,b,c):
        self.a = a # varful a
        self.b = b
        self.c = c

def draw_triangle(triangle, color, my_turtle):

    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(triangle.c.x, triangle.c.y)
    my_turtle.begin_fill()
    my_turtle.down()
    my_turtle.goto(triangle.a.x, triangle.a.y)
    my_turtle.goto(triangle.b.x, triangle.b.y)
    my_turtle.goto(triangle.c.x, triangle.c.y)
    my_turtle.end_fill()


def get_mid(point1, point2):
    return Point((point1.x + point2.x)/2,(point1.y + point2.y)/2)


def sierpinski_triangle(triangle, degree, my_turtle):
# degree = number of times I want to make the recursion => the triangle be splitted
    colors = ['blue','red','green','white','yellow',
                'violet','orange']
    draw_triangle(triangle, colors[degree], my_turtle)

    if degree > 0:
        sierpinski_triangle(Triangle(triangle.a, get_mid(triangle.a, triangle.b), get_mid(triangle.a, triangle.c)),
                            degree-1, my_turtle)
        sierpinski_triangle(Triangle(triangle.b, get_mid(triangle.b, triangle.c), get_mid(triangle.b, triangle.a)),
                            degree-1, my_turtle)
        sierpinski_triangle(Triangle(triangle.c, get_mid(triangle.c, triangle.a), get_mid(triangle.b, triangle.c)),
                            degree-1, my_turtle)


def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()

   # triangle = Triangle(Point(-100,-50),Point(0,100),Point(100,-50))
   triangle = Triangle(Point(-200,-10),Point(0,200),Point(200,-100))

   sierpinski_triangle(triangle,6,myTurtle)
   myWin.exitonclick()

main()












