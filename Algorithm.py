from __future__ import annotations
from math import sqrt, floor
from operator import attrgetter

"""
RULES OF A* ALGORITHM

We calculate the gcost, hcost and fcost values
gcost - Distance from start point
hcost - Distance from end point
fcost - Addition of the previous two



TODO - List 
- Change the type of algorithm so it favors nodes with least h_cost


"""


class Node:
    # Initialize cost variables to max int32 values because we probably don't have that big board
    # 2**32 = 4294967296 so the board would be over 65536 nodes in width
    gcost = 2**32-1
    hcost = 2**32-1
    fcost = 2**32-1

    previous_node = None
    traversable = True

    def __init__(self, x: int, y: int) -> None:
        """ To create a node we need a x and a y coordinates """
        self.x = x
        self.y = y

    def calculate_values(self, start_node: Node, end_node: Node) -> None:
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

    def gcost_to(self, node: Node) -> int:
        """ returns the gcost to a node """
        return floor(sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2) * 10)

    def set_as_start(self) -> None:
        self.gcost = 0

    def __str__(self) -> str:
        return f"Node({self.x}, {self.y})"

    def __eq__(self, node) -> bool:
        """ Checking if two nodes are equal """
        return (self.x == node.x) and (self.y == node.y)


class AStar:
    nodes = []
    checked = []

    def __init__(self, start: Node, end: Node, width: int, height: int) -> None:
        """
        We make a board with given width and height, then we call the make_board method
        to initialize node for each of the squares.
        :param start:  Node we start from
        :param end:    Node we end up in
        :param width:  Width of the board
        :param height: Height of the board
        """
        # Start and end point
        self.start = start
        self.end = end

        self.width = width
        self.height = height

        self.board = self.make_board()
        self.board[self.start.y][self.start.x].set_as_start()
        self.nodes.append(start)

    def get_neighbors(self, node: Node) -> list[Node]:
        """
        Returns all the available neighbors of the given node. This excludes all the nodes that are not traversable
        and the centerpiece.
        :param node: The node of which neighbors we get
        """
        nodes = []  # Here we append all the neighbors

        for i in range(-1, 2):
            for j in range(-1, 2):
                # If we are out of the board, or we are at centerpiece
                if 0 <= node.y + i < self.height and 0 <= node.x + j < self.width and not (i == 0 and j == 0):
                    # If the node is traversable
                    if self.board[node.y + i][node.x + j].traversable:
                        nodes.append(self.board[node.y + i][node.x + j])

        return nodes

    def give_values(self, node: Node, current: Node) -> None:
        """
        Yeah dude, no idea why this is here
        :param node:
        :param current:
        :return:
        """
        node.calculate_values(current, self.end)

    def make_board(self) -> list[list[Node]]:
        """
        :return: 2D list that has height amount of lists size of the width full of nodes.
        """
        return [[Node(i, j) for i in range(0, self.width)] for j in range(0, self.height)]

    def run(self) -> list[Node]:
        """
        Runs iterations until we find the end
        :return: Path from start to the end
        """
        path = None

        while path is None:
            # Get the smallest fcost node Nodes
            path = self.iteration()

        return path

    def iteration(self) -> list[Node]:
        """
        Goes through one iteration of the algorithm
        :return: Path, if we find one on the current iteration
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

            # If the neighbor is not in the nodes or we find a shorter path to the node
            if neighbor not in self.nodes or neighbor.gcost > (current.gcost + current.gcost_to(neighbor)):
                # Then we calculate the path to this node
                neighbor.calculate_values(current, self.end)
                neighbor.previous = current
                if neighbor not in self.nodes:
                    self.nodes.append(neighbor)

    @staticmethod
    def get_path(current) -> list[Node]:
        """
        Goes back the shortest path and appends all the nodes into the list until we arrive at the start, where previous
        node is None
        :param current: the end node of our path
        :return: List is nodes that are in the path
        """
        path = []
        while current.previous_node is not None:
            path.append(current)
            current = current.previous_node
        return path

    def print_board(self) -> None:
        """ Prints the board in to the console """
        for row in self.board:
            for node in row:
                print(str(node) + "  ", end="")
            print("\n")

    def __str__(self) -> str:
        """ Return string representation of the board """
        return str([str(line) + "\n" for line in self.board])


if __name__ == "__main__":
    game = AStar(Node(0, 0), Node(4, 4), 5, 5)
    game.print_board()
