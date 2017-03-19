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
        self.hero_group = pygame.sprite.Group()
        self.all_groud = pygame.sprite.Group()
        # General loop
        self.start_game()

    def start_game(self):
        self.clock = pygame.time.Clock()
        self.left = False
        self.right = False
        self.wizard = Wizard(10, 350)
        self.hero_group.add(self.wizard)
        create_bottom(self.all_groud)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.left = True
                    if event.key == K_RIGHT:
                        self.right = True

                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.left = False
                        self.wizard.x_vel = 0
                    if event.key == K_RIGHT:
                        self.right = False
                        self.wizard.x_vel = 0

            self.screen.fill((80,114,153))
            self.all_groud.draw(self.screen)
            self.wizard.update(self.left, self.right)
            self.wizard.collide_x()
            self.wizard.collide_y(self.all_groud)
            self.hero_group.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    InitGame()