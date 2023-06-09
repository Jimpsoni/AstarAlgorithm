from AStar import AStar
from Algorithm import Algorithm
from Node import Node

try:
    import pygame as pg
except ImportError as e:
    print("Couldn't import " + e.name)
    import pygame as pg


class visualizer:
    # All the colors we need
    nodes = pg.color.Color(84, 212, 72)
    unchecked = pg.color.Color(255, 255, 255)
    checked = pg.color.Color(228, 79, 79)
    start_point_color = pg.color.Color(230, 140, 10)
    end_point_color = pg.color.Color(148, 13, 40)
    not_traversable = pg.color.Color(16, 38, 68)

    between_tiles = 1

    game = AStar(Node(0, 0), Node(49, 49), 50, 50)

    def __init__(self, width: int, height: int, title: str, game: AStar) -> None:
        self.screen = None
        self.title = title
        pg.init()

        self.buttons = []  # Stores all the buttons we have
        self.game = game

        self.width, self.height = width, height
        self.start_point = self.width - self.height
        self.tile_width = self.height / self.game.width - 2 * self.between_tiles
        self.tile_height = self.height / self.game.height - 2 * self.between_tiles
        self.DELAY = 0

    def draw_tile(self, x: float, y: float, color: pg.color) -> None:
        """ Draws a single tile """
        x_coord = self.start_point + self.between_tiles + (self.tile_width + 2 * self.between_tiles) * x
        y_coord = self.between_tiles + (self.tile_width + 2 * self.between_tiles) * y
        pg.draw.rect(self.screen, color, (x_coord, y_coord, self.tile_width, self.tile_height))

    def show_display(self):
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.title)

    def set_up(self) -> None:
        """
        Sets up the screen, draws rectangles which represents the tiles on game board
        """
        # Draw all the tiles
        for i in range(0, self.game.height):
            for j in range(0, self.game.width):
                self.draw_tile(i, j, self.unchecked)

        # Draw all non-traversable tiles
        for row in self.game.board:
            for node in row:
                if not node.traversable:
                    self.draw_tile(node.x, node.y, self.not_traversable)

        # Draw start and end point
        self.draw_tile(self.game.start.x, self.game.start.y, self.start_point_color)
        self.draw_tile(self.game.end.x, self.game.end.y, self.end_point_color)

        self.draw_buttons()

        pg.display.update()

    def draw_buttons(self):
        run = Button(150, 75, 50, 100)
        run.set_text("Start solving")

        settings = Button(150, 75, 50, 250)
        settings.set_text("Settings")

        run.set_action(self.solve)

        self.buttons.append(run)
        self.buttons.append(settings)

        pg.draw.rect(self.screen, pg.color.Color(255, 255, 255), run)
        pg.draw.rect(self.screen, pg.color.Color(255, 255, 255), settings)

    def draw_route(self, shortest_route: list[Node]) -> None:
        """ Draws the final route to destination """
        color = pg.color.Color(243, 101, 31)
        for n in shortest_route:
            self.draw_tile(n.x, n.y, color)

        pg.display.update()

    def draw_screen(self) -> None:
        """
        Gets the checked nodes and current nodes from Astar class and draws them
        """
        # Draw all the neighbors
        for n in self.game.nodes:
            self.draw_tile(n.x, n.y, self.nodes)

        # Draw all the checked tiles
        for n in self.game.checked:
            self.draw_tile(n.x, n.y, self.checked)

        pg.display.update()

    def create_maze(self):


    def solve(self):
        """
        Solves the shortest path
        :return:
        """
        running = True

        self.set_up()

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    break

            # When game iteration returns something else than none
            # it has found the path
            path = self.game.iteration()
            if path is not None:
                self.set_up()
                self.draw_route(path)
                pg.time.wait(15000)
                break

            # Draws everything on screen
            self.draw_screen()

            # Set a small delay, so it's easier to follow the progress
            pg.time.wait(self.DELAY)

    def get_node_from_coordinates(self, coordinates):
        x_coord = (coordinates[0] - self.start_point) // (self.tile_width + 2 * self.between_tiles)
        y_coord = coordinates[1] // (self.tile_height + 2 * self.between_tiles)

        if x_coord < 0:
            x_coord = 0
        if x_coord > self.game.width - 1:
            x_coord = self.game.width - 1

        if y_coord < 0:
            y_coord = 0
        if y_coord > self.game.height - 1:
            y_coord = self.game.height - 1

        return int(x_coord), int(y_coord)

    def check_button_collisions(self, x, y):
        for button in self.buttons:
            if button.check_collision(x, y):
                button.exe()
                return

    def mainloop(self):
        """
        Listens when mouse is clicked and then changes traversability of nodes according to its
        coordinates

        :return: None
        """
        drawing = False
        running = True
        draw_walls = True

        board = Algorithm.make_board(len(self.game.board[0]), len(self.game.board))

        while running:
            for event in pg.event.get():

                x, y = pg.mouse.get_pos()

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and x >= self.start_point:
                    drawing = True
                    x, y = self.get_node_from_coordinates(pg.mouse.get_pos())
                    draw_walls = board[y][x].traversable
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    drawing = False
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and x < self.start_point:
                    self.check_button_collisions(x, y)

                if event.type == pg.QUIT:
                    running = False

            if drawing:
                x, y = self.get_node_from_coordinates(pg.mouse.get_pos())
                node = board[y][x]
                if node.traversable is draw_walls:
                    color = self.not_traversable if draw_walls else self.nodes
                    self.draw_tile(x, y, color)
                    board[y][x].change_traversable()

            pg.display.update()


class Button(pg.Rect):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.action = None

    def check_collision(self, x, y):
        hit_x = (self.x <= x < self.x + self.width)
        hit_y = (self.y <= y < self.y + self.height)
        return hit_x and hit_y

    def set_text(self, text):
        # TODO
        center_x = self.width // 2
        center_y = self.height // 2

        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render('GeeksForGeeks', True, pg.color.Color(0, 0, 0))

        return text

    def set_action(self, action):
        self.action = action

    def exe(self):
        self.action()

    def set_highlight_decoration(self):
        # TODO
        pass


if __name__ == "__main__":
    problem = AStar(Node(0, 0), Node(49, 49), 50, 50)
    visualizer = visualizer(1200, 900, "A* algorithm", problem)
    visualizer.show_display()
    visualizer.set_up()
    visualizer.drawing_mode()
    visualizer.run()
