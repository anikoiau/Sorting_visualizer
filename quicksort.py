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
HEIGHT = 600

SCREEN = (WIDTH, HEIGHT)

pygame.init()

screen = pygame.display.set_mode(SCREEN)


initial = time.time()

np.random.seed(int(time.time()))


lengths = np.random.randint(50, 550, (1, 383))[0]

# lengths = list(range(50, 434))
xcoords = list(range(50, 1200, 3))

lines = [Line(xcoords[i], 599, xcoords[i], 599 - lengths[i]) for i in range(383)]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


length = len(lines)


screen.fill((0, 0, 0))

for i in range(len(lines)):
    lines[i].draw(screen)
    

pygame.display.update()





def partition(a, l, r):
    global length
    low = a[l].y2
    
    p = l
    q = r
    
    while q >= p:
        
        while p < length and a[p].y2 >= low:
            p += 1
            
        while q >= 0 and a[q].y2 < low:
            q -= 1
    
        # print('p = ', p, 'q = ', q)
            
        if p < q:
            
            a[p].y2, a[q].y2 = a[q].y2, a[p].y2
                       
            screen.fill((0, 0, 0))
            pygame.time.Clock().tick(50)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        
            for i in range(len(lines)):
                lines[i].draw(screen)
            
            pygame.display.update()
            
            
        
    a[q].y2, a[l].y2 = a[l].y2, a[q].y2
    
    lines[q].colour = RED
    screen.fill((0, 0, 0))
    pygame.time.Clock().tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(len(lines)):
        lines[i].draw(screen)
    
    pygame.display.update()
    
    # lines[q].colour = (255, 255, 255)
    
    
    
    
        
    # lines[q].colour = GREEN
    
    # screen.fill((0, 0, 0))
    # pygame.time.Clock().tick(100)

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()`

    # for i in range(len(lines)):
    #     lines[i].draw(screen)
    
    # pygame.display.update()

    
    return q


def quicksort(a, l, r):
    if r > l:

        p = partition(a, l, r)
        
   
        quicksort(a, l, p - 1)
        quicksort(a, p + 1, r)
        
        
    



quicksort(lines, 0, len(lines) - 1)

# screen.fill((0, 0, 0))
# pygame.time.Clock().tick(10)

# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         pygame.quit()
        
# for i in range(len(lines)):
#     lines[i].draw(screen)

# pygame.display.update()







