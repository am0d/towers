import math
import pygame

from tower import Tower
import util

class World:
    def __init__(self, width, height, res, screen):
        self.width = int(math.floor(width / res)*res)
        self.height = int(math.floor(height / res)*res)
        self.res = res
        self._grid = [[None] * width for i in range(0, height)]

        # the visible map
        self.__grid_background = pygame.Surface((self.width+1, self.height+1))
        self.__init_map(self.__grid_background)
        screen.blit(self.__grid_background, (0, 0))

        # the towers
        self._towers = pygame.sprite.Group()

    def add_tower(self, x, y, tower):
        try:
            row = int(math.floor(y / self.res))
            col = int(math.floor(x / self.res))

            self._grid[row][col] = tower
            pos_x = x - (x % self.res)
            pos_y = y - (y % self.res)
            tower.set_pos(pos_x, pos_y)

            self._towers.add(tower)
        except IndexError:
            print row, col

    def draw(self, screen):
        screen.blit(self.__grid_background, (0, 0))
        self._towers.draw(screen)

    def draw_map(self, screen, pos):
        return screen.blit(self.__grid_background, pos.topleft, pos)
                    
    def __init_map(self, screen):
        #max_x = self.width * self.res + 1
        #max_y = self.height * self.res + 1
        max_x, max_y = screen.get_size()
        
        screen.lock()
        for x in range(0, max_x):
            pygame.draw.line(screen, util.brown, (x*self.res, 0), (x*self.res, max_y-1))
        for y in range(0, max_y):
            pygame.draw.line(screen, util.brown, (0, y*self.res), (max_x-1, y*self.res))

        screen.unlock()
