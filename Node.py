from __future__ import annotations
from math import sqrt, floor


class Node:
    # Initialize cost variables to max int32 values because we probably don't have that big board
    # 2**32 = 4294967296 so the board would be over 65536 nodes in width
    gcost = 2**32-1
    hcost = 2**32-1
    fcost = 2**32-1

    previous_node = None
    traversable = True

    def __init__(self, x: int, y: int) -> None:
        """ To create a node we need an x and a y coordinates """
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
        self.gcost = start_node.gcost + 10
        self.hcost = floor(sqrt((self.x - end_node.x) ** 2 + (self.y - end_node.y) ** 2) * 10)  # Pythagoras
        self.fcost = self.gcost + self.hcost
        self.previous_node = start_node

    @staticmethod
    def gcost_to() -> int:
        """ returns the gcost to a node """
        return 10

    def set_as_start(self) -> None:
        self.gcost = 0

    def change_traversable(self):
        self.traversable = not self.traversable

    def __str__(self) -> str:
        return f"Node({self.x}, {self.y})"

    def __eq__(self, node) -> bool:
        return (self.x == node.x) and (self.y == node.y)

