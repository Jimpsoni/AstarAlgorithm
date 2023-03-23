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
    # Initialize cost variables
    gcost = None
    hcost = None
    fcost = None

    """ To create a node we need a x and a y coordinates """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_values(self, start_node, end_node):
        """
        Calculates the hcost, gcost and fcost using nodes own x and y and additional
        parameters "end_node" and "start_node" and calculating the distance to those points
        from nodes own coordinates
        :param start_node tuple or list of 2 values, x and y
        :param end_node same as start_node, but with endpoint coordinates
        """
        self.gcost = floor(sqrt((self.x - start_node.x) ** 2 + (self.y - start_node.y) ** 2) * 10)
        self.hcost = floor(sqrt((self.x - end_node.x) ** 2 + (self.y - end_node.y) ** 2) * 10)
        self.fcost = self.gcost + self.hcost

    def __str__(self):
        return f"I am node at ({self.x}, {self.y})"

    def __cmp__(self, node):
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

        self.board = np.zeros((width, height))

        self.width = width
        self.height = height

    def calculate_neighbors(self, node):
        """
        This function takes a node and calculates all the values for the
        surrounding nodes and adds them to Nodes list
        """

        nodes = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                # If we are out of the board, or we are at centerpiece
                if 0 <= node.y + i < self.height and 0 <= node.x + j < self.width and not (i == 0 and j == 0):
                    new_node = Node(node.x + j, node.y + i)             # Create a new node
                    new_node.calculate_values(self.start, self.end)     # Calculate values for it
                    nodes.append(new_node)                              # Append it to the list
        return nodes

    def run(self):
        self.nodes.append(self.start)
        while True:
            # Get the smallest fcost node Nodes
            current = min(self.nodes, key=attrgetter("fcost"))
            self.nodes.remove(current)
            self.checked.append(current)

            if current == self.end:
                return

            for n in current.calculate_neighbors():
                if n in self.checked:
                    continue

    def __str__(self):
        """ Return string representation of the board """
        return np.array2string(self.board)


if __name__ == "__main__":
    node1 = Node(1, 1)
    game = AStar((0, 0), (3, 3), 4, 4)
    game.calculate_neighbors(node1)
    print(game)
