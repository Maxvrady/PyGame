from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from .animations import WIZARD_LEFT, WIZARD_RIGHT, WIZARD_PASS
from .bars import IconOfSpell
import pyganim
from .skills import BluFairBall, DarkBall
from pygame.image import load


JUMP_SPEED = 10
SPEED = 7
GRAVITY = 0.4


class BaseClass(Sprite):
    def __init__(self,x, y, skill):
        Sprite.__init__(self)
        self.screen = None
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
        self.skill_group = None
        # Display skill icon
        self.spell_icon = None
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
        if not self.spell_icon == None:
            self.spell_icon.update(self.rect.x, self.rect.y, self.skill_active)
        # Update skill
        if self.skill_active:
                if self.skill_active.update(self.rect.x, self.rect.y):
                    self.skill_group.draw(self.screen)

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

    def activation_skill(self, key, skill_group, screen, all_group):
        self.skill_active = self.skill[key]
        self.skill_group = skill_group
        self.spell_icon = IconOfSpell(self.skill_active.icon_path)
        all_group.add(self.spell_icon)
        self.screen = screen
        if not (self.skill_active == None):
            self.skill_group.empty()
            self.skill_group.add(self.skill_active)

    def attack(self):
        if self.skill_active:
            self.skill_active.attack(self.x_vel)


class Wizard(BaseClass):
    """Wizard class"""
    def __init__(self, x, y, screen):
        """Class skills"""
        fairball = BluFairBall()
        darkball = DarkBall()
        BaseClass.__init__(self, x, y, [fairball, darkball])

