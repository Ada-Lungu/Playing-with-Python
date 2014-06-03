__author__ = 'ada'


# searching from the position the turtle is around
# taking the base cases into account
# given methods: update_position, is_exit, draw_maze


def search_from(maze, starting_row, starting_column):
    maze.update_position(starting_row, starting_column)
    # base one: run into wall
    if maze[starting_row][starting_column] == OBSTACLE:
        return False
    if maze[starting_row][starting_column] == TRIED:
        return False
    if maze.is_exit(starting_row, starting_column):
        maze.update_position(starting_row, starting_column, part_of_path)
    maze.update_position(starting_row, starting_column, tried)


    # searching the four directions recursively

    found = search_from(maze, starting_row-1, starting_column) or
            search_from(maze, starting_row+1, starting_column) or
            search_from(maze, starting_row, starting_column-1) or
            search_from(maze, starting_row, starting_column+1)
    if found:
         maze.update_position(else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
     else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


# initializam maze-ul, luam dintr-un file unde e reprezentat simbolic
# maze-ul este o lista de liste de rows => maze_rows sunt luate din line-urile maze-file

class Maze:
    def__init__(self, columns, rows, maze_file):
        columns_no = 0
        rows_no = 0
        self.maze_List = [] # actually compound of the rows

        maze_file = open("maze_file_name", "r")
        rows_no = 0

        for line in maze_file:
            row_list = []

            for char in line:
                row_list.append(char)
                col = 0
                if char == "S":
                    self.starting_row = rows_no
                    self.starting_column = col
                col += 1

        rows_no += 1
        self.maze_list.append(row_list)
        columns_no = len(row_list)




















