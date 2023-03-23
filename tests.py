import unittest
from Main import Node, AStar


class testNodeMethods(unittest.TestCase):
    def test_calculate_values(self):
        # Test hcost, gcost and fcost
        start, end, node = (1, 1), (5, 9), Node(2, 2)
        node.calculate_values(start, end)

        self.assertEqual(14, node.gcost)
        self.assertEqual(76, node.hcost)
        self.assertEqual(90, node.fcost)

        start, end, node = (5, 2), (2, 5), Node(2, 2)
        node.calculate_values(start, end)
        self.assertEqual(30, node.gcost)
        self.assertEqual(30, node.hcost)
        self.assertEqual(60, node.fcost)

