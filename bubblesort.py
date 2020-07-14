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
        pygame.draw.line(screen, self.colour, (self.x1, self.y1), (self.x2, self.y2), 1)

    

WIDTH = 1300
HEIGHT = 400

SCREEN = (WIDTH, HEIGHT)

pygame.init()

screen = pygame.display.set_mode(SCREEN)

initial = time.time()

np.random.seed(int(time.time()))


lengths = np.random.randint(20, 300, (1, 150))[0]
#lengths = list(range(100, 250))
xcoords = list(range(50, 1050, 10))

lines = [Line(xcoords[i], 399, xcoords[i], 399 - lengths[i]) for i in range(100)]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


screen.fill((0, 0, 0))

for i in range(len(lines)):
    lines[i].draw(screen)
    

pygame.display.update()
        

index = 0

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
            
            
#     pygame.time.delay(10)
    
#     # screen.fill((0, 0, 0), pygame.Rect(lines[index % 100].x2 - 2, lines[index % 100].y2 - 2, 8, ))
    
#     screen.fill((0, 0, 0))
         
    # if lines[index].colour == RED:
    #     lines[index].colour = (255, 255, 255)
    # else:
    #     lines[index].colour = RED
    
    # lines[index % 100].y2, lines[(index + 1) % 100].y2 = lines[(index + 1) % 100].y2, lines[index % 100].y2
    
    
    
    
for i in range(0, 99):
    # lines[i].colour = GREEN
    for j in range(0, 99 - i):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if lines[j].y2 < lines[j + 1].y2:
            lines[j].y2, lines[j + 1].y2 = lines[j + 1].y2, lines[j].y2
            
            # if lines[j].colour == RED:
            #     lines[j].colour = (255, 255, 255)
            # else:
            #     lines[j].colour = RED
    
            
            pygame.time.Clock().tick(500)
        screen.fill((0, 0, 0))
        for k in range(len(lines)):
            lines[k].draw(screen)
            
        pygame.display.update()
            
    lines[j].colour = GREEN
            
    
            
            
print('bubble sort = ', time.time() - initial)                
    
    
    
    
    # update_rect = [pygame.Rect(lines[index % 100].x2 - 3, 0, 6, 399), pygame.Rect(lines[(index + 5) % 100].x2 - 3, 0, 6, 399)]
    
    # for i in range(len(lines)):
    #     lines[i].draw(screen)
     
    # pygame.display.update()

        
        
        
        
        
        
        
        
        