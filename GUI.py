import pygame as pg
import time
from Algorithm import AStar, Node

pg.init()

# ===============================================
#              Variables

# Screen width and height
WIDTH, HEIGHT = 600, 600

checked = pg.color.Color(243, 62, 62)
nodes = pg.color.Color(84, 212, 72)
unchecked = pg.color.Color(255, 255, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("A* path solving algorithm")

game = AStar(Node(0, 0), Node(4, 4), 5, 5)


# ===============================================
#              Functions


def set_up():
    """
    Sets up the screen, draws rectangles which represents the tiles on game board
    """
    x, y, width, height = 100, 100, 100, 100

    for i in range(0, 5):
        for j in range(0, 5):
            pg.draw.rect(screen, pg.color.Color(255, 255, 255), ((x + 20) * j + 50, (y + 20) * i + 50, width, height))


def draw_route(shortest_route):
    for n in shortest_route:
        pg.draw.rect(screen, pg.color.Color(155, 155, 155), ((100 + 20) * n.x + 50, (100 + 20) * n.y + 50, 100, 100))
    pg.display.update()


def draw_screen():
    """
    Gets the checked nodes and current nodes from Astar class and draws them
    """
    for n in game.nodes:
        pg.draw.rect(screen, nodes, ((100 + 20) * n.x + 50, (100 + 20) * n.y + 50, 100, 100))

    for n in game.checked:
        pg.draw.rect(screen, checked, ((100 + 20) * n.x + 50, (100 + 20) * n.y + 50, 100, 100))

    pg.display.update()


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
        draw_route(path)
        time.sleep(2)
        break

    # Updates screen
    draw_screen()

    time.sleep(0.5)
