__author__ = 'ada'

# we'll use 2 classes, one the Vertex class, the other the Graph class

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connect_to = {} # will look like this {V0:4, V1:6}

# methods: add_neighbour, get_connections, get_ID, get_weight

# insert in the dictionary the new neighbour vertex and the weight corresponding {neighr:weight}
    def add_neighbour(self, neighbour, weight = 0):
        self.connect_to[neighbour] = weight

    def get_connections(self):
        return self.connect_to.keys() # returns a list with the vertexes to which the key is connected

    def get_id(self):
        return self.id

# my version
    def get_weight(self):
        return self.connect_to.values() # returns a list of the weights

# their version
    def get_weight(self):
        return self.connect_to[neighbour]


class Graph:
    def __init__(self):
        self.graph = {} # {key, connect_to} ==> [key, {v0:4, v1:6}]
        self.num_vertices = 0

# methods add_vertex

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.graph[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        return self.graph[key]

    def add_edge(self,key,new_edge):

    def get_vertices(self):
        return self.graph.keys()




















