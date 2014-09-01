__author__ = 'ada'

from Pythonds.basic.stack import Stack

# exploring the graph from a start_vertex
def dfs(start_vertex):

    start_vertex.set_pred(None)
    start_vertex.set_dist(0)
    visited_nodes = Stack()
    visited_nodes.push(start_vertex)
    was_visited = [start_vertex]

    while visited_nodes.size() > 0:
        current_node = visited_nodes.pop()
        if current_node.get_neighbours > 0:
            for neighbour in current_node.get_neighbours():
                if neighbour not in was_visited:
                    visited_nodes.push(neighbour)
                    if neighbour.get_neighbours() == 0:
                        visited_nodes.pop()

def dfs(start_vertex, path_of_visited_nodes):
    











