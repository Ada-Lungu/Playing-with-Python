__author__ = 'ada'

# first step: creating paths from the starting vertex to all others
# implementation of BFS

from Pythonds.basic.queue import Queue
from Algorithms.Graphs.GraphExamples import g

def bfs1(start_vertex):

    start_vertex.set_color("white")
    start_vertex.set_pred(None)
    start_vertex.set_distance(0)
    will_be_visited_vertices = Queue()
    will_be_visited_vertices.enqueue(start_vertex)


    while will_be_visited_vertices.size() > 0:
        curr_vertex = will_be_visited_vertices.dequeue()
        for neighbour in curr_vertex.get_neighbours_vertices():
            if neighbour.get_color() == "white": # could it be different ???
                neighbour.set_color("grey")
                neighbour.set_pred(curr_vertex)
                neighbour.set_distance(curr_vertex.get_distance() + 1)
                will_be_visited_vertices.enqueue(neighbour)
        curr_vertex.set_color("black")


def get_path_from_vertex_to_vertex(from_vertex, to_vertex):
    bfs1(from_vertex)
    path_from_vertex_to_vertex = []

    while to_vertex.get_pred() != from_vertex: # .id  ??
        path_from_vertex_to_vertex.append(to_vertex)
        to_vertex = to_vertex.get_pred()
    path_from_vertex_to_vertex.append(to_vertex)
    path_from_vertex_to_vertex.append(from_vertex)

    return path_from_vertex_to_vertex


def the_real_recursive(from_vertex, to_vertex, path_from_to_vertex):

    if to_vertex.get_pred() == from_vertex:
        path_from_to_vertex.append(to_vertex)
        path_from_to_vertex.append(from_vertex)
        return path_from_to_vertex
    else:

        current_vertex = to_vertex.get_pred()
        path_from_to_vertex.append(to_vertex)

        return the_real_recursive(from_vertex, current_vertex, path_from_to_vertex)


# recursively
def get_path_from_to_recursively(from_vertex, to_vertex, path_from_to_vertex):
    bfs1(from_vertex)
    return the_real_recursive(from_vertex,to_vertex, path_from_to_vertex)




print get_path_from_vertex_to_vertex(g.get_vertex("Arad"), g.get_vertex("Cluj-Napoca"))
print get_path_from_to_recursively(g.get_vertex("Arad"), g.get_vertex("Cluj-Napoca"), [])






# try again without colours

def bfs2(start_vertex):

    # is_visited/set_is_visited method looks if the vertex was in the vertices_next_be_visited


    was_visited = False
    start_vertex.set_pred(None)
    start_vertex.set_dist(0)
    vertices_next_be_visited = Queue()
    vertices_next_be_visited.enqueue(start_vertex)
    #start_vertex.set_is_visited(True)

    while vertices_next_be_visited.size() > 0 and not was_visited:
        current_node = vertices_next_be_visited.dequeue()
        was_visited = True
        for nbr in current_node.get_neighbours():

                is_visited = True
                nbr.set_pred(current_node)
                nbr.set_dist(current_node.get_dist() + 1)
                vertices_next_be_visited.enqueue(nbr) # indentation, could be here or ne more left ??? - no, then it will put it anyways, not white


def get_path_from_to_vertex(from_v, to_v):
    bfs2(from_v)
    path_from_to_vertex = [from_v]
    current_v = from_v

    while current_v.get_pred() != to_v:
        current_v = current_v.get_pred()
        path_from_to_vertex.append(current_v)
    path_from_to_vertex.append(to_v)

    return path_from_to_vertex




# try again without colours, was_visited list instead

def bfs3(start_vertex):


    start_vertex.set_pred(None)
    start_vertex.set_distance(0)
    will_be_visited_vertices = Queue()
    will_be_visited_vertices.enqueue(start_vertex)
    was_visited = []


    while will_be_visited_vertices.size() > 0:
        curr_vertex = will_be_visited_vertices.dequeue()
        was_visited.append(curr_vertex)
        for neighbour in curr_vertex.get_neighbours_vertices():
            if neighbour not in was_visited: # could it be different ???
                neighbour.set_pred(curr_vertex)
                neighbour.set_distance(curr_vertex.get_distance() + 1)
                will_be_visited_vertices.enqueue(neighbour)


def get_path_from_vertex_to_vertex3(from_vertex, to_vertex):
    bfs1(from_vertex)
    path_from_vertex_to_vertex = []

    while to_vertex.get_pred() != from_vertex: # .id  ??
        path_from_vertex_to_vertex.append(to_vertex)
        to_vertex = to_vertex.get_pred()
    path_from_vertex_to_vertex.append(to_vertex)
    path_from_vertex_to_vertex.append(from_vertex)

    return path_from_vertex_to_vertex

print get_path_from_vertex_to_vertex3(g.get_vertex("Arad"), g.get_vertex("Cluj-Napoca"))














































