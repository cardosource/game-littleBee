import pygame
from obj import Obj
from menu import Menu, GameOver
from game import Game
class Main:

    def __init__(self, sizex, sizey, title):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)


        self.start_screen = Menu("assets/start.png")
        self.game = Game()
        self.gameOver = GameOver("assets/gameover.png")

        self.loop = True
        self.fps = pygame.time.Clock()


    def draw(self):

        if self.start_screen.change_scene == False:
            self.start_screen.draw(self.window)


        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()

        elif self.gameOver.change_scene  == False:
            self.gameOver.draw(self.window)
        else:
            self.start_screen.change_scene = False
            self.game.change_scene = False
            self.gameOver.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.start_screen.change_scene:
                 self.start_screen.events(events)

            elif not self.game.change_scene:
                 self.game.bee.mov_bee(events)
            else:
                self.gameOver.events(events)

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()

            pygame.display.update()


game = Main(360, 640, "Little bee")
game.update()
