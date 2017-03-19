from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from .animations import WIZARD_LEFT, WIZARD_RIGHT
import pyganim

JUMP_SPEED = 10
SPEED = 7
GRAVITY = 0.4


class Wizard(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((49, 80))
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.x_vel = 0
        self.y_vel = 0
        self.onGround = False
        self.rect.x = x
        self.rect.y = y

        self.moveLeft_anim = pyganim.PygAnimation(WIZARD_LEFT)
        self.moveLeft_anim.play()

        self.moveRight_anim = pyganim.PygAnimation(WIZARD_RIGHT)
        self.moveRight_anim.play()

    def update(self, left, right):
        if left:
            self.x_vel = -SPEED
            self.rect.x += self.x_vel
        if right:
            self.x_vel = SPEED
            self.rect.x += self.x_vel
        if not self.onGround:
            self.y_vel += GRAVITY
            self.rect.y += self.y_vel

        if self.x_vel < 0:
            self.moveLeft_anim.blit(self.image)
        if self.x_vel > 0:
            self.moveRight_anim.blit(self.image)

    def collide_x(self):
        if self.x_vel > 0 and self.rect.x > 1300:
            self.rect.x = 1300
        if self.x_vel < 0 and self.rect.x < 0:
            self.rect.x = 0

    def collide_y(self, ground):
        for pl in ground:
            if collide_rect(self, pl):
                if self.y_vel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.y_vel = 0

    def jump(self):
        if self.onGround:
            self.y_vel = -JUMP_SPEED
            for i in range(3):
                self.rect.y += self.y_vel
        self.onGround = False
