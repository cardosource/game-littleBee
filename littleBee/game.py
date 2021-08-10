from obj import Obj, Bee, Text
import random

class Game:

    def __init__(self):
        self.bg = Obj('assets/bg.png', 0, 0)
        self.bg2 = Obj('assets/bg.png', 0, -640)

        self.spider = Obj('assets/spider1.png', random.randrange(0,300), -50)
        self.florwer = Obj('assets/florwer1.png', random.randrange(0, 300), -50)
        self.bee = Bee('assets/bee1.png', 150, 600)

        self.change_scene = False
        self.score = Text(120, "0")
        self.lifes = Text(60, "3")




    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.spider.drawing(window)
        self.florwer.drawing(window)
        self.bee.drawing(window)
        self.score.draw(window, 160, 50)
        self.lifes.draw(window, 50, 50)


    def update(self):
        self.mov_bg()
        self.spider.anim("spider", 10, 5)
        self.florwer.anim("florwer", 8, 3)
        self.move_spiders()
        self.move_florwer()
        self.bee.anim("bee", 2, 5)
        self.bee.colisao(self.spider.group, "Spider")
        self.bee.colisao(self.florwer.group, "Flower")
        self.gameOver()
        self.score.update(str(self.bee.pts))
        self.lifes.update(str(self.bee.life))
    def mov_bg(self):
        self.bg.sprite.rect[1] += 6
        self.bg2.sprite.rect[1] += 6

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = 640



    def move_florwer(self):
        self.florwer.sprite.rect[1] += 3

        if self.florwer.sprite.rect[1] > 500:
            self.florwer.sprite.kill()
            # print("morreu")
            self.florwer = Obj('assets/florwer1.png', random.randrange(0, 300), -50)

    def gameOver(self):
        if self.bee.life <= 0:
            self.change_scene = True


    def move_spiders(self):

        if self.bee.pts < 5:
            print("nivel 1 ",self.bee.pts)
            self.spider.sprite.rect[1] += 5
        if self.bee.pts  >= 5 :
            print("nivel 2 ",self.bee.pts)
            self.spider.sprite.rect[1] += 10
        if self.bee.pts  >= 10 :
            print("nivel 3",self.bee.pts)
            self.spider.sprite.rect[1] += 15

        if self.bee.pts  >= 15 :
            print("nivel 4 ",self.bee.pts)
            self.spider.sprite.rect[1] += 20


        
        if self.spider.sprite.rect[1] > 500:
            self.spider.sprite.kill()
            # print("morreu")
            self.spider = Obj('assets/spider1.png', random.randrange(0,300), -50)
