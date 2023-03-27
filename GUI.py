import pygame as pg
import time
from Algorithm import AStar, Node

pg.init()

# ===============================================
#              Variables

# Screen, width and height
WIDTH, HEIGHT = 1200, 900
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("A* path solving algorithm")

# All the colors
checked = pg.color.Color(243, 62, 62)
nodes = pg.color.Color(84, 212, 72)
unchecked = pg.color.Color(255, 255, 255)
start_point_color = pg.color.Color(230, 140, 10)
end_point_color = pg.color.Color(148, 13, 40)
not_traversable = pg.color.Color(16, 38, 68)

# init the game
game = AStar(Node(0, 0), Node(49, 49), 50, 50)

# Everything needed to draw the tiles to screen
start_point = WIDTH - HEIGHT
between_tiles = 1

tile_width = HEIGHT / game.width - 2 * between_tiles
tile_height = HEIGHT / game.height - 2 * between_tiles


# ===============================================
#              Functions

def draw_tile(x, y, color):
    """ Draws a single tile """
    x_coord = start_point + between_tiles + (tile_width + 2 * between_tiles) * x
    y_coord = between_tiles + (tile_width + 2 * between_tiles) * y
    pg.draw.rect(screen, color, (x_coord, y_coord, tile_width, tile_height))


def set_up():
    """
    Sets up the screen, draws rectangles which represents the tiles on game board
    """
    # Draw all the tiles
    for i in range(0, game.height):
        for j in range(0, game.width):
            draw_tile(i, j, unchecked)

    # Draw all non-traversable tiles
    for row in game.board:
        for node in row:
            if not node.traversable:
                draw_tile(node.x, node.y, not_traversable)

    # Draw start and end point
    draw_tile(game.start.x, game.start.y, start_point_color)
    draw_tile(game.end.x, game.end.y, end_point_color)


def draw_route(shortest_route):
    """ Draws the final route to destination """
    color = pg.color.Color(155, 155, 155)
    for n in shortest_route:
        draw_tile(n.x, n.y, color)

    pg.display.update()


def draw_screen():
    """
    Gets the checked nodes and current nodes from Astar class and draws them
    """
    for n in game.nodes:
        draw_tile(n.x, n.y, nodes)

    for n in game.checked:
        draw_tile(n.x, n.y, checked)

    pg.display.update()


if __name__ == "__main__":
    running = True

    # Create a map
    game.board[1][1].traversable = False
    game.board[1][2].traversable = False
    game.board[2][3].traversable = False
    game.board[3][3].traversable = False
    game.board[4][3].traversable = False
    game.board[1][4].traversable = False

    set_up()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

        # When game iteration returns something else than none
        # it has found the path
        path = game.iteration()
        if path is not None:
            set_up()
            draw_route(path)
            time.sleep(3)
            break

        # Draws everything on screen
        draw_screen()

        time.sleep(0.1)
