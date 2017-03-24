from sys import exit
import pygame
from my_gui.PyGame.RPG.heros import Wizard
from pygame.locals import *
from my_gui.PyGame.RPG.make_level import create_level


class InitGame:
    def __init__(self):
        # Set display
        pygame.init()
        self.screen = pygame.display.set_mode((1400, 900), FULLSCREEN)
        pygame.display.set_caption("Battle")
        # Sprite group
        self.block_group = pygame.sprite.Group()
        self.all_elements = pygame.sprite.Group()
        self.player1 = pygame.sprite.Group()
        self.player2 = pygame.sprite.Group()
        # Skill group
        self.player1_skill_group = pygame.sprite.Group()
        self.player2_skill_group = pygame.sprite.Group()
        # General loop
        self.start_game()

    def start_game(self):
        # Time
        self.clock = pygame.time.Clock()
        # Player 1 trigger
        self.player1_left = False
        self.player1_right = False
        # Player 2 trigger
        self.player2_left = False
        self.player2_right = False
        # Create player 1
        self.hero_player1 = Wizard(700, 350, self.screen)
        self.player1.add(self.hero_player1)
        self.all_elements.add(self.hero_player1)
        # Create player 2
        self.hero_player2 = Wizard(700, 350, self.screen)
        self.player2.add(self.hero_player2)
        self.all_elements.add(self.hero_player2)
        # Create bottom
        create_level(self.all_elements, self.block_group)
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)

                # Player KEYDOWN
                if event.type == KEYDOWN:

                    # Player 1 control
                    if event.key == K_a:
                        self.player1_left = True
                    if event.key == K_d:
                        self.player1_right = True
                    if event.key == K_w:
                        self.hero_player1.jump()
                    if event.key == K_SPACE:
                        self.hero_player1.attack(self.hero_player2)
                    if event.key == K_1:
                        self.hero_player1.activation_skill(0, self.player1_skill_group, self.screen, self.all_elements)
                    if event.key == K_2:
                        self.hero_player1.activation_skill(1, self.player1_skill_group, self.screen, self.all_elements)

                    # player 2 control
                    if event.key == K_LEFT:
                        self.player2_left = True
                    if event.key == K_RIGHT:
                        self.player2_right = True
                    if event.key == K_UP:
                        self.hero_player2.jump()
                    if event.key == K_KP1:
                        self.hero_player2.activation_skill(0, self.player2_skill_group, self.screen, self.all_elements)
                    if event.key == K_KP2:
                        self.hero_player2.activation_skill(1, self.player2_skill_group, self.screen, self.all_elements)
                    if event.key == K_KP0:
                        self.hero_player2.attack(self.hero_player1)

                # Player KEYUP
                if event.type == KEYUP:

                    # Player 1 control
                    if event.key == K_a:
                        self.player1_left = False
                        self.hero_player1.x_vel = 0
                    if event.key == K_d:
                        self.player1_right = False
                        self.hero_player1.x_vel = 0

                    # Player 2 control
                    if event.key == K_LEFT:
                        self.player2_left = False
                        self.hero_player2.x_vel = 0
                    if event.key == K_RIGHT:
                        self.player2_right = False
                        self.hero_player2.x_vel = 0

            # Background color
            self.screen.fill((80,114,153))
            # Draw all
            self.all_elements.draw(self.screen)
            # Draw player 1
            self.hero_player1.update(self.player1_left, self.player1_right, self.block_group)
            # Draw player 2
            self.hero_player2.update(self.player2_left, self.player2_right, self.block_group)
            # FPS
            self.clock.tick(70)
            # Draw screen
            pygame.display.flip()


if __name__ == '__main__':
    game = InitGame()