from operator import attrgetter
from Algorithm import Algorithm
from Node import Node


"""
RULES OF A* ALGORITHM

TODO - List 
- Change the type of algorithm so it favors nodes with least h_cost
- Change the algorithm so it doesn't skip corners

"""


class AStar(Algorithm):
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

        super().__init__(width, height)

        self.board[self.start.y][self.start.x].set_as_start()
        self.nodes.append(start)

    def give_values(self, node: Node, current: Node) -> None:
        """
        Yeah dude, no idea why this is here
        :param node:
        :param current:
        :return:
        """
        node.calculate_values(current, self.end)

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

    @staticmethod
    def validate_neighbor(node):
        return node.traversable

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

        for neighbor in self.get_neighbors(current, 1, self.validate_neighbor):
            if neighbor in self.checked:
                continue

            # If the neighbor is not in the nodes, or we find a shorter path to the node
            if neighbor not in self.nodes or neighbor.gcost > (current.gcost + current.gcost_to()):
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

    def __str__(self) -> str:
        return str([str(line) + "\n" for line in self.board])


if __name__ == "__main__":
    print("This is the AStar algorithm\n")
    print("Rules are simple:")

    """
    def get_neighbors(self, node: Node) -> list[Node]:
        Returns all the available neighbors of the given node. This excludes all the nodes that are not traversable
        and the centerpiece.
        :param node: The node of which neighbors we get

        nodes = []  # Here we append all the neighbors

        for i in range(-1, 2):
            for j in range(-1, 2):
                # If we are out of the board, or we are at centerpiece
                if 0 <= node.y + i < self.height and 0 <= node.x + j < self.width and not (i == 0 and j == 0):
                    # If the node is traversable
                    if self.board[node.y + i][node.x + j].traversable:
                        nodes.append(self.board[node.y + i][node.x + j])

        return nodes
    """
