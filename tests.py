import unittest
from AStar import Node, AStar


class testNodeMethods(unittest.TestCase):
    def test_calculate_values(self):
        # Test hcost, gcost and fcost
        start, end, node = Node(1, 1), Node(5, 9), Node(2, 2)
        start.gcost = 0
        node.calculate_values(start, end)

        self.assertEqual(14, node.gcost)
        self.assertEqual(76, node.hcost)
        self.assertEqual(90, node.fcost)

        start, end, node = Node(5, 2), Node(2, 5), Node(2, 2)
        start.gcost = 0
        node.calculate_values(start, end)
        self.assertEqual(30, node.gcost)
        self.assertEqual(30, node.hcost)
        self.assertEqual(60, node.fcost)

    def test_gcost_to(self):
        start_node = Node(1, 1)
        end_node = Node(1, 2)
        self.assertEqual(10, start_node.gcost_to(end_node))

        end_node = Node(2, 2)
        self.assertEqual(14, start_node.gcost_to(end_node))

        end_node = Node(1, 1)
        self.assertEqual(0, start_node.gcost_to(end_node))


class testAstarMethods(unittest.TestCase):
    def test_get_neighbors(self):
        start, end = Node(1, 1), Node(4, 4)
        start.gcost = 0
        width, height = 5, 5
        alg = AStar(start, end, width, height)
        nodes = alg.get_neighbors(Node(1, 1))

        self.assertEqual(8, len(nodes))
        self.assertEqual(0, nodes[0].x)
        self.assertEqual(0, nodes[0].y)
        self.assertEqual(1, nodes[6].x)
        self.assertEqual(2, nodes[6].y)

        nodes = alg.get_neighbors(Node(0, 0))
        self.assertEqual(3, len(nodes))

        nodes = alg.get_neighbors(Node(4, 4))
        self.assertEqual(3, len(nodes))


