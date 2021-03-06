#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:00:06 2016

@author: Katie
"""

'''http://programarcadegames.com/index.php?chapter=introduction_to_animation&lang=en#section_8'''
import pygame
 
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

#starting and direction of rectangle
rect_x=50
rect_y=50

#speed and direction of rectangle
rect_change_x=5
rect_change_y=5

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code
    pygame.draw.rect(screen,WHITE,[rect_x,rect_y,50,50])
    #move rectangle starting point
    rect_x+=rect_change_x
    rect_y+=rect_change_y
    
    #Rebound
    if rect_y>450 or rect_y<0:
        rect_change_y=rect_change_y*-1
    if rect_x>650 or rect_x<0:
        rect_change_x=rect_change_x*-1
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()