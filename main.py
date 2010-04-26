import sys
import math
import pygame
from random import randint

import util
import tower
from grid import Grid

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

map_res = 40
map_width, map_height = 500, 400
map = Grid(map_width, map_height, map_res, screen)

tower_type = 0
tower_types = [tower.WaterTower, tower.FireTower, tower.EarthTower]

mouse_rect = pygame.Rect(pygame.mouse.get_pos(), (map_res, map_res))
map.draw_map(screen, screen.get_rect())
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            tower = tower_types[tower_type](x, y)
            map.add_tower(x, y, tower)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                tower_type = (tower_type + 1) % len(tower_types)

    # clear the screen

    # drawing code goes here
    draw_list = []
    draw_list += map.draw(screen)

    pygame.display.update(draw_list)
