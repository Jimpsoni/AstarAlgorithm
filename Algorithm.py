try:
    from math import sqrt, floor
    import numpy as np
    from operator import attrgetter
except ImportError as e:
    print("Couldn't import " + e.name)
    from math import sqrt, floor
    import numpy as np
    from operator import attrgetter


"""
RULES OF A* ALGORITHM

We calculate the gcost, hcost and fcost values
gcost - Distance from start point
hcost - Distance from end point
fcost - Addition of the previous two

"""


class Node:
    # Initialize cost variables to max int64 values
    gcost = 2**63-1
    hcost = 2**63-1
    fcost = 2**63-1
    previous_node = None
    traversable = True

    """ To create a node we need a x and a y coordinates """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_values(self, start_node, end_node):
        """
        Calculates the hcost, gcost and fcost using nodes own x and y and additional
        parameters "end_node" and "start_node" and calculating the distance to those points
        from nodes own coordinates
        :param start_node node where we entered this current node
        :param end_node same as start_node, but with endpoint coordinates
        """
        self.gcost = start_node.gcost + floor(sqrt((self.x - start_node.x) ** 2 + (self.y - start_node.y) ** 2) * 10)
        self.hcost = floor(sqrt((self.x - end_node.x) ** 2 + (self.y - end_node.y) ** 2) * 10)
        self.fcost = self.gcost + self.hcost
        self.previous_node = start_node

    def gcost_to(self, node):
        return floor(sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2) * 10)

    def set_as_start(self):
        self.gcost = 0

    def __str__(self):
        return f"Node({self.x}, {self.y})"

    def __eq__(self, node):
        return (self.x == node.x) and (self.y == node.y)


class AStar:
    """
    In the board, we mark all the available spaces with 0 and walls with 1
    """
    nodes = []
    checked = []

    def __init__(self, start, end, width, height):
        # Start and end point
        self.start = start
        self.end = end

        self.width = width
        self.height = height

        self.board = self.make_board()
        self.board[self.start.y][self.start.x].set_as_start()
        self.nodes.append(start)

    def get_neighbors(self, node):
        """ Returns all the available neighbors of the given node """
        nodes = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                # If we are out of the board, or we are at centerpiece
                if 0 <= node.y + i < self.height and 0 <= node.x + j < self.width and not (i == 0 and j == 0):
                    # If the node is traversable
                    if self.board[node.y + i][node.x + j].traversable:
                        nodes.append(self.board[node.y + i][node.x + j])

        return nodes

    def give_values(self, node, current):
        node.calculate_values(current, self.end)

    @staticmethod
    def get_path(current):
        """
        Makes a list of all the nodes needed
        :param current: the end node of our path
        :return: List is nodes that are in the path
        """
        path = []
        while current.previous_node is not None:
            path.append(current)
            current = current.previous_node
        return path

    def run(self):
        """ The main method to solve the path """
        path = None

        while path is None:
            # Get the smallest fcost node Nodes
            path = self.iteration()

        return path

    def make_board(self):
        return [[Node(i, j) for i in range(0, self.width)] for j in range(0, self.height)]

    def iteration(self):
        """
        Goes through one iteration of the algorithm
        :return: Path, when we find one
        """
        # Get the smallest fcost node Nodes
        if len(self.nodes) < 1:
            return []
        current = min(self.nodes, key=attrgetter("fcost"))
        self.nodes.remove(current)
        self.checked.append(current)

        if current == self.end:
            return self.get_path(current)

        for neighbor in self.get_neighbors(current):
            if neighbor in self.checked:
                continue

            if neighbor not in self.nodes or neighbor.gcost > (current.gcost + current.gcost_to(neighbor)):
                neighbor.calculate_values(current, self.end)
                neighbor.previous = current
                if neighbor not in self.nodes:
                    self.nodes.append(neighbor)

    def print_board(self):
        for row in self.board:
            for node in row:
                print(node)

    def __str__(self):
        """ Return string representation of the board """
        return str([str(line) + "\n" for line in self.board])


if __name__ == "__main__":
    game = AStar(Node(0, 0), Node(4, 4), 5, 5)
    game.print_board()
