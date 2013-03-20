'''
Created on Mar 18, 2013

Real project was created on Mar 12, 2013

First REAL start on the Maze 31213 project. Hear wee goe!

Follows the example of the IDEA/ALTER game framework by Andy Harris in the book "Game Programming: The L Line, The Express Line to Learning", published by Wiley Publishing, Inc.


@author: Us
'''

#I - Import and Initialize
import pygame
pygame.init()

#D - Display configuration
screen = pygame.display.set_mode(640, 480)
pygame.display.set_caption("Maze 31213")

#E - Entities
    #All the sprites, but I think they'll go in their own module
    #background for now
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 255))

#A - Action (broken into ALTER steps)

    #A - Assign values to key variables
clock = pygame.time.Clock()
keepGoing = True
    
    #L - Set up main loop
while keepGoing:
    #T - Timer to set frame rate
    clock.tick(30)
    
    #E - Event handlint
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    
    #R - Refresh display
    #This is needed for now, but it will be unnecessary once a sprite is implemented for the background
    screen.blit(background, (0, 0))
    pygame.display.flip()

def main():
    screen = pygame.

if __name__ == '__main__':
    main()