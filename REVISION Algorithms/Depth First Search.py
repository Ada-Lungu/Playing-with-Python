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


# dfs recursively + backtracking
def dfs(start_vertex,):

    visited_nodes = Stack()
    start_vertex.no_more_nbr_to_explore() == False
    visited_nodes.push(start_vertex)
    current_node = visited_nodes.pop()

    if visited_nodes.size() == 0:
        return visited_nodes

        if current_node.no_more_nbr_to_explore() == True:
            visited_nodes.pop()
            current_node = visited_nodes.pop()
        else:
            for nbr in current_node.get_neighbours_vertices():
                visited_nodes.push(nbr)
                current_node = nbr
























