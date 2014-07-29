
class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle():
    # a
    def __init__(self, a,b,c):
        # assert(isinstance(a, Point))
        self.a = a
        self.b = b
        self.c = c

myPoints = [[-100,-50],[0,100],[100,-50]]
assert (myPoints[0][0] == -100)
assert (myPoints[0][1] == -50)

points = [ Point (-100,50), Point (100,50), Point (0,-100)]
assert (points[0].x == -100)
assert (points[0].y  == 50)


triangle = Triangle(Point(-100,-50), Point (100,50), Point (0,-100))
assert (triangle.a.x == -100)
assert (triangle.a.y == -50)


triangle = Triangle([-100,-50],[0,100],[100,-50])
assert (triangle.a[0] == -100)
assert (triangle.a[1] == -50)


