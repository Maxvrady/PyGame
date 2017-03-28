from pygame.sprite import Sprite
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


class TreeOne(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('RPG/item/ground/tree0.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 100


class TreeTwo(TreeOne):
    def __init__(self, x, y):
        TreeOne.__init__(self, x, y - 50)
        self.image = load('RPG/item/ground/tree1.png')
        self.image.set_colorkey((255, 255, 255))


class Bottom(HellCenter):
    def __init__(self, x, y):
        HellCenter.__init__(self, x, y)
        self.image = load('RPG/item/ground/bottom.png')
        # self.image.set_colorkey((255, 255, 255))


class Top(Bottom):
    def __init__(self, x, y):
        Bottom.__init__(self, x, y)
        self.image = load('RPG/item/ground/Top.png').convert()
        self.image.set_colorkey((255, 255, 255))


class Table(TreeOne):
    def __init__(self, x, y):
        TreeOne.__init__(self, x, y + 90)
        self.image = load('RPG/item/ground/Table0.png')
        self.image.set_colorkey((255, 255, 255))
