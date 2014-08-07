
from Algorithms.Graphs.GraphImplementation import Vertex, Graph
from Pythonds.basic.stack import Stack

def ask_input_board_size():
    no_rows_columns = input("How many squares on rows/columns does the board have?")
    while not isinstance(no_rows_columns, int): # example: the user uses a string for num "three"
        print "Please use a number."
        no_rows_columns = input("How many squares on rows/columns does the board have?")
    return no_rows_columns

def build_knight_graph(no_rows_columns):

    knight_graph = Graph()

    # create vertices for each square on board and add them to the graph, the no of vertices is equal to no_rows_col squared
    # knight_graph.create_and_add_vertex_from_info(str(square_on_board))

    #chess_board = {}

    # the position of the knight is given by the row and col coordinates (any of the numbers of the board squares)
    for row_coord in range(no_rows_columns):
        for col_coord in range(no_rows_columns):
            square_coordinates = (row_coord, col_coord)
            knight_graph.create_and_add_vertex_from_info(square_coordinates) # create the Vertices in the graph with the info: coordinates
            #chess_board[square_coordinates] = knight_graph.create_and_add_vertex_from_info(square_coordinates)

    #patratel = (row_coord - 1)* 8 + col_coord
    #chess_board[patratel] = knight_graph.create_and_add_vertex_from_info(str(square_coordinates))

    #print chess_board

    # adding edges between connected nodes (each Vertex Square n board and possible moves rm there)
    for square_on_board_vertex in knight_graph.get_vertices():
        position_row, position_col = square_on_board_vertex.get_info()  # chess_board("square_on_board_vertex")
        list_of_moves = generate_possible_moves(position_row, position_col, no_rows_columns)
        for move in list_of_moves:
            print 'edge %s -> %s' % (square_on_board_vertex, knight_graph.get_vertex(move))
            knight_graph.add_edge(square_on_board_vertex, knight_graph.get_vertex(move))

    return knight_graph


# generated the possible moves of the knight from one square position, knowing the row and col of the knight's position on the board
def generate_possible_moves(position_row, position_col, no_rows_columns):

    moves_from_a_square = []
    possible_moves_coord = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, 1), (-2, -1), (2, -1), (2, 1)] # (col, row) (x, y)
    knight_init_pos = (position_row, position_col)

    for move in possible_moves_coord:
        knight_new_pos = knight_init_pos[0] + move[0], knight_init_pos[1] + move[1]
        if is_legal_coord(knight_new_pos, no_rows_columns): # legal_coord returns true/false
            moves_from_a_square.append(knight_new_pos)

    return moves_from_a_square


def is_legal_coord(knight_pos, no_rows_colums):
    if no_rows_colums > knight_pos[0] >= 0 and no_rows_colums > knight_pos[1] >= 0:
        return True
    return False


# using DFS and Recursion
def knight_tour(curr_node_square, no_rows_columns, path_of_visited_node_squares = []):
# this function gives us the path = sequence of moves by the knight so that
# it visits all the squares on the board only once

# we need as parameters/arguments: current depth in the search tree/ path_of_visited_squares/
#  square_to_be_visited / limit_num_of_nodes_in the path

    #curr_node_square = Vertex()
    #print ' ' * len(path_of_visited_node_squares) + str(curr_node_square)

    limit_num_of_nodes_in_the_path = int(no_rows_columns**2)
    curr_node_square.set_color("grey")
    path_of_visited_node_squares.append(curr_node_square)

    #we stop our search when the path of visited nodes is equal with the no of squares
    if len(path_of_visited_node_squares) < limit_num_of_nodes_in_the_path:
       # curr_node_square.get_neighbours_vertices()
        for neighbour_node in curr_node_square.get_neighbours_vertices():
            if neighbour_node.get_color() == "white":
                # daca neighbour_node are si el neighbours, si nu e dead-end
                # path_of_visited_node_squares.append(neighbour_node)
                result = knight_tour(neighbour_node, no_rows_columns, path_of_visited_node_squares)
                if result:
                    return result

    else:
        return path_of_visited_node_squares

    # it means ca nu am ajuns la sfarsit + fiecare nod vizitat este
    curr_node_square.set_color("white")
    path_of_visited_node_squares.pop()


# DFS without Recursion
def knight_tour_with_stack(knight_graph, board_size):
    dfs_stack = Stack() # nu importa modulul Stack
    path_visited_nodes = []


    start_vertex = knight_graph.get_vertex((0,0))
    partial_sol_stack = Stack()
    dfs_stack.push(start_vertex)
    path_visited_nodes.append(start_vertex)
    start_vertex.set_color("grey")

    while dfs_stack.size() > 0:
        current_node = dfs_stack.pop()
        if len(path_visited_nodes) == board_size*board_size:
            return path_visited_nodes

        path_visited_nodes.append(current_node)
        partial_sol_stack.push(path_visited_nodes)


        at_least_one_white_child = False
        for neighbour in current_node.get_neighbour_vertices():
            if neighbour.get_color() == "white":
                dfs_stack.push(neighbour)
                at_least_one_white_child = True


        if not at_least_one_white_child:
            path_visited_nodes = partial_sol_stack.pop()
        current_node.set_color("grey")

    return path_visited_nodes



board_size = ask_input_board_size()
build_knight_graph(board_size)
#print knight_tour((build_knight_graph(board_size)).get_vertex((0,0)), board_size, [])

print knight_tour_with_stack((build_knight_graph(board_size))



