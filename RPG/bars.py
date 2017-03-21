from pygame.image import load
from pygame.sprite import Sprite


class IconOfSpell(Sprite):
    def __init__(self, image):
        Sprite.__init__(self)
        self.image = load(image)
        self.rect = self.image.get_rect()

    def update(self, x, y, skill):
        self.image = load(skill.icon_path)
        self.rect.x = x
        self.rect.y = y - 60
        self.image.blit(self.image, [0,0])
