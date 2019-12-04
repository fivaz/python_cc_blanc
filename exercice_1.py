"""
1. Coder la fonction find_path_from pour aider la tortue à trouver la sortie d'un labyrinthe
à partir d'une position initiale S

La fonction reçoit un labyrinthe, une position x et une position y

Les cas d'arrêt sont données par les fonctions:
- is_exit
- is_obstacle
- is_explored

La méthode update_position peut être utilisée pour changer la position de la tortue
et aussi marquer les positions explorées:
- TRIED: essayé
- DEAD_END: pas une solution
- PART_OF_PATH: solution

"""

import random
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    def __init__(self, maze_file_name: str):
        """
        maze constructor
        :param maze_file_name: a file containing the maze configuration:
                ' ' space for open path, S for start position and + for obstacles
        """
        self.rows_in_maze: int = None
        self.columns_in_maze: int = None
        self.start_row: int = None
        self.start_col: int = None
        self.maze_list = []
        self.__load_map(maze_file_name)

        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(self.columns_in_maze - 1) / 2 - .5,
            -(self.rows_in_maze - 1) / 2 - .5,
            (self.columns_in_maze - 1) / 2 + .5,
            (self.rows_in_maze - 1) / 2 + .5)

        self.__draw_maze()

    def __load_map(self, maze_file_name: str):
        """
        load map configuration
        :param maze_file_name: configuration file
        :return:
        """
        self.rows_in_maze: int = 0
        self.columns_in_maze: int = 0
        maze_file = open(maze_file_name, 'r')
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = self.rows_in_maze
                    self.start_col = col
                    self.columns_in_maze = len(line) - 1
                col = col + 1
            self.rows_in_maze = self.rows_in_maze + 1
            self.maze_list.append(row_list)

    def __draw_maze(self):
        """
        draw initial maze defined in the config file
        basically draws obstacles and the turtle
        :return:
        """
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.__draw_centered_box(x + self.x_translate, -y + self.y_translate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def __draw_centered_box(self, x: float, y: float, color: str):
        """
        draw an obstacle box
        :param x: initial x coordinate of the box
        :param y: initial y coordinate of the box
        :param color: obstacle color
        :return:
        """
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def __move_turtle(self, x: int, y: int):
        """
        move turtle to position x, y
        :param x: new turtle x position
        :param y: new turtle y position
        :return:
        """
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def __drop_breadcrumb(self, color):
        """
        draw a breadcrumb point
        :param color: breadcrumb color
        :return:
        """
        self.t.dot(10, color)

    def update_position(self, row: int, col: int, val: str = None):
        """
        update turtle position and drop a breadcrumb
        :param row: new turtle x position
        :param col: new turtle y position
        :param val: path value: 0 (part of path) . (tried) + (obstacle) - (dead end)
        :return:
        """
        if val is not None:
            self.maze_list[row][col] = val
        self.__move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color is not None:
            self.__drop_breadcrumb(color)

    def is_obstacle(self, row: int, col: int):
        """
        check if row, col is an obstacle
        :param row: maze row id
        :param col: maze col id
        :return:
        """
        return self.maze_list[row][col] == OBSTACLE

    def is_explored(self, row: int, col: int):
        """
        check if row, col has been explored
        :param row: maze row id
        :param col: maze col id
        :return:
        """
        return self.maze_list[row][col] == TRIED or self.maze_list[row][col] == DEAD_END

    def is_exit(self, row: int, col: int):
        """
        check if row, col is an exit
        :param row: maze row id
        :param col: maze col id
        :return:
        """
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]


def get_directions_from_point(row, col):
    #       south          north           west            east
    res = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    random.shuffle(res)
    return res


def find_path_from(maze: Maze, start_row: int, start_column: int):
    """
    search an exit within a maze given start row and col
    :param maze: a maze
    :param start_row: turtle start row
    :param start_column: turtle start column
    :return: true if an exit if found
    """
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    pass


    #  2. We have found a square that has already been explored




    # 3. We have found an outside edge not occupied by an obstacle




    # 4. We are in a square not visited




    # Otherwise, use logical short circuiting to try each direction




    # update position (DEAD_END or PART_OF_PATH)







if __name__ == "__main__":
    my_maze = Maze('maze2.txt')
    my_maze.update_position(my_maze.start_row, my_maze.start_col)
    input("ready to go?")
    find_path_from(my_maze, my_maze.start_row, my_maze.start_col)
    input("quit?")
