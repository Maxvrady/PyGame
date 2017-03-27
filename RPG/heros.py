from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from .animations import WIZARD_LEFT, WIZARD_RIGHT, WIZARD_PASS, DEAD, ARCHER_LEFT, ARCHER_RIGHT, ARCHER_PASS
from .bars import IconOfSpell
from pygame.font import SysFont
import pyganim
from .skills import BluFairBall, DarkBall, Arrow
from pygame.image import load


JUMP_SPEED = 10
SPEED = 7
GRAVITY = 0.4


class BaseClass(Sprite):
    def __init__(self,x, y, skill, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.image = Surface((49, 80))
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.x_vel = 0
        self.y_vel = 0
        self.rect.x = x
        self.rect.y = y
        # All group
        self.all_group = None
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
        # Dead animation
        self.deadAnim = pyganim.PygAnimation(DEAD)
        self.deadAnim.play()
        # Health
        self.health = 100
        self.dead = False
        # Jump trigger
        self.jump_stage = False
        # On ground
        self.onGround = False
        # Font for display health
        self.my_font = SysFont("None", 20, True)

    def update(self, left, right, block_group):
        if not self.dead:
            # Render font
            self.render = self.my_font.render(str(self.health), True, (209,33,34))
            # Move
            if left:
                self.x_vel = -SPEED
            if right:
                self.x_vel = SPEED
            if not(left or right):
                self.x_vel = 0
            if not self.jump_stage:
                if not self.onGround:
                    self.y_vel += GRAVITY
            # Jump
            if not self.jump_stage:
                self.onGround = False
            # Update hero
            self.rect.y += self.y_vel
            self.collide_y(block_group)
            self.rect.x += self.x_vel
            self.collide_x(block_group)
            # Animation
            if self.screen:
                self.screen.blit(self.render, (self.rect.x + 15, self.rect.y - 80))
            if self.x_vel < 0:
                self.moveLeft_anim.blit(self.image)
            if self.x_vel > 0:
                self.moveRight_anim.blit(self.image)
            if self.x_vel == 0:
                self.passAnim.blit(self.image)
            if self.spell_icon:
                self.spell_icon.update(self.rect.x, self.rect.y, self.skill_active)
            # Update skill
            if self.skill_active:
                if self.skill_active.update(self.rect.x, self.rect.y):
                    self.skill_group.draw(self.screen)
        else:
            self.image.fill((80, 114, 153))
            self.deadAnim.blit(self.image)

    def collide_x(self, ground):
        for pl in ground:
            if collide_rect(self, pl):
                if self.x_vel > 0:
                    self.rect.right = pl.rect.left
                if self.x_vel < 0:
                    self.rect.left = pl.rect.right

        if self.x_vel > 0 and self.rect.x > 1350:
            self.rect.x = 1350
        if self.x_vel < 0 and self.rect.x < 0:
            self.rect.x = 0

    def collide_y(self, ground):
        for pl in ground:
            if collide_rect(self, pl):
                if self.y_vel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                if self.y_vel < 0:
                    self.rect.top = pl.rect.bottom
                    self.y_vel = 0

    def jump(self):
        if self.onGround:
            self.jump_stage = True
            self.y_vel = -JUMP_SPEED
            for i in range(5):
                self.rect.y += self.y_vel
            self.onGround = False
            self.jump_stage = False

    def hero_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead = True

    def activation_skill(self, key, skill_group, all_group):
        self.skill_active = self.skill[key]
        self.skill_group = skill_group
        self.all_group = all_group
        if not self.spell_icon:
            self.spell_icon = IconOfSpell(self.skill_active.icon_path)
        self.all_group.add(self.spell_icon)
        if not (self.skill_active == None):
            self.skill_group.empty()
            self.skill_group.add(self.skill_active)

    def attack(self, target):
        if self.skill_active:
            self.skill_active.attack(self.x_vel, target)


class Wizard(BaseClass):
    """Wizard class"""
    def __init__(self, x, y, screen):
        """Class skills"""
        fairball = BluFairBall()
        darkball = DarkBall()
        BaseClass.__init__(self, x, y, [fairball, darkball], screen)


class Archer(BaseClass):
    """Archer class"""
    def __init__(self, x, y, screen):
        """Class skills"""
        arrow = Arrow()
        darkball = DarkBall()
        BaseClass.__init__(self, x, y, [darkball, arrow], screen)

        # Left animation
        self.moveLeft_anim = pyganim.PygAnimation(ARCHER_LEFT)
        self.moveLeft_anim.play()
        # Right animation
        self.moveRight_anim = pyganim.PygAnimation(ARCHER_RIGHT)
        self.moveRight_anim.play()
        # Pass animation
        self.passAnim = pyganim.PygAnimation(ARCHER_PASS)
        self.passAnim.play()

