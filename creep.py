import pygame
import util

class Creep(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15, 15])
        self.image.fill(util.purple)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, time):
        pass

    def draw(self, screen):
        return screen.blit(self.image, self.rect)
