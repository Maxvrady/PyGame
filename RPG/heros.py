from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from .animations import WIZARD_LEFT, WIZARD_RIGHT, WIZARD_PASS
import pyganim
from .skills import BluFairBall

JUMP_SPEED = 10
SPEED = 7
GRAVITY = 0.4


class BaseClass(Sprite):
    def __init__(self,x, y, skill):
        Sprite.__init__(self)
        self.image = Surface((49, 80))
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.x_vel = 0
        self.y_vel = 0
        self.onGround = False
        self.rect.x = x
        self.rect.y = y
        # Skill
        self.skill_active = None
        self.skill = skill
        # Left animation
        self.moveLeft_anim = pyganim.PygAnimation(WIZARD_LEFT)
        self.moveLeft_anim.play()
        # Right animation
        self.moveRight_anim = pyganim.PygAnimation(WIZARD_RIGHT)
        self.moveRight_anim.play()
        # Stay animation
        self.passAnim = pyganim.PygAnimation(WIZARD_PASS)
        self.passAnim.play()

    def update(self, left, right):
        # Move
        if left:
            self.x_vel = -SPEED
            self.rect.x += self.x_vel
        if right:
            self.x_vel = SPEED
            self.rect.x += self.x_vel
        if not self.onGround:
            self.y_vel += GRAVITY
            self.rect.y += self.y_vel
        # Animation
        if self.x_vel < 0:
            self.moveLeft_anim.blit(self.image)
        if self.x_vel > 0:
            self.moveRight_anim.blit(self.image)
        if self.x_vel == 0:
            self.passAnim.blit(self.image)
        # Update skill
        if self.skill_active:
            self.skill_active.update(self.rect.x, self.rect.y)

    def collide_x(self, ground):
        for pl in ground:
            if collide_rect(self, pl):
                if self.x_vel > 0:
                    self.rect.right = pl.rect.left
                if self.x_vel < 0:
                    self.rect.left = pl.rect.right

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
                if self.y_vel < 0:
                    self.rect.top = pl.rect.bottom
                    self.onGround = False

    def jump(self):
        if self.onGround:
            self.y_vel = -JUMP_SPEED
            for i in range(3):
                self.rect.y += self.y_vel
        self.onGround = False

    def activation_skill(self, key, skill_group):
        self.skill_active = self.skill[key]
        if self.skill_active not in skill_group:
            skill_group.add(self.skill_active)

    def attack(self):
        if self.skill_active:
            self.skill_active.attack(self.x_vel)

from .skills import BluFairBall


class Wizard(BaseClass):
    def __init__(self, x, y):
        fairball = BluFairBall()
        BaseClass.__init__(self, x, y, [fairball])

