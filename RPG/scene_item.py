from pygame.sprite import Sprite
from pygame import Surface


class BottomPlatform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((50, 50))
        self.image.fill((180,168,154))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

