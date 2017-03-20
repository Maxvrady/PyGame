from sys import exit
import pygame
from my_gui.PyGame.RPG.heros import Wizard
from pygame.locals import *
from my_gui.PyGame.RPG.make_level import create_bottom


class InitGame:
    def __init__(self):
        # Set display
        pygame.init()
        self.screen = pygame.display.set_mode((1400, 900), FULLSCREEN)
        pygame.display.set_caption("Battle")
        # Sprite group
        self.block_group = pygame.sprite.Group()
        self.all_elements = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group()
        # Skill group
        self.skill_group = pygame.sprite.Group()
        # General loop
        self.start_game()

    def start_game(self):
        self.clock = pygame.time.Clock()
        # Class trigger
        self.left = False
        self.right = False
        # Create wizard
        self.wizard = Wizard(10, 350)
        self.hero_group.add(self.wizard)
        self.all_elements.add(self.wizard)
        # Create bottom
        create_bottom(self.all_elements, self.block_group)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.left = True
                    if event.key == K_RIGHT:
                        self.right = True
                    if event.key == K_UP:
                        self.wizard.jump()
                    if event.key == K_SPACE:
                        self.wizard.attack()
                    if event.key == K_1:
                        self.wizard.activation_skill(0, self.skill_group)

                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.left = False
                        self.wizard.x_vel = 0
                    if event.key == K_RIGHT:
                        self.right = False
                        self.wizard.x_vel = 0

            # Background color
            self.screen.fill((80,114,153))
            # Draw all
            self.skill_group.draw(self.screen)
            self.all_elements.draw(self.screen)
            self.wizard.update(self.left, self.right)
            self.wizard.collide_y(self.block_group)
            self.wizard.collide_x(self.block_group)
            self.clock.tick(70)
            pygame.display.flip()


if __name__ == '__main__':
    InitGame()