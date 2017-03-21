from pygame.sprite import Sprite
from pygame import Surface
import pyganim
from .animations import FAIR_BALL_LEFT, FAIR_BALL_RIGHT

SKILL_SPEED = 20


class BluFairBall(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = Surface((100, 38))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.x_vel = 0
        self.attacks = False

        self.AnimLeft = pyganim.PygAnimation(FAIR_BALL_LEFT)
        self.AnimLeft.play()

        self.AnimRight = pyganim.PygAnimation(FAIR_BALL_RIGHT)
        self.AnimRight.play()

    def update(self, x, y):
        if not self.attacks:
            self.rect.x = x
            self.rect.y = y
        else:
            if self.x_vel > 0:
                self.rect.x += SKILL_SPEED
            if self.x_vel < 0:
                self.rect.x += -SKILL_SPEED

    def attack(self, hero_xvel):
        if not self.attacks:
            self.x_vel = hero_xvel
            self.attacks = True
