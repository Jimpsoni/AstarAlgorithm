from Node import Node


class Algorithm:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = self.make_board(width, height)

    def get_neighbors(self, node, steps, validate):
        # TODO could this possibly be made faster?
        nodes = []  # Here we append all the neighbors

        if node.x + steps < len(self.board[0]):
            if validate(self.board[node.y][node.x + steps]):
                nodes.append(self.board[node.y][node.x + steps])

        if node.x - steps >= 0:
            if validate(self.board[node.y][node.x - steps]):
                nodes.append(self.board[node.y][node.x - steps])

        if node.y + steps < len(self.board):
            if validate(self.board[node.y + steps][node.x]):
                nodes.append(self.board[node.y + steps][node.x])

        if node.y - steps >= 0:
            if validate(self.board[node.y - steps][node.x]):
                nodes.append(self.board[node.y - steps][node.x])

        return nodes

    @staticmethod
    def make_board(width, height) -> list[list[Node]]:
        """
        :return: 2D list that has height amount of lists size of the width full of nodes.
        """
        return [[Node(i, j) for i in range(0, width)] for j in range(0, height)]

    def get_board(self):
        return self.board

    def print_board(self) -> None:
        for row in self.board:
            for node in row:
                print(str(node) + "  ", end="")
            print("\n")
