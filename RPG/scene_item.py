from pygame.sprite import Sprite
from pygame import Surface
from pygame.image import load


class HellRight(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/ground/hell_right.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HellCenter(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/ground/hell_center.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HellLeft(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/ground/hell_left.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Tree(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/ground/tree0.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
