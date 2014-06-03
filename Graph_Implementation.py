__author__ = 'ada'

# we'll use 2 classes, one the Vertex class, the other the Graph class

class Heap:
    pass

class Vertex:

    def __init__(self, id):
        self.id = id
        self.neighbours = {} # {neighbour: weight}

# methods: add_neighbour, get_connections, get_ID, get_weight

# insert in the dictionary the new neighbour vertex and the weight corresponding {neighr:weight}
    def add_neighbour(self, neighbour, weight = 0):
        self.neighbours[neighbour] = weight

    def add_undirected_neighbour(self, neighbour, weight = 0):
        self.add_neighbour(neighbour, weight)
        neighbour.add_neighbour(self, weight)

    def get_connections(self):
        return self.neighbours.keys() # returns a list with the vertexes to which the key is connected

    def get_info(self):
        return self.id

    def get_weight(self, neighbour):
        return self.neighbours[neighbour]

    def is_path(self, vertex):
        if vertex in self.neighbours:
            return True
        else:
            for n in self.neighbours:
                if n.is_path(vertex):
                    return True
        return False

    def shortest_path(self, vertex):
        # if vertex is neighbour then ...
        min_dist = 100000
        # think about heap
        if vertex in self.neighbours:
            return self.get_weight(vertex)
        else:
            for n in self.get_connections():
                dist_via_n = self.get_weight(n) + n.shortest_path(vertex)
                if dist_via_n < min_dist:
                    min_dist = dist_via_n
            return min_dist

    def shortest_path(self, vertex): # from vertex self to another vertex
    # if the vertex is one way distance
        if self.is_path(vertex):
            if vertex in self.neighbours:
                return self.neighbours[vertex]
            else:
                minimum_distance = 100000
                for n in self.neighbours:
                    short_path = self.get_weight(n) + n.shortest_path(vertex)
                    if short_path < minimum_distance:
                        minimum_distance = short_path
                return minimum_distance


    def __str__(self):
        return "vertex: " + self.id + "(" + str(len(self.neighbours)) + ")"

    def __repr__(self):
        return str(self)




class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

# methods add_vertex

    # expects a string and constructs a vertex on its own!!!
    def add_vertex(self, info):
        assert(isinstance(info, str))
        self.num_vertices += 1
        new_vertex = Vertex(info)
        self.vertices[info] = new_vertex
        return new_vertex

    def get_vertex(self, info):
        return self.vertices[info]

    def add_edge(self, info_from, info_to, weight):

        info_from.add_neighbour(info_to, weight)

    def get_vertices(self):
        return self.vertices.values()



vertex0 = Vertex("v0")
vertex1 = Vertex("v1")
vertex2 = Vertex("v2")
vertex3 = Vertex("v3")
vertex4 = Vertex("v4")
vertex5 = Vertex("v5")

assert (vertex0.id == "v0")
assert (vertex0.get_connections() == [])

vertex0.add_neighbour(vertex1, 5)
vertex0.add_neighbour(vertex5, 2)
vertex1.add_neighbour(vertex2, 4)
vertex2.add_neighbour(vertex3, 9)
vertex3.add_neighbour(vertex4, 7)
vertex3.add_neighbour(vertex5, 3)
vertex4.add_neighbour(vertex0, 1)
vertex5.add_neighbour(vertex4, 8)
vertex5.add_neighbour(vertex2, 1)


assert (vertex1 in vertex0.get_connections())
assert (vertex5 in vertex0.get_connections())

assert (vertex0.get_weight(vertex1) == 5)

assert (vertex0.shortest_path(vertex1) == 5)
assert (vertex0.shortest_path(vertex2) == 3)



orash1 = Vertex("Arad") # obiect de tip Vertex cu id Arad
orash2 = Vertex("Timisoara")
orash3 = Vertex("Cluj-Napoca")
orash4 = Vertex("Brasov")
orash5 = Vertex("Sibiu")
orash6 = Vertex("Constanta")


orash1.add_neighbour(orash2, 50)
orash1.add_neighbour(orash3, 250)
orash1.add_neighbour(orash4, 460)
orash1.add_neighbour(orash5, 600)
orash1.add_neighbour(orash6, 700)


orash2.add_neighbour(orash3, 330)
orash2.add_neighbour(orash4, 430)
orash2.add_neighbour(orash5, 290)
orash2.add_neighbour(orash6, 780)

orash3.add_neighbour(orash4, 273)
orash3.add_neighbour(orash5, 175)
orash3.add_neighbour(orash6, 670)

orash4.add_neighbour(orash5, 140)
orash4.add_neighbour(orash6, 400)

orash5.add_neighbour(orash6, 500)

orash5.id = "Victoria"
assert(orash5.id == "Victoria")


assert (orash1.is_path(orash2))
assert (not orash2.is_path(orash1))


print orash1.get_connections()
print "Distanta de la Arad la Sibiu:" + str(orash1.get_weight(orash5))




















