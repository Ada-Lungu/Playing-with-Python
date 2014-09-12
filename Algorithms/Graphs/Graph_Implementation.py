__author__ = 'ada'

# we'll use 2 classes, one the Vertex class, the other the Graph class

from algorithms.pythonds.basic import Queue
from algorithms.pythonds.graphs import PriorityQueue

class Heap:
    pass

class Vertex:

    def __init__(self, id):  #[v_id, {}]  Vertex(id, )
        self.id = id
        self.neighbour_to_weight = {} # {neighbour: weight}
        self.color = "white"
        self.pred = None
        self.distance = 0

# methods: add_neighbour, get_connections, get_ID, get_weight

# insert in the dictionary the new neighbour vertex and the weight corresponding {neighr:weight}
    def add_neighbour(self, neighbour, weight = 0):
        self.neighbour_to_weight[neighbour] = weight

    def add_undirected_neighbour(self, neighbour, weight = 0):
        self.add_neighbour(neighbour, weight)
        neighbour.add_neighbour(self, weight)

    def get_neighbours_vertices(self):
        return self.neighbour_to_weight.keys() # returns a list with the vertexes to which the key is connected (without the values: weights)

    def get_neighbours_number(self):
        return len(self.get_neighbours_vertices())

    def get_edges(self): # node_name = vertex.id
        node_and_neighbour = []
        pairs_of_node_and_its_neighbours = []

        for neighbour in self.neighbour_to_weight.keys():
            node_and_neighbour.append(self.id)
            node_and_neighbour.append(neighbour.id)
            pairs_of_node_and_its_neighbours.append(node_and_neighbour)
            node_and_neighbour = []
        return pairs_of_node_and_its_neighbours

    def get_info(self):
        return self.id

    def get_weight(self, neighbour):
        return self.neighbour_to_weight[neighbour]

    def is_path(self, to_vertex, visited):
        visited.append(self)
        if to_vertex in self.neighbour_to_weight:
            return True
        else:
            for n in self.neighbour_to_weight:
                if n not in visited:
                    if n.is_path(to_vertex, visited):
                        return True
        return False

    def shortest_path1(self, to_vertex):
        # if vertex is neighbour/one-way distance then ...
        min_dist = 100000
        # think about heap
        if to_vertex in self.neighbour_to_weight:
            return self.get_weight(to_vertex)
        else:
            for n in self.get_neighbours_vertices():
                dist_via_n = self.get_weight(n) + n.shortest_path1(to_vertex)
                if dist_via_n < min_dist:
                    min_dist = dist_via_n
            return min_dist


    def shortest_path(self, to_vertex, visited_neighbours): # from vertex self to another vertex
    # if the vertex is one way distance
        if self.is_path(to_vertex, visited_neighbours):
            if to_vertex in self.neighbour_to_weight:
                return self.neighbour_to_weight[to_vertex] # ==> gonna give me the weight
            else:
                minimum_distance = 100000
                visited_neighbours.append(self)

                for n in self.neighbour_to_weight:
                    # search through the visited_neighbours =>
                    if n not in visited_neighbours:
                        short_path = self.get_weight(n) + n.shortest_path(to_vertex, []) # ?????  why not visited_neighbours instead of []
                        if short_path < minimum_distance:
                            minimum_distance = short_path
                return minimum_distance

        # breadth first search
    def create_paths_from_start_vertex(self):
    # each vertex will have as instant values: distance, predecessor, colour => they all have the "set" and "get" methods
    # we first set these values of the start vertex
        self.set_distance(0)
        self.set_color("grey")
        will_be_visited_vertexes = Queue()
        will_be_visited_vertexes.enqueue(self)

        while will_be_visited_vertexes.size() > 0:
            curr_vertex = will_be_visited_vertexes.dequeue()
            for neighbour_vertex in curr_vertex.get_neighbours_vertices():
                if neighbour_vertex.get_color() == "white":
                    neighbour_vertex.set_color("grey")
                    neighbour_vertex.set_pred(curr_vertex)
                    neighbour_vertex.set_distance(curr_vertex.get_distance() + 1)
                    will_be_visited_vertexes.enqueue(neighbour_vertex)
            curr_vertex.set_color("black")


    # print the path from one vertex to another
    def get_path_to_vertex(self, end_vertex):
        self.create_paths_from_start_vertex()
        get_path_list_vertices = [end_vertex]
        x = end_vertex
        while x.get_pred() != self:
            x = x.get_pred()
            get_path_list_vertices.append(x)
        get_path_list_vertices.append(self)
        return get_path_list_vertices

    def print_path_from_vertex1_to_vertex2(self, vertex2):
        for vertex_visited in self.get_path_to_vertex(vertex2):
            print vertex_visited.id

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_pred(self, pred):
        self.pred = pred

    def get_pred(self):
        return self.pred

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def __str__(self):
        return "vertex: " + self.id + "(" + str(len(self.neighbour_to_weight)) + ")"

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

    def get_vertex(self, id):
        return self.vertices[id]

    def add_edge(self, info_from, info_to, weight = 1):
        info_from.add_neighbour(info_to, weight)

    def get_vertices(self):
        return self.vertices.values()

    def get_all_edges(self):
        all_edges = []
        for vertex in self.get_vertices():
            for vertex_and_neighbour in vertex.get_edges():
                all_edges.append(vertex_and_neighbour) # append to all_edges the edges of each vertex through the get_edges vertex method
        return all_edges

    # print with only one edge between nodes => folosim o conditie care sa restrictioneze repetitia de same edge between same nodes/same pair of nodes - (vertex, neighbour) (neighbour,vertex)
    def edges_as_dot_string(self):
        result = ""
        for vertex in self.vertices.values():
            for neighbour in vertex.get_neighbours_vertices():
                if vertex < neighbour:
                    result += vertex.id + " -> " + neighbour.id + " [dir = both];" "\n"

        return result

    # uses the get_edges method of vertex class
    def edges_as_dot_string2(self):
        result = ""
        for vertex in self.get_vertices():
            for vertex_and_neighbour in vertex.get_edges():
                if vertex_and_neighbour[0] < vertex_and_neighbour[1]:
                    result += vertex_and_neighbour[0] + "->" + vertex_and_neighbour[1] + "\n"
        return result   # returns all the edges in the graph as dot string => pentru fiecare node in graph: get.edges =>

    # uses the get_all_edges method of Graph class
    def edges_as_dot_string3(self):
        result = ""
        for vertex_and_neighbour in self.get_all_edges():
            if vertex_and_neighbour[0] < vertex_and_neighbour[1]:
                result += vertex_and_neighbour[0] + "->" + vertex_and_neighbour[1] + "\n"
        return result   # returns all the edges in the graph as dot string => pentru fiecare node in graph: get.edges =>


    # formatating into the .dot all the nodes and edges for further printing
    def string_as_dot(self, list_of_colored_vertices = [], color_input = "green"):
        result = ""
        result += "digraph {\n"

        # print all the nodes
        for each_vertex in self.get_vertices():
            if each_vertex in list_of_colored_vertices:
                result += each_vertex.id + " [fillcolor = " + color_input + ", style = filled];" + "\n"
            elif each_vertex.get_neighbours_number() == 1:
                result += each_vertex.id + " [fillcolor = white, style = filled]; " + "\n"
            elif each_vertex.get_neighbours_number() == 2:
                result += each_vertex.id + " [fillcolor = yellow, style = filled];" + "\n"
            elif each_vertex.get_neighbours_number() == 3:
                result += each_vertex.id + " [fillcolor = orange, style = filled];" + "\n"
            else:
                result += each_vertex.id + " [fillcolor = blue, style = filled];" + "\n"

        result += "\n"

        # print all the edges
        result += self.edges_as_dot_string3()
        result += "}"
        return result


    def print_as_dot(self, colored_vertices_list = [], color_input = "green"):
        print self.string_as_dot(colored_vertices_list, color_input)

    # saves graph to file named fileNamed
    def save_dot_to_file(self, file_name, colored_vertices_list = [], color_input = "green"):

        dot_script_file = open(file_name, "w")
        dot_script_file.write(self.string_as_dot(colored_vertices_list, color_input))
        dot_script_file.close()


    # breadth first search
    def create_paths_from_start_vertex(self, start_vertex):
        return self.create_paths_from_start_vertex(start_vertex)

    # print the path from one vertex to another
    def get_path_from_vertex1_to_vertex2(self, vertex1, vertex2):
        return vertex1.get_path_to_vertex(vertex2)


    def print_path_from_vertex1_to_vertex2(self, vertex1, vertex2):
        for vertex_visited in self.get_path_from_vertex1_to_vertex2(vertex1, vertex2):
            print vertex_visited.id


    def dijkstras_shortest_path(self, starting_vertex):
    # iterates over each vertex in the graph
    # the order of iteration through vertices is kept by a Priority Queue
    # the criteria that organizes the order in the priority queue is the value of dist
    # for each new vertex visited we set for it: predecessor, dist
    # make use of set + get methods for distance/predecessor

        to_be_visited_vertices = PriorityQueue() # list of tuples (vertex1, value=distance)
        starting_vertex.set_distance(0)
        starting_vertex.set_pred(None)

        # insert in the PQ the vertexes in the order of their value
        # buildheap() - creates a heap from a list of keys

        list_of_vertices_values = []
        maxint = 10000
        for vertex in self:
            # vertex_value = vertex.get_distance()
            vertex_value = vertex.set_distance(maxint) # doesn't it overrides the starting_vertex value?
            list_of_vertices_values.append(vertex_value)

        list_of_vertices_values.append(starting_vertex)
        to_be_visited_vertices.buildheap(list_of_vertices_values)

        # setting the current vertex and comparing the neighbours
        while not to_be_visited_vertices.isEmpty():
            current_vertex = to_be_visited_vertices.delMin() # returns the min item + removing it from heap

            for neighbour in current_vertex.get_neighbours_vertices():
                if neighbour.get_distance() > (current_vertex.get_distance + current_vertex.get_weight(neighbour)):
                    neighbour_new_dist = current_vertex.get_distance + current_vertex.get_weight(neighbour)
                    neighbour.set_distance(neighbour_new_dist)
                    neighbour.set_pred(current_vertex)
                    list_of_vertices_values.decreaseKey(neighbour, neighbour_new_dist) # il repozitioneaza in PQ in functie de noua value


    def print_dijkstra_shortest_path(self, vertex1, vertex2):

        self.dijkstras_shortest_path(vertex1)
        curr_vertex = vertex2
        path_from_vertex2_to_vertex1 = [curr_vertex]
        while curr_vertex.get_pred() != vertex1:
            # when we set a node to current_vertex, it is inserted in the path
            curr_vertex = curr_vertex.get_pred()
            path_from_vertex2_to_vertex1.append(curr_vertex)
        path_from_vertex2_to_vertex1.append(vertex1)

        return path_from_vertex2_to_vertex1




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

assert (vertex0.shortest_path(vertex1, []) == 5)
# assert (vertex0.shortest_path(vertex2) == 3)

print vertex0.get_path_to_vertex(vertex5)

print vertex0.get_edges()

# g = Graph({vertex0, vertex1, vertex2}, 3)

g = Graph()
g.add_vertex_object(vertex0)
g.add_vertex_object(vertex1)
g.add_vertex_object(vertex2)

print g.print_as_dot()

print g.get_path_from_vertex1_to_vertex2(vertex0, vertex5)

#print g.dijkstras_shortest_path(vertex0, vertex5)

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


assert (orash1.is_path(orash2, []))
assert (not orash2.is_path(orash1, []))


print orash1.get_neighbours_vertices()
print "Distanta de la Arad la Sibiu:" + str(orash1.get_weight(orash5))

print orash1.shortest_path(orash3, [])
print orash1.shortest_path(orash5, [])





















