import pygame.time

from AStar import AStar, Node
from CreateMaze import CreateMaze
from GUI import visualizer
from TkinterWindow import setUpWindow

setup = setUpWindow()
setup.create_window("Setup window", 300, 250)
setup.create_attributes()
setup.call_mainloop()
board_width, board_height = int(setup.board_dim), int(setup.board_dim)
# ===============================================
#               Variables

delay = 0

# ================================================


problem = AStar(Node(0, 0), Node(board_width - 1, board_height - 1), board_width, board_height)
maze = CreateMaze(board_width, board_height)
maze.fill_with_walls()
problem.board = maze.get_board()

v = visualizer(1200, 900, "A* algorithm", problem)
v.show_display()
v.set_up()

maze.stack.append(Node(0, 0))

while True:
    iteration = maze.iteration()
    if maze.iteration() is not None:
        break
    v.board = maze.get_board()
    v.set_up()

    pygame.time.wait(delay)

v.set_up()
v.run()
