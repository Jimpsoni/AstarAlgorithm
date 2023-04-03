from random import choice
from AStar import AStar, Node
from Algorithm import Algorithm
from GUI import visualizer


"""
TODO Make it faster
"""


class CreateMaze(Algorithm):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__(width, height)

        self.stack = []
        self.visited = []

    def fill_with_walls(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                if i % 2 != 0 or j % 2 != 0:
                    self.board[i][j].traversable = False

    def iteration(self):
        # Take the top node of the stack
        if len(self.stack) == 0:
            return 1
        current = self.stack[-1]

        # Get its neighbors
        neighbors = self.get_neighbors(current, 2, self.validate_neighbor)

        if len(neighbors) == 0:
            self.visited.append(current)
            self.stack.pop()
            return

        random_node = choice(neighbors)

        self.destroy_wall(current, random_node)
        self.stack.append(random_node)
        self.visited.append(current)

    def validate_neighbor(self, node):
        return node not in self.visited

    def destroy_wall(self, start_node, end_node):
        y = int(start_node.y + (end_node.y - start_node.y) / 2)
        x = int(start_node.x + (end_node.x - start_node.x) / 2)
        self.board[y][x].traversable = True


if __name__ == "__main__":
    problem = AStar(Node(0, 0), Node(48, 48), 49, 49)
    maze = CreateMaze(50, 50)
    maze.fill_with_walls()
    problem.board = maze.get_board()

    v = visualizer(1200, 900, "A* algorithm", problem)
    v.show_display()
    v.set_up()

    maze.stack.append(Node(0, 0))

    while True:
        if maze.iteration() == "Complete!":
            break
        v.board = maze.get_board()
        v.set_up()

    v.set_up()
    v.run()
