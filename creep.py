import pygame
import math

import util

class Creep(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15, 15])
        self.image.fill(util.purple)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.direction = math.radians(305.0)
        self.speed = 8.0
        self.x = float(self.rect.left)
        self.y = float(self.rect.top)

	self._path = [(0, 0)]

    def update(self, type, arguments):
        functions = {'time': self.time,
                     'path': self.path}
        return functions[type](*arguments)

    def time(self, timediff):
        delta = timediff / 1000.0
        self.x += self.speed * delta * math.cos(self.direction)
        self.y += self.speed * delta * math.sin(self.direction)
        self.rect.topleft = (int(self.x), int(self.y))

    def path(self, world, node):
	if node in self._path:
            self._path = world.get_new_path(self.rect.topleft)
        goal = self._path[0]
        self.direction = math.atan2(goal[0] - self.rect.top, goal[1] - self.rect.left)

    def draw(self, screen):
        return screen.blit(self.image, self.rect)
