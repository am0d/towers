import math
import pygame

from tower import Tower
import util

class World:
    def __init__(self, width, height, res, screen):
        self.width = int(math.floor(width / res)*res)
        self.height = int(math.floor(height / res)*res)
        self.grid_width = int(math.floor(width / res))
        self.grid_height = int(math.floor(height / res))
        self.res = res
        self._grid = [[None] * self.grid_width for i in range(0, self.grid_height)]

        # the visible map
        self.__grid_background = pygame.Surface((self.width+1, self.height+1))
        self.__init_map(self.__grid_background)
        screen.blit(self.__grid_background, (0, 0))

        # the towers
        self._towers = pygame.sprite.Group()

        # the creeps
        self._creeps = pygame.sprite.Group()

    def __init_map(self, screen):
        max_x, max_y = screen.get_size()

        screen.lock()
        for x in range(0, max_x):
            pygame.draw.line(screen, util.brown, (x*self.res, 0), (x*self.res, max_y-1))
            for y in range(0, max_y):
                pygame.draw.line(screen, util.brown, (0, y*self.res), (max_x-1, y*self.res))
                screen.unlock()

    def add_tower(self, x, y, tower):
        try:
            row = int(math.floor(y / self.res))
            col = int(math.floor(x / self.res))

            self._grid[row][col] = tower
            pos_x = x - (x % self.res) + 1
            pos_y = y - (y % self.res) + 1
            tower.set_pos(pos_x, pos_y)

            self._towers.add(tower)

            self._creeps.update('path', 
                                [self, (pos_x, pos_y)])
        except IndexError:
            print row, col

    def add_creep(self, creep):
        self._creeps.add(creep)
        creep.update('path', [self, (0, 0)])

    def draw(self, screen):
        screen.blit(self.__grid_background, (0, 0))
        self._towers.draw(screen)
        self._creeps.draw(screen)

    def draw_map(self, screen, pos):
        return screen.blit(self.__grid_background, pos.topleft, pos)

    def update(self, time):
        import creep
        self._towers.update(time)
        self._creeps.update('time', [time])

    def get_goal(self):
        return (self.width, self.height)

    def get_new_path(self, src):
        return []
