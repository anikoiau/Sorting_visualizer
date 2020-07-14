# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:26:15 2020

@author: soumitra
"""

import pygame
import numpy as np
import time

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.colour = (255, 255, 255)
    
    def draw(self, screen):
        pygame.draw.line(screen, self.colour, (self.x1, self.y1), (self.x2, self.y2), 3)

    

WIDTH = 1300
HEIGHT = 400

SCREEN = (WIDTH, HEIGHT)

pygame.init()

screen = pygame.display.set_mode(SCREEN)


initial = time.time()

np.random.seed(int(time.time()))


lengths = np.random.randint(20, 300, (1, 150))[0]

#lengths = list(range(100, 250))
xcoords = list(range(50, 800, 5))

lines = [Line(xcoords[i], 399, xcoords[i], 399 - lengths[i]) for i in range(150)]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


screen.fill((0, 0, 0))

for i in range(len(lines)):
    lines[i].draw(screen)
    

pygame.display.update()
        

for i in range(1, 150):
    key = lines[i].y2
    
    
    j = i - 1
    
    while j >= 0 and lines[j].y2 < key:
        
        screen.fill((0, 0, 0))
        pygame.time.Clock().tick(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        
        lines[j + 1].colour = RED
              
        lines[j + 1].y2 = lines[j].y2
        j = j - 1
        
        
        for i in range(len(lines)):
            lines[i].draw(screen)
    
    
        pygame.display.update()
        
        lines[j + 2].colour = (255, 255, 255)
        
    lines[j + 1].y2 = key
    # lines[j + 1].colour = (255, 255, 255)
    
    # lines[j + 1].colour = GREEN
    
    # for i in range(len(lines)):
    #     lines[i].draw(screen)
        
    # pygame.display.update()
print('insertion sort = ', time.time() - initial)
    
    

