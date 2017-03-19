from pygame.sprite import Sprite, collide_rect
from pygame import Surface
import pyganim

SPEED = 15
GRAVITY = 0.4


animation_delay = 1
animation_stay = [('RPG/item/pass_hero/pass_hero.png', animation_delay)]
animation_left = [('RPG/item/move_hero/move_left.png', animation_delay)]


class Wizard(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((64, 76))
        self.rect = self.image.get_rect()
        self.x_vel = 0
        self.y_vel = 0
        self.onGround = False
        self.rect.x = x
        self.rect.y = y

        self.pass_anim = pyganim.PygAnimation(animation_stay)
        self.pass_anim.play()

        self.left_anim = pyganim.PygAnimation(animation_left)
        self.left_anim.play()

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
            self.left_anim.blit(self.image)
        if self.x_vel > 0:
            self.pass_anim.blit(self.image)
        if self.x_vel == 0:
            self.pass_anim.blit(self.image)

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

