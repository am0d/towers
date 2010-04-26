import pygame
import util

tower_sprites = [pygame.image.load('data/towers/firetower.png')]

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, color=util.blue):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.image = pygame.Surface([40, 40])
        self._color = color
        self.image.fill(self._color)

    def draw(self, screen):
        return screen.blit(self.image, self.rect)

    def set_pos(self, x, y):
        self.rect.left = x
        self.rect.top = y


class WaterTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y)

class FireTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y, util.red)
        self.image = tower_sprites[0]
        self.rect.size = self.image.get_rect().size

class EarthTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y, util.green)
