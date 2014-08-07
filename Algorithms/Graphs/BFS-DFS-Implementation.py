__author__ = 'ada'

# BFS: we use: color, distance, predecessor - as methods of Vertex class
# we use a Queue, where we deposit the nodes that will be visited
# we need a current_node as a valuable variable

# the idea of predecessor, each node (except first) will have one predecessor,
# each will be predecessor for others except the last children

from GraphImplementation import Vertex, Graph
from Pythonds.basic.queue import Queue, Stack

def bfs(current_node):

    to_be_visited_nodes = Queue()
    to_be_visited_nodes.enqueue(current_node)
    current_node.set_color("grey")
    current_node.set_pred(None)
    current_node.set_distance(0)

    while to_be_visited_nodes.size() > 0:
        to_be_visited_nodes.dequeue(current_node)
        for neighbour in current_node.get_neighbours():
            if neighbour.get_color() == "white":
                to_be_visited_nodes.enqueue(neighbour)
                neighbour.set_color("grey")
                neighbour.set_pred(current_node)
                neighbour.set_distance(current_node.get_distance() + 1)
        current_node.set_color("black")


def get_path_from_one_vertex_to_another(the_graph, vertex1, vertex2):

    bfs(vertex1, the_graph)
    while vertex2.get_pred() != vertex1:
        print vertex2.get_pred()
        vertex2 = vertex2.get_pred()


def get_path_from_vertex1_to_vertex2(the_graph, vertex1, vertex2):

    bfs(vertex1, the_graph)
    path_from_vertex2_to_vertex1 = []

    vertex2 = x
    while x.get_pred() != vertex1:
        path_from_vertex2_to_vertex1.append(x)
        x = x.get_pred()
    path_from_vertex2_to_vertex1.append(x)
    path_from_vertex2_to_vertex1.append(vertex1)

    return path_from_vertex2_to_vertex1



def get_path_from_vertex1_to_vertex2(the_graph, vertex1, vertex2):

    bfs(vertex1, the_graph)
    path_from_vertex2_to_vertex1 = []

    while vertex2.get_pred() != vertex1:
        path_from_vertex2_to_vertex1.append(vertex2)
        vertex2 = vertex2.get_pred()
    path_from_vertex2_to_vertex1.append(vertex2)
    path_from_vertex2_to_vertex1.append(vertex1)

    return path_from_vertex2_to_vertex1



def dfs(starting_node):

    to_be_visited_nodes = Stack()
    dfs_path = []
    to_be_visited_nodes.push(starting_node)
    starting_node.set_color("grey")

    while to_be_visited_nodes.size() > 0:
        current_node = to_be_visited_nodes.pop()
        dfs_path.append(current_node)
        for neighbour in current_node.get_neighbours_vertices():
            if neighbour.get_color() == "white":
                to_be_visited_nodes.enqueue(neighbour)
                neighbour.set_color("grey")





















































