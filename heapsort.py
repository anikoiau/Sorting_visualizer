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
xcoords = list(range(50, 800, 5))

lines = [Line(xcoords[i], 399, xcoords[i], 399 - lengths[i]) for i in range(150)]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


length = len(lines)


screen.fill((0, 0, 0))

for i in range(len(lines)):
    lines[i].draw(screen)
    

pygame.display.update()





def heapify(a, i, n):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    
    if left < n and a[largest].y2 > a[left].y2:
        largest = left

    if right < n and a[largest].y2 > a[right].y2:
        largest = right


    if largest != i:
        a[largest].y2, a[i].y2 = a[i].y2, a[largest].y2
        
        
        screen.fill((0, 0, 0))
        pygame.time.Clock().tick(100)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        for i in range(len(lines)):
            lines[i].draw(screen)
        
        pygame.display.update()
        
        heapify(a, largest, n)
        
        
def buildheap(a):
    i = (len(a) - 2) // 2

    while i >= 0:
        heapify(a, i, len(a))
        
        
        i-= 1
        

def heapsort(a):
    buildheap(a)
    
    n = len(a)
    
    for i in reversed(range(len(a))):
        a[i].y2, a[0].y2 = a[0].y2, a[i].y2
        n -= 1
        
        heapify(a, 0, n)
        
        
    screen.fill((0, 0, 0))
    pygame.time.Clock().tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(len(lines)):
        lines[i].draw(screen)
    
    pygame.display.update()
    

heapsort(lines)



