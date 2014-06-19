__author__ = 'ada'

# we'll use 2 classes, one the Vertex class, the other the Graph class

class Heap:
    pass

class Vertex:

    def __init__(self, id):  #[v_id, {}]  Vertex(id, )
        self.id = id
        self.neighbours = {} # {neighbour: weight}

# methods: add_neighbour, get_connections, get_ID, get_weight

# insert in the dictionary the new neighbour vertex and the weight corresponding {neighr:weight}
    def add_neighbour(self, neighbour, weight = 0):
        self.neighbours[neighbour] = weight

    def add_undirected_neighbour(self, neighbour, weight = 0):
        self.add_neighbour(neighbour, weight)
        neighbour.add_neighbour(self, weight)

    def get_neighbours_vertices(self):
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
            for n in self.get_neighbours_vertices():
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
        self.vertices = {} # (vertex_name: vertex)
        self.num_vertices = 0

# methods add_vertex

    # expects a string and constructs a vertex on its own!!!
    def create_and_add_vertex_from_info(self, info):
        assert(isinstance(info, str))
        self.num_vertices += 1
        new_vertex = Vertex(info)
        self.vertices[info] = new_vertex
        return new_vertex

    def add_vertex_object(self, vertex):
        self.num_vertices += 1
        self.vertices[vertex.id] = vertex

    def get_vertex(self, info):
        return self.vertices[info]

    def add_edge(self, info_from, info_to, weight = None):
        info_from.add_neighbour(info_to, weight)

    def get_vertices(self):
        return self.vertices.values()

    def string_as_dot(self):
        result = ""
        result += "graph {\n"

        # print all the nodes
        for each in self.vertices.keys(): # just the name of the vertices <= keys
            result += each + "\n"
        result += "\n"
        # print all the edges
        for vertex in self.vertices.values(): # values: the vertex(es), the keys are the vertexes_name
            for neighbour in vertex.get_neighbours_vertices():
                result += vertex.id + "--" + neighbour.id + "\n"
        result += "}"
        return result

    def print_as_dot(self):
        print self.string_as_dot()

    # saves graph to file named fileNamed
    def save_dot_to_file(self, file_name):

        dot_script_file = open(file_name, "w")
        dot_script_file.write(self.string_as_dot())
        dot_script_file.close()

# 1000 most frequent letter words


vertex0 = Vertex("v0")
vertex1 = Vertex("v1")
vertex2 = Vertex("v2")
vertex3 = Vertex("v3")
vertex4 = Vertex("v4")
vertex5 = Vertex("v5")

assert (vertex0.id == "v0")
assert (vertex0.get_neighbours_vertices() == [])

vertex0.add_neighbour(vertex1, 5)
vertex0.add_neighbour(vertex5, 2)
vertex1.add_neighbour(vertex2, 4)
vertex2.add_neighbour(vertex3, 9)
vertex3.add_neighbour(vertex4, 7)
vertex3.add_neighbour(vertex5, 3)
vertex4.add_neighbour(vertex0, 1)
vertex5.add_neighbour(vertex4, 8)
vertex5.add_neighbour(vertex2, 1)

assert (vertex1 in vertex0.get_neighbours_vertices())
assert (vertex5 in vertex0.get_neighbours_vertices())

assert (vertex0.get_weight(vertex1) == 5)

assert (vertex0.shortest_path(vertex1) == 5)
assert (vertex0.shortest_path(vertex2) == 3)


# g = Graph({vertex0, vertex1, vertex2}, 3)

g = Graph()
g.add_vertex_object(vertex0)
g.add_vertex_object(vertex1)
g.add_vertex_object(vertex2)

print g.print_as_dot()



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


print orash1.get_neighbours_vertices()
print "Distanta de la Arad la Sibiu:" + str(orash1.get_weight(orash5))




















