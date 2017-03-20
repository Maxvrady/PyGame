from pygame.sprite import Sprite
from pygame import Surface
import pyganim
from .animations import FAIR_BALL_PASS

SKILL_SPEED = 15


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

        self.Anim = pyganim.PygAnimation(FAIR_BALL_PASS)
        self.Anim.play()

    def update(self, x, y):
        self.image.fill((255, 255, 255))
        self.Anim.blit(self.image)
        if not self.attacks:
            self.rect.x = x
            self.rect.y = y
        else:
            self.rect.x += self.x_vel
            if self.x_vel > 0 and self.rect.right > 1400:
                self.attacks = False
            if self.x_vel < 0 and self.rect.x < 0:
                self.attacks = False
            if self.x_vel == 0:
                self.attacks = False

    def attack(self, hero_xvel):
        if not self.attacks:
            self.x_vel = hero_xvel
            self.attacks = True
