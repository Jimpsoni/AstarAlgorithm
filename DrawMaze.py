import pygame as pg

from AStar import Node, AStar
from Window import Window

"""
This is probably going to be removed and merged with GUI.py
"""


class DrawingBoard(Window):
    def __init__(self, width, height, board: list[list[Node]], title: str = "Drawing board"):
        super().__init__(width, height, title)
        self.board = board

        # Colors
        self.wall_color = pg.color.Color(16, 38, 68)
        self.path_color = pg.color.Color(255, 255, 255)

        self.between_tiles = 1
        self.board_height = len(self.board[0])
        self.board_width = len(self.board)

        self.tile_width = self.height / self.board_width - 2 * self.between_tiles
        self.tile_height = self.height / self.board_height - 2 * self.between_tiles

    def drawing_mode(self):
        drawing = False
        running = True
        draw_walls = True

        while running:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    drawing = True
                    x, y = self.get_node_from_coordinates(pg.mouse.get_pos())
                    draw_walls = self.board[y][x].traversable
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    drawing = False

                if event.type == pg.QUIT:
                    running = False

            if drawing:
                x, y = self.get_node_from_coordinates(pg.mouse.get_pos())
                node = self.board[y][x]
                if node.traversable == draw_walls:
                    color = self.wall_color if draw_walls else self.path_color
                    self.draw_tile(x, y, color)
                    self.board[y][x].change_traversable()

            pg.display.update()

    def draw_tile(self, x: float, y: float, color: pg.color) -> None:
        """ Draws a single tile """
        x_coord = self.between_tiles + (self.tile_width + 2 * self.between_tiles) * x
        y_coord = self.between_tiles + (self.tile_width + 2 * self.between_tiles) * y
        pg.draw.rect(self.screen, color, (x_coord, y_coord, self.tile_width, self.tile_height))

    def draw_board(self):
        """ Draws the board """
        for i in range(self.board_height):
            for j in range(self.board_width):
                self.draw_tile(i, j, self.path_color)

    def get_node_from_coordinates(self, coordinates):
        x_coord = coordinates[0] // (self.tile_width + 2 * self.between_tiles)
        y_coord = coordinates[1] // (self.tile_height + 2 * self.between_tiles)
        return int(x_coord), int(y_coord)

    def get_board(self):
        return self.board


if __name__ == "__main__":
    maze = AStar(Node(1, 1), Node(49, 49), 50, 50).make_board()
    b = DrawingBoard(600, 600, maze, "Draw a maze")
    b.show_display()
    b.draw_board()
    b.drawing_mode()
