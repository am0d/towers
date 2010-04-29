import pygame
import util

def square(size, color):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf

tower_sprites = [square([39, 39], util.blue),
                 square([39, 39], util.red),
                 square([39, 39], util.green)]

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, image_number):
        pygame.sprite.Sprite.__init__(self)
        self.image = tower_sprites[image_number]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        return screen.blit(self.image, self.rect)

    def set_pos(self, x, y):
        self.rect.left = x
        self.rect.top = y


class WaterTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y, 0)

class FireTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y, 1)

class EarthTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y, 2)

class MouseTower(Tower):
    def __init__(self, x, y):
        Tower.__init__(self, x, y, 0)

    def set_tower_type(self, tower_type):
        self.image = tower_sprites[tower_type]
        self.rect.size = self.image.get_rect().size
