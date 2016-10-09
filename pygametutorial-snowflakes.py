#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:00:06 2016

@author: Katie
"""

'''http://programarcadegames.com/index.php?chapter=introduction_to_animation&lang=en#section_8'''
import pygame
import numpy as np
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # --- Drawing code

    for i in range(50):
        x=np.random.random_integers(0,400)
        y=np.random.random_integers(0,400)
        pygame.draw.circle(screen,WHITE,[x,y],2)
        
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()