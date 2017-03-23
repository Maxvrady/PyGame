from pygame.sprite import Sprite
from pygame import Surface
from pygame.image import load


class BottomPlatform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/ground/stage0.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class UpPlatform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/ground/hell_platform.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
