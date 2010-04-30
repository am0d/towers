import sys
import math
import pygame
from random import randint

import util
import tower
import creep
from world import World

pygame.init()

size = width, height = 800, 480
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

map_res = 40
map_width, map_height = 500, 400
world = World(map_width, map_height, map_res, screen)

tower_type = 0
tower_types = [tower.WaterTower, tower.FireTower, tower.EarthTower]
mouse_pos = pygame.mouse.get_pos()
mouse_tower = tower.MouseTower(0, 0)

num_creeps = 0
last_creep_added = 0

last_time = pygame.time.get_ticks()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            tower = tower_types[tower_type](x, y)
            world.add_tower(x, y, tower)
        elif event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_ESCAPE:
	       finished = True
            elif event.key == pygame.K_t:
                tower_type = (tower_type + 1) % len(tower_types)
                mouse_tower.set_tower_type(tower_type)

    
    # update everything
    current_time = pygame.time.get_ticks()
    world.update(current_time - last_time)
    last_time = current_time

    if num_creeps < 5 and (current_time - last_creep_added) > 2000:
    	world.add_creep(creep.Creep())
	num_creeps += 1
	last_creep_added = current_time

    # drawing code goes here
    world.draw(screen)

    mouse_pos = pygame.mouse.get_pos()
    mouse_tower.set_pos(math.floor(mouse_pos[0] / map_res) * map_res + 1,
                        math.floor(mouse_pos[1] / map_res) * map_res + 1)
    mouse_tower.draw(screen)

    #pygame.display.update(draw_list)
    pygame.display.flip()

print "Shutting down ..."
pygame.quit()
sys.exit(0)
