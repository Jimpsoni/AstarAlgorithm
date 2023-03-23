try:
    # put all import here
    pass
except ImportError as e:
    print("Couldn't import " + e.name)

from math import sqrt, floor

"""
RULES OF A* ALGORITHM

We calculate the gcost, hcost and fcost values
gcost - Distance from start point
hcost - Distance from end point
fcost - Addition of the previous two

"""


class Node:
    gcost = 16
    hcost = 14
    fcost = None

    """ To create a node we need a x and a y coordinates """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_values(self, start_node, end_node):
        """
        Calculates the hcost, gcost and fcost using nodes own x and y and additional
        parameters "end_node" and "start_node"
        :param start_node tuple or list of 2 values, x and y
        :param end_node same as start_node, but with endpoint coordinates
        """
        self.gcost = floor(sqrt((self.x - start_node[0])**2 + (self.y - start_node[1])**2) * 10)
        self.hcost = floor(sqrt((self.x - end_node[0])**2 + (self.y - end_node[1])**2) * 10)
        self.fcost = self.gcost + self.hcost

    def __str__(self):
        return f"I am node at ({self.x}, {self.y})"


class AStar:
    # This is where we store all the nodes
    Nodes = []

    def __init__(self, start, end):
        # Start and end point
        self.start = start
        self.end = end


if __name__ == "__main__":
    node1 = Node(5, 9)
    print(node1)
    node1.calculate_values((1, 1))
    print(node1.hcost)
