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

node = Node(3, 3)
game = AStar(Node(0, 0), Node(3, 3), 4, 4)
print(game)


# ===============================================
#              Functions

def set_up():
    x, y, width, height = 100, 100, 100, 100

    for i in range(0, 4):
        for j in range(0, 4):
            pg.draw.rect(screen, pg.color.Color(255, 255, 255), ((x + 20) * j + 50, (y + 20) * i + 50, width, height))


def draw_screen():
    for n in game.nodes:
        pg.draw.rect(screen, nodes, ((100 + 20) * n.x + 50, (100 + 20) * n.y + 50, 100, 100))

    for n in game.checked:
        pg.draw.rect(screen, checked, ((100 + 20) * n.x + 50, (100 + 20) * n.y + 50, 100, 100))

    pg.display.update()


running = True
game.set_up()
game.board[1, 1] = 1
game.board[1, 2] = 1
set_up()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break

    if game.iteration() is not None:
        break

    draw_screen()

    time.sleep(1)
