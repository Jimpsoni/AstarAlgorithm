import pygame as pg


class Window:
    def __init__(self, width, height, title: str):
        pg.init()
        self.screen = None
        self.width = width
        self.height = height
        self.title = title
    
    def show_display(self):
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.title)

    @staticmethod
    def show():
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    running = False
        
        
        