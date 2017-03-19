from pygame.sprite import Sprite, collide_rect
from pygame.image import load

SPEED = 7
GRAVITY = 0.4

class Wizard(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/warrior.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.x_vel = 0
        self.y_vel = 0
        self.onGround = False
        self.rect.x = x
        self.rect.y = y

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

    def collide(self, ground):
        for pl in ground:
            if collide_rect(self, pl):
                if self.y_vel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.y_vel = 0

