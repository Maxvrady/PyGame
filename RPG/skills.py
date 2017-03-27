from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from pygame.image import load
import pyganim
from .animations import FAIR_BALL_LEFT, FAIR_BALL_RIGHT, DARK_BALL, EXPLODE, ARROW_LEFT, ARROW_RIGHT



class BluFairBall(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.SKILL_SPEED = 20
        self.image = Surface((100, 38))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.x_vel = 0
        self.attacks = False
        self.icon_path = 'RPG/item/wizard/icon/stage0.png'
        # Left anim.
        self.AnimLeft = pyganim.PygAnimation(FAIR_BALL_LEFT)
        self.AnimLeft.play()
        # Right anim.
        self.AnimRight = pyganim.PygAnimation(FAIR_BALL_RIGHT)
        self.AnimRight.play()
        # Explode animation
        self.explodeAnim = pyganim.PygAnimation(EXPLODE)
        self.explodeAnim.play()
        # Target
        self.target = None
        # Damage
        self.damage = 20

    def update(self, x, y):
        if not self.attacks:
            self.rect.x = x
            self.rect.y = y
            return False
        else:
            self.image.fill((80,114,153))
            if self.target:
                if collide_rect(self, self.target):
                    self.image.set_colorkey((255, 255, 255))
                    self.explodeAnim.blit(self.image)
                    self.target.hero_damage(self.damage)
                    self.attacks = False

            if self.x_vel > 0:
                self.rect.x += self.SKILL_SPEED
                self.AnimRight.blit(self.image)
            if self.x_vel < 0:
                self.rect.x += -self.SKILL_SPEED
                self.AnimLeft.blit(self.image)

            if self.rect.right > 1400:
                self.attacks = False
            if self.rect.left < 0:
                self.attacks = False
            return True

    def attack(self, hero_xvel, target):
        self.target = target
        if hero_xvel == 0:
            return False
        if not self.attacks:
            self.x_vel = hero_xvel
            self.attacks = True


class DarkBall(BluFairBall):
    def __init__(self):
        BluFairBall.__init__(self)
        self.image = Surface((50, 53))
        self.image.set_colorkey((255, 255, 255))
        self.icon_path = 'RPG/item/wizard/icon/stage1.png'
        self.AnimLeft = pyganim.PygAnimation(DARK_BALL)
        self.AnimLeft.play()

        self.AnimRight = pyganim.PygAnimation(DARK_BALL)
        self.AnimRight.play()


class Arrow(BluFairBall):
    def __init__(self):
        BluFairBall.__init__(self)
        self.image = Surface((50, 8))
        self.image.set_colorkey((255, 255, 255))
        self.SKILL_SPEED += 10
        self.icon_path = 'RPG/item/archer/icon/stage0.png'
        self.AnimLeft = pyganim.PygAnimation(ARROW_LEFT)
        self.AnimLeft.play()

        self.AnimRight = pyganim.PygAnimation(ARROW_RIGHT)
        self.AnimRight.play()